from functools import partial

from telebot import TeleBot, custom_filters

from bot import handlers as handlers
from bot import states as bot_states


class Handler:
    def __init__(self, callback, **kwargs):
        self.callback = callback
        self.kwargs = kwargs


def get_start_handlers():
    return [
        Handler(callback=handlers.handle_register, commands=["start"]),
        Handler(
            callback=handlers.handle_get_first_name,
            state=bot_states.RegisterState.first_name,
        ),
        Handler(
            callback=handlers.handle_get_last_name,
            state=bot_states.RegisterState.last_name,
        ),
    ]


def get_show_data_handlers():
    return [
        Handler(callback=handlers.handle_show_data, commands=["show_data"]),
    ]


def get_delete_account_handlers():
    return [
        Handler(callback=handlers.handle_delete_account, commands=["delete_account"]),
        Handler(
            callback=handlers.handle_finish_delete_account,
            state=bot_states.DeleteAccountState.are_you_sure,
        ),
    ]


def get_change_data_handlers():
    return [
        Handler(callback=handlers.handle_change_data, commands=["change_data"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.ChangeDataState.select_field,
                bot_states.ChangeDataState.write_new_value,
            ],
        ),
        Handler(
            callback=handlers.handle_choose_field_to_change,
            state=bot_states.ChangeDataState.select_field,
        ),
        Handler(
            callback=handlers.handle_save_changed_data,
            state=bot_states.ChangeDataState.write_new_value,
        ),
    ]


def get_create_group_handlers():
    return [
        Handler(callback=handlers.handle_create_group, commands=["create_group"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.CreateGroup.name,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_name,
            state=bot_states.CreateGroup.name,
        ),
    ]


def get_show_groups_handlers():
    return [
        Handler(callback=handlers.handle_show_groups, commands=["show_groups"]),
    ]


def get_show_members_handlers():
    return [
        Handler(callback=handlers.handle_show_members, commands=["show_members"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.ShowMembers.setId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_show,
            state=bot_states.ShowMembers.setId,
        ),
    ]


def get_join_group_handlers():
    return [
        Handler(callback=handlers.handle_join_group, commands=["join"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.JoinGroup.setId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_join,
            state=bot_states.JoinGroup.setId,
        ),
    ]


def get_left_group_handlers():
    return [
        Handler(callback=handlers.handle_left_group, commands=["left_group"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.LeftGroup.setId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_left,
            state=bot_states.LeftGroup.setId,
        ),
    ]


def get_delete_group_handlers():
    return [
        Handler(callback=handlers.handle_delete_group, commands=["delete_group"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.DeleteGroup.setId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_delete_group,
            state=bot_states.DeleteGroup.setId,
        ),
    ]


def get_show_want_members_handlers():
    return [
        Handler(callback=handlers.handle_show_want_members, commands=["show_want_join"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.JoinGroup.setId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_join,
            state=bot_states.JoinGroup.setId,
        ),
    ]


def get_join_accept_handlers():
    return [
        Handler(callback=handlers.handle_accept_join, commands=["join_accepts"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.AcceptJoin.setUserId,
                bot_states.AcceptJoin.setGroupId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_accept_join,
            state=bot_states.AcceptJoin.setGroupId,
        ),
        Handler(
            callback=handlers.handle_get_user_id_for_accept_join,
            state=bot_states.AcceptJoin.setUserId,
        ),
    ]


def get_delete_member_handlers():
    return [
        Handler(callback=handlers.handle_delete_member, commands=["delete_member"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.DeleteMember.setUserId,
                bot_states.DeleteMember.setGroupId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_delete,
            state=bot_states.DeleteMember.setGroupId,
        ),
        Handler(
            callback=handlers.handle_get_user_id_for_delete,
            state=bot_states.DeleteMember.setUserId,
        ),
    ]


def get_ban_name_handlers():
    return [
        Handler(callback=handlers.handle_ban_name, commands=["ban_name"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.BanName.setName,
            ],
        ),
        Handler(
            callback=handlers.handle_get_name_for_ban,
            state=bot_states.BanName.setName,
        ),
    ]


def get_baned_name_handlers():
    return [
        Handler(callback=handlers.handle_get_baned_names, commands=["get_baned_names"]),
    ]


def get_unban_name_handlers():
    return [
        Handler(callback=handlers.handle_unban_name, commands=["unban_name"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.UnbanName.setName,
            ],
        ),
        Handler(
            callback=handlers.handle_get_name_for_unban,
            state=bot_states.UnbanName.setName,
        ),
    ]


def get_rank_names_handlers():
    return [
        Handler(callback=handlers.handle_rate_names, commands=["rate_names"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.RateNames.chooseTier,
                bot_states.RateNames.select_field,
                bot_states.RateNames.get_first_letter,
                bot_states.RateNames.get_gender_field,
                bot_states.RateNames.compareNames,
            ],
        ),
        Handler(
            callback=handlers.handle_choose_field_to_rate,
            state=bot_states.RateNames.select_field,
        ),
        Handler(
            callback=handlers.handle_get_gender_filter_to_rate,
            state=bot_states.RateNames.get_gender_field,
        ),
        Handler(
            callback=handlers.handle_get_first_letter_filter_to_rate,
            state=bot_states.RateNames.get_first_letter,
        ),
        Handler(
            callback=handlers.handle_choose_tier,
            state=bot_states.RateNames.chooseTier
        ),
        Handler(
            callback=handlers.handle_compare_names,
            state=bot_states.RateNames.compareNames
        ),
    ]


def get_get_rate_handlers():
    return [
        Handler(callback=handlers.handle_get_rate_names, commands=["get_rate_names"]),
    ]


def get_get_group_rate_handlers():
    return [
        Handler(callback=handlers.handle_get_group_rate, commands=["get_group_rate"]),
        Handler(
            callback=handlers.handle_cancel,
            commands=["cancel"],
            state=[
                bot_states.GroupRate.setId,
            ],
        ),
        Handler(
            callback=handlers.handle_get_group_id_for_group_rate,
            state=bot_states.GroupRate.setId,
        ),
    ]


def create_bot(bot_token, pool):
    state_storage = bot_states.StateYDBStorage(pool)
    bot = TeleBot(bot_token, state_storage=state_storage)

    handlers = []
    handlers.extend(get_start_handlers())
    handlers.extend(get_show_data_handlers())
    handlers.extend(get_delete_account_handlers())
    handlers.extend(get_change_data_handlers())

    handlers.extend(get_create_group_handlers())
    handlers.extend(get_join_accept_handlers())
    handlers.extend(get_show_members_handlers())
    handlers.extend(get_show_want_members_handlers())
    handlers.extend(get_delete_member_handlers())
    handlers.extend(get_delete_group_handlers())

    handlers.extend(get_show_groups_handlers())
    handlers.extend(get_join_group_handlers())
    handlers.extend(get_left_group_handlers())

    handlers.extend(get_ban_name_handlers())
    handlers.extend(get_baned_name_handlers())
    handlers.extend(get_unban_name_handlers())
    handlers.extend(get_get_rate_handlers())

    handlers.extend(get_rank_names_handlers())
    handlers.extend(get_get_group_rate_handlers())

    for handler in handlers:
        bot.register_message_handler(
            partial(handler.callback, pool=pool), **handler.kwargs, pass_bot=True
        )

    bot.add_custom_filter(custom_filters.StateFilter(bot))
    return bot
