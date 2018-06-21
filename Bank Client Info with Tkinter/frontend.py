from tkinter import *
import backend

def confirm_exit(update_function, exit_function):
    
    global personal_info_exit_window
    personal_info_exit_window = Toplevel()

    ask_label = Label(personal_info_exit_window, text = "Do you want to save changes?")
    ask_label.grid(row = 0, column = 0, columnspan = 2)

    yes_button = Button(personal_info_exit_window, text = "Yes", command = update_function)
    yes_button.grid(row = 1, column = 0)

    no_button = Button(personal_info_exit_window, text = "No", command = exit_function)
    no_button.grid(row = 1, column = 1)

    
def open_menu():

    def update_client_info():
        backend.update_personal(selected_tuple[0], address_entry_value.get(), city_entry_value.get(),
                                province_entry_value.get(), phone_number_entry_value.get(), zip_code_entry_value.get())
        new_window.destroy()
        
    def confirm_save_client_info():
        update_client_info()
        personal_info_exit_window.destroy()

    def info_exit():
        new_window.destroy()
        personal_info_exit_window.destroy()
        
    global new_window

    new_window = Toplevel()
    new_window.wm_title("Client Information")

    greyed_first_name_entry = Entry(new_window)
    greyed_first_name_entry.grid(row = 0, column = 0)
    greyed_first_name_entry.delete(0, END)
    greyed_first_name_entry.insert(END, selected_tuple[1])
    greyed_first_name_entry.configure(state = 'disable')

    greyed_last_name_entry = Entry(new_window, width = 30)
    greyed_last_name_entry.grid(row = 0, column = 1, columnspan = 2)    
    greyed_last_name_entry.delete(0, END)
    greyed_last_name_entry.insert(END, selected_tuple[2])
    greyed_last_name_entry.configure(state = 'disable')

    greyed_gender_entry = Entry(new_window)
    greyed_gender_entry.grid(row = 0, column = 3)
    greyed_gender_entry.delete(0, END)
    greyed_gender_entry.insert(END, selected_tuple[3])
    greyed_gender_entry.configure(state = 'disable')

    address_label = Label(new_window, text = "Address")
    address_label.grid(row = 1, column = 0)

    address_entry_value = StringVar()
    address_entry = Entry(new_window, width = 50, textvariable = address_entry_value)
    address_entry.grid(row = 1, column = 1, columnspan = 3)
    address_entry.delete(0, END)
    if extended_tuple[0][4] is not None:
        address_entry.insert(END, extended_tuple[0][4])

    city_label = Label(new_window, text = "City")
    city_label.grid(row = 2, column = 0)

    city_entry_value = StringVar()
    city_entry = Entry(new_window, textvariable = city_entry_value)
    city_entry.grid(row = 2, column = 1)
    if extended_tuple[0][5] is not None:
        city_entry.insert(END, extended_tuple[0][5])

    province_label = Label(new_window, text = "Province")
    province_label.grid(row = 2, column = 2)

    province_entry_value = StringVar()
    province_entry = Entry(new_window, textvariable = province_entry_value)
    province_entry.grid(row = 2, column = 3)
    if extended_tuple[0][6] is not None:
        province_entry.insert(END, extended_tuple[0][6])    

    phone_number_label = Label(new_window, text = "Phone Number")
    phone_number_label.grid(row = 3, column = 0)

    phone_number_entry_value = StringVar()
    phone_number_entry = Entry(new_window, textvariable = phone_number_entry_value)
    phone_number_entry.grid(row = 3, column = 1)
    if extended_tuple[0][7] is not None:
        phone_number_entry.insert(END, extended_tuple[0][7])  

    zip_code_label = Label(new_window, text = "Zip Code")
    zip_code_label.grid(row = 3, column = 2)

    zip_code_entry_value = StringVar()
    zip_code_entry = Entry(new_window, textvariable = zip_code_entry_value)
    zip_code_entry.grid(row = 3, column = 3)
    if extended_tuple[0][8] is not None:
        zip_code_entry.insert(END, extended_tuple[0][8])  

    update_button = Button(new_window, width = 20, text = "Update", command = update_client_info)
    update_button.grid(row = 4, column = 0, columnspan = 2)

    close_button = Button(new_window, width = 20, text = "Close", command = lambda: confirm_exit(confirm_save_client_info, info_exit))
    close_button.grid(row = 4, column = 2, columnspan = 2)
    

