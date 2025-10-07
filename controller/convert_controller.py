from bll.rates_bll import RatesBll

class ConvertMoney:
    def __init__(self, data_source: str):
        self.rates_bll = RatesBll(data_source)

    def convert(self, source: str, target: str, amount: float):
        return self.rates_bll.convert_amount(source, target, amount)
