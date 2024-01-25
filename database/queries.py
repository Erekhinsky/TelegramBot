USER_TABLE = "users"
STATE_TABLE = "states"
GROUP_TABLE = "group"
USER_GROUP_TABLE = "users_group"

get_user_state = f"""
    DECLARE $user_id AS Uint64;

    SELECT state
    FROM `{STATE_TABLE}`
    WHERE user_id == $user_id;
"""

set_user_state = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $state AS Utf8?;

    UPSERT INTO `{STATE_TABLE}` (`user_id`, `state`)
    VALUES ($user_id, $state);
"""


######################################################################################################################

get_user = f"""
    DECLARE $user_id AS Int64;

    SELECT
        user_id,
        first_name,
        last_name
    FROM `{USER_TABLE}`
    WHERE user_id == $user_id;
"""

add_user = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $first_name AS Utf8;
    DECLARE $last_name AS Utf8;

    INSERT INTO `{USER_TABLE}` (user_id, first_name, last_name)
    VALUES ($user_id, $first_name, $last_name);
"""

delete_user = f"""
    DECLARE $user_id AS Uint64;

    DELETE FROM `{USER_TABLE}`
    WHERE user_id == $user_id;

    DELETE FROM `{STATE_TABLE}`
    WHERE user_id == $user_id;
"""

update_user = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $first_name AS Utf8;
    DECLARE $last_name AS Utf8;

    REPLACE INTO `{USER_TABLE}`
    SELECT
        $user_id AS user_id,
        $first_name AS first_name,
        $last_name AS last_name
    FROM `{USER_TABLE}`
    WHERE user_id == $user_id;
"""


# Получение всех групп #############################################################################################

get_user_group = f"""
    DECLARE $user_id AS Int64;

    SELECT
        group_id,
        user_id,
        name
    FROM `{GROUP_TABLE}`
    WHERE user_id == $user_id;
"""

get_not_user_group = f"""
    DECLARE $user_id AS Int64;

    SELECT
        `{GROUP_TABLE}`.group_id AS group_id,
        `{GROUP_TABLE}`.name AS name,
        `{USER_TABLE}`.first_name AS first_name,
        `{USER_TABLE}`.last_name AS last_name
    FROM `{USER_GROUP_TABLE}`
    FULL JOIN `{GROUP_TABLE}` ON `{USER_GROUP_TABLE}`.group_id = `{GROUP_TABLE}`.group_id
    FULL JOIN `{USER_TABLE}` ON  `{GROUP_TABLE}`.user_id = `{USER_TABLE}`.user_id
    WHERE `{USER_GROUP_TABLE}`.user_id == $user_id AND `{GROUP_TABLE}`.user_id != $user_id AND `{USER_GROUP_TABLE}`.joined == True;
"""

get_id_group_by_name = f"""
    DECLARE $user_id AS Int64;
    DECLARE $name AS Utf8;

    SELECT
        group_id,
        name
    FROM `{GROUP_TABLE}`
    WHERE user_id == $user_id AND name == $name;
"""

get_by_id_group = f"""
    DECLARE $group_id AS Int64;

    SELECT
        group_id,
        user_id,
        name,
    FROM `{GROUP_TABLE}`
    WHERE group_id == $group_id;
"""

delete_group_by_id = f"""
    DECLARE $group_id AS Int64;

    DELETE FROM `{GROUP_TABLE}`WHERE group_id == $group_id;
"""


# Добавление группы в группу и из группы ##############################################################################

add_group = f"""
    DECLARE $group_id AS Uint64;
    DECLARE $user_id AS Uint64;
    DECLARE $name AS Utf8;

    INSERT INTO `{GROUP_TABLE}` (group_id, user_id, name)
    VALUES ($group_id, $user_id, $name);
"""

add_group_u = f"""
    DECLARE $user_group_id AS Uint64;
    DECLARE $user_id AS Uint64;
    DECLARE $group_id AS Uint64;
    DECLARE $joined AS Bool;

    INSERT INTO `{USER_GROUP_TABLE}` (user_group_id, user_id, group_id, joined)
    VALUES ($user_group_id, $user_id, $group_id, $joined);
"""

left_group = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $group_id AS Uint64;

    DELETE FROM `{USER_GROUP_TABLE}` WHERE user_id == $user_id AND group_id == $group_id;
"""


# Принять в группу и удалить ###########################################################################################

accept_join = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $group_id AS Uint64;

    UPDATE `{USER_GROUP_TABLE}` 
    SET joined = True WHERE user_id == $user_id AND group_id == $group_id;
"""

delete_member = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $group_id AS Uint64;

    DELETE FROM `{USER_GROUP_TABLE}` WHERE user_id == $user_id AND group_id == $group_id;
"""


# Посмотреть участников и потенциальных участников ################################################################

get_members = f"""
    DECLARE $group_id AS Int64;

    SELECT
        `{GROUP_TABLE}`.name AS name,
        `{USER_TABLE}`.user_id AS user_id,
        `{USER_TABLE}`.first_name AS first_name,
        `{USER_TABLE}`.last_name AS last_name
    FROM `{USER_GROUP_TABLE}`
    FULL JOIN `{GROUP_TABLE}` ON `{USER_GROUP_TABLE}`.group_id = `{GROUP_TABLE}`.group_id
    FULL JOIN `{USER_TABLE}` ON `{USER_GROUP_TABLE}`.user_id = `{USER_TABLE}`.user_id
    WHERE `{GROUP_TABLE}`.group_id == $group_id AND `{USER_GROUP_TABLE}`.joined == true;
"""

get_member = f"""
    DECLARE $group_id AS Int64;
    DECLARE $user_id AS Int64;

    SELECT
        user_id,
        group_id,
        joined
    FROM `{USER_GROUP_TABLE}`
    WHERE group_id == $group_id AND user_id == $user_id;
"""

get_want_members = f"""
    DECLARE $user_id AS Int64;

    SELECT
        `{GROUP_TABLE}`.group_id AS group_id,
        `{GROUP_TABLE}`.name AS name,
        `{USER_TABLE}`.user_id AS user_id,
        `{USER_TABLE}`.first_name AS first_name,
        `{USER_TABLE}`.last_name AS last_name
    FROM `{USER_GROUP_TABLE}`
    FULL JOIN `{GROUP_TABLE}` ON `{USER_GROUP_TABLE}`.group_id = `{GROUP_TABLE}`.group_id
    FULL JOIN `{USER_TABLE}` ON `{USER_GROUP_TABLE}`.user_id = `{USER_TABLE}`.user_id
    WHERE `{GROUP_TABLE}`.user_id == $user_id AND `{USER_GROUP_TABLE}`.joined == false;
"""

# Удаление группы и из них #############################################################################################

delete_all_user_group = f"""
    DECLARE $user_id AS Uint64;

    DELETE FROM `{GROUP_TABLE}`
    WHERE user_id == $user_id;
"""

delete_all_members_from_user_group = f"""
    DECLARE $group_id AS Uint64;

    DELETE FROM `{USER_GROUP_TABLE}`
    WHERE group_id == $group_id;
"""

delete_user_from_not_user_group = f"""
    DECLARE $user_id AS Uint64;

    DELETE FROM `{USER_GROUP_TABLE}`
    WHERE user_id == $user_id;
"""
