START = (
    "Добро пожаловать! Я бот для определения лучшего имени для ваших будущих детей!"
    "Вы можете составить свой рейтинг имён и вступить в группу для составления общего рейтинга\n\n"
    "Список доступных команд:\n"

    "/start - вступительное сообщение и регистрация\n"
    "/show_data - показать ваши данные\n"
    "/change_data - изменить ваши данные\n"
    "/join - вступить в группу\n"
    "/show_groups - просмотр групп\n"
    "/left_group - покинуть группу\n\n"

    "/ban_name - заблокировать имя для оценивания\n"
    "/unban_name - разблокировать имя для оценивания\n"
    "/get_baned_names - показать список заблокированных имен\n"
    "/rate_names - начать оценивать имена\n"
    "/get_rate_names - показать ваш рейтинг имен\n\n"

    "/create_group - создание группы\n"
    "/join_accepts - принять пользователей в группу\n"
    "/show_members - показать участников вашей группы\n"
    "/show_want_join - показать желающих вступить в ваши группы\n"
    "/delete_member - выгнать участника вашей группы\n"
    "/delete_group - удалить вашу группу\n\n"

    "/delete_account - удалить ваш аккаунт и ваши группы\n\n"
)

IT_NOT_DIGIT = "Вы ввели не число"
NOT_REGISTERED = "Вы не зарегистрированы, используйте команду: /start"
CANCEL = "Прекращено!"
NOT_OWNER = "Вы не владелец этой группы!"

SHOW_DATA = "Ваше имя: {}\nВаша фамилия: {}"
DATA_IS_SAVED = "Данные сохранены!\n" + SHOW_DATA
SHOW_DATA_WITH_PREFIX = "Ваши данные:\n" + SHOW_DATA
FIRST_NAME = "Введите ваше Имя"
LAST_NAME = "Введите вашу Фамилию"

DELETE_ACCOUNT = "Вы уверены, что хотите удалить ваш аккаунт в боте? Будут удалены и ваши группы."
DELETE_ACCOUNT_OPTIONS = {"Да!": True, "Нет": False}
DELETE_ACCOUNT_UNKNOWN = "Введите Да! или Нет"
DELETE_ACCOUNT_DONE = "Вы удалены!"
DELETE_ACCOUNT_CANCEL = "Удаление прекращено!"

FIELD_LIST = ["Имя", "Фамилия"]
UNKNOWN_FIELD = "Вы выбрали неизвестный параметр"
SELECT_FIELD = "Выберите поле для изменения:"
WRITE_NEW_VALUE = "Введите новое значение для: {}"
CANCEL_CHANGE = "Прекращено обновление ваших данных!"
CHANGE_DATA_DONE = "Ваши данные обновлены!"

GROUP_NAME = "Введите имя группы"
CANCEL_CREATE_GROUP = "Прекращено, ваша группа не сохранена"
GROUP_DATA_IS_SAVED = "Ваша группа сохранена:\nID группы: {}\nНазвание группы: {}\n"
SHOW_USER_GROUPS = "Ваши подконтрольные группы:\n"
USER_GROUPS_DATA = "ID группы: {}\nНазвание группы: {}\n"
SHOW_ALL_GROUPS = "Ваши группы, где вы не владелец:\n"
ALL_GROUPS_DATA = "ID и Название группы: {} {}\nИмя владельца: {} {}\n"
NOT_GROUPS = "Вы не состоите ни в одной группе"

JOIN_GROUP = "Введите ID группы, в которую хотите вступить:"
CANCEL_JOIN_GROUP = "Прекращено, вступление в группу не сохранено"
IT_NOT_GROUP_ID = "Введен несуществующий ID группы"
OK_JOIN_GROUP = "Вы вступили в группу: {}"

ACCEPT_JOIN = "Вы хотите принять пользователя в вашу группу, введите ID вашей группы:"
CANCEL_ACCEPT_JOIN = "Прекращено! Никто не принят"
GET_USER_ID = "Введите ID пользователя:"
USER_NOT_FOUND = "Такого пользователя нет!"
ACCEPT_JOIN_OK = "Пользователь теперь в вашей группе!"

