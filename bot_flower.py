# from constants import *
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from constants import *
import time
import datetime

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import copy
import logging
weekadays =["Понедельник","Вторник","Среда","Четверг", "Пятница","Суббота","Воскресенье"]
def water_all():
    for j in list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT.keys()):
        for i in FLOWER_TOPICS_LIST_WITH_ROOM_DICT[j]:
            publish.single(topic=i + "/water", payload=MQTT_TEXT_TO_WATER, hostname=MQTT_HOST, port=MQTT_PORT,
                           auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)
            publish.single(topic=i + "/lastWater", payload=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), hostname=MQTT_HOST, port=MQTT_PORT,
                           auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)


def water_room(callback):
    room = callback.split("_")[0]  # beautiful smile "_" XD
    for i in list(FLOWER_TOPICS_LIST_WITH_ROOM_DICT[room].keys()):
        publish.single(topic=i + "/water", payload=MQTT_TEXT_TO_WATER, hostname=MQTT_HOST, port=MQTT_PORT,
                       auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)
        publish.single(topic=i + "/lastWater", payload=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), hostname=MQTT_HOST, port=MQTT_PORT,
                       auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)


def water_flower(flower_topic):
    publish.single(topic=flower_topic + "/water", payload=MQTT_TEXT_TO_WATER, hostname=MQTT_HOST, port=MQTT_PORT,
                   auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)
    publish.single(topic=flower_topic + "/lastWater", payload=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), hostname=MQTT_HOST, port=MQTT_PORT,
                   auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)


def generateTopics(mode):
    global MQTT_TOPIC_SETTINGS_MEASUREMENT, MQTT_TOPIC_GET_MEASUREMENT
    MQTT_TOPIC_SETTINGS_MEASUREMENT = (mode + "{0}").format(MQTT_TOPIC_SETTINGS_MEASUREMENT)
    MQTT_TOPIC_GET_MEASUREMENT = (mode + "{0}").format(MQTT_TOPIC_GET_MEASUREMENT)
    # print("in generateTopics")
    global FLOWER_TOPICS_LIST_WITH_ROOM_DICT
    copy_topics = copy.deepcopy(FLOWER_TOPICS_LIST_WITH_ROOM_DICT)
    for j in list(copy_topics.keys()):
        for i in copy_topics[j]:
            new = (mode + "{0}").format(i)
            old = i
            # print(new, old)
            FLOWER_TOPICS_LIST_WITH_ROOM_DICT[j][new] = FLOWER_TOPICS_LIST_WITH_ROOM_DICT[j].pop(old)


def getCurrentSettings(flowerTopic):
    topicsList = [flowerTopic + "/mode", flowerTopic + "/humidity", flowerTopic + "/humidityThreshold",
                  flowerTopic + "/dayWatering", flowerTopic + "/waterDelay", flowerTopic + "/waterDuration", flowerTopic+"/lastWater"]
    data = subscribe.simple(topicsList,
                            auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD},
                            hostname=MQTT_HOST, port=MQTT_PORT, msg_count=7, keepalive=10)
    decodeData = []
    for i in data:
        decodeData.append(i.payload.decode("utf-8"))
    strToReturn = "Режим:" + decodeData[0] + "\n"
    strToReturn += "Влажность:" + decodeData[1] + "%\n"
    strToReturn += "Порог влажности:" + decodeData[2] + "%\n"
    strToReturn += "День недели следующего полива:" + decodeData[3] +" (" +weekadays[int(decodeData[3])]+")\n"
    strToReturn += "Перерыв между поливами:" + decodeData[4] + " дней\n"
    strToReturn += "Продолжительность полива:" + decodeData[5] + " секунд\n"
    strToReturn += "Последний полив:" + decodeData[6] + "\n"
    # print(strToReturn)
    return strToReturn


