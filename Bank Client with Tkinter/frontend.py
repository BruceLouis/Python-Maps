from tkinter import *
import backend

class MainMenu:
    """
    certain buttons are disabled when the window first starts up
    this is due to its reliance for client's id info
    as soon as a client gets selected on the listbox and
    get_selected_row finally gets invoked, all buttons will be enabled
    """
    def __init__(self, window):

        window.wm_title("Client Information")

        self.first_name_label = Label(window, text = "First Name")
        self.first_name_label.grid(row = 0, column = 0)

        self.first_name_value = StringVar()
        self.first_name_entry = Entry(window, textvariable = self.first_name_value)
        self.first_name_entry.grid(row = 0, column = 1)

        self.last_name_label = Label(window, text = "Last Name")
        self.last_name_label.grid(row = 0, column = 2)

        self.last_name_value = StringVar()
        self.last_name_entry = Entry(window, textvariable = self.last_name_value)
        self.last_name_entry.grid(row = 0, column = 3)

        self.gender_label = Label(window, text = "Gender")
        self.gender_label.grid(row = 0, column = 4)

        self.gender_value = StringVar()
        self.gender_entry = Entry(window, textvariable = self.gender_value)
        self.gender_entry.grid(row = 0, column = 5)

        self.scroll_bar = Scrollbar(window)
        self.scroll_bar.grid(row = 1, column = 4, rowspan = 6)

        self.listbox = Listbox(window, width = 75, height = 10)
        self.listbox.grid(row = 1, column = 0, columnspan = 4, rowspan = 7)
        
        self.listbox.bind("<Double-Button-1>", self.open_clients_entry)
        self.listbox.bind("<<ListboxSelect>>", self.get_selected_row)

        self.listbox.configure(yscrollcommand = self.scroll_bar.set)
        self.scroll_bar.configure(command = self.listbox.yview)
        
        self.view_all_button = Button(window, width = 12, text = "View All", command = self.view_clients)
        self.view_all_button.grid(row = 1, column = 5)
        
        self.search_entry_button = Button(window, width = 12, text = "Search Entry", command = self.search_clients)
        self.search_entry_button.grid(row = 2, column = 5)
       
        self.add_entry_button = Button(window, width = 12, text = "Add Entry", command = self.add_client)
        self.add_entry_button.grid(row = 3, column = 5)
        
        self.open_entry_button = Button(window, width = 12, text = "Open Entry", command = self.open_personal_info_menu)
        self.open_entry_button.grid(row = 4, column = 5)
        
        self.update_balance_button = Button(window, width = 12, text = "Update Balance", command = self.open_balance_window)
        self.update_balance_button.grid(row = 5, column = 5)
        
        self.delete_button = Button(window, width = 12, text = "Delete", command = self.delete_client)
        self.delete_button.grid(row = 6, column = 5)
        
        self.close_button = Button(window, width = 12, text = "Close", command = window.destroy)
        self.close_button.grid(row = 7, column = 5)

        self.menu_activation('disable')
        

    def get_selected_row(self, event):

        """
        try & catch/except prevents the program from showing an error
        whenever a blank listbox gets selected
        """
        try:
            index = self.listbox.curselection()[0]
            self.selected_tuple = self.listbox.get(index)
            self.selected_tuple = self.selected_tuple.split()
            self.extended_tuple = backend.select_client(self.selected_tuple[0])
            self.first_name_entry.delete(0,END)
            self.first_name_entry.insert(END, self.selected_tuple[1])
            self.last_name_entry.delete(0,END)
            self.last_name_entry.insert(END, self.selected_tuple[2])
            self.gender_entry.delete(0,END)
            self.gender_entry.insert(END, self.selected_tuple[3])
            self.menu_activation('normal')

        except IndexError:
            pass

    def menu_activation(self, on_or_off):
        self.open_entry_button.configure(state = on_or_off)
        self.update_balance_button.configure(state = on_or_off)
        self.delete_button.configure(state = on_or_off)

    def open_personal_info_menu(self):
        self.personal_info = PersonalInfoMenu(  self.selected_tuple[0], self.selected_tuple[1], self.selected_tuple[2],
                                                self.selected_tuple[3], self.extended_tuple[0][4], self.extended_tuple[0][5],
                                                self.extended_tuple[0][6], self.extended_tuple[0][7], self.extended_tuple[0][8])

    def open_clients_entry(self, event):
        self.open_personal_info_menu()

    def open_balance_window(self):
        self.balance_info = ClientBalance(self.selected_tuple[0], self.selected_tuple[1], self.selected_tuple[2],
                                          self.extended_tuple[0][9], self.extended_tuple[0][10])

    def view_clients(self):
        client_rows = backend.view()
        self.listbox.delete(0, END)
        
        for clients in client_rows:
            print_string = str(clients[0]) + " " + str(clients[1]) + " " + str(clients[2]) + " " + str(clients[3])
            if clients[9] is not None and clients[10] is not None:
                self.listbox.insert(END, print_string + " : $" + str(clients[9]) + " $" + str(clients[10]))
            else:
                self.listbox.insert(END, print_string)


    def search_clients(self):
        searched_clients = backend.search(self.first_name_value.get(), self.last_name_value.get(), self.gender_value.get())
        self.listbox.delete(0, END)
        
        for clients in searched_clients:
            print_string = str(clients[0]) + " " + str(clients[1]) + " " + str(clients[2]) + " " + str(clients[3])
            if clients[9] is not None and clients[10] is not None:
                self.listbox.insert(END, print_string + " : $" + str(clients[9]) + " $" + str(clients[10]))
            else:
                self.listbox.insert(END, print_string)

    def add_client(self):
        backend.insert_basic(self.first_name_value.get(), self.last_name_value.get(), self.gender_value.get())
        self.listbox.delete(0, END)
        self.listbox.insert(END, (self.first_name_value.get(), self.last_name_value.get(), self.gender_value.get()))

    def delete_client(self):
        backend.delete(self.selected_tuple[0])

