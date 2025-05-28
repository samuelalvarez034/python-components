import logging
from time import sleep
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class FanEmulatorTask(BaseActuatorSimTask):
    def __init__(self):
        super(FanEmulatorTask, self).__init__(
            name = "FanActuator",
            typeID = 888,  # Usa un ID único no utilizado, por ejemplo 888
            simpleName = "FAN"
        )
        enableEmulation = ConfigUtil().getBoolean(
            ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
        self.sh = SenseHAT(emulate = enableEmulation)

    def _activateActuator(self, val: float = 0.0, stateData: str = None) -> int:
        if self.sh.screen:
            msg = self.getSimpleName() + ' ON: ' + str(val)
            self.sh.screen.scroll_text(msg)
            return 0
        else:
            logging.warning("No SenseHAT LED screen instance to write.")
            return -1

    def _deactivateActuator(self, val: float = 0.0, stateData: str = None) -> int:
        if self.sh.screen:
            msg = self.getSimpleName() + ' OFF'
            self.sh.screen.scroll_text(msg)
            sleep(2)
            self.sh.screen.clear()
            return 0
        else:
            logging.warning("No SenseHAT LED screen instance to clear.")
            return -1
