from abc import ABC, abstractmethod

class RateABC(ABC):
    @abstractmethod
    def get_rates(self) -> dict:
        pass

    @abstractmethod
    def get_currency_rate(self, currency: str) -> float:
        pass
