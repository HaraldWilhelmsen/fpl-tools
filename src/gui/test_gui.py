import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Verdana', 12)

class FplGuiApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'FPL')

        container = tk.Frame(self, height=500, width=1000)
        
        container.pack(side='top', fill='both', expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo, PageThree):
            
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text='Start page', font=LARGE_FONT)  
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Visit Page One', command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text='Visit Page Two', command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text='Visit Graph Page', command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text='Page2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text='Page1', command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage))
        button1.pack()



if __name__ == '__main__':
    app = FplGuiApp()
    app.mainloop()

