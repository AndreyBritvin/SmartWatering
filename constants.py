from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

MQTT_HOST = "XXX.XXX.X.X"
MQTT_PORT = XXXX
MQTT_LOGIN = "LOGIN"
MQTT_PASSWORD = "PASSWORD"
MQTT_TOPIC_DOOR_STAIRS = "corridor/door/stairs"
MQTT_TOPIC_DOOR_LIFT = "corridor/door/lift"
MQTT_TOPIC_DOOR_APARTMENT = "corridor/door/apartment"
MQTT_TEXT_TO_OPEN_DOOR = "on"  # on
MQTT_TEXT_TO_WATER = "on"  # on

LOG_FILE_NAME_PROD = "bot.log"
LOG_FILE_NAME_TEST = "bot_test.log"

TELEGRAM_ALLOWED_USERS_ID = ["IDS"
                             ]
USER_ID_TO_NAME = {"ID":"Name"
                   }
TELEGRAM_REPLAY_GROUPS_PROD = [  "IDS GROUPS prod"
]
TELEGRAM_REPLAY_GROUPS_TEST = ["IDS groups test"
                               ]
TELEGRAM_BOT_TOKEN_PROD = "TOKEN_PROD"  # smartHome_bot
TELEGRAM_BOT_TOKEN_TEST = "TOKEN_TEST"  # testBot

TELEGRAM_WEATHER_USER_LOCATION_LAST = {"ID":["longitude", "altitude"]}

TELEGRAM_MAIN_MENU_TEXT = "Выберите интересующий пункт меню:"

KEYBOARD_TEXT_MAIN_MENU = "Главное меню"
KEYBOARD_CALLBACK_MAIN_MENU = "главное меню"

KEYBOARD_MAIN_CALLBACK_LOCK = "ЗАМОК"
KEYBOARD_MAIN_CALLBACK_FLOWER = "СПИСОК КОМНАТ ДЛЯ РАСТЕНИЙ"
KEYBOARD_MAIN_CALLBACK_FLAT_CLIMATE = "КЛИМАТ КВАРТИРЫ"
KEYBOARD_MAIN_CALLBACK_WEATHER = "ПОГОДА"
KEYBOARD_MAIN_CALLBACK_HIDE_BUTTONS = "СКРЫТЬ КНОПКИ"

KEYBOARD_MAIN_TEXT_LOCK = "Открыть дверь"
KEYBOARD_MAIN_TEXT_FLOWER = "Полив растений"
KEYBOARD_MAIN_TEXT_FLAT_CLIMATE = "Климат квартиры"
KEYBOARD_MAIN_TEXT_WEATHER = "Погода"
KEYBOARD_MAIN_TEXT_HIDE_BUTTONS = "Скрыть кнопки"

KEYBOARD_MAIN = InlineKeyboardMarkup([
    [InlineKeyboardButton(KEYBOARD_MAIN_TEXT_LOCK, callback_data=KEYBOARD_MAIN_CALLBACK_LOCK),
     InlineKeyboardButton(KEYBOARD_MAIN_TEXT_FLOWER, callback_data=KEYBOARD_MAIN_CALLBACK_FLOWER)],
    [InlineKeyboardButton(KEYBOARD_MAIN_TEXT_FLAT_CLIMATE, callback_data=KEYBOARD_MAIN_CALLBACK_FLAT_CLIMATE)],
    [InlineKeyboardButton(KEYBOARD_MAIN_TEXT_WEATHER, callback_data=KEYBOARD_MAIN_CALLBACK_WEATHER)],
    [InlineKeyboardButton(KEYBOARD_MAIN_TEXT_HIDE_BUTTONS, callback_data=KEYBOARD_MAIN_CALLBACK_HIDE_BUTTONS)]])

KEYBOARD_DOOR_LIST_CALLBACK_LIFT = "у лифта"
KEYBOARD_DOOR_LIST_CALLBACK_STAIRS = "у лестницы"
KEYBOARD_DOOR_LIST_CALLBACK_APARTMENT = "в квартиру"
KEYBOARD_DOOR_LIST_CALLBACK_APARTMENT_AND_LIFT = "у лифта и в квартиру"
KEYBOARD_DOOR_LIST_CALLBACK_APARTMENT_AND_STAIRS = "у лестницы и в квартиру"

KEYBOARD_DOOR_LIST_TEXT_LIFT = "Лифтовая дверь"
KEYBOARD_DOOR_LIST_TEXT_STAIRS = "Лестничная дверь"
KEYBOARD_DOOR_LIST_TEXT_APARTMENT = "Квартира"
KEYBOARD_DOOR_LIST_TEXT_APARTMENT_AND_LIFT = "Лифтовая и квартира"
KEYBOARD_DOOR_LIST_TEXT_APARTMENT_AND_STAIRS = "Лестничная и квартира"

