"""
Ziwei Adam Mao

Helper class for laser doppler BLE devices

LDF peripheral
contains UUIDs for different BLE services
"""


class LDFPeripheral(object):
    def __int__(self):
        self.NAME = "unknown"
        self.ADDR = "unknown"
        self.SYSCFG = "0000fff0-0000-1000-8000-00805f9b34fb"
        self.CHAR1 = ""
        self.CHAR2 = ""
        self.CHAR3 = ""
        self.CHAR4 = "0000fff4-0000-1000-8000-00805f9b34fb"
        self.CHAR5 = ""
        self.CHAR_LIST = [self.CHAR1, self.CHAR2, self.CHAR3, self.CHAR4, self.CHAR5]
        self.SYSCFG_DATA = []
        self.CHAR1_DATA = []
        self.CHAR2_DATA = []
        self.CHAR3_DATA = []
        self.CHAR4_DATA = []
        self.CHAR5_DATA = []
        self.ALL_DATA = [self.CHAR1_DATA, self.CHAR2_DATA, self.CHAR3_DATA, self.CHAR4_DATA, self.CHAR5_DATA]

    def set_name(self, name):
        self.NAME = name

    def get_address(self, device_list):
        """ Search list for device name and retrieve address"""
        for device in device_list:
            if device.name == self.NAME:
                self.ADDR = device.address
                return True
        return False

