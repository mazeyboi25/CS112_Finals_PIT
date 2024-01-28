import tkinter as tk

class GameTransaction:
    def __init__(self, game_name, cost):
        self.game_name = game_name
        self.cost = cost
        self.remaining_balance = 0

    def total(self):
        try:
            remaining_balance = int(self.coins_balance.get())
            expression = remaining_balance - self.cost
            if remaining_balance >= self.cost:
                label_total = tk.Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                  '\nWould you like to purchase again?')
                label_total.pack()
                return_submit_yes = tk.Button(width=25, text='Yes', command=lambda: self.retry_purchase(label_total))
                return_submit_yes.pack()
                return_submit_no = tk.Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()
            else:
                label_total = tk.Label(root, text='Your balance is insufficient. Please try again later.')
                label_total.pack()
                return_label = tk.Label(root, text="Would you like to retry?")
                return_label.pack()
                return_submit_yes = tk.Button(root, width=25, text='Yes',
                                              command=lambda: self.retry_purchase(label_total, return_label))
                return_submit_yes.pack()
                return_submit_no = tk.Button(root, width=25, text='No', command=root.quit)
                return_submit_no.pack()
        except ValueError:
            error_label = tk.Label(text='Input is not a number. Would you like to retry?')
            error_label.pack()
            return_submit_yes = tk.Button(width=25, text='Yes', command=lambda: self.retry_purchase(error_label))
            return_submit_yes.pack()
            return_submit_no = tk.Button(width=25, text='No', command=root.quit)
            return_submit_no.pack()

    def retry_purchase(self, *widgets_to_forget):
        for widget in widgets_to_forget:
            widget.pack_forget()
        self.intro()

    def intro(self):
        coins_balance_label = tk.Label(root, text=f'Enter your Pixpay balance for {self.game_name}.')
        coins_balance_label.pack()
        self.coins_balance = tk.Entry(root, width=15)
        self.coins_balance.pack()
        balance_submit = tk.Button(text='Submit', width=15, command=lambda: self.handle_balance_submit(coins_balance_label))
        balance_submit.pack()

    def handle_balance_submit(self, coins_balance_label):
        self.remaining_balance = int(self.coins_balance.get())
        coins_balance_label.pack_forget()
        self.coins_balance.pack_forget()
        self.total()

root = tk.Tk()
root.title("Game Purchase Application")

class ValorantTransaction(GameTransaction):
    def __init__(self):
        super().__init__("Valorant", 100)

class CODMTransaction(GameTransaction):
    def __init__(self):
        super().__init__("CODM", 420)

def valorant_game_choice():
    valorant_transaction = ValorantTransaction()
    valorant_transaction.intro()

def codm_game_choice():
    codm_transaction = CODMTransaction()
    codm_transaction.intro()

valorant_game_button = tk.Button(text='Valorant', width=25, command=valorant_game_choice)
valorant_game_button.pack()

codm_game_button = tk.Button(text='CODM', width=25, command=codm_game_choice)
codm_game_button.pack()

root.mainloop()