SHOW_MEMBERS = "Введите ID вашей группы, у которой вы хотите посмотреть участников:"
SHOW_MEMBERS_PRE = "Участники группы {}:\n\n"
MEMBER = "Участник: {} {} {}\n"
NOT_MEMBERS = "В вашей группе нет участников!"

SHOW_WANT_MEMBERS = "Пользователи, которые хотят к вам вступить:\n"
WANT_MEMBER = "Группа: {} {}\nПользователь: {} {} {}"
NOT_WANT_MEMBERS = "Нет желающих вступить в ваши группы!"

LEFT_GROUP = "Вы хотите покинуть группу. Укажите её ID:"
YOU_OWNER = "Вы владелец группы"
YOU_NOT_MEMBER = "Вы не состоите в этой группе"
OK_LEFT_GROUP = "Вы вышли из группы!"

DELETE_GROUP = "Вы хотите удалить группу. Укажите её ID:"
OK_DELETE = "Вы успешно удалили свою группу!"

DELETE_MEMBER = "Вы хотите удалить пользователя из вашей группы. Введите её ID:"
DELETE_MEMBER_OK = "Вы удалили пользователя из вашей группы"

BAN_NAME = "Вы хотите заблокировать оценивание имени. Введите его:"
NOT_FOUND_NAME = "Такого имени у нас нет"
ALREADY_BANNED = "Такое имя уже заблокировано"
BAN_OK = "Вы заблокировали имя: {}"

UNBAN_NAME = "Вы хотите разблокировать оценивание имени. Введите его:"
NAME_NOT_BANNED = "Такое имя не заблокировано"
UNBAN_OK = "Вы разблокировали имя: {}"

NOT_BANNED_NAMES = "У вас нет забанненых имен"
BANNED_NAMES = "Имена, которые вы заблокировали:\n"
NAME = "{}\n"

GET_RATE_NAMES = "Получение вашего рейтинга имен:\n"
GET_RATE_NAMES_WOMAN = "Женские имена:\n"
GET_RATE_NAMES_MAN = "\nМужские имена:\n"
RATE_NAME_BANNED = "{} | Заблокировано \n"
RATE_NAME_NOT_BANNED = "{} | Tier {} | Рейтинг {}\n"

GROUP_RATE = "Введите ID группы, у который вы хотите получить рейтинг имён"
GET_GROUP_RATE = "Получение рейтинга имен группы {}:\n"
GROUP_RATE_NAME_NOT_BANNED = "{} | Рейтинг {}\n"

SELECT_FIELD_RATE = "Выберите способ ранжирования: "
FIELD_LIST_RATE = ["Определение Tier", "Сравнение в Tier 1-2"]
CHOOSE_TIER_FOR_NAME = "Выберите Tier для имени: {}"
FIELD_TIER = ["Лучшее", "Возможное", "Сомнительное", "Неподходящее"]
CHOOSE_TIER_OK = "Вы оценили это имя!"
NO_CHOOSE_FOR_TIER = "Имен для оценивания Tier не осталось!"

CHOOSE_NAME = "Выберите лучшее из двух имен:"
COMPARE_OK = "Вы сравнили имена"
NO_COMPARE = "Нет имен для сравнения"

SELECT_GENDER_FILTER = "Имена какого пола вы хотите оценивать?"
FILTER_GENDER_LIST = ["Женские", "Мужские"]
NO_GENDER_FILTER = "Такого пола нет!"
SELECT_FIRST_LETTER_FILTER = "На какую букву будут начинаться имена? Введите заглавную букву (если нет этого фильтра - 0):"
FILTER_FIRST = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Ш",
                "У", "Я", "Х", "Ч", "Э", 0]
NO_FIRST_LETTER = "Нет такой первой буквы имени!"
NO_FIRST_LETTER_TO_GENDER = "У выбранного пола нет имен на такую букву!"

COMPLETE_LIST = ["Продолжить", "/cancel"]
CONTINUE = "Еще имена для ранжирования!"

