import tkinter as tk
import tkinter.messagebox as tkm

if __name__ =="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")

    canv =tk.Canvas(root,width=1500,height=900,bg="black")
    canv.pack()

    tori=tk.PhotoImage(file="fig/5.png")
    cx,cy=390,400
    canv.create_image(cx,cy,image=tori,tag="")

    root.mainloop()