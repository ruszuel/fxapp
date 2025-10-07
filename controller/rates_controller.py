from bll.rates_bll import RatesBll

class RatesController:
    def __init__(self, source: str):
        self.rates_bll = RatesBll(source)

    def retrieve_rates(self):
        return self.rates_bll.get_rates_data()
