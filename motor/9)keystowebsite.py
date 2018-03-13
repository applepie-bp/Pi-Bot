from tkinter import *
import urllib.request

ip="http://192.168.1.4:5000"
print("use: 'arrow keys' (to move), 's' (start), 'e' (end), 'q' (quit)")

def leftKey(event):
    print("Left key pressed")
    urllib.request.urlopen(ip+"/leftturn")

def rightKey(event):
    print("Right key pressed")
    urllib.request.urlopen(ip+"/rightturn")

def up(event):
    print("Up pressed")
    urllib.request.urlopen(ip+"/forward")

def down(event):
    print("down pressed")
    urllib.request.urlopen(ip+"/backward")

def esc(event):
    print("end")
    urllib.request.urlopen(ip+"/stop")

def start(event):
    print("start")
    urllib.request.urlopen(ip+"/start")

def close(event):
    print("closing")
    urllib.request.urlopen(ip+"/close")


main = Tk()

frame = Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', up)
main.bind('<Down>', down)
main.bind('s', start)
main.bind('e',esc)
main.bind('q',close)
frame.pack()
main.mainloop()
