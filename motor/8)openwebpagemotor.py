import tkinter
import urllib.request

def left(event):
    print("left")

def right(event):
    print("right")

main = tkinter.tk()


frame = Frame(main, width=100, height=100)
main.bind('<Left>',left)
main.bind('<Right>',right)
frame.pack()
main.mainloop()
