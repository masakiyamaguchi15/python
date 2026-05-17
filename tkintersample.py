import tkinter

root = tkinter.Tk()
root.title('My app')
root.geometry('320x240+20+20')
label = tkinter.Label(text='Hello,world!') 
label.pack()
button = tkinter.Button(text='Push') 
button.pack()
root.mainloop()