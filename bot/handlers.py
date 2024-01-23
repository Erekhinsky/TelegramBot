from bot import keyboards, states
from database import model as db_model
from logs import logged_execution
from user_interaction import texts


def check_register(message, bot, current_data):
    if not current_data:
        bot.send_message(
            message.chat.id, texts.NOT_REGISTERED, reply_markup=keyboards.EMPTY
        )
        return 1
    else:
        return 0


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
        if db_model.get_user_groups(pool, message.from_user.id):
            db_model.delete_from_user_group(pool, message.from_user.id)
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
def handle_cancel_change_data(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(
        message.chat.id,
        texts.CANCEL_CHANGE,
        reply_markup=keyboards.EMPTY,
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


# Создание группы


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
def handle_cancel_create_group(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(
        message.chat.id,
        texts.CANCEL_CREATE_GROUP,
        reply_markup=keyboards.EMPTY,
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


# Получение всех групп


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
                c["name"], c["first_name"], c["last_name"]
            )
        bot.send_message(
            message.chat.id,
            # texts.SHOW_ALL_GROUPS.format(
            #     current_data_2["name"], current_data_2["first_name"], current_data_2["last_name"]
            # ),
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
            # texts.SHOW_USER_GROUPS.format(
            #     current_data["group_id"], current_data["name"]
            # ),
            txt,
            reply_markup=keyboards.EMPTY,
        )
        return

    txt2 = texts.SHOW_ALL_GROUPS
    for c in current_data_2:
        txt2 += texts.ALL_GROUPS_DATA.format(
            c["name"], c["first_name"], c["last_name"]
        )
    txt1 = texts.SHOW_USER_GROUPS
    for c in current_data_2:
        txt1 += texts.USER_GROUPS_DATA.format(
            c["group_id"], c["name"]
        )

    bot.send_message(
        message.chat.id,
        # texts.SHOW_USER_GROUPS.format(
        #     current_data["group_id"], current_data["name"]
        # ) +
        # texts.SHOW_ALL_GROUPS.format(
        #     current_data_2["name"], current_data_2["first_name"], current_data_2["last_name"]
        # ),
        txt1 + txt2,
        reply_markup=keyboards.EMPTY,
    )


# Вступление в группу


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
def handle_cancel_join_group(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(
        message.chat.id,
        texts.CANCEL_JOIN_GROUP,
        reply_markup=keyboards.EMPTY,
    )


@logged_execution
def handle_get_group_id(message, bot, pool):
    if not message.text.isdigit():
        bot.send_message(
            message.chat.id,
            texts.IT_NOT_DIGIT,
            reply_markup=keyboards.EMPTY,
        )
        return

    group_id = int(message.text)
    current_data = db_model.get_by_id_group(pool, group_id)

    if not current_data:
        bot.send_message(
            message.chat.id,
            texts.IT_NOT_GROUP_ID,
            reply_markup=keyboards.EMPTY,
        )
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
