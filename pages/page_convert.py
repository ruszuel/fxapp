from controller.convert_controller import ConvertMoney
from controller.input_controller import InputController

class ConvertMenu:
    def input_menu(self):
        print("-------------------------------")
        input_ctrl = InputController("json")

        source = input_ctrl.get_currency("Source Ccy")
        if not source: 
            return None

        target = input_ctrl.get_currency("Target Ccy")
        if not target: 
            return None

        amount = input_ctrl.get_amount(f"Amount in {source}")
        if amount is None: 
            return None

        result = ConvertMoney("json").convert(source, target, amount)
        print(f"Converted Amt: {result:.2f} {target}")
