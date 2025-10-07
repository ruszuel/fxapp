from dal.abstract_rates import RateABC
from dal.dal_factory import RatesFactory

class RatesBll:
    __rate_dao: RateABC

    def __init__(self, data_source: str):
        self.__rate_dao = RatesFactory().create_instance(data_source)

    def get_rates_data(self):
        return self.__rate_dao.get_rates()

    def convert_amount(self, source: str, target: str, amount: float):
        source = source.upper()
        target = target.upper()
        rates = self.__rate_dao.get_rates()
        get_curr_rate = self.__rate_dao.get_currency_rate

        if source == target:
            return float(amount)

        try:
            if source == "PHP":
                target_rate = get_curr_rate(target)
                return float(amount) / target_rate
            elif target == "PHP":
                source_rate = get_curr_rate(source)
                return float(amount) * source_rate
            else:
                source_rate = get_curr_rate(source)
                target_rate = get_curr_rate(target)
                php_amount = float(amount) * source_rate
                return php_amount / target_rate
        except Exception as ex:
            print(f"Value not in the list. {str(ex)}")
