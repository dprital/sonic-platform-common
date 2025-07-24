"""
    bmc_base.py

    Base class for implementing a platform-specific class with which
    to interact with a BMC device in SONiC.
"""


from . import device_base

class BMCBase(device_base.DeviceBase):

    def get_eeprom(self):
        raise NotImplementedError
    
    def get_version(self):
        raise NotImplementedError
    
    def reset_password(self):
        raise NotImplementedError
    
    def trigger_bmc_debug_log_dump(self):
        raise NotImplementedError
    
    def get_bmc_debug_log_dump(self, task_id, filename, path, timeout = 120):
        raise NotImplementedError
    
    def update_firmware(self, fw_image):
        raise NotImplementedError
