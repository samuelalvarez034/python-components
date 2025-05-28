# 
# This class is part of the Programming the Internet of Things project.
# 

import logging

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class AirPurifierEmulatorTask(BaseActuatorSimTask):
	"""
	Emulated air purifier actuator using SenseHAT screen.
	"""

	def __init__(self):
		super( \
			AirPurifierEmulatorTask, self).__init__( \
				name = ConfigConst.AIR_PURIFIER_ACTUATOR_NAME, \
				typeID = ConfigConst.AIR_PURIFIER_ACTUATOR_TYPE, \
				simpleName = "AIR PURIFIER")

		enableEmulation = \
			ConfigUtil().getBoolean( \
				ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)

		self.sh = SenseHAT(emulate = enableEmulation)

	def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		if self.sh.screen:
			msg = self.getSimpleName() + ' ON: ' + str(val)
			self.sh.screen.scroll_text(msg)
			return 0
		else:
			logging.warning("No SenseHAT LED screen instance to write.")
			return -1

	def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		if self.sh.screen:
			msg = self.getSimpleName() + ' OFF'
			self.sh.screen.scroll_text(msg)

			sleep(5)

			self.sh.screen.clear()
			return 0
		else:
			logging.warning("No SenseHAT LED screen instance to clear / close.")
			return -1
