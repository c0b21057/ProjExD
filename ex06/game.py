import pygame as pg
import sys
from random import randint
import time
import sys

speed=randint(0,1)


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:#こうかとんを表示
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class enemy:#敵の鳥を表示
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) 
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        self.blit(scr) 


class fight:#合図表示
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) 
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        self.blit(scr) 


class Text:
    def __init__(self,xy,ntime):
        self.xy=xy
        self.font=pg.font.Font(None,40)
        self.text=self.font.render(str(ntime),True,(255,255,255),(0,255,0))

    def blit(self,scr:Screen):
        scr.sfc.blit(self.text,self.xy)


def main():

    # 背景
    scr = Screen("穿て！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # こうかとん
    kkt = Bird("fig/6.png", 2.0, (600, 700))

    #敵の鳥
    ebd=enemy("fig/enemy_bird.png",0.3,(900,400))

    #合図
    st=fight("fig/fight.jpg",1.0,(600,400))

    clock = pg.time.Clock()
    diley_frame = randint(2500,5000)
    flag=0


    while True:
        #pg.init()
        scr.blit()
        #print(pg.time.get_ticks())
        
        if pg.time.get_ticks() >= diley_frame and pg.time.get_ticks()<=7000:
            st.update(scr)
            flag=1
            #pg.quit()

        if pg.time.get_ticks()>= 10000:#30秒後強制終了
            return
        
        if key_states[pg.K_SPACE]:
            if flag==1: 
                key_states = pg.key.get_pressed()
                
            else:
                    font=pg.font.Font(None,40)
                    text=font.render(str(pg.time.get_ticks()),True,(255,255,255),(0,255,0))
                    scr.blit(text, (700,700))
        
        if key_states:
            ntime=(pg.time.get_ticks()-diley_frame)*0.001 
            text=Text((700,700),ntime)
            text.blit(scr)

        kkt.update(scr)#こうかとんを表示
        ebd.update(scr)#敵を表示


        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() 
    main()    
    pg.quit() 
    sys.exit()