KEYBOARD_DOOR_LIST = InlineKeyboardMarkup([
    [InlineKeyboardButton(KEYBOARD_DOOR_LIST_TEXT_LIFT, callback_data=KEYBOARD_DOOR_LIST_CALLBACK_LIFT)],
    [InlineKeyboardButton(KEYBOARD_DOOR_LIST_TEXT_STAIRS, callback_data=KEYBOARD_DOOR_LIST_CALLBACK_STAIRS)],
    [InlineKeyboardButton(KEYBOARD_DOOR_LIST_TEXT_APARTMENT, callback_data=KEYBOARD_DOOR_LIST_CALLBACK_APARTMENT)],

    [InlineKeyboardButton(KEYBOARD_DOOR_LIST_TEXT_APARTMENT_AND_LIFT,
                          callback_data=KEYBOARD_DOOR_LIST_CALLBACK_APARTMENT_AND_LIFT),
     InlineKeyboardButton(KEYBOARD_DOOR_LIST_TEXT_APARTMENT_AND_STAIRS,
                          callback_data=KEYBOARD_DOOR_LIST_CALLBACK_APARTMENT_AND_STAIRS)],

    [InlineKeyboardButton(KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)]])

KEYBOARD_ROOM_ZAL = "Зал"
KEYBOARD_ROOM_ANDREY = "Андрей"
KEYBOARD_ROOM_KATYA = "Катя"
KEYBOARD_ROOM_KITCHEN = "Кухня"
KEYBOARD_ROOM_BALCONY1 = "Балкон-1"
KEYBOARD_ROOM_BALCONY2 = "Балкон-2"
KEYBOARD_ROOM_CORRIDOR = "Коридор"
KEYBOARD_ROOM_BATHROOM = "Ванная"

ROOM_LIST = [KEYBOARD_ROOM_ANDREY, KEYBOARD_ROOM_ZAL, KEYBOARD_ROOM_KATYA, KEYBOARD_ROOM_BATHROOM,
             KEYBOARD_ROOM_KITCHEN,
             KEYBOARD_ROOM_CORRIDOR, KEYBOARD_ROOM_BALCONY1, KEYBOARD_ROOM_BALCONY2]
ROOM_DICT_TOPIC = {KEYBOARD_ROOM_ANDREY: ["Andrey", 4],
                   KEYBOARD_ROOM_ZAL: ["zal", 4],
                   KEYBOARD_ROOM_KATYA: ["Katya", 3],
                   KEYBOARD_ROOM_BATHROOM: ["bathroom", 2],

                   }
KEYBOARD_ROOM_LIST = InlineKeyboardMarkup([
    [InlineKeyboardButton(KEYBOARD_ROOM_ZAL, callback_data=KEYBOARD_ROOM_ZAL),
     InlineKeyboardButton(KEYBOARD_ROOM_ANDREY, callback_data=KEYBOARD_ROOM_ANDREY),
     InlineKeyboardButton(KEYBOARD_ROOM_KATYA, callback_data=KEYBOARD_ROOM_KATYA)],
    [
        InlineKeyboardButton(KEYBOARD_ROOM_BATHROOM, callback_data=KEYBOARD_ROOM_BATHROOM),
        # InlineKeyboardButton(KEYBOARD_ROOM_BALCONY1, callback_data=KEYBOARD_ROOM_BALCONY1),
        # InlineKeyboardButton(KEYBOARD_ROOM_BALCONY2, callback_data=KEYBOARD_ROOM_BALCONY2)
    ],

    [
        # InlineKeyboardButton(KEYBOARD_ROOM_CORRIDOR, callback_data=KEYBOARD_ROOM_CORRIDOR)
    ],
    [InlineKeyboardButton(KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)]
])

TRANSLATIONS = {"temp": ["температура", "℃"],
                "humidity": ["влажность", "%"],
                "co2": ["CO2", "ppm"],
                "pressure": ["давление", "мм рт. ст."],
                "altitude": ["высота", "м"],
                "temperatureBME": ["температура", "℃"],
                "humidityBME": ["влажность", "%"],
                "magnet": ["магнетизм", "t"],
                }

KEYBOARD_TIME_WEATHER_LIST = InlineKeyboardMarkup([
    [InlineKeyboardButton("Сейчас", callback_data='Погода_сейчас'),
     InlineKeyboardButton("Завтра", callback_data='Погода_завтра')],
    # [InlineKeyboardButton("на 3 дня", callback_data='Погода_3'),
    # InlineKeyboardButton("Погода на неделю", callback_data='Погода_7')],
    [InlineKeyboardButton("Изменить местоположение", callback_data="Изменить местоположение")],
    [InlineKeyboardButton(KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)]])

