from tkinter import *
root = Tk()
theLabel = Label(root, text="Hello world", width=80, height=40)
theLabel = Listbox(root)
theLabel.insert(1, 'Python')
theLabel.insert(2, 'Java')
theLabel.insert(3, 'C++')
theLabel.pack()
root.mainloop()