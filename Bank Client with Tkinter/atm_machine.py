from tkinter import *
import backend

class Account:

    def __init__(self, window, window_2):
        """ initialize all the buttons and text entry here
            then gets hidden by calling hide_items()
        """
        
        self.id_key = IntVar()
        
        self.chequing_balance = DoubleVar()
        self.savings_balance = DoubleVar()
        
        self.window = window
        self.window_2 = window_2
        
        self.account = ["chequing", "savings"]
        self.current_account = self.account[0]          

        self.first_name_value = StringVar()
        self.last_name_value = StringVar()
        
        self.login_window(self.window_2)
        
        self.chequing_button = Button(self.window, text = "Chequing Account", command = lambda: self.switched_accounts(0))
        self.chequing_button.grid(row = 0, column = 0)

        self.savings_button = Button(self.window, text = "Savings Account", command = lambda: self.switched_accounts(1))
        self.savings_button.grid(row = 0, column = 1)

        self.sink_buttons()

        self.withdraw_button = Button(self.window, text = "Withdraw", command = self.withdraw_tab)
        self.withdraw_button.grid(row = 1, column = 2)

        self.deposit_button = Button(self.window, text = "Deposit", command = self.deposit_tab)
        self.deposit_button.grid(row = 2, column = 2)

        self.view_balance_button = Button(self.window, text = "View Balance", command = self.view_balance)
        self.view_balance_button.grid(row = 3, column = 2)
    
        self.transfer_button = Button(self.window, text = "Transfer")
        self.transfer_button.grid(row = 4, column = 2)

        self.main_text = Text(self.window, width = 30, height = 7.5, wrap = WORD)
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
        self.window.withdraw()

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

        self.exit_button = Button(new_window, text = "Exit", command = self.window.destroy)
        self.exit_button.grid(row = 2, column = 1)

        window_2.protocol("WM_DELETE_WINDOW", self.disable_x)

    def login_command(self):
        selected_client = backend.login_client(self.first_name_value.get(), self.last_name_value.get())
        self.id_key = selected_client[0][0]
        self.first_name_value = selected_client[0][1]
        self.last_name_value = selected_client[0][2]
        self.main_screen(self.first_name_value, self.last_name_value)
        self.chequing_balance = selected_client[0][9]
        self.savings_balance = selected_client[0][10]
        self.window.deiconify()
        self.window.attributes("-topmost", "true")
        self.window_2.destroy()

    def main_screen(self, f_name, l_name):
        self.hide_items()
        self.main_text.configure(state = 'normal')
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, "Welcome to your " + self.current_account.capitalize() + " Account, ")
        self.main_text.insert(END, f_name + " " + l_name + ". What would you like to do?")    
        self.main_text.configure(state = 'disable')

    def switched_accounts(self, acc_num):
        self.current_account = self.account[acc_num]
        self.sink_buttons()
        self.main_screen(self.first_name_value, self.last_name_value)

    def view_balance(self):
        self.hide_items()
        self.main_text.configure(state = 'normal')
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, self.first_name_value + " " + self.last_name_value + ", you have:" )
        if (self.current_account == self.account[0]):
            self.main_text.insert(END, "\n\n$" + str(self.chequing_balance))
        else:
            self.main_text.insert(END, "\n\n$" + str(self.savings_balance))
        self.back_button.grid()
        self.main_text.configure(state = 'disable')  

    def withdraw_tab(self):
        self.hide_items()
        self.main_text.configure(state = 'normal')        
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, "How much would you like to withdraw? ")

        self.withdraw_entry.grid()
        self.withdraw_button.grid()
        self.cancel_button.grid()
        
        self.main_text.configure(state = 'disable')  
       
    def withdraw(self, amount):
        if self.current_account == self.account[0]:
            self.chequing_balance -= amount
            backend.update_balance(self.id_key, 0, self.chequing_balance)
        else:
            self.savings_balance -= amount
            backend.update_balance(self.id_key, 1, self.savings_balance)
            
        self.main_screen(self.first_name_value, self.last_name_value)
        self.hide_items()

    def deposit_tab(self):
        self.hide_items()
        self.main_text.configure(state = 'normal') 
        self.main_text.delete("1.0", END)
        self.main_text.insert(END, "How much would you like to deposit? ")

        self.deposit_entry.grid()
        self.deposit_button.grid()
        self.cancel_button.grid()
        
        self.main_text.configure(state = 'disable')
        
    def deposit(self, amount):
        if self.current_account == self.account[0]:
            self.chequing_balance += amount
            backend.update_balance(self.id_key, 0, self.chequing_balance)
        else:
            self.savings_balance += amount
            backend.update_balance(self.id_key, 1, self.savings_balance)

        self.main_screen(self.first_name_value, self.last_name_value)
        self.hide_items()

    def transfer(self, amount):
        self.chequing_balance -= amount

    def sink_buttons(self):
        if self.current_account == self.account[0]:
            self.savings_button.configure(relief = RAISED)
            self.chequing_button.configure(relief = SUNKEN)
        else:
            self.savings_button.configure(relief = SUNKEN)
            self.chequing_button.configure(relief = RAISED)        

    def disable_x(self):
        pass

window = Tk()
new_window = Toplevel()

account = Account(window, new_window)

window.mainloop()
    
