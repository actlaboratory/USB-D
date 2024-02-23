#Copyright (C) 2024 Hiroki Fujii <hiroki@efuji.jp>

import config
CONFIG_GLOBAL_KEY = "actlab_USB-D_global"


def getAutoUpdateCheckSetting():
    try:
        return config.conf[CONFIG_GLOBAL_KEY]["checkForUpdatesOnStartup"]
    except:
        return False
def setAutoUpdateCheckSetting(val):
    config.conf[CONFIG_GLOBAL_KEY]["checkForUpdatesOnStartup"] = val

def getEnableTurnOverSetting():
    try:
        return config.conf[CONFIG_GLOBAL_KEY]["enableTurnOver"]
    except:
        return False

def setEnableTurnOverSetting(val):
    config.conf[CONFIG_GLOBAL_KEY]["enableTurnOver"] = val

def initializeSettings():
    if (not hasattr(config.conf, CONFIG_GLOBAL_KEY)) or (not hasattr(config.conf[CONFIG_GLOBAL_KEY], "enableTurnOver")):
        setEnableTurnOverSetting(True)
    else:
        setEnableTurnOverSetting(getEnableTurnOverSetting())
    setAutoUpdateCheckSetting(getAutoUpdateCheckSetting())
