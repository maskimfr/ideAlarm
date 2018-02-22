# -*- coding: utf-8 -*-
from org.eclipse.smarthome.core.library.types import OnOffType
from org.eclipse.smarthome.core.types import UnDefType
ON = OnOffType.ON
OFF = OnOffType.OFF
NULL = UnDefType.NULL
UNDEF = UnDefType.UNDEF

ALARM_TEST_MODE = True
LOGGING_LEVEL = 'DEBUG'
NAG_INTERVAL_MINUTES = 6

# You can define functions to determine if a sensor is enabled or not.
# These functions take 3 arguments, events itemRegistry and and log.
# The function shall return a boolean.
def d5Enabled(events, itemRegistry, log):
    '''
    Door 5 sensor shall only be enabled if an Internet connection is available.
    '''
    return (itemRegistry.getItem('Network_Internet').state == ON)

ALARM_ZONES = [
    {
        'name': 'My Home',
        'armingModeItem': 'Z1_Arming_Mode',
        'statusItem': 'Z1_Status',
        'alertDevices': ['Siren_Indoors', 'Siren_Gardenshed'],
        'sensors': [
            {'name': 'Door_1_Lock', 'sensorClass': 'A', 'nag': True, 'nagTimeoutMins': 4, 'armWarn': True, 'enabled': True},
            {'name': 'Door_3_Lock', 'sensorClass': 'A', 'nag': True, 'nagTimeoutMins': 4, 'armWarn': True, 'enabled': True},
            {'name': 'MD_Bathroom_1', 'sensorClass': 'B', 'nag': False, 'nagTimeoutMins': 4, 'armWarn': False, 'enabled': True}
        ],
        'armAwayToggleSwitch': 'Toggle_Z1_Armed_Away',
        'armHomeToggleSwitch': 'Toggle_Z1_Armed_Home',
        'mainZone': True,
        'canArmWithTrippedSensors': False
    },
    {
        'name': 'Pembridge Square Residence',
        'armingModeItem': 'Z2_Arming_Mode',
        'statusItem': 'Z2_Status',
        'alertDevices': ['Notting Hill Alert Horn', 'Big Ben Chimes'],
        'sensors': [
            {'name': 'Door_GardenShed', 'sensorClass': 'B', 'nag': True, 'nagTimeoutMins': 4, 'armWarn': True, 'enabled': True},
            {'name': 'Glenn_Sensor', 'sensorClass': 'B', 'nag': False, 'nagTimeoutMins': 4, 'armWarn': False, 'enabled': True},
            {'name': 'Mains_Cabinet', 'sensorClass': 'A', 'nag': True, 'nagTimeoutMins': 4, 'armWarn': True, 'enabled': True}
        ],
        'armAwayToggleSwitch': 'Toggle_Z2_Armed_Away',
        'armHomeToggleSwitch': 'Toggle_Z2_Armed_Home',
        'mainZone': False,
        'canArmWithTrippedSensors': True
    }
]
