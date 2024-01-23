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


def delete_from_user_group(pool, user_id):
    result = get_user_groups(pool, user_id)
    for gr in result:
        execute_update_query(
            pool,
            queries.delete_all_members_from_user_group,
            group_id=gr["group_id"]
        )


def delete_from_not_user_group(pool, user_id):
    execute_update_query(
        pool,
        queries.delete_user_from_not_user_group,
        user_id=user_id,
    )


def delete_group_by_id(pool, user_id):
    execute_update_query(
        pool,
        queries.delete_user,
        user_id=user_id
    )


# Вступление в группу


def add_to_group(pool, user_id, group_id):
    user_group_id = random.randint(0, sys.maxsize)
    execute_update_query(
        pool,
        queries.add_group_u,
        user_group_id=user_group_id,
        user_id=user_id,
        group_id=group_id,
    )
