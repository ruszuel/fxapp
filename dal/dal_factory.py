from dal.rates_dal import RateDao
from dal.abstract_rates import RateABC

class RatesFactory:
    def create_instance(self, data_source: str) -> RateABC:
        obj_map = {
            "json": RateDao
        }
        dao_class = obj_map.get(data_source)
        if dao_class is None:
            raise Exception(f"[Error] Invalid data source.")
        return dao_class()