QUERY_TO_ADD_RATE_NAMES = """ ($rate_id, $user_id, 0, false, 0, 0),
($rate_id, $user_id, 1, false, 0, 0),
($rate_id, $user_id, 2, false, 0, 0),
($rate_id, $user_id, 3, false, 0, 0),
($rate_id, $user_id, 4, false, 0, 0),
($rate_id, $user_id, 5, false, 0, 0),
($rate_id, $user_id, 6, false, 0, 0),
($rate_id, $user_id, 7, false, 0, 0),
($rate_id, $user_id, 8, false, 0, 0),
($rate_id, $user_id, 9, false, 0, 0),
($rate_id, $user_id, 10, false, 0, 0),
($rate_id, $user_id, 11, false, 0, 0),
($rate_id, $user_id, 12, false, 0, 0),
($rate_id, $user_id, 13, false, 0, 0),
($rate_id, $user_id, 14, false, 0, 0),
($rate_id, $user_id, 15, false, 0, 0),
($rate_id, $user_id, 16, false, 0, 0),
($rate_id, $user_id, 17, false, 0, 0),
($rate_id, $user_id, 18, false, 0, 0),
($rate_id, $user_id, 19, false, 0, 0),
($rate_id, $user_id, 20, false, 0, 0),
($rate_id, $user_id, 21, false, 0, 0),
($rate_id, $user_id, 22, false, 0, 0),
($rate_id, $user_id, 23, false, 0, 0),
($rate_id, $user_id, 24, false, 0, 0),
($rate_id, $user_id, 25, false, 0, 0),
($rate_id, $user_id, 26, false, 0, 0),
($rate_id, $user_id, 27, false, 0, 0),
($rate_id, $user_id, 28, false, 0, 0),
($rate_id, $user_id, 29, false, 0, 0),
($rate_id, $user_id, 30, false, 0, 0),
($rate_id, $user_id, 31, false, 0, 0),
($rate_id, $user_id, 32, false, 0, 0),
($rate_id, $user_id, 33, false, 0, 0),
($rate_id, $user_id, 34, false, 0, 0),
($rate_id, $user_id, 35, false, 0, 0),
($rate_id, $user_id, 36, false, 0, 0),
($rate_id, $user_id, 37, false, 0, 0),
($rate_id, $user_id, 38, false, 0, 0),
($rate_id, $user_id, 39, false, 0, 0),
($rate_id, $user_id, 40, false, 0, 0),
($rate_id, $user_id, 41, false, 0, 0),
($rate_id, $user_id, 42, false, 0, 0),
($rate_id, $user_id, 43, false, 0, 0),
($rate_id, $user_id, 44, false, 0, 0),
($rate_id, $user_id, 45, false, 0, 0),
($rate_id, $user_id, 46, false, 0, 0),
($rate_id, $user_id, 47, false, 0, 0),
($rate_id, $user_id, 48, false, 0, 0),
($rate_id, $user_id, 49, false, 0, 0),
($rate_id, $user_id, 50, false, 0, 0),
($rate_id, $user_id, 51, false, 0, 0),
($rate_id, $user_id, 52, false, 0, 0),
($rate_id, $user_id, 53, false, 0, 0),
($rate_id, $user_id, 54, false, 0, 0),
($rate_id, $user_id, 55, false, 0, 0),
($rate_id, $user_id, 56, false, 0, 0),
($rate_id, $user_id, 57, false, 0, 0),
($rate_id, $user_id, 58, false, 0, 0),
($rate_id, $user_id, 59, false, 0, 0),
($rate_id, $user_id, 60, false, 0, 0),
($rate_id, $user_id, 61, false, 0, 0),
($rate_id, $user_id, 62, false, 0, 0),
($rate_id, $user_id, 63, false, 0, 0),
($rate_id, $user_id, 64, false, 0, 0),
($rate_id, $user_id, 65, false, 0, 0),
($rate_id, $user_id, 66, false, 0, 0),
($rate_id, $user_id, 67, false, 0, 0),
($rate_id, $user_id, 68, false, 0, 0),
($rate_id, $user_id, 69, false, 0, 0),
($rate_id, $user_id, 70, false, 0, 0),
($rate_id, $user_id, 71, false, 0, 0),
($rate_id, $user_id, 72, false, 0, 0),
($rate_id, $user_id, 73, false, 0, 0),
($rate_id, $user_id, 74, false, 0, 0),
($rate_id, $user_id, 75, false, 0, 0),
($rate_id, $user_id, 76, false, 0, 0),
($rate_id, $user_id, 77, false, 0, 0),
($rate_id, $user_id, 78, false, 0, 0),
($rate_id, $user_id, 79, false, 0, 0),
($rate_id, $user_id, 80, false, 0, 0),
($rate_id, $user_id, 81, false, 0, 0),
($rate_id, $user_id, 82, false, 0, 0),
($rate_id, $user_id, 83, false, 0, 0),
($rate_id, $user_id, 84, false, 0, 0),
($rate_id, $user_id, 85, false, 0, 0),
($rate_id, $user_id, 86, false, 0, 0),
($rate_id, $user_id, 87, false, 0, 0),
($rate_id, $user_id, 88, false, 0, 0),
($rate_id, $user_id, 89, false, 0, 0),
($rate_id, $user_id, 90, false, 0, 0),
($rate_id, $user_id, 91, false, 0, 0),
($rate_id, $user_id, 92, false, 0, 0),
($rate_id, $user_id, 93, false, 0, 0),
($rate_id, $user_id, 94, false, 0, 0),
($rate_id, $user_id, 95, false, 0, 0),
($rate_id, $user_id, 96, false, 0, 0),
($rate_id, $user_id, 97, false, 0, 0),
($rate_id, $user_id, 98, false, 0, 0),
($rate_id, $user_id, 99, false, 0, 0),
($rate_id, $user_id, 100, false, 0, 0),
($rate_id, $user_id, 101, false, 0, 0),
($rate_id, $user_id, 102, false, 0, 0),
($rate_id, $user_id, 103, false, 0, 0),
($rate_id, $user_id, 104, false, 0, 0),
($rate_id, $user_id, 105, false, 0, 0),
($rate_id, $user_id, 106, false, 0, 0),
($rate_id, $user_id, 107, false, 0, 0),
($rate_id, $user_id, 108, false, 0, 0),
($rate_id, $user_id, 109, false, 0, 0),
($rate_id, $user_id, 110, false, 0, 0),
($rate_id, $user_id, 111, false, 0, 0),
($rate_id, $user_id, 112, false, 0, 0),
($rate_id, $user_id, 113, false, 0, 0),
($rate_id, $user_id, 114, false, 0, 0),
($rate_id, $user_id, 115, false, 0, 0),
($rate_id, $user_id, 116, false, 0, 0),
($rate_id, $user_id, 117, false, 0, 0),
($rate_id, $user_id, 118, false, 0, 0),
($rate_id, $user_id, 119, false, 0, 0),
($rate_id, $user_id, 120, false, 0, 0),
($rate_id, $user_id, 121, false, 0, 0),
($rate_id, $user_id, 122, false, 0, 0),
($rate_id, $user_id, 123, false, 0, 0),
($rate_id, $user_id, 124, false, 0, 0),
($rate_id, $user_id, 125, false, 0, 0),
($rate_id, $user_id, 126, false, 0, 0),
($rate_id, $user_id, 127, false, 0, 0),
($rate_id, $user_id, 128, false, 0, 0),
($rate_id, $user_id, 129, false, 0, 0),
($rate_id, $user_id, 130, false, 0, 0),
($rate_id, $user_id, 131, false, 0, 0),
($rate_id, $user_id, 132, false, 0, 0),
($rate_id, $user_id, 133, false, 0, 0),
($rate_id, $user_id, 134, false, 0, 0),
($rate_id, $user_id, 135, false, 0, 0),
($rate_id, $user_id, 136, false, 0, 0),
($rate_id, $user_id, 137, false, 0, 0),
($rate_id, $user_id, 138, false, 0, 0),
($rate_id, $user_id, 139, false, 0, 0),
($rate_id, $user_id, 140, false, 0, 0),
($rate_id, $user_id, 141, false, 0, 0),
($rate_id, $user_id, 142, false, 0, 0),
($rate_id, $user_id, 143, false, 0, 0),
($rate_id, $user_id, 144, false, 0, 0),
($rate_id, $user_id, 145, false, 0, 0),
($rate_id, $user_id, 146, false, 0, 0),
($rate_id, $user_id, 147, false, 0, 0),
($rate_id, $user_id, 148, false, 0, 0),
($rate_id, $user_id, 149, false, 0, 0),
($rate_id, $user_id, 150, false, 0, 0),
($rate_id, $user_id, 151, false, 0, 0),
($rate_id, $user_id, 152, false, 0, 0),
($rate_id, $user_id, 153, false, 0, 0),
($rate_id, $user_id, 154, false, 0, 0),
($rate_id, $user_id, 155, false, 0, 0),
($rate_id, $user_id, 156, false, 0, 0),
($rate_id, $user_id, 157, false, 0, 0),
($rate_id, $user_id, 158, false, 0, 0),
($rate_id, $user_id, 159, false, 0, 0),
($rate_id, $user_id, 160, false, 0, 0),
($rate_id, $user_id, 161, false, 0, 0),
($rate_id, $user_id, 162, false, 0, 0),
($rate_id, $user_id, 163, false, 0, 0),
($rate_id, $user_id, 164, false, 0, 0),
($rate_id, $user_id, 165, false, 0, 0),
($rate_id, $user_id, 166, false, 0, 0),
($rate_id, $user_id, 167, false, 0, 0),
($rate_id, $user_id, 168, false, 0, 0),
($rate_id, $user_id, 169, false, 0, 0),
($rate_id, $user_id, 170, false, 0, 0),
($rate_id, $user_id, 171, false, 0, 0),
($rate_id, $user_id, 172, false, 0, 0),
($rate_id, $user_id, 173, false, 0, 0),
($rate_id, $user_id, 174, false, 0, 0),
($rate_id, $user_id, 175, false, 0, 0),
($rate_id, $user_id, 176, false, 0, 0),
($rate_id, $user_id, 177, false, 0, 0),
($rate_id, $user_id, 178, false, 0, 0),
($rate_id, $user_id, 179, false, 0, 0),
($rate_id, $user_id, 180, false, 0, 0),
($rate_id, $user_id, 181, false, 0, 0),
($rate_id, $user_id, 182, false, 0, 0),
($rate_id, $user_id, 183, false, 0, 0),
($rate_id, $user_id, 184, false, 0, 0),
($rate_id, $user_id, 185, false, 0, 0),
($rate_id, $user_id, 186, false, 0, 0),
($rate_id, $user_id, 187, false, 0, 0),
($rate_id, $user_id, 188, false, 0, 0),
($rate_id, $user_id, 189, false, 0, 0),
($rate_id, $user_id, 190, false, 0, 0),
($rate_id, $user_id, 191, false, 0, 0),
($rate_id, $user_id, 192, false, 0, 0),
($rate_id, $user_id, 193, false, 0, 0),
($rate_id, $user_id, 194, false, 0, 0),
($rate_id, $user_id, 195, false, 0, 0),
($rate_id, $user_id, 196, false, 0, 0),
($rate_id, $user_id, 197, false, 0, 0),
($rate_id, $user_id, 198, false, 0, 0),
($rate_id, $user_id, 199, false, 0, 0),
($rate_id, $user_id, 200, false, 0, 0),
($rate_id, $user_id, 201, false, 0, 0),
($rate_id, $user_id, 202, false, 0, 0),
($rate_id, $user_id, 203, false, 0, 0),
($rate_id, $user_id, 204, false, 0, 0),
($rate_id, $user_id, 205, false, 0, 0),
($rate_id, $user_id, 206, false, 0, 0),
($rate_id, $user_id, 207, false, 0, 0),
($rate_id, $user_id, 208, false, 0, 0),
($rate_id, $user_id, 209, false, 0, 0),
($rate_id, $user_id, 210, false, 0, 0),
($rate_id, $user_id, 211, false, 0, 0),
($rate_id, $user_id, 212, false, 0, 0),
($rate_id, $user_id, 213, false, 0, 0),
($rate_id, $user_id, 214, false, 0, 0),
($rate_id, $user_id, 215, false, 0, 0),
($rate_id, $user_id, 216, false, 0, 0),
($rate_id, $user_id, 217, false, 0, 0),
($rate_id, $user_id, 218, false, 0, 0),
($rate_id, $user_id, 219, false, 0, 0),
($rate_id, $user_id, 220, false, 0, 0),
($rate_id, $user_id, 221, false, 0, 0),
($rate_id, $user_id, 222, false, 0, 0),
($rate_id, $user_id, 223, false, 0, 0),
($rate_id, $user_id, 224, false, 0, 0),
($rate_id, $user_id, 225, false, 0, 0),
($rate_id, $user_id, 226, false, 0, 0),
($rate_id, $user_id, 227, false, 0, 0),
($rate_id, $user_id, 228, false, 0, 0),
($rate_id, $user_id, 229, false, 0, 0),
($rate_id, $user_id, 230, false, 0, 0),
($rate_id, $user_id, 231, false, 0, 0),
($rate_id, $user_id, 232, false, 0, 0),
($rate_id, $user_id, 233, false, 0, 0),
($rate_id, $user_id, 234, false, 0, 0),
($rate_id, $user_id, 235, false, 0, 0),
($rate_id, $user_id, 236, false, 0, 0),
($rate_id, $user_id, 237, false, 0, 0),
($rate_id, $user_id, 238, false, 0, 0),
($rate_id, $user_id, 239, false, 0, 0),
($rate_id, $user_id, 240, false, 0, 0),
($rate_id, $user_id, 241, false, 0, 0),
($rate_id, $user_id, 242, false, 0, 0),
($rate_id, $user_id, 243, false, 0, 0),
($rate_id, $user_id, 244, false, 0, 0),
($rate_id, $user_id, 245, false, 0, 0),
($rate_id, $user_id, 246, false, 0, 0),
($rate_id, $user_id, 247, false, 0, 0),
($rate_id, $user_id, 248, false, 0, 0),
($rate_id, $user_id, 249, false, 0, 0),
($rate_id, $user_id, 250, false, 0, 0),
($rate_id, $user_id, 251, false, 0, 0),
($rate_id, $user_id, 252, false, 0, 0),
($rate_id, $user_id, 253, false, 0, 0),
($rate_id, $user_id, 254, false, 0, 0),
($rate_id, $user_id, 255, false, 0, 0),
($rate_id, $user_id, 256, false, 0, 0),
($rate_id, $user_id, 257, false, 0, 0),
($rate_id, $user_id, 258, false, 0, 0),
($rate_id, $user_id, 259, false, 0, 0),
($rate_id, $user_id, 260, false, 0, 0),
($rate_id, $user_id, 261, false, 0, 0),
($rate_id, $user_id, 262, false, 0, 0),
($rate_id, $user_id, 263, false, 0, 0),
($rate_id, $user_id, 264, false, 0, 0),
($rate_id, $user_id, 265, false, 0, 0),
($rate_id, $user_id, 266, false, 0, 0),
($rate_id, $user_id, 267, false, 0, 0),
($rate_id, $user_id, 268, false, 0, 0),
($rate_id, $user_id, 269, false, 0, 0),
($rate_id, $user_id, 270, false, 0, 0),
($rate_id, $user_id, 271, false, 0, 0),
($rate_id, $user_id, 272, false, 0, 0),
($rate_id, $user_id, 273, false, 0, 0),
($rate_id, $user_id, 274, false, 0, 0),
($rate_id, $user_id, 275, false, 0, 0),
($rate_id, $user_id, 276, false, 0, 0),
($rate_id, $user_id, 277, false, 0, 0),
($rate_id, $user_id, 278, false, 0, 0),
($rate_id, $user_id, 279, false, 0, 0),
($rate_id, $user_id, 280, false, 0, 0),
($rate_id, $user_id, 281, false, 0, 0),
($rate_id, $user_id, 282, false, 0, 0),
($rate_id, $user_id, 283, false, 0, 0),
($rate_id, $user_id, 284, false, 0, 0),
($rate_id, $user_id, 285, false, 0, 0),
($rate_id, $user_id, 286, false, 0, 0),
($rate_id, $user_id, 287, false, 0, 0),
($rate_id, $user_id, 288, false, 0, 0),
($rate_id, $user_id, 289, false, 0, 0),
($rate_id, $user_id, 290, false, 0, 0),
($rate_id, $user_id, 291, false, 0, 0),
($rate_id, $user_id, 292, false, 0, 0),
($rate_id, $user_id, 293, false, 0, 0),
($rate_id, $user_id, 294, false, 0, 0),
($rate_id, $user_id, 295, false, 0, 0),
($rate_id, $user_id, 296, false, 0, 0),
($rate_id, $user_id, 297, false, 0, 0),
($rate_id, $user_id, 298, false, 0, 0),
($rate_id, $user_id, 299, false, 0, 0),
($rate_id, $user_id, 300, false, 0, 0),
($rate_id, $user_id, 301, false, 0, 0),
($rate_id, $user_id, 302, false, 0, 0),
($rate_id, $user_id, 303, false, 0, 0),
($rate_id, $user_id, 304, false, 0, 0),
($rate_id, $user_id, 305, false, 0, 0),
($rate_id, $user_id, 306, false, 0, 0),
($rate_id, $user_id, 307, false, 0, 0),
($rate_id, $user_id, 308, false, 0, 0),
($rate_id, $user_id, 309, false, 0, 0),
($rate_id, $user_id, 310, false, 0, 0),
($rate_id, $user_id, 311, false, 0, 0),
($rate_id, $user_id, 312, false, 0, 0),
($rate_id, $user_id, 313, false, 0, 0),
($rate_id, $user_id, 314, false, 0, 0),
($rate_id, $user_id, 315, false, 0, 0),
($rate_id, $user_id, 316, false, 0, 0),
($rate_id, $user_id, 317, false, 0, 0),
($rate_id, $user_id, 318, false, 0, 0),
($rate_id, $user_id, 319, false, 0, 0),
($rate_id, $user_id, 320, false, 0, 0),
($rate_id, $user_id, 321, false, 0, 0),
($rate_id, $user_id, 322, false, 0, 0),
($rate_id, $user_id, 323, false, 0, 0),
($rate_id, $user_id, 324, false, 0, 0),
($rate_id, $user_id, 325, false, 0, 0),
($rate_id, $user_id, 326, false, 0, 0),
($rate_id, $user_id, 327, false, 0, 0),
($rate_id, $user_id, 328, false, 0, 0),
($rate_id, $user_id, 329, false, 0, 0),
($rate_id, $user_id, 330, false, 0, 0),
($rate_id, $user_id, 331, false, 0, 0),
($rate_id, $user_id, 332, false, 0, 0),
($rate_id, $user_id, 333, false, 0, 0),
($rate_id, $user_id, 334, false, 0, 0),
($rate_id, $user_id, 335, false, 0, 0),
($rate_id, $user_id, 336, false, 0, 0),
($rate_id, $user_id, 337, false, 0, 0),
($rate_id, $user_id, 338, false, 0, 0),
($rate_id, $user_id, 339, false, 0, 0),
($rate_id, $user_id, 340, false, 0, 0),
($rate_id, $user_id, 341, false, 0, 0),
($rate_id, $user_id, 342, false, 0, 0),
($rate_id, $user_id, 343, false, 0, 0),
($rate_id, $user_id, 344, false, 0, 0),
($rate_id, $user_id, 345, false, 0, 0),
($rate_id, $user_id, 346, false, 0, 0),
($rate_id, $user_id, 347, false, 0, 0),
($rate_id, $user_id, 348, false, 0, 0),
($rate_id, $user_id, 349, false, 0, 0),
($rate_id, $user_id, 350, false, 0, 0),
($rate_id, $user_id, 351, false, 0, 0),
($rate_id, $user_id, 352, false, 0, 0),
($rate_id, $user_id, 353, false, 0, 0),
($rate_id, $user_id, 354, false, 0, 0),
($rate_id, $user_id, 355, false, 0, 0),
($rate_id, $user_id, 356, false, 0, 0),
($rate_id, $user_id, 357, false, 0, 0),
($rate_id, $user_id, 358, false, 0, 0),
($rate_id, $user_id, 359, false, 0, 0),
($rate_id, $user_id, 360, false, 0, 0),
($rate_id, $user_id, 361, false, 0, 0),
($rate_id, $user_id, 362, false, 0, 0),
($rate_id, $user_id, 363, false, 0, 0),
($rate_id, $user_id, 364, false, 0, 0),
($rate_id, $user_id, 365, false, 0, 0),
($rate_id, $user_id, 366, false, 0, 0),
($rate_id, $user_id, 367, false, 0, 0),
($rate_id, $user_id, 368, false, 0, 0),
($rate_id, $user_id, 369, false, 0, 0),
($rate_id, $user_id, 370, false, 0, 0),
($rate_id, $user_id, 371, false, 0, 0),
($rate_id, $user_id, 372, false, 0, 0),
($rate_id, $user_id, 373, false, 0, 0),
($rate_id, $user_id, 374, false, 0, 0),
($rate_id, $user_id, 375, false, 0, 0),
($rate_id, $user_id, 376, false, 0, 0),
($rate_id, $user_id, 377, false, 0, 0),
($rate_id, $user_id, 378, false, 0, 0),
($rate_id, $user_id, 379, false, 0, 0),
($rate_id, $user_id, 380, false, 0, 0),
($rate_id, $user_id, 381, false, 0, 0),
($rate_id, $user_id, 382, false, 0, 0),
($rate_id, $user_id, 383, false, 0, 0),
($rate_id, $user_id, 384, false, 0, 0),
($rate_id, $user_id, 385, false, 0, 0),
($rate_id, $user_id, 386, false, 0, 0),
($rate_id, $user_id, 387, false, 0, 0),
($rate_id, $user_id, 388, false, 0, 0),
($rate_id, $user_id, 389, false, 0, 0),
($rate_id, $user_id, 390, false, 0, 0),
($rate_id, $user_id, 391, false, 0, 0),
($rate_id, $user_id, 392, false, 0, 0),
($rate_id, $user_id, 393, false, 0, 0),
($rate_id, $user_id, 394, false, 0, 0),
($rate_id, $user_id, 395, false, 0, 0),
($rate_id, $user_id, 396, false, 0, 0),
($rate_id, $user_id, 397, false, 0, 0),
($rate_id, $user_id, 398, false, 0, 0),
($rate_id, $user_id, 399, false, 0, 0),
($rate_id, $user_id, 400, false, 0, 0),
($rate_id, $user_id, 401, false, 0, 0),
($rate_id, $user_id, 402, false, 0, 0),
($rate_id, $user_id, 403, false, 0, 0),
($rate_id, $user_id, 404, false, 0, 0),
($rate_id, $user_id, 405, false, 0, 0),
($rate_id, $user_id, 406, false, 0, 0),
($rate_id, $user_id, 407, false, 0, 0),
($rate_id, $user_id, 408, false, 0, 0),
($rate_id, $user_id, 409, false, 0, 0),
($rate_id, $user_id, 410, false, 0, 0),
($rate_id, $user_id, 411, false, 0, 0),
($rate_id, $user_id, 412, false, 0, 0),
($rate_id, $user_id, 413, false, 0, 0),
($rate_id, $user_id, 414, false, 0, 0),
($rate_id, $user_id, 415, false, 0, 0),
($rate_id, $user_id, 416, false, 0, 0),
($rate_id, $user_id, 417, false, 0, 0),
($rate_id, $user_id, 418, false, 0, 0),
($rate_id, $user_id, 419, false, 0, 0),
($rate_id, $user_id, 420, false, 0, 0),
($rate_id, $user_id, 421, false, 0, 0),
($rate_id, $user_id, 422, false, 0, 0),
($rate_id, $user_id, 423, false, 0, 0),
($rate_id, $user_id, 424, false, 0, 0),
($rate_id, $user_id, 425, false, 0, 0),
($rate_id, $user_id, 426, false, 0, 0);
"""
