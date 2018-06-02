import tkinter as tk
from tkinter import filedialog
import datetime
import os
import os.path

root = tk.Tk()
root.title("Dropdown Title Here")

# Add a grid
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=('n', 'w', 'e', 's'))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

###################################################################################
# DROPDOWN GRID
###################################################################################
# Create a Tkinter variable
tkvar11 = tk.StringVar(root)
name11 = "Title11"
choices11 = {'Option1', 'Option2', 'Option3', 'Option4', 'Option5'}
popupMenu = tk.OptionMenu(mainframe, tkvar11, *choices11)
tk.Label(mainframe, text=name11, padx=10).grid(row=1, column=1)
popupMenu.grid(row=2, column=1)

# Create a Tkinter variable
tkvar12 = tk.StringVar(root)
name12 = "Title12"
choices12 = {'Option1', 'Option2', 'Option3', 'Option4', 'Option5'}
popupMenu = tk.OptionMenu(mainframe, tkvar12, *choices12)
tk.Label(mainframe, text=name12, padx=10).grid(row=1, column=2)
popupMenu.grid(row=2, column=2)

# Create a Tkinter variable
tkvar13 = tk.StringVar(root)
name13 = "Title13"
choices13 = {'Option1', 'Option2', 'Option3', 'Option4', 'Option5'}
popupMenu = tk.OptionMenu(mainframe, tkvar13, *choices13)
tk.Label(mainframe, text=name13, padx=10).grid(row=1, column=3)
popupMenu.grid(row=2, column=3)

# Add empty row
tk.Label(mainframe, text=" ").grid(row=3, column=2)

# Create a Tkinter variable
tkvar21 = tk.StringVar(root)
name21 = "Title21"
choices21 = {'Option1', 'Option2', 'Option3', 'Option4', 'Option5'}
popupMenu = tk.OptionMenu(mainframe, tkvar21, *choices21)
tk.Label(mainframe, text=name21, padx=10).grid(row=4, column=1)
popupMenu.grid(row=5, column=1)

# Create a Tkinter variable
tkvar22 = tk.StringVar(root)
name22 = "Title22"
choices22 = {'Option1', 'Option2', 'Option3', 'Option4', 'Option5'}
popupMenu = tk.OptionMenu(mainframe, tkvar22, *choices22)
tk.Label(mainframe, text=name22, padx=10).grid(row=4, column=2)
popupMenu.grid(row=5, column=2)

# Create a Tkinter variable
tkvar23 = tk.StringVar(root)
name23 = "Title23"
choices23 = {'Option1', 'Option2', 'Option3', 'Option4', 'Option5'}
popupMenu = tk.OptionMenu(mainframe, tkvar23, *choices23)
tk.Label(mainframe, text=name23, padx=10).grid(row=4, column=3)
popupMenu.grid(row=5, column=3)

#def change_dropdown(*args):
#    print(tkvar1.get())
#tkvar1.trace('w', change_dropdown)
tk.Label(mainframe, text=" ").grid(row=6, column=2)

###################################################################################
# BROWSE
###################################################################################
folder_path = tk.StringVar()
#folder_path.set(os.getcwd()) # default path
def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    #print(filename)
button1 = tk.Button(mainframe, text="Browse", command=lambda: browse_button()).grid(row=7, column=1)
label1 = tk.Label(master=mainframe,textvariable=folder_path).grid(row=7, column=2)

###################################################################################
# GENERATE
###################################################################################
def generate(*args):
    if folder_path.get():
        d = str(datetime.datetime.now().strftime("%Y_%m_%d"))
        s = 'ROD_Report_'+d+'.txt'
        #print(s)
        a = folder_path.get()
        #print(a)
        name = os.path.join(a, s)
        #print(name)
        f = open(name, "w")
        f.write(name11 + ': ' + tkvar11.get() + '\n')
        f.write(name12 + ': ' + tkvar12.get() + '\n')
        f.write(name13 + ': ' + tkvar13.get() + '\n')
        f.write(name21 + ': ' + tkvar21.get() + '\n')
        f.write(name22 + ': ' + tkvar22.get() + '\n')
        f.write(name23 + ': ' + tkvar23.get() + '\n')
        f.close()
    #else:
    #   print('asdf')
tk.Button(mainframe, text="Generate Report", command=generate).grid(row=7, column=3)
tk.Entry()

root.mainloop()