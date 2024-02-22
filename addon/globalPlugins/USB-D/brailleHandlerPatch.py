import braille
from . import configUtil

# Dots

DOT_1 = 1
DOT_2 = 2
DOT_3 = 4
DOT_4 = 8
DOT_5 = 16
DOT_6 = 32
DOT_7 = 64
DOT_8 = 128

# dot mapping table
dotMap = [
    [DOT_1, DOT_8],
    [DOT_2, DOT_6],
    [DOT_3, DOT_5],
    [DOT_4, DOT_7],
    [DOT_5, DOT_3],
    [DOT_6, DOT_2],
    [DOT_7, DOT_4],
    [DOT_8, DOT_1]
]

class BrailleHandlerPatch:
    driverDisplayOriginal = None
    handlerWriteCellsOriginal = None
    handleBgThreadExecutorOriginal = None
    
    def turnOverData(data):
        result = []
        for d in data:
            cell = 0
            for m in dotMap:
                if (d & m[0]): cell += m[1]
            result.insert(0, cell)
        return result

    def processData(data):
        # cut when disabled
        if not configUtil.getEnableTurnOverSetting():
            return data
        else:
            return BrailleHandlerPatch.turnOverData(data)
    def driverDisplay(data):
        data = BrailleHandlerPatch.processData(data)
        return BrailleHandlerPatch.driverDisplayOriginal(data)

    def displayPatch():
        if hasattr(braille.handler.display, "NVDA0000ACTLAB_patched"):
            return
        braille.handler.display.NVDA0000ACTLAB_patched = True
        BrailleHandlerPatch.driverDisplayOriginal = braille.handler.display.display
        braille.handler.display.display = BrailleHandlerPatch.driverDisplay

    def handlerWriteCells(self, cells):
        BrailleHandlerPatch.displayPatch()
        BrailleHandlerPatch.handlerWriteCellsOriginal(self, cells)

    def handleBgThreadExecutor(self, param):
        BrailleHandlerPatch.displayPatch()
        BrailleHandlerPatch.handleBgThreadExecutorOriginal(self, param)
