import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from tkinter import *
from tkinter import PhotoImage
from tkinter import font as tkfont
import sqlite3
import requests
import pyttsx3
import pygame
import time
from PIL import ImageTk, Image

from playsound import playsound
from gtts import gTTS








class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance': tk.IntVar()}
#         self.shared_data={'Kiosk Balance': tk.IntVar()}
        

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight='bold', slant='italic')

        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomePage, OptionPage, StartPage,OptionA, OptionB,OptionC, OptionD, ServicePage):
            page = F.__name__
            frame = F(parent=window, controller=self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        
        
        

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#87CEFA')
        self.controller = controller

        self.controller.title('Kiosk')
        self.controller.state('normal')
        
        

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        heading_label = tk.Label(self,
                                 text='Welcome to Kiosk',
                                 font=('Arial', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')
        heading_label.pack(pady=25)
        
        heading_label2 = tk.Label(self,
                                 text='Government of India',
                                 font=('Arial', 30, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')
        heading_label2.pack(pady=25)

        
#         photo = tk.PhotoImage(file='cdac.jpg')
#         label = Label(self, image=photo,height=50, width=50)
#         label = tk.Label(bottom_frame, image=photo)
# #         resized_image = photo.resize(50, 50)
#         label.pack(pady=40, padx=40)
#         label.image = photo


        img=Image.open("cdac.jpg")
        #img=img.resize(200,400)
        photo=ImageTk.PhotoImage(img)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(pady=25)

        # engine = pyttsx3.init()
        # engine.say('Welcome to Kiosk')
        # engine.say('Thank you')
        # engine.runAndWait()

        def on_click():
            controller.show_frame('StartPage')
        
        heading_label.after(3000, on_click)
        
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#87CEFA')
        self.controller = controller

        self.controller.title('Kiosk')
        self.controller.state('normal')
        self.controller.iconphoto(False, tk.PhotoImage(file="atm_icon.png"))

        heading_label = tk.Label(self,
                                 text='Kiosk',
                                 font=('Arial', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#87CEFA')
        space_label.pack()


        engine = pyttsx3.init()
        engine.say('Please enter your account number and password ')
        engine.say('Thank you')
        # engine.runAndWait()

        account_label = tk.Label(self,
                                 text="Enter your account number : ",
                                 font=('orbitron', 13),
                                 bg='#87CEFA',
                                 fg='#ffffff')
        account_label.pack()

        my_account = tk.StringVar()
        account_entry_box = tk.Entry(
            self, textvariable=my_account, font=('orbitron', 12), width=40)
        account_entry_box.pack(ipady=7)

        password_label = tk.Label(self, text="Enter your password : ",
                                  font=('orbitron', 13),
                                  bg='#87CEFA',
                                  fg='#ffffff')
        password_label.pack()

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password,
                                      font=(
                                          'orbitron', 12),
                                      width=40)
        password_entry_box.pack(ipady=7)

        def check_password():
            if my_password.get() == '123':
                my_password.set('')
                controller.show_frame('OptionPage')
            else:
                incorrect_password_label['text'] = 'Incorrect Password'
        enter_button = tk.Button(self,
                                 text="Enter",
                                 command=check_password,
                                 relief='raised',
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self,
                                            text="",
                                            font=('orbitron', 13),
                                            bg='#00BFFF',
                                            fg='#ffffff',
                                            anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)
        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')
        tick()
        

class OptionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#87CEFA')
        self.controller = controller

        # engine = pyttsx3.init()
        # engine.say('Please select an option for withdrawl')
        # engine.say('Thank you')
        # engine.runAndWait()

        heading_label = tk.Label(self,
                                 text='Kiosk',
                                 font=('Arial', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')

        main_menu_label = tk.Label(self,
                                   text='Service Option',
                                   font=('orbitron', 35, 'bold'),
                                   foreground='#ffffff',
                                   background='#87CEFA')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 20, 'bold'),
                                   foreground='#ffffff',
                                   background='#87CEFA',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self,
                                bg='#00BFFF')
        button_frame.pack(fill='both', expand=True)

        def optionA():
            controller.show_frame('OptionA')
        withdraw_button = tk.Button(button_frame,
                                    text='Rice',
                                    command=optionA,
                                    relief='raised',
                                    borderwidth=3,
                                    width=40,
                                    height=2)
        withdraw_button.grid(row=0, column=2,padx=50, pady=30)

        def optionB():
            controller.show_frame('OptionB')
        balance_button = tk.Button(button_frame,
                                   text='Wheat',
                                   command=optionB,
                                   relief='raised',
                                   borderwidth=3,
                                   width=40,
                                   height=2)
        balance_button.grid(row=1, column=2,padx=50, pady=30)
        
        def optionC():
            controller.show_frame('OptionC')
        withdraw_button = tk.Button(button_frame,
                                    text='Sugar',
                                    command=optionC,
                                    relief='raised',
                                    borderwidth=3,
                                    width=40,
                                    height=2)
        withdraw_button.grid(row=2, column=2,padx=50, pady=30)
        
        def optionD():
            controller.show_frame('OptionD')
        withdraw_button = tk.Button(button_frame,
                                    text='Dal',
                                    command=optionD,
                                    relief='raised',
                                    borderwidth=3,
                                    width=40,
                                    height=2)
        withdraw_button.grid(row=3, column=2,padx=50, pady=30)

        def exit():
            controller.show_frame('StartPage')
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=2)
        exit_button.grid(row=4, column=2,padx=50, pady=30)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)
        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')
        tick()


        
        

class OptionA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#87CEFA')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Kiosk',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')
        heading_label.pack(pady=25)
        



        button_frame = tk.Frame(self, bg='#00BFFF')
        button_frame.pack(fill='both', expand=True)


#         

        def account():
            if account_entry_box.get() == '':
                messagebox.showinfo("Opps!", "Please enter an amount")
            else:
                messagebox.showinfo("Great", "You can collect your amount")
        
        account_label = tk.Label(self,
                                 text='Enter Amount',
                                 font=('orbitron', 12),
                                 bg='#87CEFA',
                                 fg='white')
        account_label.pack( padx=25 )
        
        my_account1 = tk.StringVar()
        account_entry_box = tk.Entry(self,
                                     textvariable=my_account1,
                                     font=('orbitron', 12),
                                     width=22)
        account_entry_box.focus_set()
        account_entry_box.pack(padx=25, ipady=7)                
        
        enter_button = tk.Button(button_frame,
                                text='Enter',
                                command=account,
                                relief='raised',
                                borderwidth=3,
                                width=30,
                                height=2)
        enter_button.grid(row=2, column=2,padx=50, pady=30)
        
        def exit():
            controller.show_frame('StartPage')
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=30,
                                height=2)
        exit_button.grid(row=3, column=2,padx=50, pady=30)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)
        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')
        tick()
    
class OptionB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#87CEFA')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Kiosk',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')
        heading_label.pack(pady=25)
        


        # current_amount_label = tk.Label(self,
        #                                 text='Current Amount: ',
        #                                 font=('orbitron', 13),
        #                                 fg='white',
        #                                 bg='#87CEFA')
        # current_amount_label.pack()
        #
        #
        # global current_balance
        # controller.shared_data['Balance'].set(current_balance)
        # balance_label = tk.Label(self,
        #                          textvariable=controller.shared_data['Balance'],
        #                          font=('orbitron', 13),
        #                          fg='white',
        #                          bg='#87CEFA',
        #                          anchor='w')
        # balance_label.pack()

        



        button_frame = tk.Frame(self, bg='#00BFFF')
        button_frame.pack(fill='both', expand=True)


        def account():
            if account_entry_box.get() == '':
                messagebox.showinfo("Opps!", "Please enter an amount")
            else:
                messagebox.showinfo("Great", "You can collect your amount")
        
        account_label = tk.Label(self,
                                 text='Enter Amount',
                                 font=('orbitron', 12),
                                 bg='#87CEFA',
                                 fg='white')
        account_label.pack( padx=25 )
        
        my_account = tk.StringVar()
        account_entry_box = tk.Entry(self,
                                     textvariable=my_account,
                                     font=('orbitron', 12),
                                     width=22)
        account_entry_box.focus_set()
        account_entry_box.pack(padx=25, ipady=7)                
        
        enter_button = tk.Button(button_frame,
                                text='Enter',
                                command=account,
                                relief='raised',
                                borderwidth=3,
                                width=30,
                                height=2)
        enter_button.grid(row=2, column=2,padx=50, pady=30)
        
        def exit():
            controller.show_frame('StartPage')
        exit_button2 = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=30,
                                height=2)
        exit_button2.grid(row=3, column=2,padx=50, pady=30)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)
        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')
        tick()
        
