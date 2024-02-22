#Copyright (C) 2021-2024 Hiroki Fujii <hiroki@efuji.jp>

import re
import wx
import gui
import braille
import inputCore
import globalPluginHandler
from .inputManagerPatch import InputManagerPatch
from .brailleHandlerPatch import BrailleHandlerPatch
from . import configUtil



class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        configUtil.initializeSettings()

        BrailleHandlerPatch.handlerWriteCellsOriginal = braille.BrailleHandler._writeCells
        braille.BrailleHandler._writeCells = BrailleHandlerPatch.handlerWriteCells
        BrailleHandlerPatch.handleBgThreadExecutorOriginal = braille.BrailleHandler._bgThreadExecutor
        braille.BrailleHandler._bgThreadExecutor = BrailleHandlerPatch.handleBgThreadExecutor
        InputManagerPatch.executeGestureOriginal = inputCore.InputManager.executeGesture
        inputCore.InputManager.executeGesture = InputManagerPatch.executeGesture
        self._setupMenu()

    def terminate(self):
        super(GlobalPlugin, self).terminate()
        try:
            gui.mainFrame.sysTrayIcon.menu.Remove(self.rootMenuItem)
        except BaseException:
            pass
    
    def _setupMenu(self):
        self.rootMenu = wx.Menu()
        
        self.turnOverStateToggleItem = self.rootMenu.Append(wx.ID_ANY, self._turnOverStateToggleString(),
            _("点字ディスプレイの向きを切り替えます。")
        )
        gui.mainFrame.sysTrayIcon.Bind(
            wx.EVT_MENU, self.toggleTurnOverState, self.turnOverStateToggleItem)
        
        self.rootMenuItem = gui.mainFrame.sysTrayIcon.menu.Insert(
            2, wx.ID_ANY, _("Up Side Braille-Down"), self.rootMenu)
        

    def _turnOverStateToggleString(self):
        return _("(点字ディスプレイの向きを元に戻す&S)") if configUtil.getEnableTurnOverSetting() else _("点字ディスプレイの向きをサカサマにする(&S)")        
    
    def toggleTurnOverState(self, evt=None):
        self.script_toggleTurnOverState()

    def script_toggleTurnOverState(self, gesture=None):
        configUtil.setEnableTurnOverSetting(not configUtil.getEnableTurnOverSetting())
        self.turnOverStateToggleItem.SetItemLabel(self._turnOverStateToggleString())