CHANGE_LOCATION = ReplyKeyboardMarkup(
    [[KeyboardButton(text="Изменить локацию для погоды", resize_markup=True, request_location=True)]],
    resize_keyboard=True, one_time_keyboard=True)

KEYBOARD_FLOWER_CALLBACK_WATER_ALL = "полить всё"
KEYBOARD_FLOWER_CALLBACK_SHOW_FLOWER_LIST_BALCONY = "Балкон-1_список"
KEYBOARD_FLOWER_CALLBACK_WATER_BALCONY = "балкон-1_полив"
"""
KEYBOARD_FLOWER_ROOM_LIST = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(KEYBOARD_ROOM_BALCONY1, callback_data=KEYBOARD_FLOWER_CALLBACK_SHOW_FLOWER_LIST_BALCONY),
    ],
    [
        InlineKeyboardButton("Полить все", callback_data=KEYBOARD_FLOWER_CALLBACK_WATER_ALL)
    ],
    [InlineKeyboardButton(KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)]])
"""
HOME_TOPIC = "home"
TEST_TOPIC = "test"
MQTT_TOPIC_FLOWER_BALCONY_1_1 = "/watering/balcony-1/flower/1"  # Callback must be topic!!!
MQTT_TOPIC_FLOWER_BALCONY_1_2 = "/watering/balcony-1/flower/2"
MQTT_TOPIC_FLOWER_BALCONY_1_3 = "/watering/balcony-1/flower/3"
MQTT_TOPIC_FLOWER_BALCONY_1_4 = "/watering/balcony-1/flower/4"
MQTT_TOPIC_FLOWER_ANDREY_1 = "/watering/andrey/flower/1"
MQTT_TOPIC_FLOWER_ANDREY_2 = "/watering/andrey/flower/2"
MQTT_TOPIC_FLOWER_ANDREY_3 = "/watering/andrey/flower/3"
MQTT_TOPIC_FLOWER_ANDREY_4 = "/watering/andrey/flower/4"
MQTT_TOPIC_FLOWER_ANDREY_5 = "/watering/andrey/flower/5"
MQTT_TOPIC_FLOWER_ANDREY_6 = "/watering/andrey/flower/6"

FLOWER_TOPICS_LIST_WITH_ROOM_DICT = {
    "Балкон-1": {MQTT_TOPIC_FLOWER_BALCONY_1_1: "1", MQTT_TOPIC_FLOWER_BALCONY_1_2: "2",
                 MQTT_TOPIC_FLOWER_BALCONY_1_3: "3",
                 MQTT_TOPIC_FLOWER_BALCONY_1_4: "4"},

"Андрей": {MQTT_TOPIC_FLOWER_ANDREY_1: "1",
           MQTT_TOPIC_FLOWER_ANDREY_2: "2",
           MQTT_TOPIC_FLOWER_ANDREY_3: "3",
           MQTT_TOPIC_FLOWER_ANDREY_4: "4",
           MQTT_TOPIC_FLOWER_ANDREY_5: "5",
           MQTT_TOPIC_FLOWER_ANDREY_6: "6"}
}

"""
KEYBOARD_FLOWER_BALCONY_1_FLOWER_LIST = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("1", callback_data="Settings:" + MQTT_TOPIC_FLOWER_BALCONY_1_1),
        # Callback must be topic!!!
        InlineKeyboardButton("2", callback_data="Settings:" + MQTT_TOPIC_FLOWER_BALCONY_1_2),
        InlineKeyboardButton("3", callback_data="Settings:" + MQTT_TOPIC_FLOWER_BALCONY_1_3),
        InlineKeyboardButton("4", callback_data="Settings:" + MQTT_TOPIC_FLOWER_BALCONY_1_4),
    ],
    [InlineKeyboardButton("Полить все на балконе", callback_data=KEYBOARD_FLOWER_CALLBACK_WATER_BALCONY), ],
    [InlineKeyboardButton(KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)]
])"""
FLOWER_SETTINGS_LIST = {"waterDuration": "Продолжительность полива", "waterDelay": "Задержка между поливами",
                        "dayWatering": "День недели полива", "humidityThreshold": "Порог влажности", "mode": "Режим"}


def getKeyBoardForWatering():
    buttonsForKeyboard = []
    for i in range(len(list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT.keys()))):
        room = list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT.keys())[i]
        if i % 2 == 0:
            buttonsForKeyboard.append([InlineKeyboardButton(
                text=room,
                callback_data=room + "_список")])
        else:
            buttonsForKeyboard[i // 2].append(InlineKeyboardButton(
                text=room,
                callback_data=room + "_список"))
    buttonsForKeyboard.append(
        [InlineKeyboardButton(text="Полить все", callback_data=KEYBOARD_FLOWER_CALLBACK_WATER_ALL)])
    buttonsForKeyboard.append(
        [InlineKeyboardButton(text="Настройки", callback_data="Цветы_настройки")])
    buttonsForKeyboard.append(
        [InlineKeyboardButton(text=KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)])
    keyboard = InlineKeyboardMarkup(
        buttonsForKeyboard
    )
    return keyboard


