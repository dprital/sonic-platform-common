"""
    bmc_base.py

    Base class for implementing a platform-specific class with which
    to interact with a BMC device in SONiC.
"""


from . import device_base

class BMCBase(device_base.DeviceBase):
    # TODO(BMC): add virtual BMC APIs
    '''
    get_eeprom()

    get_version()

    # TODO(BMC): check if params are needed or use the root
    reset_password()

    collect_dump()

    update_firmware(fw_image)
    '''
    pass
