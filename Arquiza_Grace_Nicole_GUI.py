from tkinter import *
from tkinter import messagebox

class CRYPTO(Frame):
    def __init__(self):

        Frame.__init__(self)
        self.master.title("CRYPTOGRAPHY") # MAIN TITLE
        self.pack()
        
        # LABEL FOR THE TITLE OF THE PROGRAM
        self.nameLabel = Label(self, text = "RECIPROCAL OF LETTERS\nENCRYPTION & DECRYPTION  ", fg = "black", font = ("sans-serif", 15))
        self.nameLabel.pack(pady = 20)
        # LABEL AND TEXT BOX FOR INPUTTING A MESSAGE || WORD 
        self.msgLabel = Label(self, text = "INPUT A WORD TO ENCRYPT/DECRYPT", fg = "black", font = ("sans-serif", 14))
        self.msgLabel.pack(pady = 0)
        self.msg = StringVar()
        self.textMsg = Entry(self, textvariable = self.msg, width=19, bd=0, bg="light blue", font=("arial",25))
        self.textMsg.pack(pady = 10)
        self.msg.set(self.msg.get().upper())
        # BUTTON FOR ENCRYPT AND DECRYPT
        self.encButton = Button(self, text = "ENCRYPT", height="2", width=25, bg="pink", fg="black", bd=0, command = self.encode)
        self.encButton.pack(side = LEFT, pady = 10)
        self.decButton = Button(self, text = "DECRYPT", height="2", width=25, bg="pink", fg="black", bd=0, command = self.decode)
        self.decButton.pack(side = RIGHT, pady = 10)
        
        # self.resetButton = Button(self, text = "EXIT", height="2", width=20, bg="red", fg="white", bd=0, command = self.Exit)
        # self.resetButton.pack(side = BOTTOM, pady = 30)

    def to_uppercase(*args, self):
        self.msg.set(self.msg.get().upper())

    def encode(self): # LOGIC & OUTPUT FOR ENCRYPTION
        try:
            enc = (self.textMsg.get())
            enc.upper()
            code = ""
            for ch in enc:
                ordVal = ord(ch) 
                if ordVal >= 65 and ordVal <= 90:
                    code += chr(ord('Z') - ord(ch) + ord('A'))
                elif ordVal >= 97 and ordVal <= 122:
                    code += chr(ord('z') - ord(ch) + ord('a'))
            messagebox.showinfo("Encrypted text:", f"Encrypted Text: {code}")
        except ValueError:
            messagebox.showerror("Error!", "Invalid Input!")
 
    def decode(self): # LOGIC & OUTPUT FOR DECRYPTION
        try:
            dec = (self.textMsg.get())
            dec.upper()
            text = ""
            for ch in dec:
                ordVal = ord(ch) 
                if ordVal >= 65 and ordVal <= 90: 
                    text += chr(ord('A') - ord(ch) + ord('Z'))
                elif ordVal >= 97 and ordVal <= 122:
                    text += chr(ord('a') - ord(ch) + ord('z'))
            messagebox.showinfo("Decryption", f"Decrypted Text: {text}")
        except ValueError:
            messagebox.showerror("Error", "Invalid Input!")

    # def Exit():
    #     main.destroy()

def main():
    CRYPTO().mainloop()

main() # CALLING THE MAIN TO MAKE THE PROGRAM WORK

