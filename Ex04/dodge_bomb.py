from math import radians
import pygame as pg
import sys
from random import randint


def check_bound(obj_rct,scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def check_bound2(obj_rct,scr_rct):
    yoko2, tate2 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko2 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate2 = -1
    return yoko2, tate2


def main():
    count1=0
    count2=0
    vx=1
    vy=1
    pg.display.set_caption("Run away!! Bleach Character")
    scrn_sfc=pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    haikei_sfc=pg.image.load("fig/pg_bg.jpg")#背景
    haikei_rct=haikei_sfc.get_rect()

    tori_sfc=pg.image.load("fig/hirako.png")#ひらこしんじをつくる
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,0.12)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400

    tori_sfc2=pg.image.load("fig/stark.png")#スタークを作る
    tori_sfc2=pg.transform.rotozoom(tori_sfc2,0,0.12)
    tori_rct2=tori_sfc2.get_rect()
    tori_rct2.center=600,400

    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)#爆弾
    
    clock=pg.time.Clock()
    

    while True:
        scrn_sfc.blit(haikei_sfc,haikei_rct)#スクリーンに画像を貼り付ける
        scrn_sfc.blit(tori_sfc,tori_rct)
        scrn_sfc.blit(tori_sfc2,tori_rct2)
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)#金髪の操作

        if key_states[pg.K_w]:    tori_rct2.centery -= 1
        if key_states[pg.K_s]:  tori_rct2.centery += 1
        if key_states[pg.K_a]:  tori_rct2.centerx -= 1
        if key_states[pg.K_d]: tori_rct2.centerx += 1
        yoko2, tate2 = check_bound2(tori_rct2, scrn_rct)#茶髪の操作

        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1

        if yoko2 == -1:
            if key_states[pg.K_a]: 
                tori_rct2.centerx += 1
            if key_states[pg.K_d]:
                tori_rct2.centerx -= 1
        if tate2 == -1:
            if key_states[pg.K_w]: 
                tori_rct2.centery += 1
            if key_states[pg.K_s]:
                tori_rct2.centery -= 1

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) 

        
        if tori_rct.colliderect(bomb_rct):# こうかとんrct(hirako)が爆弾rctと重なったら
            if count1==0:
                a=tori_rct.centery
                b=tori_rct.centerx
                tori_sfc=pg.image.load("fig/hirako2.png")#ひらこしんじをつくる
                tori_sfc=pg.transform.rotozoom(tori_sfc,0,0.12)
                tori_rct=tori_sfc.get_rect()
                tori_rct.center=900,400
                scrn_sfc.blit(tori_sfc,tori_rct)
                count1+=1
            else:
                return


        if tori_rct2.colliderect(bomb_rct): # こうかとんrct2(stark)が爆弾rctと重なったら
            if count2==0:
                tori_sfc2=pg.image.load("fig/stark2.png")#stark make
                tori_sfc2=pg.transform.rotozoom(tori_sfc2,0,0.12)
                tori_rct2=tori_sfc2.get_rect()
                tori_rct2.center=600,400
                count2+=1
            else:
                return
        
        
        clock.tick(1000)


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()