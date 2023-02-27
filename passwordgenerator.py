import customtkinter
import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    letters = string.ascii_lowercase
    digits = string.digits
    special =("!","@","#","$","?")
    password = random.choice(string.ascii_uppercase) + random.choice(letters) + random.choice(string.ascii_uppercase) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(digits) + random.choice(special) + random.choice(letters) + random.choice(letters) + random.choice(special)
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def save_password():
    kullanici_adi = user_entry.get()
    password_usage = platform_entry.get()
    password = generate_password()

    with open("passwords.txt", "a") as file:
        file.write("Username : " + kullanici_adi + "\n")
        file.write("Password : " + password + "\n")
        file.write("Platform : " + password_usage + "\n")
        file.write("-------------------------------\n")
    messagebox.showinfo("Password Generator","Password Saved To ""Passwords.txt""")
    root.destroy()

customtkinter.set_appearance_mode("grey")

root = tk.Tk()
root.geometry("300x200")
root.title("Password Generator")
root.resizable(False,False)


user_label = tk.Label(root, text="Username :")
user_label.place(relx = 0.1, rely = 0.3)

user_entry = tk.Entry(root)
user_entry.place(relx = 0.4, rely = 0.3)

platform_label = tk.Label(root, text="Platform :")
platform_label.place(relx = 0.1, rely = 0.4)

platform_entry = tk.Entry(root)
platform_entry.place(relx = 0.4, rely = 0.4)

save_button = tk.Button(root,text="Save Password" , command=save_password)
save_button.place(relx = 0.4, rely = 0.5)


root.mainloop()
