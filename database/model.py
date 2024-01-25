import json
import sys
import random

from database import queries
from database.utils import execute_select_query, execute_update_query


def get_state(pool, user_id):
    results = execute_select_query(pool, queries.get_user_state, user_id=user_id)
    if len(results) == 0:
        return None
    if results[0]["state"] is None:
        return None
    return json.loads(results[0]["state"])


def set_state(pool, user_id, state):
    execute_update_query(
        pool, queries.set_user_state, user_id=user_id, state=json.dumps(state)
    )


def clear_state(pool, user_id):
    execute_update_query(pool, queries.set_user_state, user_id=user_id, state=None)


#############################################################################################


def add_user(pool, user_id, first_name, last_name):
    execute_update_query(
        pool,
        queries.add_user,
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )


def get_all_names(pool):
    result = execute_select_query(
        pool,
        queries.get_all_names,
    )

    return result


def add_user_rate(pool, user_id):
    rate_id = random.randint(0, sys.maxsize)
    execute_update_query(
        pool,
        queries.add_names_to_user_rate,
        rate_id=rate_id,
        user_id=user_id,
    )


def get_user(pool, user_id):
    result = execute_select_query(pool, queries.get_user, user_id=user_id)

    if len(result) != 1:
        return None
    return result[0]


def delete_user(pool, user_id):
    execute_update_query(
        pool,
        queries.delete_user,
        user_id=user_id
    )


def delete_user_rate(pool, user_id):
    execute_update_query(
        pool,
        queries.delete_user_rate,
        user_id=user_id
    )


def update_user(pool, user_id, first_name, last_name):
    execute_update_query(
        pool,
        queries.update_user,
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )


# Создание группы и получение id ###################################################################################


def add_group(pool, user_id, name):
    group_id = random.randint(0, sys.maxsize)
    execute_update_query(
        pool,
        queries.add_group,
        group_id=group_id,
        user_id=user_id,
        name=name,
    )
    user_group_id = random.randint(0, sys.maxsize)
    execute_update_query(
        pool,
        queries.add_group_u,
        user_group_id=user_group_id,
        user_id=user_id,
        group_id=group_id,
        joined=True,
    )


def get_id_group_by_name(pool, user_id, name):
    result = execute_select_query(
        pool,
        queries.get_id_group_by_name,
        user_id=user_id,
        name=name,
    )

    if len(result) != 1:
        return None

    return result[0]


def get_by_id_group(pool, group_id):
    result = execute_select_query(
        pool,
        queries.get_by_id_group,
        group_id=group_id,
    )

    if len(result) != 1:
        return None

    return result[0]


# Получение всех групп #############################################################################################


def get_user_groups(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_user_group,
        user_id=user_id,
    )

    if len(result) == 0:
        return None

    return result


def get_not_user_groups(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_not_user_group,
        user_id=user_id,
    )

    if len(result) == 0:
        return None

    return result


# Удаление группы и из них


def delete_all_user_group(pool, user_id):
    execute_update_query(
        pool,
        queries.delete_all_user_group,
        user_id=user_id
    )


def delete_from_user_groups(pool, user_id):
    result = get_user_groups(pool, user_id)
    for gr in result:
        execute_update_query(
            pool,
            queries.delete_all_members_from_user_group,
            group_id=gr["group_id"]
        )


def delete_from_user_group(pool, group_id):
    execute_update_query(
        pool,
        queries.delete_all_members_from_user_group,
        group_id=group_id
    )


def delete_from_not_user_group(pool, user_id):
    execute_update_query(
        pool,
        queries.delete_user_from_not_user_group,
        user_id=user_id,
    )


def delete_group_by_id(pool, group_id):
    execute_update_query(
        pool,
        queries.delete_group_by_id,
        group_id=group_id
    )


# Вступление в группу и выход ########################################################################################


def add_to_group(pool, user_id, group_id):
    user_group_id = random.randint(0, sys.maxsize)
    execute_update_query(
        pool,
        queries.add_group_u,
        user_group_id=user_group_id,
        user_id=user_id,
        group_id=group_id,
        joined=False,
    )


def left_group(pool, user_id, group_id):
    execute_update_query(
        pool,
        queries.left_group,
        user_id=user_id,
        group_id=group_id
    )


# Принять в группу и удалить ########################################################################################


def accept_join(pool, user_id, group_id, user_id_join):
    execute_update_query(
        pool,
        queries.accept_join,
        user_id=user_id_join,
        group_id=group_id,
    )


def delete_member(pool, group_id, user_id_delete):
    execute_update_query(
        pool,
        queries.delete_member,
        user_id=user_id_delete,
        group_id=group_id,
    )

# Просмотр участников группы и заявок на вступление ###################################################################


def get_members(pool, user_id, group_id):
    result = execute_select_query(
        pool,
        queries.get_members,
        group_id=group_id,
    )

    if len(result) == 0:
        return None

    return result


def get_member(pool, user_id, group_id):
    result = execute_select_query(
        pool,
        queries.get_member,
        user_id=user_id,
        group_id=group_id,
    )

    if len(result) == 0:
        return None

    return result


def get_want_members(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_want_members,
        user_id=user_id
    )

    if len(result) == 0:
        return None

    return result


# Забанить, разбанить и посмотреть забаненные имена #############################################################


def ban_name(pool, user_id, name):
    name_id = get_name_id_by_name(pool, name)["name_id"]
    execute_update_query(
        pool,
        queries.ban_name,
        user_id=user_id,
        name_id=name_id
    )


def unban_name(pool, user_id, name):
    name_id = get_name_id_by_name(pool, name)["name_id"]
    execute_update_query(
        pool,
        queries.unban_name,
        user_id=user_id,
        name_id=name_id
    )


def get_baned_names(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_baned_names,
        user_id=user_id
    )

    if len(result) == 0:
        return None

    return result


def get_rate_names(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_rate_names,
        user_id=user_id
    )

    return result


def get_name_id_by_name(pool, name):
    result = execute_select_query(
        pool,
        queries.get_name_id_by_name,
        name=name
    )

    return result[0]


# Tier


def get_name_for_tier(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_name_for_tier,
        user_id=user_id
    )

    if not result:
        return None

    return result[0]


def update_tier_for_name(pool, user_id, name, tier):
    name_id = get_name_id_by_name(pool, name)["name_id"]
    execute_update_query(
        pool,
        queries.update_tier,
        user_id=user_id,
        name_id=name_id,
        tier=tier
    )


# Compare

def get_name_for_compare(pool, user_id):
    result = execute_select_query(
        pool,
        queries.get_name_for_compare,
        user_id=user_id
    )

    if not result:
        return None
    if len(result) != 2:
        return None

    return result


def update_value_for_name(pool, user_id, name):
    name_id = get_name_id_by_name(pool, name)["name_id"]
    value = get_value_by_name_id(pool, user_id, name_id)["value"] + 1
    execute_update_query(
        pool,
        queries.update_value_for_name,
        user_id=user_id,
        name_id=name_id,
        value=value
    )


def get_value_by_name_id(pool, user_id, name_id):
    result = execute_select_query(
        pool,
        queries.get_value_by_name_id,
        user_id=user_id,
        name_id=name_id
    )

    return result[0]
