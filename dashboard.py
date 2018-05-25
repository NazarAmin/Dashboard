import tkinter as tk
from tkinter import ttk

class ToggledFrame(tk.Frame):

    def __init__(self, parent, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

        self.show = tk.IntVar()
        self.show.set(0)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text).pack(side="left", fill="x", expand=1)

        self.toggle_button = ttk.Checkbutton(self.title_frame, width=2, text='+', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='+')


def create_dashboard():
    root = tk.Tk()
    root.title("The Title Goes Here")
    #root.minsize(width=400, height=300)
    #root.maxsize(width=1200, height=900)

    root_label = tk.Label(root, text="The Label At The Top")
    root_label.pack()

    t = ToggledFrame(root, text='Load Project', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")
    # load .csv code

    t1 = ToggledFrame(root, text='Pie Charts', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(t1.sub_frame, text='Pie Chart 1').pack(side="left")
    ttk.Label(t1.sub_frame, text='Pie Chart 2').pack(side="right")

    t2 = ToggledFrame(root, text='Data 1', relief="raised", borderwidth=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(t2.sub_frame, text='Input field 1').grid(row=0,column=0)
    ttk.Entry(t2.sub_frame).grid(row=0,column=1)
    ttk.Label(t2.sub_frame, text='Input field 2').grid(row=0,column=2)
    ttk.Entry(t2.sub_frame).grid(row=0,column=3)
    ttk.Label(t2.sub_frame, text='Input field 3').grid(row=0,column=4)
    ttk.Entry(t2.sub_frame).grid(row=0,column=5)
    ttk.Label(t2.sub_frame, text='Input field 4').grid(row=1,column=0)
    ttk.Entry(t2.sub_frame).grid(row=1,column=1)
    ttk.Label(t2.sub_frame, text='Input field 5').grid(row=1,column=2)
    ttk.Entry(t2.sub_frame).grid(row=1,column=3)
    ttk.Label(t2.sub_frame, text='Input field 6').grid(row=1,column=4)
    ttk.Entry(t2.sub_frame).grid(row=1,column=5)

    t3 = ToggledFrame(root, text='Data 2', relief="raised", borderwidth=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")
    for i in range(3):
        ttk.Label(t3.sub_frame, text='Bar' + str(i)).pack()

    root.mainloop()


if __name__ == "__main__":
    create_dashboard()