class OptionC(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg='#87CEFA')
            self.controller = controller

            heading_label = tk.Label(self,
                                     text='Kiosk',
                                     font=('orbitron', 45, 'bold'),
                                     foreground='#ffffff',
                                     background='#87CEFA')
            heading_label.pack(pady=25)
        


            current_amount_label = tk.Label(self,
                                        text='Current Amount: ',
                                        font=('orbitron', 13),
                                        fg='white',
                                        bg='#87CEFA')
            current_amount_label.pack()
        
        
            # global current_balance
            # controller.shared_data['Balance'].set(current_balance)
            # balance_label = tk.Label(self,
            #                          textvariable=controller.shared_data['Balance'],
            #                          font=('orbitron', 13),
            #                          fg='white',
            #                          bg='#87CEFA',
            #                          anchor='w')
            # balance_label.pack()

        



            button_frame = tk.Frame(self, bg='#00BFFF')
            button_frame.pack(fill='both', expand=True)


            def account():
                if account_entry_box.get() == '':
                    messagebox.showinfo("Opps!", "Please enter an amount")
                else:
                    messagebox.showinfo("Great", "You can collect your amount")
            
            account_label = tk.Label(self,
                                     text='Enter Amount',
                                     font=('orbitron', 12),
                                     bg='#87CEFA',
                                     fg='white')
            account_label.pack( padx=25 )
            
            my_account = tk.StringVar()
            account_entry_box = tk.Entry(self,
                                         textvariable=my_account,
                                         font=('orbitron', 12),
                                         width=22)
            account_entry_box.focus_set()
            account_entry_box.pack(padx=25, ipady=7)                
            
            enter_button = tk.Button(button_frame,
                                    text='Enter',
                                    command=account,
                                    relief='raised',
                                    borderwidth=3,
                                    width=30,
                                    height=2)
            enter_button.grid(row=2, column=2,padx=50, pady=30)
            def exit():
                controller.show_frame('StartPage')
            exit_button2 = tk.Button(button_frame,
                                    text='Exit',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=30,
                                    height=2)
            exit_button2.grid(row=3, column=2,padx=50, pady=30)

            bottom_frame = tk.Frame(self,
                                    relief='raised',
                                    borderwidth=3)
            bottom_frame.pack(fill='x', side='bottom')

            def tick():
                current_time = time.strftime('%I:%M %p')
                time_label.config(text=current_time)
                time_label.after(200, tick)
            time_label = tk.Label(bottom_frame, font=('orbitron', 12))
            time_label.pack(side='right')
            tick()
        
        