def update_balance():
    
    def update_client_balance():
        backend.update_balance(selected_tuple[0], float(balance_entry_value.get()))
        balance_window.destroy()

    def confirm_save_balance_info():
        update_client_balance()
        personal_info_exit_window.destroy()

    def balance_exit():
        personal_info_exit_window.destroy()
        balance_window.destroy()
        
    global balance_window
    balance_window = Toplevel()
    balance_window.wm_title("Client's Balance")
    
    first_name_label = Label(balance_window, text = selected_tuple[1])
    first_name_label.grid(row = 0, column = 0)

    last_name_label = Label(balance_window, text = selected_tuple[2])
    last_name_label.grid(row = 0, column = 1)

    balance_label = Label(balance_window, text = "Current Balance")
    balance_label.grid(row = 1, column = 0)

    balance_entry_value = StringVar()
    balance_entry = Entry(balance_window, textvariable = balance_entry_value)
    balance_entry.grid(row = 1, column = 1)
    if extended_tuple[0][9] is not None:
        balance_entry.insert(END, extended_tuple[0][9])  

    update_button = Button(balance_window, width = 20, text = "Update", command = update_client_balance)
    update_button.grid(row = 4, column = 0, columnspan = 2)

    close_button = Button(balance_window, width = 20, text = "Close", command = lambda: confirm_exit(confirm_save_balance_info, balance_exit))
    close_button.grid(row = 4, column = 2, columnspan = 2)
  
def get_selected_row(event):
    try:
        global selected_tuple
        global extended_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        selected_tuple = selected_tuple.split()
        extended_tuple = backend.select_client(selected_tuple[0])
        first_name_entry.delete(0,END)
        first_name_entry.insert(END, selected_tuple[1])
        last_name_entry.delete(0,END)
        last_name_entry.insert(END, selected_tuple[2])
        gender_entry.delete(0,END)
        gender_entry.insert(END, selected_tuple[3])

    except IndexError:
        pass

def view_clients():
    client_rows = backend.view()
    listbox.delete(0, END)
    
    for clients in client_rows:
        print_string = str(clients[0]) + " " + str(clients[1]) + " " + str(clients[2]) + " " + str(clients[3])
        if clients[9] is not None:
            listbox.insert(END, print_string + ": $" + str(clients[9]))
        else:
            listbox.insert(END, print_string)

def add_client():
    backend.insert_basic(first_name_entry_value.get(), last_name_entry_value.get(), gender_entry_value.get())
    listbox.delete(0, END)
    listbox.insert(END, (first_name_entry_value.get(), last_name_entry_value.get(), gender_entry_value.get()))

def search_clients():
    searched_clients = backend.search(first_name_entry_value.get(), last_name_entry_value.get(), gender_entry_value.get())
    listbox.delete(0, END)
    
    for clients in searched_clients:
        listbox.insert(END, str(clients[0]) + " " + str(clients[1]) + " " + str(clients[2]) + " " + str(clients[3]))

def delete_client():
    backend.delete(selected_tuple[0])

def open_clients_entry(event):
    open_menu()
        

window = Tk()
window.wm_title("Clients")

first_name_label = Label(window, text = "First Name")
first_name_label.grid(row = 0, column = 0)

first_name_entry_value = StringVar()
first_name_entry = Entry(window, textvariable = first_name_entry_value)
first_name_entry.grid(row = 0, column = 1)

last_name_label = Label(window, text = "Last Name")
last_name_label.grid(row = 0, column = 2)

last_name_entry_value = StringVar()
last_name_entry = Entry(window, textvariable = last_name_entry_value)
last_name_entry.grid(row = 0, column = 3)

gender_label = Label(window, text = "Gender")
gender_label.grid(row = 0, column = 4)

gender_entry_value = StringVar()
gender_entry = Entry(window, textvariable = gender_entry_value)
gender_entry.grid(row = 0, column = 5)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 1, column = 4, rowspan = 6)

listbox = Listbox(window, width = 75, height = 10)
listbox.grid(row = 1, column = 0, columnspan = 4, rowspan = 7)

listbox.bind("<Double-Button-1>", open_clients_entry)
listbox.bind("<<ListboxSelect>>", get_selected_row)

listbox.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = listbox.yview)

view_all_button = Button(window, width = 12, text = "View All", command = view_clients)
view_all_button.grid(row = 1, column = 5)

search_entry_button = Button(window, width = 12, text = "Search Entry", command = search_clients)
search_entry_button.grid(row = 2, column = 5)

add_entry_button = Button(window, width = 12, text = "Add Entry", command = add_client)
add_entry_button.grid(row = 3, column = 5)

open_entry_button = Button(window, width = 12, text = "Open Entry", command = open_menu)
open_entry_button.grid(row = 4, column = 5)

update_balance_button = Button(window, width = 12, text = "Update Balance", command = update_balance)
update_balance_button.grid(row = 5, column = 5)

delete_button = Button(window, width = 12, text = "Delete", command = delete_client)
delete_button.grid(row = 6, column = 5)

close_button = Button(window, width = 12, text = "Close", command = window.destroy)
close_button.grid(row = 7, column = 5)

window.mainloop()