class PersonalInfoMenu:

    def __init__(self, id_key, f_name, l_name, gender, address, city, province, phone, zip_code):

        self.personal_window = Toplevel()
        self.personal_window.wm_title("Personal Information")

        self.id_key = id_key

        self.greyed_first_name_entry = Entry(self.personal_window)
        self.greyed_first_name_entry.grid(row = 0, column = 0)
        self.greyed_first_name_entry.delete(0, END)
        self.greyed_first_name_entry.insert(END, f_name)
        self.greyed_first_name_entry.configure(state = 'disable')

        self.greyed_last_name_entry = Entry(self.personal_window, width = 30)
        self.greyed_last_name_entry.grid(row = 0, column = 1, columnspan = 2)    
        self.greyed_last_name_entry.delete(0, END)
        self.greyed_last_name_entry.insert(END, l_name)
        self.greyed_last_name_entry.configure(state = 'disable')

        self.greyed_gender_entry = Entry(self.personal_window)
        self.greyed_gender_entry.grid(row = 0, column = 3)
        self.greyed_gender_entry.delete(0, END)
        self.greyed_gender_entry.insert(END, gender)
        self.greyed_gender_entry.configure(state = 'disable')        

        self.address_label = Label(self.personal_window, text = "Address")
        self.address_label.grid(row = 1, column = 0)

        self.address_value = StringVar()
        self.address_entry = Entry(self.personal_window, width = 50, textvariable = self.address_value)
        self.address_entry.grid(row = 1, column = 1, columnspan = 3)
        self.address_entry.delete(0, END)
        if address is not None:
            self.address_entry.insert(END, address)
        
        self.city_label = Label(self.personal_window, text = "City")
        self.city_label.grid(row = 2, column = 0)

        self.city_value = StringVar()
        self.city_entry = Entry(self.personal_window, textvariable = self.city_value)
        self.city_entry.grid(row = 2, column = 1)
        if city is not None:
            self.city_entry.insert(END, city)
        
        self.province_label = Label(self.personal_window, text = "Province")
        self.province_label.grid(row = 2, column = 2)

        self.province_value = StringVar()
        self.province_entry = Entry(self.personal_window, textvariable = self.province_value)
        self.province_entry.grid(row = 2, column = 3)
        if province is not None:
            self.province_entry.insert(END, province)    
        
        self.phone_number_label = Label(self.personal_window, text = "Phone Number")
        self.phone_number_label.grid(row = 3, column = 0)

        self.phone_number_value = StringVar()
        self.phone_number_entry = Entry(self.personal_window, textvariable = self.phone_number_value)
        self.phone_number_entry.grid(row = 3, column = 1)
        if phone is not None:
            self.phone_number_entry.insert(END, phone)  
        
        self.zip_code_label = Label(self.personal_window, text = "Zip Code")
        self.zip_code_label.grid(row = 3, column = 2)

        self.zip_code_value = StringVar()
        self.zip_code_entry = Entry(self.personal_window, textvariable = self.zip_code_value)
        self.zip_code_entry.grid(row = 3, column = 3)
        if zip_code is not None:
            self.zip_code_entry.insert(END, zip_code)  

        self.update_button = Button(self.personal_window, width = 20, text = "Update", command = self.update_client_info)
        self.update_button.grid(row = 4, column = 0, columnspan = 2)

        self.close_button = Button(self.personal_window, width = 20, text = "Close", command = self.personal_window.destroy)
        self.close_button.grid(row = 4, column = 2, columnspan = 2)

       
    def update_client_info(self):
        
        backend.update_personal(self.id_key, self.address_value.get(), self.city_value.get(),
                                self.province_value.get(), self.phone_number_value.get(), self.zip_code_value.get())        
        self.personal_window.destroy()

