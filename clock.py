# Import GUI moduel
from tkinter import *
from tkinter.ttk import *

# Import strftime function for system's time
from time import strftime

# Create tkinter window
root = Tk()
root.title('Clock')

# Display time onto label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# Style label widget 
lbl = Label(root, font = ('system', 40, 'bold'),
            background = 'green',
            foreground = 'black')

# Center clock in tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()