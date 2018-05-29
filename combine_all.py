import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv


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


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo


def load_data(filename):
    data = []
    with open(filename) as f:
        raw_data = csv.reader(f)
        for row in raw_data:
            data.append([int(x) for x in row])
    return data


def bake_pie(data_row):

    cols = len(data_row)

    # Assign data_row values
    sizes_1 = data_row[0:cols-1]
    labels_1 = ['Category 1\n'+str("{0:.2f}".format(100*sizes_1[0]/sum(sizes_1)))+'%',
                'Category 2\n'+str("{0:.2f}".format(100*sizes_1[1]/sum(sizes_1)))+'%',
                'Category 3\n'+str("{0:.2f}".format(100*sizes_1[2]/sum(sizes_1)))+'%',
                'Category 4\n'+str("{0:.2f}".format(100*sizes_1[3]/sum(sizes_1)))+'%']
    sizes_2 = data_row[0:cols-2]
    sizes_2.append(data_row[cols-2]-data_row[cols-1])
    sizes_2.append(data_row[cols-1])
    which_subsection = cols-2 # -1 for 0 index, -1 for last col subset
    labels_2 = ['','','',
                'Category 4a\n'+str("{0:.2f}".format(100*sizes_2[which_subsection]/sum(sizes_1)))+'%',
                '']
    colors_1 = ['#ff0000', '#00ff00', '#0000ff', '#ffff00']
    colors_2 = ['#ffff00']

    # Plot
    m = plt.pie(sizes_1, labels=labels_1, colors=colors_1, startangle=90, radius=1)
    n = plt.pie(sizes_2, labels=labels_2, colors=colors_2, startangle=90, radius=1)

    # Set font size
    for i in range(len(m[1])):
        m[1][i].set_fontsize(8)
    for i in range(len(m[1])):
        n[1][i].set_fontsize(8)

    # Transparency
    for i in range(len(n[0])):
        n[0][i].set_alpha(0.0)
    n[0][which_subsection].set_hatch('/')
    n[0][which_subsection].set_alpha(1.0)

    # Outline/Border
    for i in range(len(m[0])):
        m[0][i].set_edgecolor('k')
    n[0][which_subsection].set_edgecolor('k')

    # Draw circle
    centre_circle = plt.Circle((0, 0), 0.1, color='black', fc='white', linewidth=1)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    return fig


def create_dashboard():

    # Create a canvas
    min_w, min_h = 1000, 130
    root = tk.Tk()
    root.title("The Title Goes Here")
    root.minsize(width=min_w, height=min_h)
    root.maxsize(width=min_w, height=1050)

    # load project collapsible
    t = ToggledFrame(root, text='Load Project', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")
    #dropdown to get correct file
    filename = 'data.csv'
    data = load_data(filename)

    t1 = ToggledFrame(root, text='Pie Charts', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    # create pie charts
    # NOTE: change figsize if pie charts are warped
    plt.subplots(1, 2, figsize=(2.1, 4))
    plt.subplot(121)
    bake_pie(data[0]) # 0 is the row
    plt.title("Pie 1")
    plt.subplot(122)
    fig = bake_pie(data[1]) # 1 is the row
    plt.title("Pie 2")
    plt.tight_layout()

    # embed figure (of 2 pie charts)
    canvas1 = FigureCanvasTkAgg(fig, master=t1.sub_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # data 1 collapsible
    t2 = ToggledFrame(root, text='Data 1', relief="raised", borderwidth=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    # data 1 fields
    ttk.Label(t2.sub_frame, text='Input field 1').grid(row=0,column=1)
    ttk.Entry(t2.sub_frame).grid(row=0,column=2)
    ttk.Label(t2.sub_frame, text='Input field 2').grid(row=0,column=3)
    ttk.Entry(t2.sub_frame).grid(row=0,column=4)
    ttk.Label(t2.sub_frame, text='Input field 3').grid(row=0,column=5)
    ttk.Entry(t2.sub_frame).grid(row=0,column=6)

    ttk.Label(t2.sub_frame, text='Input field 4').grid(row=1,column=1)
    ttk.Entry(t2.sub_frame).grid(row=1,column=2)
    ttk.Label(t2.sub_frame, text='Input field 5').grid(row=1,column=3)
    ttk.Entry(t2.sub_frame).grid(row=1,column=4)
    ttk.Label(t2.sub_frame, text='Input field 6').grid(row=1,column=5)
    ttk.Entry(t2.sub_frame).grid(row=1,column=6)

    # add empty columns before and after to center
    t2.sub_frame.grid_columnconfigure(0, weight=1)
    t2.sub_frame.grid_columnconfigure(7, weight=1)

    # data 2 collapsible
    t3 = ToggledFrame(root, text='Data 2', relief="raised", borderwidth=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    # data 2 fields
    for i in range(3):
        ttk.Label(t3.sub_frame, text='Bar' + str(i)).pack()

    root.mainloop()


if __name__ == "__main__":
    create_dashboard()
