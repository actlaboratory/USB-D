#Copyright (C) 2024 Hiroki Fujii <hiroki@efuji.jp>

import config
CONFIG_GLOBAL_KEY = "actlab_USB-D_global"


def getAutoUpdateCheckSetting():
    try:
        return config.conf[CONFIG_GLOBAL_KEY]["checkForUpdatesOnStartup"]
    except:
        return True
def setAutoUpdateCheckSetting(val):
    config.conf[CONFIG_GLOBAL_KEY]["checkForUpdatesOnStartup"] = val

def getEnableTurnOverSetting():
    try:
        return config.conf[CONFIG_GLOBAL_KEY]["enableTurnOver"]
    except:
        return True

def setEnableTurnOverSetting(val):
    config.conf[CONFIG_GLOBAL_KEY]["enableTurnOver"] = val

def initializeSettings():
    confspec = {
        "checkForUpdatesOnStartup": "boolean(default=True)",
        "enableTurnOver": "boolean(default=True)",
    }
    config.conf.spec[CONFIG_GLOBAL_KEY] = confspec
