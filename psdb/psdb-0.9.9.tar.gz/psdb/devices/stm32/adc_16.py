# Copyright (c) 2019-2021 Phase Advanced Sensor Systems, Inc.
from builtins import range

from ..device import Device, AReg32, AReg32R


class ADC16(Device):
    '''
    Driver for the STM32H7 16-bit ADC.
    '''
    PER_ADC_REGS = [(AReg32,  'ISR',      0x00, [('ADRDY',         0),
                                                 ('EOSMP',         1),
                                                 ('EOC',           2),
                                                 ('EOS',           3),
                                                 ('OVR',           4),
                                                 ('JEOC',          5),
                                                 ('JEOS',          6),
                                                 ('AWD1',          7),
                                                 ('AWD2',          8),
                                                 ('AWD3',          9),
                                                 ('JQOVF',        10),
                                                 ('LDORDY',       12),
                                                 ]),
                    (AReg32,  'IER',      0x04, [('ADRDYIE',       0),
                                                 ('EOSMPIE',       1),
                                                 ('EOCIE',         2),
                                                 ('EOSIE',         3),
                                                 ('OVRIE',         4),
                                                 ('JEOCIE',        5),
                                                 ('JEOSIE',        6),
                                                 ('AWD1IE',        7),
                                                 ('AWD2IE',        8),
                                                 ('AWD3IE',        9),
                                                 ('JQOVFIE',      10),
                                                 ]),
                    (AReg32,  'CR',       0x08, [('ADEN',          0),
                                                 ('ADDIS',         1),
                                                 ('ADSTART',       2),
                                                 ('JADSTART',      3),
                                                 ('ADSTP',         4),
                                                 ('JADSTP',        5),
                                                 ('BOOST',         8,  9),
                                                 ('ADCALLIN',     16),
                                                 ('LINCALRDYW1',  22),
                                                 ('LINCALRDYW2',  23),
                                                 ('LINCALRDYW3',  24),
                                                 ('LINCALRDYW4',  25),
                                                 ('LINCALRDYW5',  26),
                                                 ('LINCALRDYW6',  27),
                                                 ('ADVREGEN',     28),
                                                 ('DEEPPWD',      29),
                                                 ('ADCALDIF',     30),
                                                 ('ADCAL',        31),
                                                 ]),
                    (AReg32,  'CFGR',     0x0C, [('DMNGT',         0,  1),
                                                 ('RES',           2,  4),
                                                 ('EXTSEL',        5,  9),
                                                 ('EXTEN',        10, 11),
                                                 ('OVRMOD',       12),
                                                 ('CONT',         13),
                                                 ('AUTDLY',       14),
                                                 ('DISCEN',       16),
                                                 ('DISCNUM',      17, 19),
                                                 ('JDISCEN',      20),
                                                 ('JQM',          21),
                                                 ('AWD1SGL',      22),
                                                 ('AWD1EN',       23),
                                                 ('JAWD1EN',      24),
                                                 ('JAUTO',        25),
                                                 ('AWD1CH',       26, 30),
                                                 ('JQDIS',        31),
                                                 ]),
                    (AReg32,  'CFGR2',    0x10, [('ROVSE',         0),
                                                 ('JOVSE',         1),
                                                 ('OVSS',          5,  8),
                                                 ('TROVS',         9),
                                                 ('ROVSM',        10),
                                                 ('RSHIFT1',      11),
                                                 ('RSHIFT2',      12),
                                                 ('RSHIFT3',      13),
                                                 ('RSHIFT4',      14),
                                                 ('OSVR',         16, 25),
                                                 ('LSHIFT',       28, 31),
                                                 ]),
                    (AReg32,  'SMPR1',    0x14, [('SMP0',          0,  2),
                                                 ('SMP1',          3,  5),
                                                 ('SMP2',          6,  8),
                                                 ('SMP3',          9, 11),
                                                 ('SMP4',         12, 14),
                                                 ('SMP5',         15, 17),
                                                 ('SMP6',         18, 20),
                                                 ('SMP7',         21, 23),
                                                 ('SMP8',         24, 26),
                                                 ('SMP9',         27, 29),
                                                 ]),
                    (AReg32,  'SMPR2',    0x18, [('SMP10',         0,  2),
                                                 ('SMP11',         3,  5),
                                                 ('SMP12',         6,  8),
                                                 ('SMP13',         9, 11),
                                                 ('SMP14',        12, 14),
                                                 ('SMP15',        15, 17),
                                                 ('SMP16',        18, 20),
                                                 ('SMP17',        21, 23),
                                                 ('SMP18',        24, 26),
                                                 ('SMP19',        27, 29),
                                                 ]),
                    (AReg32,  'PCSEL',    0x1C, [('PCSEL0',        0),
                                                 ('PCSEL1',        1),
                                                 ('PCSEL2',        2),
                                                 ('PCSEL3',        3),
                                                 ('PCSEL4',        4),
                                                 ('PCSEL5',        5),
                                                 ('PCSEL6',        6),
                                                 ('PCSEL7',        7),
                                                 ('PCSEL8',        8),
                                                 ('PCSEL9',        9),
                                                 ('PCSEL10',      10),
                                                 ('PCSEL11',      11),
                                                 ('PCSEL12',      12),
                                                 ('PCSEL13',      13),
                                                 ('PCSEL14',      14),
                                                 ('PCSEL15',      15),
                                                 ('PCSEL16',      16),
                                                 ('PCSEL17',      17),
                                                 ('PCSEL18',      18),
                                                 ('PCSEL19',      19),
                                                 ]),
                    (AReg32,  'LTR1',     0x20, [('LTR1',          0, 25),
                                                 ]),
                    (AReg32,  'HTR1',     0x24, [('HTR1',          0, 25),
                                                 ]),
                    (AReg32,  'SQR1',     0x30, [('L',             0,  4),
                                                 ('SQ1',           6, 10),
                                                 ('SQ2',          12, 16),
                                                 ('SQ3',          18, 22),
                                                 ('SQ4',          24, 28),
                                                 ]),
                    (AReg32,  'SQR2',     0x34, [('SQ5',           0,  4),
                                                 ('SQ6',           6, 10),
                                                 ('SQ7',          12, 16),
                                                 ('SQ8',          18, 22),
                                                 ('SQ9',          24, 28),
                                                 ]),
                    (AReg32,  'SQR3',     0x38, [('SQ10',          0,  4),
                                                 ('SQ11',          6, 10),
                                                 ('SQ12',         12, 16),
                                                 ('SQ13',         18, 22),
                                                 ('SQ14',         24, 28),
                                                 ]),
                    (AReg32,  'SQR4',     0x3C, [('SQ15',          0,  4),
                                                 ('SQ16',          6, 10),
                                                 ]),
                    (AReg32R, 'DR',       0x40, [('RDATA',         0, 31),
                                                 ]),
                    (AReg32,  'JSQR',     0x4C, [('JL',            0,  1),
                                                 ('JEXTSEL',       2,  6),
                                                 ('JEXTEN',        7,  8),
                                                 ('JSQ1',          9, 13),
                                                 ('JSQ2',         15, 19),
                                                 ('JSQ3',         21, 25),
                                                 ('JSQ4',         27, 31),
                                                 ]),
                    (AReg32,  'OFR1',     0x60, [('OFFSET1',       0, 25),
                                                 ('OFFSET1_CH',   26, 30),
                                                 ('SSATE',        31),
                                                 ]),
                    (AReg32,  'OFR2',     0x64, [('OFFSET2',       0, 25),
                                                 ('OFFSET2_CH',   26, 30),
                                                 ('SSATE',        31),
                                                 ]),
                    (AReg32,  'OFR3',     0x68, [('OFFSET3',       0, 25),
                                                 ('OFFSET3_CH',   26, 30),
                                                 ('SSATE',        31),
                                                 ]),
                    (AReg32,  'OFR4',     0x6C, [('OFFSET4',       0, 25),
                                                 ('OFFSET4_CH',   26, 30),
                                                 ('SSATE',        31),
                                                 ]),
                    (AReg32R, 'JDR1',     0x80, [('JDATA',         0, 31)]),
                    (AReg32R, 'JDR2',     0x84, [('JDATA',         0, 31)]),
                    (AReg32R, 'JDR3',     0x88, [('JDATA',         0, 31)]),
                    (AReg32R, 'JDR4',     0x8C, [('JDATA',         0, 31)]),
                    (AReg32,  'AWD2CR',   0xA0, [('AWD2CH',        0, 19)]),
                    (AReg32,  'AWD3CR',   0xA4, [('AWD3CH',        0, 19)]),
                    (AReg32,  'LTR2',     0xB0, [('LTR2',          0, 25)]),
                    (AReg32,  'HTR2',     0xB4, [('HTR2',          0, 25)]),
                    (AReg32,  'LTR3',     0xB8, [('LTR3',          0, 25)]),
                    (AReg32,  'HTR3',     0xBC, [('HTR3',          0, 25)]),
                    (AReg32,  'DIFSEL',   0xC0, [('DIFSEL',        0, 19)]),
                    (AReg32,  'CALFACT',  0xC4, [('CALFACT_S',     0, 10),
                                                 ('CALFACT_D',    16, 26),
                                                 ]),
                    (AReg32,  'CALFACT2', 0xC8, [('LINCALFACT',    0, 29)]),
                    ]
    COM_ADC_REGS = [AReg32R('CSR',  0x300,     [('ADRDY_MST',     0),
                                                ('EOSMP_MST',     1),
                                                ('EOC_MST',       2),
                                                ('EOS_MST',       3),
                                                ('OVR_MST',       4),
                                                ('JEOC_MST',      5),
                                                ('JEOS_MST',      6),
                                                ('AWD1_MST',      7),
                                                ('AWD2_MST',      8),
                                                ('AWD3_MST',      9),
                                                ('JQOVF_MST',    10),
                                                ('ADRDY_SLV',    16),
                                                ('EOSMP_SLV',    17),
                                                ('EOC_SLV',      18),
                                                ('EOS_SLV',      19),
                                                ('OVR_SLV',      20),
                                                ('JEOC_SLV',     21),
                                                ('JEOS_SLV',     22),
                                                ('AWD1_SLV',     23),
                                                ('AWD2_SLV',     24),
                                                ('AWD3_SLV',     25),
                                                ('JQOVF_SLV',    26),
                                                ]),
                    AReg32 ('CCR',  0x308,     [('DUAL',          0,  4),
                                                ('DELAY',         8, 11),
                                                ('DAMDF',        14, 15),
                                                ('CKMODE',       16, 17),
                                                ('PRESC',        18, 21),
                                                ('VREFEN',       22),
                                                ('TSEN',         23),
                                                ('VBATEN',       24),
                                                ]),
                    AReg32R('CDR',  0x30C,     [('RDATA_MST',     0, 15),
                                                ('RDATA_SLV',    16, 31),
                                                ]),
                    AReg32R('CDR2', 0x310,     [('RDATA_ALT',     0, 31),
                                                ]),
                    ]

    def __init__(self, target, ap, name, addr, first_adc, nadcs, **kwargs):
        regs = []
        for i in range(nadcs):
            base = 0x100*i
            regs += [cls(_name + ('_%u' % (first_adc + i)), base + offset,
                         fields)
                     for cls, _name, offset, fields in ADC16.PER_ADC_REGS]
        regs += ADC16.COM_ADC_REGS

        super().__init__(target, ap, addr, name, regs, **kwargs)
