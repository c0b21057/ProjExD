import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random 

#キーを押したときの関数
def key_down(event):
    global key
    key=event.keysym

#キーが離されたときの関数
def key_up(event):
    global key
    key=""

#こうかとんいどう関数
def main_proc():
    global tori_id ,tori
    global mx ,my
    global cx,cy
    if mazelst[my-1][mx]==0:
        if key=="Up":
            my-=1
    if mazelst[my+1][mx]==0:
        if key=="Down":
            my+=1
    if mazelst[my][mx-1]==0:
        if key=="Left":
            mx-=1
    if mazelst[my][mx+1]==0:
        if key=="Right":
            mx+=1
    cx,cy=50+mx*100,50+my*100
    

    if cx==1350 and cy==750:
        canv.delete(tori_id)
        tori=tk.PhotoImage(file=f"fig/3.png")
        cx,cy=300,400
        mx,my=1,1
        tori_id=canv.create_image(cx,cy,image=tori,tag="tori")
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__ =="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")

    canv =tk.Canvas(root,width=1500,height=900,bg="black")
    canv.pack()

    #床を作成
    mazelst=mm.make_maze(15,9)
    mm.show_maze(canv,mazelst)

    #こうかとんを出現させる
    tori=tk.PhotoImage(file="fig/5.png")
    cx,cy=300,400
    mx,my=1,1
    tori_id=canv.create_image(cx,cy,image=tori,tag="tori")

    #キーが押されたときの設定
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #こうかとん移動関数よびだし
    main_proc()

    root.mainloop()