def getListOfSettingsForTopic(flowerTopic, room):
    listCallback = list(FLOWER_SETTINGS_LIST.keys())
    """
    keyboard = [[InlineKeyboardButton(text="Полить цветок", callback_data="water:" + flowerTopic),
                 InlineKeyboardButton(text=FLOWER_SETTINGS_LIST[listCallback[0]],
                                      callback_data="waterDuration:" + flowerTopic)], [
                    InlineKeyboardButton(text="Задержка между поливами",
                                         callback_data="waterDelay:" + flowerTopic),
                    InlineKeyboardButton(text="Изменить день полива",
                                         callback_data="dayWatering:" + flowerTopic)], [
                    InlineKeyboardButton(text="порог влажности",
                                         callback_data="humidityThreshold:" + flowerTopic),
                    InlineKeyboardButton(text="Режим",
                                         callback_data="mode:" + flowerTopic)], ]"""
    keyboard = [[InlineKeyboardButton(text="Полить цветок", callback_data="water:" + flowerTopic)]]
    for i in range(len(listCallback)):
        if i % 2 == 1:
            keyboard[i // 2].append(
                InlineKeyboardButton(text=FLOWER_SETTINGS_LIST[listCallback[i]],
                                     callback_data=listCallback[i] + ":" + flowerTopic))
        else:
            keyboard.append([
                InlineKeyboardButton(text=FLOWER_SETTINGS_LIST[listCallback[i]],
                                     callback_data=listCallback[i] + ":" + flowerTopic)])
    keyboard.append([
        InlineKeyboardButton(text="Вернуться назад",
                             callback_data=room)])
    keyboard.append([
        InlineKeyboardButton(text=KEYBOARD_TEXT_MAIN_MENU,
                             callback_data=KEYBOARD_CALLBACK_MAIN_MENU)])
    listButton = InlineKeyboardMarkup(keyboard
                                      )

    return listButton


def waitForNextWateringInMode1(flowerTopic):
    """
    0 = mode
    1 = humidity
    2 = humidityThreshold
    3 = dayWatering
    4 = waterDelay
    """
    topicsList = [flowerTopic + "/mode", flowerTopic + "/humidity", flowerTopic + "/humidityThreshold",
                  flowerTopic + "/dayWatering", flowerTopic + "/waterDelay"]
    while True:

        data = subscribe.simple(topicsList,
                                auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD},
                                hostname=MQTT_HOST, port=MQTT_PORT, msg_count=5)
        decodeData = []
        # print(data.payload)
        for i in data:
            decodeData.append(i.payload.decode("utf-8"))
        #   print(decodeData)
        mode = decodeData[0]
        #  print("Mode " + mode)
        if mode == "humidity":
            humidity = decodeData[1]
            humidityThreshold = decodeData[2]
            if humidity <= humidityThreshold:
                publish.single(topic=flowerTopic + "/water", payload=MQTT_TEXT_TO_WATER, hostname=MQTT_HOST,
                               port=MQTT_PORT,
                               auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)
        elif mode == "time":
            if datetime.datetime.now().hour == 10:
                dayWatering = int(decodeData[3])
                delayWatering = int(decodeData[4])

                if dayWatering == datetime.datetime.today().weekday():
                    #     print("need to water")
                    nextDayWatering = (dayWatering + delayWatering) % 7
                    publish.multiple(msgs=[(flowerTopic + "/water", MQTT_TEXT_TO_WATER, 0, True),
                                           (flowerTopic + "/dayWatering", nextDayWatering, 0, True)],
                                     hostname=MQTT_HOST,
                                     port=MQTT_PORT,
                                     auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD})

        elif mode == "manual":
            pass
        publish.single(topic=flowerTopic + "/heartbeat", payload=str(datetime.datetime.now()), hostname=MQTT_HOST,
                       port=MQTT_PORT,
                       auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)
        time.sleep(600)


def sendCommandToGetMeasurement():
    global MQTT_TOPIC_SETTINGS_MEASUREMENT, MQTT_TOPIC_GET_MEASUREMENT
    while True:


        #    print("started")
        # print(MQTT_TOPIC_SETTINGS_MEASUREMENT)

        data = subscribe.simple(topics=
                                MQTT_TOPIC_SETTINGS_MEASUREMENT,
                                auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD},
                                hostname=MQTT_HOST, port=MQTT_PORT, msg_count=1)
        logging.info("Subscribed to MQTT_TOPIC_SETTINGS_MEASUREMENT")
        decodeData = []
        # print(data.payload)

        decodeData.append(int(data.payload.decode("utf-8")))

        publish.single(topic=MQTT_TOPIC_GET_MEASUREMENT, payload="1", hostname=MQTT_HOST,
                       port=MQTT_PORT,
                       auth={"username": MQTT_LOGIN, "password": MQTT_PASSWORD}, retain=True)
        logging.info("Sent to MQTT_TOPIC_GET_MEASUREMENT 1. Go to sleep %s seconds", decodeData[0])
        time.sleep(decodeData[0])
#print(getCurrentSettings("home/watering/balcony-1/flower/3"))