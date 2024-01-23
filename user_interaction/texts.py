START = (
    "Добро пожаловать! Я бот для определения лучшего имени для ваших будущих детей!"
    "Вы можете составить свой рейтинг имён и вступить в группу для составления общего рейтинга\n\n"
    "Список доступных команд:\n"
    "/show_data\n"
    "/delete_account\n"
    "/change_data\n\n"
    "/create_group\n"
    "/show_groups\n"
    "/join\n\n"
)

IT_NOT_DIGIT = "Вы ввели не число"
NOT_REGISTERED = "Вы не зарегистрированы, используйте команду: /start"

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
UNKNOWN_FIELD = "Введите Имя или Фамилия"
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
ALL_GROUPS_DATA = "Название группы: {}\nИмя владельца: {} {}\n"
NOT_GROUPS = "Вы не состоите ни в одной группе"

JOIN_GROUP = "Введите ID группы, в которую хотите вступить:"
CANCEL_JOIN_GROUP = "Прекращено, вступление в группу не сохранено"
IT_NOT_GROUP_ID = "Введен несуществующий ID группы"
OK_JOIN_GROUP = "Вы вступили в группу: {}"
