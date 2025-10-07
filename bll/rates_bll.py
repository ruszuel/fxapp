from dal.abstract_rates import RateABC
from dal.dal_factory import RatesFactory

class RatesBll:
    __rate_dao: RateABC

    def __init__(self, data_source: str):
        self.__rate_dao = RatesFactory().create_instance(data_source)

    def get_rates_data(self):
        return self.__rate_dao.get_rates()

    def convert_amount(self, source: str, target: str, amount: float):
        data = self.__rate_dao.get_rates()
        base, rates = data.get("base"), data.get("rates", {})
        source, target = source.upper(), target.upper()

        if base not in rates:
            key, val = next(iter(rates.items()))
            rates[base] = rates[key] / val

        try:
            return float(amount) * rates[source] / rates[target]
        except Exception:
            print("[Error] Conversion failed. [Info] Source or target currency not found in rate list.")

