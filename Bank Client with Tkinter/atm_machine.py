from tkinter import *
import backend

class Account:

    def __init__(self, window, window_2):
        """ initialize all the buttons and text entry here
            then gets hidden by calling hide_items()"""
        self.id_key = IntVar()
        self.balance = DoubleVar()
        self.window = window
        self.window_2 = window_2

        self.first_name_value = StringVar()
        self.last_name_value = StringVar()
        
        self.login_window(self.window_2)
        
        self.chequing_button = Button(self.window, text = "Chequing Account")
        self.chequing_button.grid(row = 0, column = 0)

        self.savings_button = Button(self.window, text = "Savings Account")
        self.savings_button.grid(row = 0, column = 1)

        self.withdraw_button = Button(self.window, text = "Withdraw", command = self.withdraw_tab)
        self.withdraw_button.grid(row = 1, column = 2)

        self.deposit_button = Button(self.window, text = "Deposit", command = self.deposit_tab)
        self.deposit_button.grid(row = 2, column = 2)

        self.view_balance_button = Button(self.window, text = "View Balance", command = self.view_balance)
        self.view_balance_button.grid(row = 3, column = 2)
    
        self.transfer_button = Button(self.window, text = "Transfer")
        self.transfer_button.grid(row = 4, column = 2)

        self.main_text = Text(self.window, width = 30, height = 7.5)
        self.main_text.grid(row = 1, column = 0, columnspan = 2, rowspan = 4)

        self.withdraw_value = DoubleVar()
        self.withdraw_entry = Entry(self.window, textvariable = self.withdraw_value)
        self.withdraw_entry.grid(row = 2, column = 0, columnspan = 2)
        
        self.withdraw_button = Button(self.window, text = "Withdraw", command = lambda: self.withdraw(self.withdraw_value.get()))
        self.withdraw_button.grid(row = 3, column = 0)

        self.deposit_value = DoubleVar()
        self.deposit_entry = Entry(self.window, textvariable = self.deposit_value)
        self.deposit_entry.grid(row = 2, column = 0, columnspan = 2)
        
        self.deposit_button = Button(self.window, text = "Deposit", command = lambda: self.deposit(self.deposit_value.get()))
        self.deposit_button.grid(row = 3, column = 0)
        
        self.cancel_button = Button(self.window, text = "Cancel", command = lambda: self.main_screen(self.first_name_value, self.last_name_value))
        self.cancel_button.grid(row = 3, column = 1)

        self.back_button = Button(self.window, text = "Back", command = lambda: self.main_screen(self.first_name_value, self.last_name_value))
        self.back_button.grid(row = 3, column = 0)

        self.hide_items()

    def hide_items(self):
        self.withdraw_entry.grid_remove()
        self.withdraw_button.grid_remove()
        self.deposit_entry.grid_remove()
        self.deposit_button.grid_remove()
        self.cancel_button.grid_remove()
        self.back_button.grid_remove()

    def login_window(self, window_2):
        window_2.attributes("-topmost", "true")
        
        self.first_name_label = Label(new_window, text = "First Name")
        self.first_name_label.grid(row = 0, column = 0)

        self.first_name_entry = Entry(new_window, textvariable = self.first_name_value)
        self.first_name_entry.grid(row = 0, column = 1)

        self.last_name_label = Label(new_window, text = "Last Name")
        self.last_name_label.grid(row = 1, column = 0)

        self.last_name_entry = Entry(new_window, textvariable = self.last_name_value)
        self.last_name_entry.grid(row = 1, column = 1)

        self.login_button = Button(new_window, text = "Login", command = self.login_command)
        self.login_button.grid(row = 2, column = 0)

    def login_command(self):
        selected_client = backend.login_client(self.first_name_value.get(), self.last_name_value.get())
        self.id_key = selected_client[0][0]
        self.first_name_value = selected_client[0][1]
        self.last_name_value = selected_client[0][2]
        self.main_screen(self.first_name_value, self.last_name_value)
        self.balance = selected_client[0][9]
        self.window.attributes("-topmost", "true")
        self.window_2.destroy()

    def main_screen(self, f_name, l_name):
        self.hide_items()
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, "Welcome " + f_name + " " + l_name)
        self.main_text.insert(END, "\nWhat would you like to do?")        

    def view_balance(self):
        self.hide_items()
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, self.first_name_value + " " + self.last_name_value + ", you have:" )
        self.main_text.insert(END, "\n\n$" + str(self.balance))
        self.back_button.grid()

    def withdraw_tab(self):
        self.hide_items()
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, "How much would you like to withdraw? ")

        self.withdraw_entry.grid()
        self.withdraw_button.grid()
        self.cancel_button.grid()
       
    def withdraw(self, amount):
        self.balance -= amount
        backend.update_balance(self.id_key, self.balance)
        self.main_screen(self.first_name_value, self.last_name_value)
        self.hide_items()

    def deposit_tab(self):
        self.hide_items()
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, "How much would you like to deposit? ")

        self.deposit_entry.grid()
        self.deposit_button.grid()
        self.cancel_button.grid()

    def deposit(self, amount):
        self.balance += amount
        backend.update_balance(self.id_key, self.balance)
        self.main_screen(self.first_name_value, self.last_name_value)
        self.hide_items()

    def transfer(self, amount):
        self.balance -= amount

    def hide_buttons(self, button, entry):
        button.grid_forget()
        entry.grid_forget()


window = Tk()
new_window = Toplevel()

account = Account(window, new_window)

window.mainloop()
    
