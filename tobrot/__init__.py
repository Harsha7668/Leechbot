#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import os
import time
import socket
from tobrot.config import Config

socket.setdefaulttimeout(600)
botStartTime = time.time()

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    # Add your code here if you need to handle the case when ENV is set to True.
    # If there's no code needed, you can add 'pass' to avoid errors.
    pass

# Continue with the rest of your code
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH_CHANNEL = list(Config.AUTH_CHANNEL)
AUTH_CHANNEL.append(539295917)
AUTH_CHANNEL = list(set(AUTH_CHANNEL))
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
CHUNK_SIZE = Config.CHUNK_SIZE
DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT
ARIA_TWO_STARTED_PORT = Config.ARIA_TWO_STARTED_PORT
MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = Config.MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START
MAX_TG_SPLIT_FILE_SIZE = Config.MAX_TG_SPLIT_FILE_SIZE
FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR
UN_FINISHED_PROGRESS_STR = Config.UN_FINISHED_PROGRESS_STR
TG_OFFENSIVE_API = Config.TG_OFFENSIVE_API
CUSTOM_FILE_NAME = Config.CUSTOM_FILE_NAME
RCLONE_CONFIG = Config.RCLONE_CONFIG
DESTINATION_FOLDER = Config.DESTINATION_FOLDER
INDEX_LINK = Config.INDEX_LINK
