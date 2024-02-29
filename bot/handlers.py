from bot import keyboards, states
from database import model as db_model
from logs import logged_execution, logger
from user_interaction import texts


def check_register(message, bot, current_data):
    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.NOT_REGISTERED,
            reply_markup=keyboards.EMPTY,
        )
        return 1
    else:
        return 0


def check_digit(message, bot):
    if not message.text.isdigit():
        bot.send_message(
            message.chat.id,
            texts.IT_NOT_DIGIT,
            reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
        )
        return 1
    return 0


def check_exist_group(message, bot, pool):
    if check_digit(message, bot):
        return 1

    group_id = int(message.text)
    current_data = db_model.get_by_id_group(pool, group_id)

    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.IT_NOT_GROUP_ID,
            reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
        )
        return 1

    return group_id, current_data


def check_full_id_group(message, bot, pool):
    group_id, current_data = check_exist_group(message, bot, pool)

    if not group_id or not current_data:
        return 1

    if current_data["user_id"] != message.from_user.id:
        bot.send_message(
            message.chat.id,
            texts.NOT_OWNER,
            reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
        )
        return 1

    return group_id, current_data


def check_name_exist(message, bot, pool):
    name = message.text
    names = db_model.get_all_names(pool)

    flag = 0
    for n in names:
        if name == n["name"]:
            flag = 1

    if not flag:
        bot.send_message(
            message.chat.id,
            texts.NOT_FOUND_NAME,
            reply_markup=keyboards.get_reply_keyboard(["/cancel"])
        )
        return 1

    return name


#####################################################################################################################


