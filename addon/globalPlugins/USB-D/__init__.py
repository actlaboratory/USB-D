#Copyright (C) 2024 Hiroki Fujii <hiroki@efuji.jp>

import re
import wx
import gui
import braille
import inputCore
import globalPluginHandler
from .inputManagerPatch import InputManagerPatch
from .brailleHandlerPatch import BrailleHandlerPatch
from . import configUtil
from . import updater as updater
from .compat import messageBox

try:
	import addonHandler
	addonHandler.initTranslation()
except:
	_ = lambda x : x


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        configUtil.initializeSettings()
        
        self.autoUpdateChecker = updater.AutoUpdateChecker()
        if configUtil.getAutoUpdateCheckSetting():
            self.autoUpdateChecker.autoUpdateCheck(mode=updater.AUTO)
        
        BrailleHandlerPatch.handlerWriteCellsOriginal = braille.BrailleHandler._writeCells
        braille.BrailleHandler._writeCells = BrailleHandlerPatch.handlerWriteCells
        BrailleHandlerPatch.handleBgThreadExecutorOriginal = braille.BrailleHandler._bgThreadExecutor
        braille.BrailleHandler._bgThreadExecutor = BrailleHandlerPatch.handleBgThreadExecutor
        InputManagerPatch.executeGestureOriginal = inputCore.InputManager.executeGesture
        inputCore.InputManager.executeGesture = InputManagerPatch.executeGesture
        self._setupMenu()

    def terminate(self):
        super(GlobalPlugin, self).terminate()
        self.autoUpdateChecker.terminate()
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
        
        self.updateCheckToggleItem = self.rootMenu.Append(
            wx.ID_ANY,
            self._updateCheckToggleString(),
            _("起動時に自動でアップデートを確認するかどうかを切り替えます。")
        )
        gui.mainFrame.sysTrayIcon.Bind(
            wx.EVT_MENU, self.toggleUpdateCheck, self.updateCheckToggleItem)

        self.updateCheckPerformItem = self.rootMenu.Append(
            wx.ID_ANY,
            _("アップデートを確認"),
            _("アップデートを手動で確認します。")
        )
        gui.mainFrame.sysTrayIcon.Bind(
            wx.EVT_MENU, self.performUpdateCheck, self.updateCheckPerformItem)


        self.rootMenuItem = gui.mainFrame.sysTrayIcon.menu.Insert(
            2, wx.ID_ANY, _("Upside Braille-Down"), self.rootMenu)


    def _turnOverStateToggleString(self):
        return _("点字ディスプレイの向きを元に戻す(&S)") if configUtil.getEnableTurnOverSetting() else _("点字ディスプレイの向きをサカサマにする(&S)")

    def _updateCheckToggleString(self):
        return _("起動時のアップデートの確認を無効化") if configUtil.getAutoUpdateCheckSetting() else _("起動時のアップデートの確認を有効化")

    
    def toggleTurnOverState(self, evt=None):
        self.script_toggleTurnOverState()

    def script_toggleTurnOverState(self, gesture=None):
        configUtil.setEnableTurnOverSetting(not configUtil.getEnableTurnOverSetting())
        self.turnOverStateToggleItem.SetItemLabel(self._turnOverStateToggleString())

    def toggleUpdateCheck(self, evt):
        changed = not configUtil.getAutoUpdateCheckSetting()
        configUtil.setAutoUpdateCheckSetting(changed)
        msg = _("NVDA起動時に、自動でアップデートを確認します。") if changed is True else _(
            "NVDA起動時に、自動でアップデートを確認しません。")
        self.updateCheckToggleItem.SetItemLabel(self._updateCheckToggleString())
        messageBox(msg, _("設定完了"))

    def performUpdateCheck(self, evt):
        updater.AutoUpdateChecker().autoUpdateCheck(mode=updater.MANUAL)

    
