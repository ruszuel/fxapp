from pages.page_rates import PageRates
from pages.page_convert import ConvertMenu
from controller.input_controller import InputController

class Router:
    def route_choice(self):
        input_ctrl = InputController("json")
        pages = {1: PageRates().display_rates, 2: ConvertMenu().input_menu}

        while True:
            print("-------------- Fx App --------------")
            print("[1] View Available Rates")
            print("[2] Convert Money")

            choice = input_ctrl.get_menu_choice(list(pages.keys()))
            if not choice:
                continue 
            pages[choice]()
