from user_interaction import texts

USER_TABLE = "users"
STATE_TABLE = "states"
GROUP_TABLE = "group"
USER_GROUP_TABLE = "users_group"
USER_RATE_TABLE = "user_rate"
GROUP_RATE_TABLE = "group_rate"
NAMES_TABLE = "names"

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

delete_user_rate = f"""
    DECLARE $user_id AS Uint64;

    DELETE FROM `{USER_RATE_TABLE}`
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


# Получение и добавление списка имен #########################################################################

get_all_names = f"""
    SELECT
        name_id,
        first_letter,
        gender,
        `{NAMES_TABLE}`.name AS name,

    FROM `{NAMES_TABLE}`;
"""

get_name_id_by_name = f"""
    DECLARE $name AS Utf8;

    SELECT name_id
    FROM `{NAMES_TABLE}` WHERE name == $name;
"""

get_name_id_by_first_letter = f"""
    DECLARE $first_letter AS Utf8;

    SELECT name_id
    FROM `{NAMES_TABLE}` WHERE first_letter == $first_letter;
"""

get_value_by_name_id = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name_id AS Uint64;

    SELECT value
    FROM `{USER_RATE_TABLE}` WHERE user_id == $user_id AND name_id == $name_id;
"""

get_baned_names = f"""
    DECLARE $user_id AS Uint64; 

    SELECT
        `{NAMES_TABLE}`.name AS name,
    FROM `{USER_RATE_TABLE}`
    FULL JOIN `{NAMES_TABLE}` ON `{NAMES_TABLE}`.name_id = `{USER_RATE_TABLE}`.name_id 
    WHERE `{USER_RATE_TABLE}`.user_id == $user_id AND `{USER_RATE_TABLE}`.banned == true;
"""


get_rate_names = f"""
    DECLARE $user_id AS Uint64; 

    SELECT
        `{NAMES_TABLE}`.name AS name,
        `{USER_RATE_TABLE}`.banned AS banned,
        `{USER_RATE_TABLE}`.tier AS tier,
        `{USER_RATE_TABLE}`.value AS value,
    FROM `{USER_RATE_TABLE}`
    FULL JOIN `{NAMES_TABLE}` ON `{NAMES_TABLE}`.name_id = `{USER_RATE_TABLE}`.name_id 
    WHERE `{USER_RATE_TABLE}`.user_id == $user_id;
"""


ban_name = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name_id AS Uint64;

    UPDATE `{USER_RATE_TABLE}` 
    SET banned = True
    WHERE user_id == $user_id AND name_id == $name_id;
"""


unban_name = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name_id AS Uint64;

    UPDATE `{USER_RATE_TABLE}` 
    SET banned = False
    WHERE user_id == $user_id AND name_id == $name_id;
"""

add_names_to_user_rate = f"""
    DECLARE $rate_id AS Uint64;
    DECLARE $user_id AS Uint64;

    INSERT INTO `{USER_RATE_TABLE}` (rate_id, user_id, name_id, banned, tier, value)
    VALUES 
""" + texts.QUERY_TO_ADD_RATE_NAMES

# Tier

get_name_for_tier = f"""
    DECLARE $user_id AS Uint64; 
    DECLARE $gender AS Utf8; 
    DECLARE $first_letter AS Utf8;

    SELECT `{NAMES_TABLE}`.name AS name
    FROM `{NAMES_TABLE}`
    FULL JOIN `{USER_RATE_TABLE}` ON `{NAMES_TABLE}`.name_id = `{USER_RATE_TABLE}`.name_id 
    WHERE `{USER_RATE_TABLE}`.user_id == $user_id AND `{USER_RATE_TABLE}`.tier == 0 AND `{NAMES_TABLE}`.gender == $gender AND `{NAMES_TABLE}`.first_letter = $first_letter;
"""

get_name_for_tier_no_first_letter = f"""
    DECLARE $user_id AS Uint64; 
    DECLARE $gender AS Utf8; 

    SELECT `{NAMES_TABLE}`.name AS name
    FROM `{NAMES_TABLE}`
    FULL JOIN `{USER_RATE_TABLE}` ON `{NAMES_TABLE}`.name_id = `{USER_RATE_TABLE}`.name_id 
    WHERE `{USER_RATE_TABLE}`.user_id == $user_id AND `{USER_RATE_TABLE}`.tier == 0 AND `{NAMES_TABLE}`.gender == $gender;
"""

update_tier = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name_id AS Uint64;
    DECLARE $tier AS Uint64;
    
    UPDATE `{USER_RATE_TABLE}` 
    SET tier = $tier
    WHERE user_id == $user_id AND name_id == $name_id;
"""

get_name_for_compare = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $gender AS Utf8; 
    DECLARE $first_letter AS Utf8;
    
    SELECT `{NAMES_TABLE}`.name AS name,
        `{USER_RATE_TABLE}`.value 
    FROM `{NAMES_TABLE}`
    FULL JOIN `{USER_RATE_TABLE}` ON `{NAMES_TABLE}`.name_id = `{USER_RATE_TABLE}`.name_id 
    WHERE `{USER_RATE_TABLE}`.user_id == $user_id AND (`{USER_RATE_TABLE}`.tier == 1 OR `{USER_RATE_TABLE}`.tier == 2) AND `{NAMES_TABLE}`.gender == $gender AND `{NAMES_TABLE}`.first_letter = $first_letter
    ORDER BY `{USER_RATE_TABLE}`.value 
    LIMIT 2;
"""

get_name_for_compare_no_first_letter = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $gender AS Utf8; 
    
    SELECT `{NAMES_TABLE}`.name AS name,
        `{USER_RATE_TABLE}`.value 
    FROM `{NAMES_TABLE}`
    FULL JOIN `{USER_RATE_TABLE}` ON `{NAMES_TABLE}`.name_id = `{USER_RATE_TABLE}`.name_id 
    WHERE `{USER_RATE_TABLE}`.user_id == $user_id AND (`{USER_RATE_TABLE}`.tier == 1 OR `{USER_RATE_TABLE}`.tier == 2) AND `{NAMES_TABLE}`.gender == $gender
    ORDER BY `{USER_RATE_TABLE}`.value 
    LIMIT 2;
"""

update_value_for_name = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name_id AS Uint64;
    DECLARE $value AS Uint64;
    
    UPDATE `{USER_RATE_TABLE}` 
    SET value = $value
    WHERE user_id == $user_id AND name_id == $name_id;
"""
