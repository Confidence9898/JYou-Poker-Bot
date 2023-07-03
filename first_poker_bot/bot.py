from botcity.core import DesktopBot


class Bot(DesktopBot):
    def action(self, execution=None):
        self.start_emulator()
        
    def start_emulator(self):
        self.execute("D:\Memu\MEmu\MEmu.exe")
        
        self.open_poker()
        
        self.play_poker()
        
        # self.close_all_apps()
        
    def open_poker(self):
        if not self.find("poker_app", matching = 0.97, waiting_time = 60000):
            self.not_found("app_form")
        self.click()
        
    def play_poker(self):
        
        # if self.find("sign_in_button", matching = 0.97, waiting_time = 60000):
        #     self.not_found("sign_in_button")
        # self.click()
        
        # if not self.find("cross2_button", matching = 0.97, waiting_time = 60000):
        #     self.not_found("cross2_button")
        # self.click()
        
        # if not self.find("sit_and_go", matching = 0.97, waiting_time = 60000):
        #     self.not_found("sit_and_go")
        # self.click()
        
        # if not self.find("rome", matching = 0.97, waiting_time = 60000):
        #     self.not_found("rome")
        # self.click()
        
        if not self.find("cash_game", matching = 0.97, waiting_time = 60000):
            self.not_found("cash_game")
        self.click()
        
        if not self.find("play_cash_game_button", matching = 0.97, waiting_time = 60000):
            self.not_found("play_cash_game_button")
        self.click()
        
        if not self.find("fold_button", matching = 0.97, waiting_time = 60000):
            self.not_found("fold_button")
        self.click()
        
        if self.find("call_button", matching = 0.85, waiting_time = 60000):
            self.click()
        elif self.find("check_button", matching = 0.97, waiting_time = 60000):
            self.click()
        
        # if not self.find("check_button", matching = 0.97, waiting_time = 60000):
        #     self.find("call_button", matching = 0.97, waiting_time = 60000)
        # self.click()
        
        if not self.find("raise_button", matching = 0.97, waiting_time = 60000):
            self.not_found("raise_button")
        self.click()
        
        if not self.find("raise_button", matching = 0.97, waiting_time = 60000):
            self.not_found("raise_button")
        self.click()
        
        for _ in range(2):
            if not self.find("up_button", matching = 0.97, waiting_time = 60000):
                self.not_found("raise_button")
            self.click()
            
            if not self.find("down_button", matching = 0.97, waiting_time = 60000):
                self.not_found("down_button")
            self.click()
        
        if not self.find("confirm_button", matching = 0.97, waiting_time = 60000):
            self.not_found("raise_button")
        self.click()
        
        if not self.find("menu_button", matching = 0.97, waiting_time = 60000):
            self.not_found("menu_button")
        self.click()
        
        if not self.find("home_button", matching = 0.97, waiting_time = 60000):
            self.not_found("home_button")
        self.click()
        
        if not self.find("cross_button", matching = 0.97, waiting_time = 60000):
            self.not_found("cross_button")
        self.click()
        
    def not_found(self, label):
        print(f"Element not found: {label}")
    


if __name__ == '__main__':
    Bot.main()
