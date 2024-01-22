USER_TABLE = "user"
STATE_TABLE = "states"
GROUP_TABLE = "group"

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

get_user_group = f"""
    DECLARE $group_id AS Int64;
    DECLARE $user_id AS Int64;
    DECLARE $name AS Utf8;

    SELECT
        group_id,
        user_id,
        name
    FROM `{GROUP_TABLE}`
    WHERE user_id == $user_id AND name = $name;
"""

add_group = f"""
    DECLARE $group_id AS Uint64;
    DECLARE $user_id AS Uint64;
    DECLARE $name AS Utf8;

    INSERT INTO `{GROUP_TABLE}` (group_id, user_id, name)
    VALUES ($group_id, $user_id, $name);
"""
