from CurrentAccount import *
class OverDraft(CurrentAccount):
    def __init__(self,balance,account_type ='OD'):
        super().__init__(balance,account_type)


