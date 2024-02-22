#Copyright (C) 2021-2024 Hiroki Fujii <hiroki@efuji.jp>

import config
CONFIG_GLOBAL_KEY = "actlab_USB-D_global"


def getEnableTurnOverSetting():
    try:
        return config.conf[CONFIG_GLOBAL_KEY]["enableTurnOver"]
    except:
        return False

def setEnableTurnOverSetting(val):
    config.conf[CONFIG_GLOBAL_KEY]["enableTurnOver"] = val

def initializeSettings():
    config.conf[CONFIG_GLOBAL_KEY] = {
        "enableTurnOver": True
    }
