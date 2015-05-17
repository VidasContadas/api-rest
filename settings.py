# coding=utf-8
# Mongodb
DATABASE = "vidascontadas"

# Flask
DEBUG = False

try:
    from local_settings import *
except Exception as e:
    pass
