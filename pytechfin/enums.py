from enum import Enum

class EnumApps(Enum):
    """Techfin Apps Enumerator
    """
    FMSCASH = 'fmscash'
    CASHFLOW = 'cashflow'
    RAC = 'totvs.rac'

    @classmethod
    def exists_key(cls, item): 
        return item in cls.__members__

    @classmethod
    def exists_value(cls, item): 
        return item in set([f.value for f in cls])