class OptionD(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg='#87CEFA')
            self.controller = controller

            heading_label = tk.Label(self,
                                     text='Kiosk',
                                     font=('orbitron', 45, 'bold'),
                                     foreground='#ffffff',
                                     background='#87CEFA')
            heading_label.pack(pady=25)
            


            # current_amount_label = tk.Label(self,
            #                                 text='Current Amount: ',
            #                                 font=('orbitron', 13),
            #                                 fg='white',
            #                                 bg='#87CEFA')
            # current_amount_label.pack()
            #
            #
            # global current_balance
            # controller.shared_data['Balance'].set(current_balance)
            # balance_label = tk.Label(self,
            #                          textvariable=controller.shared_data['Balance'],
            #                          font=('orbitron', 13),
            #                          fg='white',
            #                          bg='#87CEFA',
            #                          anchor='w')
            # balance_label.pack()

        



            button_frame = tk.Frame(self, bg='#00BFFF')
            button_frame.pack(fill='both', expand=True)





            def account():
                if account_entry_box.get() == '':
                    messagebox.showinfo("Opps!", "Please enter an amount")
                else:
                    messagebox.showinfo("Great", "You can collect your amount")

            # Play sound
            pygame.mixer.init()  # initialise the pygame
            def play():
                pygame.mixer.music.load("Welcome.mp3")
                pygame.mixer.music.play(loops=0)



            account_label = tk.Label(self,
                                     text='Enter Amount',
                                     font=('orbitron', 12),
                                     bg='#87CEFA',
                                     fg='white')
            account_label.pack( padx=25 )
            
            my_account = tk.StringVar()
            account_entry_box = tk.Entry(self,
                                         textvariable=my_account,
                                         font=('orbitron', 12),
                                         width=22)
            account_entry_box.focus_set()
            account_entry_box.pack(padx=25, ipady=7)                
            
            enter_button = tk.Button(button_frame,
                                    text='Enter',
                                    command=play,
                                    relief='raised',
                                    borderwidth=3,
                                    width=30,
                                    height=2)
            enter_button.grid(row=2, column=2,padx=50, pady=30)
            
            def exit():
                controller.show_frame('StartPage')
            exit_button2 = tk.Button(button_frame,
                                    text='Exit',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=30,
                                    height=2)
            exit_button2.grid(row=3, column=2,padx=50, pady=30)

            bottom_frame = tk.Frame(self,
                                    relief='raised',
                                    borderwidth=3)
            bottom_frame.pack(fill='x', side='bottom')

            def tick():
                current_time = time.strftime('%I:%M %p')
                time_label.config(text=current_time)
                time_label.after(200, tick)
            time_label = tk.Label(bottom_frame, font=('orbitron', 12))
            time_label.pack(side='right')
            tick()
        
class ServicePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#87CEFA')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Kiosk',
                                 font=('Arial', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#87CEFA')

        main_menu_label = tk.Label(self,
                                   text='Service Option',
                                   font=('orbitron', 35, 'bold'),
                                   foreground='#ffffff',
                                   background='#87CEFA')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 20, 'bold'),
                                   foreground='#ffffff',
                                   background='#87CEFA',
                                   anchor='w')
        selection_label.pack(fill='x')

        
        curr_amount_frame = tk.Frame(self,
                                bg='#00BFFF')
        curr_amount_frame.pack(fill='both', expand=True)
        
        
        
        

        button_frame = tk.Frame(self,
                                bg='#00BFFF')
        button_frame.pack(fill='both', expand=True)
        
        
        
        def exit():
            controller.show_frame('StartPage')
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=2, column=2,padx=50, pady=30)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)
        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')
        tick()
        
        
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()