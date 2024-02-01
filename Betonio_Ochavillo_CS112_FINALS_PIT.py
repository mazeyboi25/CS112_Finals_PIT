import tkinter as tk
from tkinter import Tk

root: Tk = tk.Tk()


def intro():        # Defined function for Tkinter GUI
    label_for_intro = tk.Label(root, text="Welcome to Pixpay!\n"
                                          "This shop will offer you discounted game credits of your favorite games!\n"
                                          "What game credits would you like to purchase?\n")
    label_for_intro.pack()
    valorant_game_button = tk.Button(root, text='Valorant',
                                     width=25, command=lambda: (valorant_game_choice(), valorant_game_button
                                                                .pack_forget(), codm_game_button.pack_forget(),
                                                                label_for_intro.pack_forget()))
    valorant_game_button.pack()
    codm_game_button = tk.Button(root, text='CODM',
                                 width=25, command=lambda: (codm_game_choice(), valorant_game_button.pack_forget(),
                                                            codm_game_button.pack_forget(),
                                                            label_for_intro.pack_forget()))
    codm_game_button.pack()

    def valorant_game_choice():
        coins_balance_label = tk.Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = tk.Entry(root, width=15)
        coins_balance.pack()
        balance_submit = tk.Button(text='Submit',
                                   width=15, command=lambda: (valorant_options(), coins_balance_label.pack_forget(),
                                                              coins_balance.pack_forget(),
                                                              balance_submit.pack_forget()))
        balance_submit.pack()

        def valorant_options():
            label_for_valorant_choice = tk.Label(root, text="You have selected \"Valorant.\"\n"
                                                            "Select credits:\n")
            label_for_valorant_choice.pack()
            valop1 = tk.Button(root, text='150 VP (₱75)', width=25,
                               command=lambda: (label_for_valorant_choice.pack_forget(), valop1.pack_forget(),
                                                valop2.pack_forget(), valop3.pack_forget(), valop4.pack_forget(),
                                                GameTransaction("Valorant", 75, coins_balance).total()))
            valop1.pack()
            valop2 = tk.Button(root, text='300 VP (₱150)', width=25,
                               command=lambda: (label_for_valorant_choice.pack_forget(), valop1.pack_forget(),
                                                valop2.pack_forget(), valop3.pack_forget(), valop4.pack_forget(),
                                                GameTransaction("Valorant", 150, coins_balance).total()))
            valop2.pack()
            valop3 = tk.Button(root, text='600 VP (₱295)', width=25,
                               command=lambda: (label_for_valorant_choice.pack_forget(), valop1.pack_forget(),
                                                valop2.pack_forget(), valop3.pack_forget(), valop4.pack_forget(),
                                                GameTransaction("Valorant", 295, coins_balance).total()))
            valop3.pack()
            valop4 = tk.Button(root, text='1050 VP (₱350)', width=25,
                               command=lambda: (label_for_valorant_choice.pack_forget(), valop1.pack_forget(),
                                                valop2.pack_forget(), valop3.pack_forget(), valop4.pack_forget(),
                                                GameTransaction("Valorant", 350, coins_balance).total()))
            valop4.pack()

    def codm_game_choice():
        coins_balance_label = tk.Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = tk.Entry(root, width=15)
        coins_balance.pack()
        balance_submit = tk.Button(text='Submit', width=15,
                                   command=lambda: (codm_options(), coins_balance_label.pack_forget(),
                                                    coins_balance.pack_forget(), balance_submit.pack_forget()))
        balance_submit.pack()

        def codm_options():

            label_for_codm_choice = tk.Label(root, text="You have selected \"CODM.\"\n"
                                                        "Select credits:")
            label_for_codm_choice.pack()
            codop1 = tk.Button(root, text='50 GS (₱25)',
                               width=25, command=lambda: (label_for_codm_choice.pack_forget(), codop1.pack_forget(),
                                                          codop2.pack_forget(), codop3.pack_forget(),
                                                          codop4.pack_forget(), GameTransaction("CODM", 25,
                                                          coins_balance).total()))
            codop1.pack()
            codop2 = tk.Button(root, text='150 GS (₱70)', width=25,
                               command=lambda: (label_for_codm_choice.pack_forget(), codop1.pack_forget(),
                                                codop2.pack_forget(), codop3.pack_forget(), codop4.pack_forget(),
                                                GameTransaction("CODM", 70, coins_balance).total()))
            codop2.pack()
            codop3 = tk.Button(root, text='400 GS (₱180)', width=25,
                               command=lambda: (label_for_codm_choice.pack_forget(), codop1.pack_forget(),
                                                codop2.pack_forget(), codop3.pack_forget(), codop4.pack_forget(),
                                                GameTransaction("CODM", 180, coins_balance).total()))
            codop3.pack()
            codop4 = tk.Button(root, text='1000 GS (₱420)', width=25,
                               command=lambda: (label_for_codm_choice.pack_forget(), codop1.pack_forget(),
                                                codop2.pack_forget(), codop3.pack_forget(), codop4.pack_forget(),
                                                GameTransaction("CODM", 420, coins_balance).total()))
            codop4.pack()

    class GameTransaction:
        game_name = ''
        cost = 0

        def __init__(self, game_name, cost, coin_balance):
            self.coins_balance = coin_balance
            self.game_name = game_name
            self.cost = cost
            self.remaining_balance = 0

        def total(self):
            try:
                remaining_balance = int(self.coins_balance.get())
                expression = remaining_balance - int(self.cost)
                if remaining_balance >= self.cost:
                    label_total = tk.Label(root, text=f'Your remaining balance is ₱{expression}. '
                                                      f'Thank you for purchasing!'
                                                      '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = tk.Button(root, width=25, text='Yes',
                                                  command=lambda: (intro(), label_total.pack_forget(), return_submit_yes
                                                                   .pack_forget(), return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = tk.Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    if self.game_name == "Valorant":
                        label_total = tk.Label(root, text='Your balance is insufficient. Would you like'
                                                          'to input again?')
                        label_total.pack()
                        return_submit_yes = tk.Button(root, width=25, text='Yes',
                                                      command=lambda: (valorant_game_choice(), return_submit_yes.
                                                                       pack_forget(), return_submit_no.pack_forget(),
                                                                       label_total.pack_forget()))
                        return_submit_yes.pack()
                        return_submit_no = tk.Button(root, width=25, text='No', command=root.quit)
                        return_submit_no.pack()
                    elif self.game_name == "CODM":
                        label_total = tk.Label(root, text='Input is not a number. Would you like to retry?')
                        label_total.pack()
                        return_submit_yes = tk.Button(root, width=25, text='Yes',
                                                      command=lambda: (codm_game_choice(), return_submit_yes.
                                                                       pack_forget(), return_submit_no.pack_forget(),
                                                                       label_total.pack_forget()))
                        return_submit_yes.pack()
                        return_submit_no = tk.Button(root, width=25, text='No', command=root.quit)
                        return_submit_no.pack()
            except ValueError:
                if self.game_name == "Valorant":
                    error_label = tk.Label(root, text='Input is not a number. Would you like to retry?')
                    error_label.pack()
                    return_submit_yes = tk.Button(root, width=25, text='Yes',
                                                  command=lambda: (valorant_game_choice(), return_submit_yes.
                                                                   pack_forget(), return_submit_no.pack_forget(),
                                                                   error_label.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = tk.Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                elif self.game_name == "CODM":
                    error_label = tk.Label(root, text='Input is not a number. Would you like to retry?')
                    error_label.pack()
                    return_submit_yes = tk.Button(root, width=25, text='Yes',
                                                  command=lambda: (codm_game_choice(), return_submit_yes.pack_forget(),
                                                                   return_submit_no.pack_forget(), error_label.
                                                                   pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = tk.Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()

        def handle_balance_submit(self, coins_balance_label):
            self.remaining_balance = int(self.coins_balance.get())
            coins_balance_label.pack_forget()
            self.coins_balance.pack_forget()
            self.total()
        #   ---------------------------------------------------------------------------------------------

    root.title("Game Purchase Application")


intro()
root.mainloop()