def getKeyBoardForRoom(room):
    buttonsForKeyboard = []
    for i in range(len(FLOWER_TOPICS_LIST_WITH_ROOM_DICT[room])):
        # print(FLOWER_TOPICS_LIST_WITH_ROOM_DICT[room][i])
        topics = FLOWER_TOPICS_LIST_WITH_ROOM_DICT[room]

        topic = list(topics.keys())[i]

        if i % 4 == 0:

            buttonsForKeyboard.append(
                [InlineKeyboardButton(text=topics[topic],
                                      # callback_data="Settings:" + FLOWER_TOPICS_LIST_WITH_ROOM_DICT[room][i])])
                                      callback_data="Settings:" + topic)])
        else:
            buttonsForKeyboard[i // 4].append(
                InlineKeyboardButton(text=topics[topic],
                                     # callback_data="Settings:" + FLOWER_TOPICS_LIST_WITH_ROOM_DICT[room][i]))
                                     callback_data="Settings:" + topic))

    buttonsForKeyboard.append(
        [InlineKeyboardButton(text="Полить всё в данной комнате", callback_data=room + "_полив")])
    buttonsForKeyboard.append([InlineKeyboardButton(text="Вернуться", callback_data=KEYBOARD_MAIN_CALLBACK_FLOWER),
                               InlineKeyboardButton(text=KEYBOARD_TEXT_MAIN_MENU,
                                                    callback_data=KEYBOARD_CALLBACK_MAIN_MENU)])
    keyboard = InlineKeyboardMarkup(
        buttonsForKeyboard
    )
    return keyboard


KEYBOARD_FLOWER_ROOM_LIST = getKeyBoardForWatering()
# KEYBOARD_FLOWER_BALCONY_1_FLOWER_LIST = getKeyBoardForRoom("Балкон-1")

# WATERING_ROOM_CALLBACK_CONFORMITY = {WATERING_ROOM_CALLBACK_LIST[0]: KEYBOARD_FLOWER_BALCONY_1_FLOWER_LIST}
# WATERING_ROOM_CALLBACK_LIST = [KEYBOARD_FLOWER_CALLBACK_SHOW_FLOWER_LIST_BALCONY]
CALLBACK_LIST_TO_SHOW_FLOWERS_IN_THE_ROOM = []
CALLBACK_LIST_TO_WATER_ALL_FLOWERS_IN_THE_ROOM = []

# create callback to show keyboard with flowers list
# UPD1: and (water all flowers in room) = callback
# UPD2 to UPD1:callback to water all flowers in room
WATERING_ROOM_CALLBACK_CONFORMITY = {}


def generateKeyboards():
    for i in list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT.keys()):
        CALLBACK_LIST_TO_SHOW_FLOWERS_IN_THE_ROOM.append(i + "_список")
        CALLBACK_LIST_TO_WATER_ALL_FLOWERS_IN_THE_ROOM.append(i + "_полив")

    # create keyboards with flowers list
    for i in range(len(list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT.keys()))):
        WATERING_ROOM_CALLBACK_CONFORMITY[CALLBACK_LIST_TO_SHOW_FLOWERS_IN_THE_ROOM[i]] = getKeyBoardForRoom(
            list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT.keys())[i])


"""
BALCONY_1_FLOWER_LIST = [MQTT_TOPIC_FLOWER_BALCONY_1_1, MQTT_TOPIC_FLOWER_BALCONY_1_2, MQTT_TOPIC_FLOWER_BALCONY_1_3,
                         MQTT_TOPIC_FLOWER_BALCONY_1_4]  # list of flowers in room
ALL_ROOM_FLOWER_TOPIC_LIST = [BALCONY_1_FLOWER_LIST]  # list of rooms

CALLBACK_ROOM_CONFORMITY = {KEYBOARD_FLOWER_CALLBACK_WATER_BALCONY: BALCONY_1_FLOWER_LIST}"""
MQTT_TOPIC_SETTINGS_MEASUREMENT = "/watering/settings/delayHumidityMeasurement"
MQTT_TOPIC_GET_MEASUREMENT = "/watering/doMeasurement"
KEYBOARD_WATERING_SETTINGS = InlineKeyboardMarkup([
    [InlineKeyboardButton("Изменить интервал между измерениями", callback_data="Настройка_интервала")],

    [InlineKeyboardButton(KEYBOARD_TEXT_MAIN_MENU, callback_data=KEYBOARD_CALLBACK_MAIN_MENU)]])
