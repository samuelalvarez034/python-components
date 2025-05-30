from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class AirPurifierActuatorSimTask(BaseActuatorSimTask):
    def __init__(self):
        super(AirPurifierActuatorSimTask, self).__init__(
            name=ConfigConst.AIR_PURIFIER_ACTUATOR_NAME,
            typeID=ConfigConst.AIR_PURIFIER_ACTUATOR_TYPE,
            simpleName="Purifier"
        )
