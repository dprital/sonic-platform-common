"""
    cmis.py

    Implementation of XcvrMemMap for CMIS Rev 5.0
"""

from ..xcvr_mem_map import XcvrMemMap
from ...fields.xcvr_field import (
    CodeRegField,
    DateField,
    HexRegField,
    NumberRegField,
    RegBitField,
    RegGroupField,
    StringRegField,
)
from ...fields import consts
from ...fields.public.cmis import CableLenField

class CmisMemMap(XcvrMemMap):
    def __init__(self, codes):
        super(CmisMemMap, self).__init__(codes)

        self.MGMT_CHARACTERISTICS = RegGroupField(consts.MGMT_CHAR_FIELD,
            NumberRegField(consts.MGMT_CHAR_MISC_FIELD, self.getaddr(0x0, 2),
                RegBitField(consts.FLAT_MEM_FIELD, 7)
            )
        )

        # Should contain ONLY Lower page fields
        self.ADMIN_INFO = RegGroupField(consts.ADMIN_INFO_FIELD,
            CodeRegField(consts.ID_FIELD, self.getaddr(0x0, 0), self.codes.XCVR_IDENTIFIERS),
            CodeRegField(consts.ID_ABBRV_FIELD, self.getaddr(0x0, 128), self.codes.XCVR_IDENTIFIER_ABBRV),
            StringRegField(consts.VENDOR_NAME_FIELD, self.getaddr(0x0, 129), size=16),
            HexRegField(consts.VENDOR_OUI_FIELD, self.getaddr(0x0, 145), size=3),
            StringRegField(consts.VENDOR_PART_NO_FIELD, self.getaddr(0x0, 148), size=16),
            StringRegField(consts.VENDOR_REV_FIELD, self.getaddr(0x0, 164), size=2),
            StringRegField(consts.VENDOR_SERIAL_NO_FIELD, self.getaddr(0x0, 166), size=16),
            DateField(consts.VENDOR_DATE_FIELD, self.getaddr(0x0, 182), size=8),
            RegGroupField(consts.EXT_ID_FIELD,
                CodeRegField(consts.POWER_CLASS_FIELD, self.getaddr(0x0, 200), self.codes.POWER_CLASSES,
                    *(RegBitField("%s_%d" % (consts.POWER_CLASS_FIELD, bit), bit) for bit in range(5, 8))
                ),
                NumberRegField(consts.MAX_POWER_FIELD, self.getaddr(0x0, 201), scale=4.0),
            ),
            NumberRegField(consts.LEN_MULT_FIELD, self.getaddr(0x0, 202),
                *(RegBitField("%s_%d" % (consts.LEN_MULT_FIELD, bit), bit) for bit in range (6, 8))
            ),
            CableLenField(consts.LENGTH_ASSEMBLY_FIELD, self.getaddr(0x0, 202),
                *(RegBitField("%s_%d" % (consts.LENGTH_ASSEMBLY_FIELD, bit), bit) for bit in range(0, 6))
            ),

            CodeRegField(consts.CONNECTOR_FIELD, self.getaddr(0x0, 203), self.codes.CONNECTORS),

            RegGroupField(consts.APPLS_ADVT_FIELD,
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 1), self.getaddr(0x0, 86 + 4 * (1 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 2), self.getaddr(0x0, 86 + 4 * (2 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 3), self.getaddr(0x0, 86 + 4 * (3 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 4), self.getaddr(0x0, 86 + 4 * (4 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 5), self.getaddr(0x0, 86 + 4 * (5 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 6), self.getaddr(0x0, 86 + 4 * (6 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 7), self.getaddr(0x0, 86 + 4 * (7 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 8), self.getaddr(0x0, 86 + 4 * (8 - 1)), self.codes.HOST_ELECTRICAL_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 1), self.getaddr(0x0, 87 + 4 * (1 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 2), self.getaddr(0x0, 87 + 4 * (2 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 3), self.getaddr(0x0, 87 + 4 * (3 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 4), self.getaddr(0x0, 87 + 4 * (4 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 5), self.getaddr(0x0, 87 + 4 * (5 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 6), self.getaddr(0x0, 87 + 4 * (6 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 7), self.getaddr(0x0, 87 + 4 * (7 - 1)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 8), self.getaddr(0x0, 87 + 4 * (8 - 1)), self.codes.NM_850_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 1), self.getaddr(0x0, 87 + 4 * (1 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 2), self.getaddr(0x0, 87 + 4 * (2 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 3), self.getaddr(0x0, 87 + 4 * (3 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 4), self.getaddr(0x0, 87 + 4 * (4 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 5), self.getaddr(0x0, 87 + 4 * (5 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 6), self.getaddr(0x0, 87 + 4 * (6 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 7), self.getaddr(0x0, 87 + 4 * (7 - 1)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 8), self.getaddr(0x0, 87 + 4 * (8 - 1)), self.codes.SM_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 1), self.getaddr(0x0, 87 + 4 * (1 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 2), self.getaddr(0x0, 87 + 4 * (2 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 3), self.getaddr(0x0, 87 + 4 * (3 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 4), self.getaddr(0x0, 87 + 4 * (4 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 5), self.getaddr(0x0, 87 + 4 * (5 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 6), self.getaddr(0x0, 87 + 4 * (6 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 7), self.getaddr(0x0, 87 + 4 * (7 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 8), self.getaddr(0x0, 87 + 4 * (8 - 1)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 1), self.getaddr(0x0, 87 + 4 * (1 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 2), self.getaddr(0x0, 87 + 4 * (2 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 3), self.getaddr(0x0, 87 + 4 * (3 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 4), self.getaddr(0x0, 87 + 4 * (4 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 5), self.getaddr(0x0, 87 + 4 * (5 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 6), self.getaddr(0x0, 87 + 4 * (6 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 7), self.getaddr(0x0, 87 + 4 * (7 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 8), self.getaddr(0x0, 87 + 4 * (8 - 1)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 1), self.getaddr(0x0, 87 + 4 * (1 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 2), self.getaddr(0x0, 87 + 4 * (2 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 3), self.getaddr(0x0, 87 + 4 * (3 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 4), self.getaddr(0x0, 87 + 4 * (4 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 5), self.getaddr(0x0, 87 + 4 * (5 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 6), self.getaddr(0x0, 87 + 4 * (6 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 7), self.getaddr(0x0, 87 + 4 * (7 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 8), self.getaddr(0x0, 87 + 4 * (8 - 1)), self.codes.BASE_T_MEDIA_INTERFACE),

                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 1), self.getaddr(0x0, 88 + 4 * (1 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 2), self.getaddr(0x0, 88 + 4 * (2 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 3), self.getaddr(0x0, 88 + 4 * (3 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 4), self.getaddr(0x0, 88 + 4 * (4 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 5), self.getaddr(0x0, 88 + 4 * (5 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 6), self.getaddr(0x0, 88 + 4 * (6 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 7), self.getaddr(0x0, 88 + 4 * (7 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 8), self.getaddr(0x0, 88 + 4 * (8 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 1), self.getaddr(0x0, 88 + 4 * (1 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 2), self.getaddr(0x0, 88 + 4 * (2 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 3), self.getaddr(0x0, 88 + 4 * (3 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 4), self.getaddr(0x0, 88 + 4 * (4 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 5), self.getaddr(0x0, 88 + 4 * (5 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 6), self.getaddr(0x0, 88 + 4 * (6 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 7), self.getaddr(0x0, 88 + 4 * (7 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 8), self.getaddr(0x0, 88 + 4 * (8 - 1)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),

                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 1), self.getaddr(0x0, 89 + 4 * (1 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 2), self.getaddr(0x0, 89 + 4 * (2 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 3), self.getaddr(0x0, 89 + 4 * (3 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 4), self.getaddr(0x0, 89 + 4 * (4 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 5), self.getaddr(0x0, 89 + 4 * (5 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 6), self.getaddr(0x0, 89 + 4 * (6 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 7), self.getaddr(0x0, 89 + 4 * (7 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 8), self.getaddr(0x0, 89 + 4 * (8 - 1)), format="B", size=1),

            ),

            CodeRegField(consts.HOST_ELECTRICAL_INTERFACE, self.getaddr(0x0, 86), self.codes.HOST_ELECTRICAL_INTERFACE),
            CodeRegField(consts.MEDIA_TYPE_FIELD, self.getaddr(0x0, 85), self.codes.MODULE_MEDIA_TYPE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_850NM, self.getaddr(0x0, 87), self.codes.NM_850_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_SM, self.getaddr(0x0, 87), self.codes.SM_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, self.getaddr(0x0, 87), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, self.getaddr(0x0, 87), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
            CodeRegField(consts.MODULE_MEDIA_INTERFACE_BASE_T, self.getaddr(0x0, 87), self.codes.BASE_T_MEDIA_INTERFACE),
            NumberRegField(consts.MEDIA_LANE_COUNT, self.getaddr(0x0, 88),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
            ),
            NumberRegField(consts.HOST_LANE_COUNT, self.getaddr(0x0, 88),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
            ),
            NumberRegField(consts.HOST_LANE_ASSIGNMENT_OPTION, self.getaddr(0x0, 89), format="B", size=1),
            CodeRegField(consts.MEDIA_INTERFACE_TECH, self.getaddr(0x0, 212), self.codes.MEDIA_INTERFACE_TECH),
            NumberRegField(consts.CMIS_MAJOR_REVISION, self.getaddr(0x0, 1),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
            ),
            NumberRegField(consts.CMIS_MINOR_REVISION, self.getaddr(0x0, 1),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
            ),
            NumberRegField(consts.ACTIVE_FW_MAJOR_REV, self.getaddr(0x0, 39), format="B", size=1),
            NumberRegField(consts.ACTIVE_FW_MINOR_REV, self.getaddr(0x0, 40), format="B", size=1),
        )

        # Should contain ONLY upper page fields
        self.ADVERTISING = RegGroupField(consts.ADVERTISING_FIELD,
            NumberRegField(consts.HW_MAJOR_REV, self.getaddr(0x1, 130), size=1),
            NumberRegField(consts.HW_MINOR_REV, self.getaddr(0x1, 131), size=1),
            NumberRegField(consts.MEDIA_LANE_ASSIGNMENT_OPTION, self.getaddr(0x1, 176), format="B", size=1),
            NumberRegField(consts.INACTIVE_FW_MAJOR_REV, self.getaddr(0x1, 128), format="B", size=1),
            NumberRegField(consts.INACTIVE_FW_MINOR_REV, self.getaddr(0x1, 129), format="B", size=1),

            RegGroupField(consts.ACTIVE_APSEL_CODE,
                *(NumberRegField("%s%d" % (consts.ACTIVE_APSEL_HOSTLANE, lane) , self.getaddr(0x11, offset),
                    *(RegBitField("Bit%d" % bit, bit) for bit in range(4, 7)))
                 for lane, offset in zip(range(1, 9), range(206, 214)))
            ),

            RegGroupField(consts.APPLS_ADVT_FIELD_PAGE01,
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 9), self.getaddr(0x1, 223 + 4 * (9 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 10), self.getaddr(0x1, 223 + 4 * (10 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 11), self.getaddr(0x1, 223 + 4 * (11 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 12), self.getaddr(0x1, 223 + 4 * (12 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 13), self.getaddr(0x1, 223 + 4 * (13 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 14), self.getaddr(0x1, 223 + 4 * (14 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),
                CodeRegField("%s_%d" % (consts.HOST_ELECTRICAL_INTERFACE, 15), self.getaddr(0x1, 223 + 4 * (15 - 9)), self.codes.HOST_ELECTRICAL_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 9), self.getaddr(0x1, 224 + 4 * (9 - 9)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 10), self.getaddr(0x1, 224 + 4 * (10 - 9)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 11), self.getaddr(0x1, 224 + 4 * (11 - 9)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 12), self.getaddr(0x1, 224 + 4 * (12 - 9)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 13), self.getaddr(0x1, 224 + 4 * (13 - 9)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 14), self.getaddr(0x1, 224 + 4 * (14 - 9)), self.codes.NM_850_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_850NM, 15), self.getaddr(0x1, 224 + 4 * (15 - 9)), self.codes.NM_850_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 9), self.getaddr(0x1, 224 + 4 * (9 - 9)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 10), self.getaddr(0x1, 224 + 4 * (10 - 9)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 11), self.getaddr(0x1, 224 + 4 * (11 - 9)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 12), self.getaddr(0x1, 224 + 4 * (12 - 9)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 13), self.getaddr(0x1, 224 + 4 * (13 - 9)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 14), self.getaddr(0x1, 224 + 4 * (14 - 9)), self.codes.SM_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_SM, 15), self.getaddr(0x1, 224 + 4 * (15 - 9)), self.codes.SM_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 9), self.getaddr(0x1, 224 + 4 * (9 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 10), self.getaddr(0x1, 224 + 4 * (10 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 11), self.getaddr(0x1, 224 + 4 * (11 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 12), self.getaddr(0x1, 224 + 4 * (12 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 13), self.getaddr(0x1, 224 + 4 * (13 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 14), self.getaddr(0x1, 224 + 4 * (14 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_PASSIVE_COPPER, 15), self.getaddr(0x1, 224 + 4 * (15 - 9)), self.codes.PASSIVE_COPPER_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 9), self.getaddr(0x1, 224 + 4 * (9 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 10), self.getaddr(0x1, 224 + 4 * (10 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 11), self.getaddr(0x1, 224 + 4 * (11 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 12), self.getaddr(0x1, 224 + 4 * (12 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 13), self.getaddr(0x1, 224 + 4 * (13 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 14), self.getaddr(0x1, 224 + 4 * (14 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_ACTIVE_CABLE, 15), self.getaddr(0x1, 224 + 4 * (15 - 9)), self.codes.ACTIVE_CABLE_MEDIA_INTERFACE),

                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 9), self.getaddr(0x1, 224 + 4 * (9 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 10), self.getaddr(0x1, 224 + 4 * (10 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 11), self.getaddr(0x1, 224 + 4 * (11 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 12), self.getaddr(0x1, 224 + 4 * (12 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 13), self.getaddr(0x1, 224 + 4 * (13 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 14), self.getaddr(0x1, 224 + 4 * (14 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),
                CodeRegField("%s_%d" % (consts.MODULE_MEDIA_INTERFACE_BASE_T, 15), self.getaddr(0x1, 224 + 4 * (15 - 9)), self.codes.BASE_T_MEDIA_INTERFACE),

                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 9), self.getaddr(0x1, 225 + 4 * (9 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 10), self.getaddr(0x1, 225 + 4 * (10 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 11), self.getaddr(0x1, 225 + 4 * (11 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 12), self.getaddr(0x1, 225 + 4 * (12 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 13), self.getaddr(0x1, 225 + 4 * (13 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 14), self.getaddr(0x1, 225 + 4 * (14 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),
                NumberRegField("%s_%d" % (consts.MEDIA_LANE_COUNT, 15), self.getaddr(0x1, 225 + 4 * (15 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 4))
                ),

                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 9), self.getaddr(0x1, 225 + 4 * (9 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 10), self.getaddr(0x1, 225 + 4 * (10 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 11), self.getaddr(0x1, 225 + 4 * (11 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 12), self.getaddr(0x1, 225 + 4 * (12 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 13), self.getaddr(0x1, 225 + 4 * (13 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 14), self.getaddr(0x1, 225 + 4 * (14 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),
                NumberRegField("%s_%d" % (consts.HOST_LANE_COUNT, 15), self.getaddr(0x1, 225 + 4 * (15 - 9)),
                    *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8))
                ),

                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 9), self.getaddr(0x1, 226 + 4 * (9 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 10), self.getaddr(0x1, 226 + 4 * (10 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 11), self.getaddr(0x1, 226 + 4 * (11 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 12), self.getaddr(0x1, 226 + 4 * (12 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 13), self.getaddr(0x1, 226 + 4 * (13 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 14), self.getaddr(0x1, 226 + 4 * (14 - 1)), format="B", size=1),
                NumberRegField("%s_%d" % (consts.HOST_LANE_ASSIGNMENT_OPTION, 15), self.getaddr(0x1, 226 + 4 * (15 - 1)), format="B", size=1),

                *(NumberRegField("%s_%d" % (consts.MEDIA_LANE_ASSIGNMENT_OPTION, app), self.getaddr(0x1, 176 + (app - 1)), format="B", size=1)
                  for app in range(1, 16))
            )
        )

        self.MODULE_LEVEL_MONITORS = RegGroupField(consts.MODULE_MONITORS_FIELD,
            NumberRegField(consts.TEMPERATURE_FIELD, self.getaddr(0x0, 14), size=2, format=">h", scale=256.0),
            NumberRegField(consts.VOLTAGE_FIELD, self.getaddr(0x0, 16), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.GRID_SPACING, self.getaddr(0x12, 128),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (4, 8)), ro = False
            ),
            NumberRegField(consts.LASER_CONFIG_CHANNEL, self.getaddr(0x12, 136), format=">h", size=2, ro=False),
            NumberRegField(consts.LASER_CURRENT_FREQ, self.getaddr(0x12, 168), format=">L", size=4, scale = 1000.0),
            NumberRegField(consts.TX_CONFIG_POWER, self.getaddr(0x12, 200), format=">h", size=2, scale=100.0, ro=False),
            NumberRegField(consts.AUX_MON_TYPE, self.getaddr(0x1, 145), size=1),
            NumberRegField(consts.AUX1_MON, self.getaddr(0x0, 18), format=">h", size=2),
            NumberRegField(consts.AUX2_MON, self.getaddr(0x0, 20), format=">h", size=2),
            NumberRegField(consts.AUX3_MON, self.getaddr(0x0, 22), format=">h", size=2),
            NumberRegField(consts.CUSTOM_MON, self.getaddr(0x0, 24), format=">H", size=2),
        )

        self.MODULE_CHAR_ADVT = RegGroupField(consts.MODULE_CHAR_ADVT_FIELD,
            NumberRegField(consts.PAGE_SUPPORT_ADVT_FIELD, self.getaddr(0x1, 142),
                RegBitField(consts.VDM_SUPPORTED, 6),
            ),
            NumberRegField(consts.CTRLS_ADVT_FIELD, self.getaddr(0x1, 155),
                RegBitField(consts.TX_DISABLE_SUPPORT_FIELD, 1),
                size=2, format="<H"
            ),
            NumberRegField(consts.TX_FLAGS_ADVT_FIELD, self.getaddr(0x1, 157),
                RegBitField(consts.TX_FAULT_SUPPORT_FIELD, 0),
                RegBitField(consts.TX_LOS_SUPPORT_FIELD, 1),
                RegBitField(consts.TX_CDR_LOL_SUPPORT_FIELD, 2),
            ),
            NumberRegField(consts.RX_FLAGS_ADVT_FIELD, self.getaddr(0x1, 158),
                RegBitField(consts.RX_LOS_SUPPORT, 1),
                RegBitField(consts.RX_CDR_LOL_SUPPORT_FIELD, 2),
            ),
            NumberRegField(consts.LANE_MON_ADVT_FIELD, self.getaddr(0x1, 160),
                RegBitField(consts.RX_POWER_SUPPORT_FIELD, 2),
                RegBitField(consts.TX_POWER_SUPPORT_FIELD, 1),
                RegBitField(consts.TX_BIAS_SUPPORT_FIELD, 0),
            ),
            NumberRegField(consts.TX_BIAS_SCALE, self.getaddr(0x1, 160),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (3, 5))
            ),
        )

        self.THRESHOLDS = RegGroupField(consts.THRESHOLDS_FIELD,
            NumberRegField(consts.TEMP_HIGH_ALARM_FIELD, self.getaddr(0x2, 128), size=2, format=">h", scale=256.0),
            NumberRegField(consts.TEMP_LOW_ALARM_FIELD, self.getaddr(0x2, 130), size=2, format=">h", scale=256.0),
            NumberRegField(consts.TEMP_HIGH_WARNING_FIELD, self.getaddr(0x2, 132), size=2, format=">h", scale=256.0),
            NumberRegField(consts.TEMP_LOW_WARNING_FIELD, self.getaddr(0x2, 134), size=2, format=">h", scale=256.0),
            NumberRegField(consts.VOLTAGE_HIGH_ALARM_FIELD, self.getaddr(0x2, 136), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.VOLTAGE_LOW_ALARM_FIELD, self.getaddr(0x2, 138), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.VOLTAGE_HIGH_WARNING_FIELD, self.getaddr(0x2, 140), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.VOLTAGE_LOW_WARNING_FIELD, self.getaddr(0x2, 142), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.TX_POWER_HIGH_ALARM_FIELD, self.getaddr(0x2, 176), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.TX_POWER_LOW_ALARM_FIELD, self.getaddr(0x2, 178), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.TX_POWER_HIGH_WARNING_FIELD, self.getaddr(0x2, 180), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.TX_POWER_LOW_WARNING_FIELD, self.getaddr(0x2, 182), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.TX_BIAS_HIGH_ALARM_FIELD, self.getaddr(0x2, 184), size=2, format=">H", scale=500.0),
            NumberRegField(consts.TX_BIAS_LOW_ALARM_FIELD, self.getaddr(0x2, 186), size=2, format=">H", scale=500.0),
            NumberRegField(consts.TX_BIAS_HIGH_WARNING_FIELD, self.getaddr(0x2, 188), size=2, format=">H", scale=500.0),
            NumberRegField(consts.TX_BIAS_LOW_WARNING_FIELD, self.getaddr(0x2, 190), size=2, format=">H", scale=500.0),
            NumberRegField(consts.RX_POWER_HIGH_ALARM_FIELD, self.getaddr(0x2, 192), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.RX_POWER_LOW_ALARM_FIELD, self.getaddr(0x2, 194), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.RX_POWER_HIGH_WARNING_FIELD, self.getaddr(0x2, 196), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.RX_POWER_LOW_WARNING_FIELD, self.getaddr(0x2, 198), size=2, format=">H", scale=10000.0),
            NumberRegField(consts.AUX1_HIGH_ALARM, self.getaddr(0x2, 144), format=">h", size=2),
            NumberRegField(consts.AUX1_LOW_ALARM, self.getaddr(0x2, 146), format=">h", size=2),
            NumberRegField(consts.AUX1_HIGH_WARN, self.getaddr(0x2, 148), format=">h", size=2),
            NumberRegField(consts.AUX1_LOW_WARN, self.getaddr(0x2, 150), format=">h", size=2),
            NumberRegField(consts.AUX2_HIGH_ALARM, self.getaddr(0x2, 152), format=">h", size=2),
            NumberRegField(consts.AUX2_LOW_ALARM, self.getaddr(0x2, 154), format=">h", size=2),
            NumberRegField(consts.AUX2_HIGH_WARN, self.getaddr(0x2, 156), format=">h", size=2),
            NumberRegField(consts.AUX2_LOW_WARN, self.getaddr(0x2, 158), format=">h", size=2),
            NumberRegField(consts.AUX3_HIGH_ALARM, self.getaddr(0x2, 160), format=">h", size=2),
            NumberRegField(consts.AUX3_LOW_ALARM, self.getaddr(0x2, 162), format=">h", size=2),
            NumberRegField(consts.AUX3_HIGH_WARN, self.getaddr(0x2, 164), format=">h", size=2),
            NumberRegField(consts.AUX3_LOW_WARN, self.getaddr(0x2, 166), format=">h", size=2),
        )

        self.LANE_DATAPATH_CTRL = RegGroupField(consts.LANE_DATAPATH_CTRL_FIELD,
            NumberRegField(consts.DATAPATH_DEINIT_FIELD, self.getaddr(0x10, 128), ro=False),
            NumberRegField(consts.TX_DISABLE_FIELD, self.getaddr(0x10, 130), ro=False)
        )

        self.LANE_DATAPATH_STATUS = RegGroupField(consts.LANE_DATAPATH_STATUS_FIELD,
            RegGroupField(consts.TX_FAULT_FIELD,
                *(NumberRegField("%s%d" % (consts.TX_FAULT_FIELD, lane), self.getaddr(0x11, 135),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_LOS_FIELD,
                *(NumberRegField("%s%d" % (consts.RX_LOS_FIELD, lane), self.getaddr(0x11, 147),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),

            RegGroupField(consts.TX_POWER_FIELD,
                *(NumberRegField("OpticalPowerTx%dField" % channel, self.getaddr(0x11, offset), size=2, format=">H", scale=10000.0)
                for channel, offset in zip(range(1, 9), range(154, 170, 2)))
            ),
            RegGroupField(consts.TX_BIAS_FIELD,
                *(NumberRegField("LaserBiasTx%dField" % channel, self.getaddr(0x11, offset), size=2, format=">H", scale=500.0)
                for channel, offset in zip(range(1, 9), range(170, 186, 2)))
            ),
            RegGroupField(consts.RX_POWER_FIELD,
                *(NumberRegField("OpticalPowerRx%dField" % channel, self.getaddr(0x11, offset), size=2, format=">H", scale=10000.0)
                for channel, offset in zip(range(1, 9), range(186, 202, 2)))
            ),

            RegGroupField(consts.DATA_PATH_STATE,
                *(CodeRegField("DP%dState" % (lane) , self.getaddr(0x11, 128 + int((lane-1)/2)), self.codes.DATAPATH_STATE,
                    *(RegBitField("Bit%d" % bit, bit) for bit in [range(4, 8), range(0, 4)][lane%2]))
                 for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_OUTPUT_STATUS,
                *(NumberRegField("%s%d" % (consts.RX_OUTPUT_STATUS, lane), self.getaddr(0x11, 132),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_OUTPUT_STATUS,
                *(NumberRegField("%s%d" % (consts.TX_OUTPUT_STATUS, lane), self.getaddr(0x11, 133),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_LOS_FIELD,
                *(NumberRegField("%s%d" % (consts.TX_LOS_FIELD, lane), self.getaddr(0x11, 136),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_CDR_LOL,
                *(NumberRegField("%s%d" % (consts.TX_CDR_LOL, lane), self.getaddr(0x11, 137),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_POWER_HIGH_ALARM_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_POWER_HIGH_ALARM_FLAG, lane), self.getaddr(0x11, 139),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_POWER_LOW_ALARM_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_POWER_LOW_ALARM_FLAG, lane), self.getaddr(0x11, 140),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_POWER_HIGH_WARN_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_POWER_HIGH_WARN_FLAG, lane), self.getaddr(0x11, 141),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_POWER_LOW_WARN_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_POWER_LOW_WARN_FLAG, lane), self.getaddr(0x11, 142),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_BIAS_HIGH_ALARM_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_BIAS_HIGH_ALARM_FLAG, lane), self.getaddr(0x11, 143),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_BIAS_LOW_ALARM_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_BIAS_LOW_ALARM_FLAG, lane), self.getaddr(0x11, 144),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_BIAS_HIGH_WARN_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_BIAS_HIGH_WARN_FLAG, lane), self.getaddr(0x11, 145),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.TX_BIAS_LOW_WARN_FLAG,
                *(NumberRegField("%s%d" % (consts.TX_BIAS_LOW_WARN_FLAG, lane), self.getaddr(0x11, 146),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_CDR_LOL,
                *(NumberRegField("%s%d" % (consts.RX_CDR_LOL, lane), self.getaddr(0x11, 148),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_POWER_HIGH_ALARM_FLAG,
                *(NumberRegField("%s%d" % (consts.RX_POWER_HIGH_ALARM_FLAG, lane), self.getaddr(0x11, 149),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_POWER_LOW_ALARM_FLAG,
                *(NumberRegField("%s%d" % (consts.RX_POWER_LOW_ALARM_FLAG, lane), self.getaddr(0x11, 150),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_POWER_HIGH_WARN_FLAG,
                *(NumberRegField("%s%d" % (consts.RX_POWER_HIGH_WARN_FLAG, lane), self.getaddr(0x11, 151),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.RX_POWER_LOW_WARN_FLAG,
                *(NumberRegField("%s%d" % (consts.RX_POWER_LOW_WARN_FLAG, lane), self.getaddr(0x11, 152),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegGroupField(consts.CONFIG_LANE_STATUS,
                *(CodeRegField("%s%d" % (consts.CONFIG_LANE_STATUS, lane) , self.getaddr(0x11, 202 + int((lane-1)/2)), self.codes.CONFIG_STATUS,
                    *(RegBitField("Bit%d" % bit, bit) for bit in [range(4, 8), range(0, 4)][lane%2]))
                 for lane in range(1, 9))
            ),
            RegGroupField(consts.DPINIT_PENDING,
                *(NumberRegField("%s%d" % (consts.DPINIT_PENDING, lane), self.getaddr(0x11, 235),
                    RegBitField("Bit%d" % (lane-1), (lane-1))
                )
                for lane in range(1, 9))
            ),
            RegBitField(consts.TUNING_IN_PROGRESS, offset=self.getaddr(0x12, 222), bitpos=1),
            RegBitField(consts.WAVELENGTH_UNLOCKED, offset=self.getaddr(0x12, 222), bitpos=0),
            NumberRegField(consts.LASER_TUNING_DETAIL, self.getaddr(0x12, 231), size=1),
        )

        self.TRANS_LOOPBACK = RegGroupField(consts.TRANS_LOOPBACK_FIELD,
            NumberRegField(consts.LOOPBACK_CAPABILITY, self.getaddr(0x13, 128), size=1),
            NumberRegField(consts.MEDIA_OUTPUT_LOOPBACK, offset=self.getaddr(0x13, 180), size=1,  ro=False),
            NumberRegField(consts.MEDIA_INPUT_LOOPBACK, offset=self.getaddr(0x13, 181), size=1, ro=False),
            NumberRegField(consts.HOST_OUTPUT_LOOPBACK, self.getaddr(0x13, 182), size=1, ro=False),
            NumberRegField(consts.HOST_INPUT_LOOPBACK, self.getaddr(0x13, 183), size=1, ro=False),
        )

        self.TRANS_MODULE_STATUS = RegGroupField(consts.TRANS_MODULE_STATUS_FIELD,
            CodeRegField(consts.MODULE_STATE, self.getaddr(0x0, 3), self.codes.MODULE_STATE,
                 *(RegBitField("Bit%d" % (bit), bit) for bit in range (1, 4))
            ),
            NumberRegField(consts.MODULE_FIRMWARE_FAULT_INFO, self.getaddr(0x0, 8), size=1),
            NumberRegField(consts.MODULE_FLAG_BYTE1, self.getaddr(0x0, 9), size=1),
            NumberRegField(consts.MODULE_FLAG_BYTE2, self.getaddr(0x0, 10), size=1),
            NumberRegField(consts.MODULE_FLAG_BYTE3, self.getaddr(0x0, 11), size=1),
            NumberRegField(consts.CDB1_STATUS, self.getaddr(0x0, 37), size=1),
            CodeRegField(consts.MODULE_FAULT_CAUSE, self.getaddr(0x0, 41), self.codes.MODULE_FAULT_CAUSE),
        )

        self.TRANS_PM = RegGroupField(consts.TRANS_PM_FIELD,
            NumberRegField(consts.VDM_SUPPORTED_PAGE, self.getaddr(0x2f, 128),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (0, 2))
            ),
            NumberRegField(consts.VDM_CONTROL, self.getaddr(0x2f, 144), size=1, ro=False),
        )

        self.TRANS_CONFIG = RegGroupField(consts.TRANS_CONFIG_FIELD,
            NumberRegField(consts.MODULE_LEVEL_CONTROL, self.getaddr(0x0, 26), size=1, ro=False),
        )

        self.TRANS_CDB = RegGroupField(consts.TRANS_CDB_FIELD,
            NumberRegField(consts.CDB_SUPPORT, self.getaddr(0x1, 163),
                *(RegBitField("Bit%d" % (bit), bit) for bit in range (6, 8))
            ),
            NumberRegField(consts.AUTO_PAGING_SUPPORT, self.getaddr(0x1, 163),
                (RegBitField("Bit4", 4))
            ),
            NumberRegField(consts.CDB_SEQ_WRITE_LENGTH_EXT, self.getaddr(0x01, 164), size=1),
            NumberRegField(consts.CDB_RPL_LENGTH, self.getaddr(0x9f, 134), size=1, ro=False),
            NumberRegField(consts.CDB_RPL_CHKCODE, self.getaddr(0x9f, 135), size=1, ro=False),
        )

        self.STAGED_CTRL0 = RegGroupField("%s_%d" % (consts.STAGED_CTRL_FIELD, 0),
            NumberRegField("%s_%d" % (consts.STAGED_CTRL_APPLY_DPINIT_FIELD, 0),
                self.getaddr(0x10, 143), ro=False),
            NumberRegField("%s_%d" % (consts.STAGED_CTRL_APPLY_IMMEDIATE_FIELD, 0),
                self.getaddr(0x10, 144), ro=False),
            *(NumberRegField("%s_%d_%d" % (consts.STAGED_CTRL_APSEL_FIELD, 0, lane),
                self.getaddr(0x10, 144 + lane), ro=False)
                for lane in range(1, 9))
        )

        # TODO: add remaining fields

    def getaddr(self, page, offset, page_size=128):
        return page * page_size + offset
