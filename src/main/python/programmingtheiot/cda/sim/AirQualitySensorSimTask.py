from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
import programmingtheiot.common.ConfigConst as ConfigConst

class AirQualitySensorSimTask(BaseSensorSimTask):
    def __init__(self, dataSet=None):
        super(AirQualitySensorSimTask, self).__init__(
            name=ConfigConst.AIR_QUALITY_SENSOR_NAME,
            typeID=ConfigConst.AIR_QUALITY_SENSOR_TYPE,
            dataSet=dataSet,
            minVal=SensorDataGenerator.LOW_NORMAL_ENV_AIR,
            maxVal=SensorDataGenerator.HI_NORMAL_ENV_AIR
        )