@logged_execution
def handle_cancel(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(
        message.chat.id,
        texts.CANCEL,
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_register(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)

    if current_data:
        bot.send_message(
            message.chat.id,
            texts.START,
            reply_markup=keyboards.EMPTY,
        )
        return

    bot.send_message(
        message.chat.id,
        texts.START + texts.FIRST_NAME,
        reply_markup=keyboards.EMPTY,
    )
    bot.set_state(
        message.from_user.id, states.RegisterState.first_name, message.chat.id
    )


@logged_execution
def handle_get_first_name(message, bot, pool):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["first_name"] = message.text
    bot.set_state(message.from_user.id, states.RegisterState.last_name, message.chat.id)
    bot.send_message(
        message.chat.id,
        texts.LAST_NAME,
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_get_last_name(message, bot, pool):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        first_name = data["first_name"]
        last_name = message.text

    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.add_user(pool, message.from_user.id, first_name, last_name)
    db_model.add_user_rate(pool, message.from_user.id)

    bot.send_message(
        message.chat.id,
        texts.DATA_IS_SAVED.format(first_name, last_name),
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_show_data(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.SHOW_DATA_WITH_PREFIX.format(
            current_data["first_name"], current_data["last_name"]
        ),
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_delete_account(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.DELETE_ACCOUNT,
        reply_markup=keyboards.get_reply_keyboard(texts.DELETE_ACCOUNT_OPTIONS),
    )
    bot.set_state(
        message.from_user.id, states.DeleteAccountState.are_you_sure, message.chat.id
    )


@logged_execution
def handle_finish_delete_account(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)

    if message.text not in texts.DELETE_ACCOUNT_OPTIONS:
        bot.send_message(
            message.chat.id,
            texts.DELETE_ACCOUNT_UNKNOWN,
            reply_markup=keyboards.EMPTY,
        )
        return

    if texts.DELETE_ACCOUNT_OPTIONS[message.text]:
        db_model.delete_user(pool, message.from_user.id)
        db_model.delete_user_rate(pool, message.from_user.id)
        if db_model.get_user_groups(pool, message.from_user.id):
            db_model.delete_from_user_groups(pool, message.from_user.id)
            db_model.delete_all_user_group(pool, message.from_user.id)
        if db_model.get_not_user_groups(pool, message.from_user.id):
            db_model.delete_from_not_user_group(pool, message.from_user.id)
        bot.send_message(
            message.chat.id,
            texts.DELETE_ACCOUNT_DONE,
            reply_markup=keyboards.EMPTY,
        )
    else:
        bot.send_message(
            message.chat.id,
            texts.DELETE_ACCOUNT_CANCEL,
            reply_markup=keyboards.EMPTY,
        )


@logged_execution
def handle_change_data(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.set_state(
        message.from_user.id, states.ChangeDataState.select_field, message.chat.id
    )
    bot.send_message(
        message.chat.id,
        texts.SELECT_FIELD,
        reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST, ["/cancel"]),
    )


@logged_execution
def handle_choose_field_to_change(message, bot, pool):
    if message.text not in texts.FIELD_LIST:
        bot.send_message(
            message.chat.id,
            texts.UNKNOWN_FIELD,
            reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST, ["/cancel"]),
        )
        return

    bot.set_state(
        message.from_user.id, states.ChangeDataState.write_new_value, message.chat.id
    )

    field = message.text
    if field == "Имя":
        field = "first_name"
    else:
        field = "last_name"

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["field"] = field

    bot.send_message(
        message.chat.id,
        texts.WRITE_NEW_VALUE.format(message.text),
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )


@logged_execution
def handle_save_changed_data(message, bot, pool):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        field = data["field"]

    bot.delete_state(message.from_user.id, message.chat.id)

    current_data = db_model.get_user(pool, message.from_user.id)
    current_data[field] = message.text
    db_model.update_user(pool, **current_data)

    bot.send_message(
        message.chat.id,
        texts.CHANGE_DATA_DONE,
        reply_markup=keyboards.EMPTY,
    )


# Создание группы #############################################################################################


@logged_execution
def handle_create_group(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.GROUP_NAME,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.CreateGroup.name, message.chat.id
    )


@logged_execution
def handle_get_group_name(message, bot, pool):
    name = message.text
    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.add_group(pool, message.from_user.id, name)

    current_data = db_model.get_id_group_by_name(pool, message.from_user.id, name)

    bot.send_message(
        message.chat.id,
        texts.GROUP_DATA_IS_SAVED.format(
            current_data["group_id"], name
        ),
        reply_markup=keyboards.EMPTY,
    )


# Получение всех групп #########################################################################################


@logged_execution
def handle_show_groups(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    current_data = db_model.get_user_groups(pool, message.from_user.id)
    current_data_2 = db_model.get_not_user_groups(pool, message.from_user.id)

    if not current_data and not current_data_2:
        bot.send_message(
            message.chat.id, texts.NOT_GROUPS, reply_markup=keyboards.EMPTY
        )
        return
    elif not current_data:
        txt = texts.SHOW_ALL_GROUPS
        for c in current_data_2:
            txt += texts.ALL_GROUPS_DATA.format(
                c["group_id"], c["name"], c["first_name"], c["last_name"]
            )
        bot.send_message(
            message.chat.id,
            txt,
            reply_markup=keyboards.EMPTY,
        )
        return
    elif not current_data_2:
        txt = texts.SHOW_USER_GROUPS
        for c in current_data:
            txt += texts.USER_GROUPS_DATA.format(
                c["group_id"], c["name"]
            )
        bot.send_message(
            message.chat.id,
            txt,
            reply_markup=keyboards.EMPTY,
        )
        return

    txt2 = texts.SHOW_ALL_GROUPS
    for c in current_data_2:
        txt2 += texts.ALL_GROUPS_DATA.format(
            c["group_id"], c["name"], c["first_name"], c["last_name"]
        )
    txt1 = texts.SHOW_USER_GROUPS
    for c in current_data:
        txt1 += texts.USER_GROUPS_DATA.format(
            c["group_id"], c["name"]
        )

    bot.send_message(
        message.chat.id,
        txt1 + txt2,
        reply_markup=keyboards.EMPTY,
    )


# Вступление в группу #############################################################################################


@logged_execution
def handle_join_group(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.JOIN_GROUP,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.JoinGroup.setId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_join(message, bot, pool):
    group_id, current_data = check_exist_group(message, bot, pool)
    if not group_id or not current_data:
        return

    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.add_to_group(pool, message.from_user.id, group_id)

    bot.send_message(
        message.chat.id,
        texts.OK_JOIN_GROUP.format(
            current_data["name"]
        ),
        reply_markup=keyboards.EMPTY,
    )


# Выйти из группы #############################################################################################


@logged_execution
def handle_left_group(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.LEFT_GROUP,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.LeftGroup.setId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_left(message, bot, pool):
    group_id, current_data = check_exist_group(message, bot, pool)
    if not group_id or not current_data:
        return

    if current_data["user_id"] == message.from_user.id:
        bot.send_message(
            message.chat.id,
            texts.YOU_OWNER,
            reply_markup=keyboards.EMPTY,
        )
        handle_delete_group(message, bot, pool)
        return

    if not db_model.get_member(pool, message.from_user.id, group_id):
        bot.send_message(
            message.chat.id,
            texts.YOU_NOT_MEMBER,
            reply_markup=keyboards.EMPTY,
        )
        return

    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.left_group(pool, message.from_user.id, group_id)

    bot.send_message(
        message.chat.id,
        texts.OK_LEFT_GROUP,
        reply_markup=keyboards.EMPTY,
    )


# Удалить группу #############################################################################################


@logged_execution
def handle_delete_group(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.DELETE_GROUP,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.DeleteGroup.setId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_delete_group(message, bot, pool):
    group_id, current_data = check_full_id_group(message, bot, pool)
    if not group_id or not current_data:
        return

    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.delete_from_user_group(pool, group_id)
    db_model.delete_group_by_id(pool, group_id)

    bot.send_message(
        message.chat.id,
        texts.OK_DELETE,
        reply_markup=keyboards.EMPTY,
    )


# Принять пользователя в группу ############################################################


@logged_execution
def handle_accept_join(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.ACCEPT_JOIN,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.AcceptJoin.setGroupId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_accept_join(message, bot, pool):
    group_id, current_data = check_full_id_group(message, bot, pool)
    if not group_id or not current_data:
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["group_id"] = group_id

    bot.set_state(
        message.from_user.id, states.AcceptJoin.setUserId, message.chat.id
    )

    bot.send_message(
        message.chat.id,
        texts.GET_USER_ID,
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_get_user_id_for_accept_join(message, bot, pool):
    if check_digit(message, bot):
        return

    user_id = int(message.text)
    current_data = db_model.get_user(pool, user_id)

    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.USER_NOT_FOUND,
            reply_markup=keyboards.EMPTY,
        )
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        group_id = data["group_id"]
    bot.delete_state(message.from_user.id, message.chat.id)

    db_model.accept_join(pool, message.from_user.id, group_id, user_id)

    bot.send_message(
        message.chat.id,
        texts.ACCEPT_JOIN_OK,
        reply_markup=keyboards.EMPTY,
    )


# Удалить пользователя из группы ############################################################


@logged_execution
def handle_delete_member(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.DELETE_MEMBER,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.DeleteMember.setGroupId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_delete(message, bot, pool):
    group_id, current_data = check_exist_group(message, bot, pool)
    if not group_id or not current_data:
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["group_id"] = group_id

    bot.set_state(
        message.from_user.id, states.DeleteMember.setUserId, message.chat.id
    )

    bot.send_message(
        message.chat.id,
        texts.GET_USER_ID,
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_get_user_id_for_delete(message, bot, pool):
    if check_digit(message, bot):
        return

    user_id = int(message.text)
    current_data = db_model.get_user(pool, user_id)

    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.USER_NOT_FOUND,
            reply_markup=keyboards.EMPTY,
        )
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        group_id = data["group_id"]

    bot.delete_state(message.from_user.id, message.chat.id)

    db_model.delete_member(pool, group_id, user_id)

    bot.send_message(
        message.chat.id,
        texts.DELETE_MEMBER_OK,
        reply_markup=keyboards.EMPTY,
    )


# Показать участников группы #########################################################################################


@logged_execution
def handle_show_members(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.SHOW_MEMBERS,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )

    bot.set_state(
        message.from_user.id, states.ShowMembers.setId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_show(message, bot, pool):
    group_id, current_data = check_full_id_group(message, bot, pool)
    if not group_id or not current_data:
        return

    bot.delete_state(message.from_user.id, message.chat.id)
    current_data = db_model.get_members(pool, group_id)

    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.NOT_MEMBERS,
            reply_markup=keyboards.EMPTY,
        )
        return

    txt = texts.SHOW_MEMBERS_PRE.format(
        current_data[0]["name"]
    )

    for u in current_data:
        txt += texts.MEMBER.format(
            u["user_id"],
            u["first_name"],
            u["last_name"],
        )

    bot.send_message(
        message.chat.id,
        txt,
        reply_markup=keyboards.EMPTY,
    )


# Показать желающих вступить в группу ########################################################################


@logged_execution
def handle_show_want_members(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    current_data = db_model.get_want_members(pool, message.from_user.id)

    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.NOT_WANT_MEMBERS,
            reply_markup=keyboards.EMPTY,
        )
        return

    txt = texts.SHOW_WANT_MEMBERS

    for u in current_data:
        txt += texts.WANT_MEMBER.format(
            u["group_id"],
            u["name"],
            u["user_id"],
            u["first_name"],
            u["last_name"]
        )

    bot.send_message(
        message.chat.id,
        txt,
        reply_markup=keyboards.EMPTY,
    )


# Забанить имена ###########################################################################################

@logged_execution
def handle_ban_name(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.BAN_NAME,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.BanName.setName, message.chat.id
    )


@logged_execution
def handle_get_name_for_ban(message, bot, pool):
    name = check_name_exist(message, bot, pool)
    if name == 1:
        return

    bot.delete_state(message.from_user.id, message.chat.id)
    banned = db_model.get_baned_names(pool, message.from_user.id)

    flag = 0
    # if not banned:
    #     bot.send_message(
    #         message.chat.id,
    #         texts.NOT_BANNED_NAMES,
    #         reply_markup=keyboards.EMPTY,
    #     )
    #     return

    for ban in banned:
        if name == ban["name"]:
            flag = 1
            break

    if flag:
        bot.send_message(
            message.chat.id,
            texts.ALREADY_BANNED,
            reply_markup=keyboards.get_reply_keyboard(["/cancel"])
        )
        return

    db_model.ban_name(pool, message.from_user.id, name)

    bot.send_message(
        message.chat.id,
        texts.BAN_OK.format(
            name
        ),
        reply_markup=keyboards.EMPTY,
    )


# Разблокирование имени #########################################################################


@logged_execution
def handle_unban_name(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.UNBAN_NAME,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.UnbanName.setName, message.chat.id
    )


@logged_execution
def handle_get_name_for_unban(message, bot, pool):
    name = check_name_exist(message, bot, pool)
    if name == 1:
        return

    bot.delete_state(message.from_user.id, message.chat.id)
    banned = db_model.get_baned_names(pool, message.from_user.id)

    flag = 0
    if not banned:
        bot.send_message(
            message.chat.id,
            texts.NOT_BANNED_NAMES,
            reply_markup=keyboards.EMPTY,
        )
        return

    for ban in banned:
        if name == ban["name"]:
            flag = 1
            break

    if not flag:
        bot.send_message(
            message.chat.id,
            texts.NAME_NOT_BANNED,
            reply_markup=keyboards.get_reply_keyboard(["/cancel"])
        )
        return

    db_model.unban_name(pool, message.from_user.id, name)

    bot.send_message(
        message.chat.id,
        texts.UNBAN_OK.format(
            name
        ),
        reply_markup=keyboards.EMPTY,
    )


# Получение заблокированных имен #########################################################################


@logged_execution
def handle_get_baned_names(message, bot, pool):
    result = db_model.get_baned_names(pool, message.from_user.id)

    if not result:
        bot.send_message(
            message.chat.id,
            texts.NOT_BANNED_NAMES,
            reply_markup=keyboards.EMPTY,
        )
        return

    txt = texts.BANNED_NAMES
    for b in result:
        txt += texts.NAME.format(
            b["name"]
        )

    bot.send_message(
        message.chat.id,
        txt,
        reply_markup=keyboards.EMPTY,
    )


# Получение рейтинга пользователя ############################################################################

@logged_execution
def handle_get_rate_names(message, bot, pool):
    result = db_model.get_rate_names(pool, message.from_user.id)

    txt = texts.GET_RATE_NAMES
    wom = []
    man = []
    for b in result:
        if (b["tier"] == 1 or b["tier"] == 2 or b["banned"]) and b["gender"] == "Женское":
            wom.append(b)
        if (b["tier"] == 1 or b["tier"] == 2 or b["banned"]) and b["gender"] == "Мужское":
            man.append(b)

    txt += texts.GET_RATE_NAMES_WOMAN
    wom.sort(key=lambda name: int(name["value"]), reverse=True)
    for b in wom:
        if b["banned"]:
            txt += texts.RATE_NAME_BANNED.format(
                b["name"],
            )
        else:
            txt += texts.RATE_NAME_NOT_BANNED.format(
                b["name"],
                b["tier"],
                b["value"]
            )

    txt += texts.GET_RATE_NAMES_MAN
    man.sort(key=lambda name: int(name["value"]), reverse=True)
    for b in man:
        if b["banned"]:
            txt += texts.RATE_NAME_BANNED.format(
                b["name"],
            )
        else:
            txt += texts.RATE_NAME_NOT_BANNED.format(
                b["name"],
                b["tier"],
                b["value"]
            )

    bot.send_message(
        message.chat.id,
        txt,
        reply_markup=keyboards.EMPTY,
    )


# Ранжирование #########################################################################################


@logged_execution
def handle_rate_names(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.set_state(
        message.from_user.id, states.RateNames.get_gender_field, message.chat.id
    )
    bot.send_message(
        message.chat.id,
        texts.SELECT_GENDER_FILTER,
        reply_markup=keyboards.get_reply_keyboard(texts.FILTER_GENDER_LIST, ["/cancel"]),
    )


@logged_execution
def handle_get_gender_filter_to_rate(message, bot, pool):
    current_data = message.text
    if current_data not in texts.FILTER_GENDER_LIST:
        bot.send_message(
            message.chat.id,
            texts.NO_GENDER_FILTER,
            reply_markup=keyboards.get_reply_keyboard(texts.FILTER_GENDER_LIST, ["/cancel"]),
        )
        return

    if current_data == texts.FILTER_GENDER_LIST[0]:
        current_data = "Женское"
    else:
        current_data = "Мужское"

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["gender"] = current_data

    bot.send_message(
        message.chat.id,
        texts.SELECT_FIRST_LETTER_FILTER,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )

    bot.set_state(
        message.from_user.id, states.RateNames.get_first_letter, message.chat.id
    )


@logged_execution
def handle_get_first_letter_filter_to_rate(message, bot, pool):
    current_data = message.text
    if current_data != "0":
        if current_data not in texts.FILTER_FIRST:
            bot.send_message(
                message.chat.id,
                texts.NO_FIRST_LETTER,
                reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
            )
            return

    if current_data != "0":
        if not db_model.get_name_id_by_first_letter(pool, current_data):
            bot.send_message(
                message.chat.id,
                texts.NO_FIRST_LETTER_TO_GENDER,
                reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
            )
            return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["first_letter"] = current_data

    bot.send_message(
        message.chat.id,
        texts.SELECT_FIELD_RATE,
        reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST_RATE, ["/cancel"]),
    )

    bot.set_state(
        message.from_user.id, states.RateNames.select_field, message.chat.id
    )


@logged_execution
def handle_choose_field_to_rate(message, bot, pool):
    current_data = ""
    field = ""

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        field = data.get("field")
        gender = data.get("gender")
        first_letter = data.get("first_letter")

        if not field:
            if message.text not in texts.FIELD_LIST_RATE:
                bot.send_message(
                    message.chat.id,
                    texts.UNKNOWN_FIELD,
                    reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST_RATE, ["/cancel"]),
                )
                return
            field = message.text

        if field == texts.FIELD_LIST_RATE[0] or field == "tier":
            field = "tier"
            current_data = db_model.get_name_for_tier(pool, message.from_user.id, gender, first_letter)
            if not current_data:
                bot.delete_state(message.from_user.id, message.chat.id)
                bot.send_message(
                    message.chat.id,
                    texts.NO_CHOOSE_FOR_TIER,
                    reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST_RATE, ["/cancel"]),
                )
                return

            bot.set_state(
                message.from_user.id, states.RateNames.chooseTier, message.chat.id
            )
            bot.send_message(
                message.chat.id,
                texts.CHOOSE_TIER_FOR_NAME.format(
                    current_data["name"]
                ),
                reply_markup=keyboards.get_reply_keyboard(texts.FIELD_TIER, ["/cancel"]),
            )

        elif field == texts.FIELD_LIST_RATE[1] or field == "compare":
            field = "compare"
            current_data = db_model.get_name_for_compare(pool, message.from_user.id, gender, first_letter)
            if not current_data:
                bot.delete_state(message.from_user.id, message.chat.id)
                bot.send_message(
                    message.chat.id,
                    texts.NO_COMPARE,
                    reply_markup=keyboards.EMPTY,
                )
                return

            bot.set_state(
                message.from_user.id, states.RateNames.compareNames, message.chat.id
            )
            current_data = [current_data[0]["name"], current_data[1]["name"]]
            bot.send_message(
                message.chat.id,
                texts.CHOOSE_NAME,
                reply_markup=keyboards.get_reply_keyboard(current_data, ["/cancel"]),
            )

        data["field"] = field
        data["gender"] = gender
        data["first_letter"] = first_letter
        data[field] = current_data


@logged_execution
def handle_choose_tier(message, bot, pool):
    name = ""
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        name = data["tier"]["name"]

    if message.text not in texts.FIELD_TIER:
        bot.send_message(
            message.chat.id,
            texts.UNKNOWN_FIELD,
            reply_markup=keyboards.get_reply_keyboard(texts.FIELD_TIER, ["/cancel"]),
        )
        return

    tier = message.text
    if tier == texts.FIELD_TIER[0]:
        tier = 1
    elif tier == texts.FIELD_TIER[1]:
        tier = 2
    elif tier == texts.FIELD_TIER[2]:
        tier = 3
    elif tier == texts.FIELD_TIER[3]:
        tier = 4

    db_model.update_tier_for_name(pool, message.from_user.id, name, tier)

    bot.set_state(
        message.from_user.id, states.RateNames.select_field, message.chat.id
    )
    bot.send_message(
        message.chat.id,
        texts.CHOOSE_TIER_OK,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )

    handle_choose_field_to_rate(message, bot, pool)


@logged_execution
def handle_compare_names(message, bot, pool):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        names = data.get("compare")

    if message.text not in names:
        bot.send_message(
            message.chat.id,
            texts.UNKNOWN_FIELD,
            reply_markup=keyboards.get_reply_keyboard(names, ["/cancel"]),
        )
        return

    best_name = message.text
    db_model.update_value_for_name(pool, message.from_user.id, best_name)

    bot.set_state(
        message.from_user.id, states.RateNames.select_field, message.chat.id
    )
    bot.send_message(
        message.chat.id,
        texts.COMPARE_OK,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )

    handle_choose_field_to_rate(message, bot, pool)


# Рейтинг группы ###########################################################################################


@logged_execution
def handle_get_group_rate(message, bot, pool):
    current_data = db_model.get_user(pool, message.from_user.id)
    if check_register(message, bot, current_data):
        return

    bot.send_message(
        message.chat.id,
        texts.GROUP_RATE,
        reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
    )
    bot.set_state(
        message.from_user.id, states.GroupRate.setId, message.chat.id
    )


@logged_execution
def handle_get_group_id_for_group_rate(message, bot, pool):
    group_id, current_data = check_exist_group(message, bot, pool)
    if not group_id or not current_data:
        return

    result = db_model.add_group_rate(pool, group_id)
    # result = db_model.get_group_rate(pool, group_id)

    txt = texts.GET_GROUP_RATE.format(current_data["name"])
    wom = []
    man = []
    for b in result.items():
        if b[1][2] == "Женское":
            wom.append(b)
        if b[1][2] == "Мужское":
            man.append(b)

    txt += texts.GET_RATE_NAMES_WOMAN
    wom.sort(key=lambda name: int(name[1][1]), reverse=True)
    for b in wom:
        if int(b[1][1]) != 0:
            if b[1][0]:
                txt += texts.RATE_NAME_BANNED.format(
                    b[0],
                )
            else:
                txt += texts.GROUP_RATE_NAME_NOT_BANNED.format(
                    b[0],
                    b[1][1]
                )

    txt += texts.GET_RATE_NAMES_MAN
    man.sort(key=lambda name: int(name[1][1]), reverse=True)
    for b in man:
        if int(b[1][1]) != 0:
            if b[1][0]:
                txt += texts.RATE_NAME_BANNED.format(
                    b[0],
                )
            else:
                txt += texts.GROUP_RATE_NAME_NOT_BANNED.format(
                    b[0],
                    b[1][1]
                )

    bot.delete_state(message.from_user.id, message.chat.id)

    bot.send_message(
        message.chat.id,
        txt,
        reply_markup=keyboards.EMPTY,
    )

