from bll.rates_bll import RatesBll

class RatesController:
    def __init__(self, data_source: str):
        self.rates_bll = RatesBll(data_source)

    def retrieve_rates(self):
        return self.rates_bll.get_rates_data()
