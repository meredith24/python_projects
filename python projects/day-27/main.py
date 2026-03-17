from tkinter import *

window = Tk()
window.title("My First App")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I am a Label", font=("Arial", 15))
my_label.grid(column=5, row=5)

#Button

def button_clicked():
    print("Button clicked")
    text_input = input.get()
    my_label.config(text=text_input)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# button = Button(text="Click me", command=button_clicked)
# button.pack()

#Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop() #pencereyi açık tutan loop

