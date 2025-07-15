"""
    bmc_base.py

    Base class for implementing a platform-specific class with which
    to interact with a BMC device in SONiC.
"""


from . import device_base

class BMCBase(device_base.DeviceBase):
    # TODO(BMC): Add a virtual methods for the core APIs and implement them in the bmc.py file
    pass
