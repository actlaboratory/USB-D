#Copyright (C) 2021-2024 Hiroki Fujii <hiroki@efuji.jp>

import re
import braille
from .keyConvertTable import KEY_TABLE
from . import configUtil


class InputManagerPatch():
    executeGestureOriginal = None

    
    def executeGesture(self, gesture):
        # cut when disabled
        if not configUtil.getEnableTurnOverSetting():
            return InputManagerPatch.executeGestureOriginal(self, gesture)
        
        # turn over routing switch
        if isinstance(getattr(gesture, "routingIndex", None), int) and braille.handler and braille.handler.display and gesture.routingIndex >= 0 and gesture.routingIndex < braille.handler.display.numCells:
            gesture.routingIndex = braille.handler.display.numCells - gesture.routingIndex - 1
        #print("key = %s, %s, %s, %s" %(getattr(gesture, "id", ""), getattr(gesture, "space", ""), getattr(gesture, "dots", ""), getattr(gesture, "source", "")))
        # input key convert
        if hasattr(gesture, "id") and hasattr(gesture, "routingIndex"):
            for k in KEY_TABLE.get(gesture.source, []):
                gesture.id = re.sub(r'(^|\+)%s(\+|$)' %(k[0],), r'\1NVDA0000ACTLAB_%s\2' %(k[1],), gesture.id)
            gesture.id = gesture.id.replace("NVDA0000ACTLAB_", "")
        #print("key = %s, %s, %s" %(getattr(gesture, "id", ""), getattr(gesture, "space", ""), getattr(gesture, "dots", "")))
        InputManagerPatch.executeGestureOriginal(self, gesture)
