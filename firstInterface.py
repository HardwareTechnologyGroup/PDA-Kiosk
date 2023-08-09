import tkinter as tk
import customtkinter as ctk
from tkinter import scrolledtext
from tkinter.ttk import Frame
import tkinter.font as tkfont
from Mysqlconnect import cursor, db
from save_registration import save_registration_data
from refresh_registration import refresh_registration_data
from search_registration2 import search_registration_data
from saveFoodData import save_food_data
import newsecondinterface as transactionInterface


def clear_input_fields(fname_entry, lname_entry, age_entry, addhar_entry,rationId_entry,familyCount_entry):
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    addhar_entry.delete(0, tk.END)
    rationId_entry.delete(0,tk.END)
    familyCount_entry.delete(0,tk.END)

def handle_save_registration(fname_entry, lname_entry, age_entry, addhar_entry,rationId_entry,familyCount_entry, family_textbox):
    fname = fname_entry.get()
    lname = lname_entry.get()
    age = age_entry.get()
    addhar_number = addhar_entry.get()
    ration_id=rationId_entry.get()
    family_count=familyCount_entry.get()

    if save_registration_data(fname, lname, age, addhar_number,ration_id,family_count):
        clear_input_fields(fname_entry, lname_entry, age_entry, addhar_entry,rationId_entry,familyCount_entry)
        refresh_registration_data(family_textbox)
        save_food_data(ration_id,family_count)


def handle_search_registration(family_textbox,food_textbox,search_entry):
    search_query = search_entry.get()
    search_registration_data(family_textbox,food_textbox,search_query)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def main():
    # Create the tkinter window
    window = ctk.CTk()
    window.geometry("800x800")
    window.title("Registration Form")
    window.configure(background="#4682B4")

    # Define a custom font
    custom_font = tkfont.Font(family="Times New Roman", size=12)

    # Configure the font for all widgets
    window.option_add("*Font", custom_font)

    # Create form fields
    fname_label = ctk.CTkLabel(window, text="First Name:")
    fname_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")
    fname_entry = ctk.CTkEntry(window)
    fname_entry.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="ew")

    lname_label = ctk.CTkLabel(window, text="Last Name:")
    lname_label.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="ew")
    lname_entry = ctk.CTkEntry(window)
    lname_entry.grid(row=1, column=1, padx=(5, 10), pady=10, sticky="ew")

    age_label = ctk.CTkLabel(window, text="Age:")
    age_label.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="ew")
    age_entry = ctk.CTkEntry(window)
    age_entry.grid(row=2, column=1, padx=(5, 10), pady=10, sticky="ew")

    addhar_label = ctk.CTkLabel(window, text="Aadhaar Number:")
    addhar_label.grid(row=3, column=0, padx=(10, 5), pady=10, sticky="ew")
    addhar_entry = ctk.CTkEntry(window)
    addhar_entry.grid(row=3, column=1, padx=(5, 10), pady=10, sticky="ew")

    rationId_label = ctk.CTkLabel(window, text="Ration Id:")
    rationId_label.grid(row=4, column=0, padx=(10, 5), pady=10, sticky="ew")
    rationId_entry = ctk.CTkEntry(window)
    rationId_entry.grid(row=4, column=1, padx=(5, 10), pady=10, sticky="ew")

    familyCount_label = ctk.CTkLabel(window, text="Family Count:")
    familyCount_label.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="ew")
    familyCount_entry = ctk.CTkEntry(window)
    familyCount_entry.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="ew")    

    search_label = ctk.CTkLabel(window, text="Search by Ration ID:")
    search_label.grid(row=7, column=0, padx=(10, 5), pady=10, sticky="ew")
    search_entry = ctk.CTkEntry(window)
    search_entry.grid(row=7, column=1, padx=(5, 10), pady=10, sticky="ew")

    def handle_search():
        handle_search_registration(family_textbox,food_textbox,search_entry)

    search_button = ctk.CTkButton(window, text="SEARCH", command=handle_search)
    search_button.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

    def handle_save():
        handle_save_registration(fname_entry, lname_entry, age_entry, addhar_entry,rationId_entry,familyCount_entry,family_textbox )

    save_button = ctk.CTkButton(window, text="SAVE", command=handle_save)
    save_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

    textbox_frame1 = ctk.CTkFrame(window)
    textbox_frame1.grid(row=10, column=0,pady=10, sticky="nsew") #padx=30,columnspan=2

    textbox_label1 = ctk.CTkLabel(textbox_frame1, text="FAMILY DETAILS",justify="center")
    textbox_label1.pack()

    family_textbox = ctk.CTkTextbox(textbox_frame1,pady=10, width=40, height=10) #padx=10
    family_textbox.pack(expand=True, fill="both")

    textbox_frame2 = ctk.CTkFrame(window)
    textbox_frame2.grid(row=10, column=1,pady=10, sticky="nsew")
    textbox_label2 = ctk.CTkLabel(textbox_frame2, text="FOOD DETAILS",justify="center")
    textbox_label2.pack()

    food_textbox= ctk.CTkTextbox(textbox_frame2, pady=10, width=40, height=10)
    food_textbox.pack(expand=True, fill="both")

    def open_transaction_interface():
        window.destroy()
        transactionInterface.main()

    transaction_interface_button = ctk.CTkButton(window, text="ENTER TRANSACTION DETAILS", command=open_transaction_interface)
    transaction_interface_button.grid(row=9, column=1, padx=10, pady=10, sticky="ew")


    window.grid_rowconfigure(10, weight=1)
    window.grid_columnconfigure(0, weight=5)
    window.grid_columnconfigure(1, weight=5)

    if save_registration_data.__name__ not in locals():
        refresh_registration_data(family_textbox)

    window.mainloop()

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
