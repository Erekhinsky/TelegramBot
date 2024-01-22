START = (
    "Hello! This is a simple bot that can store your name and age, "
    "show them back to you and delete them if requested.\n\n"
    "List of commands:\n"
    "/start\n"
    "/register\n"
    "/show_data\n"
    "/delete_account\n"
    "/create_group\n"
    "/join"
)

IT_NOT_DIGIT = "Вы ввели не число"

FIRST_NAME = "Enter your first name."
LAST_NAME = "Enter your last name."

SHOW_DATA = "First name: {}\nLast name: {}"

DATA_IS_SAVED = "Your data is saved!\n" + SHOW_DATA
ALREADY_REGISTERED = "You are already registered!\n" + SHOW_DATA
SHOW_DATA_WITH_PREFIX = "Your data:\n" + SHOW_DATA

NOT_REGISTERED = "You are not registered yet, try /register."

CANCEL_REGISTER = "Cancelled! Your data is not saved."

DELETE_ACCOUNT = "Are you sure you want to delete your account?"
DELETE_ACCOUNT_OPTIONS = {"Yes!": True, "No..": False}
DELETE_ACCOUNT_UNKNOWN = "I don't understand this command."
DELETE_ACCOUNT_DONE = "Done! You can /register again."
DELETE_ACCOUNT_CANCEL = "Ok, stay for longer!"

FIELD_LIST = ["first_name", "last_name"]
UNKNOWN_FIELD = "Unknown field, choose a field from the list below:"
SELECT_FIELD = "Choose a field to change:"
WRITE_NEW_VALUE = "Write new value for the field {}"
CANCEL_CHANGE = "Cancelled! Your data is not changed."
CHANGE_DATA_DONE = "Done! Your data is updated."

GROUP_NAME = "Введите имя группы"
CANCEL_CREATE_GROUP = "Прекращено, ваша группа не сохранена"
GROUP_DATA_IS_SAVED = "Ваша группа сохранена:\nID группы: {}\nНазвание группы: {}\n"
SHOW_USER_GROUPS = "Ваши подконтрольные группы:\nID группы: {}\nНазвание группы: {}\n\n"
SHOW_ALL_GROUPS = "Ваши группы, где вы не владелец:\nНазвание группы: {}\nИмя владельца: {} {}\n"
NOT_GROUPS = "Вы не состоите ни в одной группе"

JOIN_GROUP = "Введите ID группы, в которую хотите вступить:"
CANCEL_JOIN_GROUP = "Прекращено, вступление в группу не сохранено"
IT_NOT_GROUP_ID = "Введен несуществующий ID группы"
OK_JOIN_GROUP = "Вы вступили в группу: {}"