class ClientBalance:

    def __init__(self, id_key, f_name, l_name, chequing_balance, savings_balance):
        
        self.balance_window = Toplevel()
        self.balance_window.wm_title("Client's Balance")
        
        self.account = ["chequing", "savings"]
        self.id_key = id_key
        self.chequing_balance = chequing_balance
        self.savings_balance = savings_balance
        
        self.first_name_label = Label(self.balance_window, text = f_name)
        self.first_name_label.grid(row = 0, column = 0)

        self.last_name_label = Label(self.balance_window, text = l_name)
        self.last_name_label.grid(row = 0, column = 1)

        self.balance_label = Label(self.balance_window, text = "Current Balance")
        self.balance_label.grid(row = 1, column = 0)

        self.balance_value = StringVar()
        self.balance_entry = Entry(self.balance_window, textvariable = self.balance_value)
        self.balance_entry.grid(row = 1, column = 1, columnspan = 2)
    
        self.chequing_button = Button(self.balance_window, width = 10, text = "Chequing", command = lambda: self.account_switch(0))
        self.chequing_button.grid(row = 1, column = 3)

        self.savings_button = Button(self.balance_window, width = 10, text = "Savings", command = lambda: self.account_switch(1))
        self.savings_button.grid(row = 1, column = 4)
        
        self.update_button = Button(self.balance_window, width = 20, text = "Update", command = lambda: self.update_client_balance(self.balance_value))
        self.update_button.grid(row = 4, column = 0, columnspan = 2)
        self.update_button.configure(state = 'disable')

        self.close_button = Button(self.balance_window, width = 20, text = "Close", command = self.balance_window.destroy)
        self.close_button.grid(row = 4, column = 2, columnspan = 2)           

    def update_client_balance(self, balance):
        
        if self.current_account == self.account[0]:
            backend.update_balance(self.id_key, 0, float(balance.get()))
            self.balance_window.destroy()
        elif self.current_account == self.account[1]:
            backend.update_balance(self.id_key, 1, float(balance.get()))      
            self.balance_window.destroy()

    def account_switch(self, acc_num):
        
        self.balance_entry.delete(0, END)
        self.current_account = self.account[acc_num]
        
        if self.current_account == self.account[0]:
            self.savings_button.configure(relief = RAISED)
            self.chequing_button.configure(relief = SUNKEN)
            if self.chequing_balance is not None:
                self.balance_entry.insert(END, self.chequing_balance)
        else:
            self.savings_button.configure(relief = SUNKEN)
            self.chequing_button.configure(relief = RAISED)
            if self.savings_balance is not None:
                self.balance_entry.insert(END, self.savings_balance)
                
        self.update_button.configure(state = 'normal')  
    

window = Tk()

main_menu = MainMenu(window)

window.mainloop()


