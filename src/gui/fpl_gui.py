import tkinter as tk

def gui():
    m = tk.Tk()
    m.title('Fantasy Premier League Tools')
    m.geometry("1000x500")

    button_start = tk.Button(m, text='start', width=25, bg='blue', command=gui_dispaly_fixtures)
    button_start.pack()
    button_end = tk.Button(m, text='Stop', bg='red', width=25, command=m.destroy)
    button_end.pack()
    m.mainloop()

def gui_dispaly_fixtures():
    m = tk.Tk()
    m.title('Fixtures')
    m.geometry('1000x500')


if __name__ == '__main__':
    gui()
