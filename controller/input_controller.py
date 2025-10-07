from dal.dal_factory import RatesFactory

class InputController:
    def __init__(self, data_source: str):
        self.rate_dao = RatesFactory().create_instance(data_source)
        self.valid_currencies = list(self.rate_dao.get_rates()["rates"].keys()) + ["PHP"]

    def get_menu_choice(self, valid_choices: list[int]):
        while True:
            value = input("Option: ").strip()
            if not value.isdigit():
                print("Error")
                continue
            choice = int(value)
            if choice not in valid_choices:
                print("Error")
                continue
            return choice

    def get_currency(self, label: str):
        while True:
            val = input(f"{label}: ").strip().upper()
            if val not in self.valid_currencies:
                print("Error")
                continue
            return val

    def get_amount(self, label: str):
        while True:
            val = input(f"{label}: ").strip()
            try:
                num = float(val)
            except ValueError:
                print("Error")
                continue

            if str(val).startswith("-") and float(val) == 0:
                print("Error")
                continue
            if num < 0:
                print("Error")
                continue

            return round(num, 2)
