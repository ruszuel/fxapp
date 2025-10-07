from bll.rates_bll import RatesBll

class ConvertMoney:
    def __init__(self, source: str):
        self.rates_bll = RatesBll(source)

    def convert(self, source: str, target: str, amount: float):
        return self.rates_bll.convert_amount(source, target, amount)
