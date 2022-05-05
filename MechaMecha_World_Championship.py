#Ce jeu vidéo est réalisé dans le cadre d'un projet scolaire par Aloszko Martin, Aubry Joshua, et Vallée Mathieu#FR
#This video game was released as a part of school project by Aloszko Martin, Aubry Joshua, and Vallée Mathieu#EN
#------------------------PLUGIN------------------------#

import pygame, os, ctypes,sys          #importation des plugins
os.environ['SDL_VIDEO_CENTERED'] = '1'          #faire apparaître le cadre au centre de l'écran
pygame.init()           #initialisation de pygame
myappid = 'MechaMecha'          #texte sans valeur
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)          #affiche l'icone dans la barre des tâches

#------------------------FONCTION------------------------#
def button_menu_fighters(button):
    if button==-0.1:
        button=0.1
    elif button==0.2:
        button=0.0
    elif button==-1.0:
        button=2.0
    elif button==-0.9:
        button=2.1
    elif button==0.9:
        button=1.1
    elif button==1.2:
        button=1.0
    elif button==1.9:
        button=2.1
    elif button==2.2:
        button=2.0
    elif button==3.0:
        button=0.0
    elif button==3.1:
        button=0.1
        
    if button==0.0:
        P_select=1
    elif button==0.1:
        P_select=2
    elif button==1.0:
        P_select=3
    elif button==1.1:
        P_select=4
    elif button==2.0:
        P_select=5
    elif button==2.1:
        P_select=6
    return[button,P_select]
        
def button_sound(key,button_old,button,button_exit,button_exit_alt,key2isok,sound):         #fonction quui gèrent les sons du menu
    select_sound=pygame.mixer.Sound("./audio/sound/button/Selection.ogg")
    validate_sound=pygame.mixer.Sound("./audio/sound/button/Valider.ogg")
    cancel_sound=pygame.mixer.Sound("./audio/sound/button/Annuler.ogg")
    if button_old != button:            #si on a bougé le curseur faire le bruit correspondant
        pygame.mixer.stop()
        select_sound.set_volume(round(sound/100,2))
        select_sound.play()
    if key==1 and not button_exit==button and not button_exit_alt==button:          #si on a fait la touche pour valider faire le son correspondant
        pygame.mixer.stop()
        validate_sound.set_volume(round(sound/100,2))
        validate_sound.play()
    elif key==2 and key2isok or key==1 and button_exit==button or key==1 and button_exit_alt==button:            #si on a fait la touche pour annuler faire le son correspondant
        pygame.mixer.stop()
        cancel_sound.set_volume(round(sound/100,2))
        cancel_sound.play()

def change_button(buttonid,background,rect):           #fonction pour faire apparraître le menu de sauvegarde des options et un curseur
    button_list=[]
    for i in range(3):
        button_adjust=image_adjust("graphic/button/cursor/Changement_curseur",763+133*i,560)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
        screen.blit(background_piece,(button_rect[0],button_rect[1]))
        button_list += [button_rect]
        if i==int(buttonid*10):
            screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))   
    if not rect:
        button_list=[]
    return button_list           #renvoyer les rectangles des boutons si demandé

def choice_button(buttonid,background,rect,choice):         #fonction qui gèrent les menus déroulants du menu option
    button_list=[]
    if choice==3:
        x=1252
        y=447
    elif choice==15:
        x=1567
        y=101
    for i in range(choice):
        button_adjust=image_adjust("graphic/button/cursor/Popup_curseur",x,y+28*i)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
        screen.blit(background_piece,(button_rect[0],button_rect[1]))
        button_list += [button_rect]
        if i==buttonid:
            screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2])) 
    if not rect:
        button_list=[]
    return button_list           #renvoyer les rectangles des boutons si demandé

def event_fight(event,UP,DOWN,RIGHT,LEFT,ATK,SPE,SHLD,MENU,old_axis,old_action,P_air):          #fonction qui gère la détection des touches dans les menus
    P_UP=False
    P_DOWN=False
    P_LEFT=False
    P_RIGHT=False
    P_ATK=False
    P_SPE=False
    P_SHLD=False
    P_MENU=False
    key_list=[UP,DOWN,RIGHT,LEFT,ATK,SPE,SHLD,MENU]
    action=""
    action2=""
    if event.type==pygame.QUIT:           #si on clique sur la croix, fermer le jeu
        sys.exit(37)
    elif event.type==pygame.MOUSEBUTTONUP:            #faire une action selon le bouton de la souris qui est relâché
        if event.button==3:
            action=7
    elif event.type==pygame.JOYBUTTONDOWN:
        for i in range(8):
            if key_list[i].split("_")[0]=="joystick":
                if int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="button" and int(key_list[i].split("_")[3])==int(event.button):
                    action=i
                    if action<=6:
                        old_action[i]=True
                    break
    elif event.type==pygame.JOYHATMOTION:
        for i in range(8):
            if key_list[i].split("_")[0]=="joystick":
                if int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="hat":
                    hat_option_value=key_list[i].split("_")[3].split("(")[1].split(")")[0]
                    hat_value=str(event.value).split("(")[1].split(")")[0]
                    if abs(int(hat_option_value.split(", ")[0]))==1 and int(hat_value.split(", ")[0])==int(hat_option_value.split(", ")[0]):
                        if action=="":
                            action=i
                            if action<=6:
                                old_action[i]=True
                        else:
                            action2=i
                            if action<=6:
                                old_action[i]=True
                            break
                    elif abs(int(hat_option_value.split(", ")[1]))==1 and int(hat_value.split(", ")[1])==int(hat_option_value.split(", ")[1]):
                        if action=="":
                            action=i
                            if action<=6:
                                old_action[i]=True
                        else:
                            action2=i
                            if action<=6:
                                old_action[i]=True
                            break
    elif event.type==pygame.JOYAXISMOTION:
        for i in range(8):
            if key_list[i].split("_")[0]=="joystick":
                if abs(event.value)>=0.9:
                    if int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="+axis" and int(key_list[i].split("_")[3])==int(event.axis) and float(event.value)>0:
                        if not old_axis==i:
                            action=i
                            if action<=6:
                                old_action[i]=True
                        old_axis=i
                        break
                    elif int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="-axis" and int(key_list[i].split("_")[3])==int(event.axis) and float(event.value)<0:
                        if not old_axis==i:
                            action=i
                            if action<=6:
                                old_action[i]=True
                        old_axis=i
                        break
                elif abs(event.value)<=0.1:
                    old_axis=""
                    break
    elif event.type==pygame.KEYDOWN:            #faire une action selon le bouton du clavier qui est enfoncé
        key_name=pygame.key.name(event.key)
        key_name=key_name.upper()
        for i in range(8):
            if key_list[i]==key_name:
                action=i
                if action<=6:
                    old_action[i]=True
                break
    if action==0 or action2==0:
        P_UP=True
    if action==1 or action2==1:
        P_DOWN=True
    if action==2 or action2==2:
        P_RIGHT=True
    if action==3 or action2==3:
        P_LEFT=True
    if action==4 or action2==4:
        P_ATK=True
    if action==5 or action2==5:
        P_SPE=True
    if action==6 or action2==6:
        P_SHLD=True
    if action==7 or action2==7:
        P_MENU=True
        old_action=[False,False,False,False,False,False,False]
    for i in range(7):
        action=""
        if old_action[i]:
            stop=False
            if key_list[i].split("_")[0]=="joystick":
                if event.type==pygame.JOYBUTTONUP and key_list[i].split("_")[2]=="button":
                    if int(key_list[i].split("_")[1])==int(event.joy) and int(key_list[i].split("_")[3])==int(event.button):
                        stop=True
                elif event.type==pygame.JOYHATMOTION and key_list[i].split("_")[2]=="hat":
                    if int(key_list[i].split("_")[1])==int(event.joy):
                        hat_option_value=key_list[i].split("_")[3].split("(")[1].split(")")[0]
                        hat_value=str(event.value).split("(")[1].split(")")[0]
                        if abs(int(hat_option_value.split(", ")[0]))==1 and not int(hat_value.split(", ")[0])==int(hat_option_value.split(", ")[0]):
                            stop=True
                        elif abs(int(hat_option_value.split(", ")[1]))==1 and not int(hat_value.split(", ")[1])==int(hat_option_value.split(", ")[1]):
                            stop=True
                elif event.type==pygame.JOYAXISMOTION:
                    if key_list[i].split("_")[2]=="+axis" or key_list[i].split("_")[2]=="-axis":
                        if int(key_list[i].split("_")[1])==int(event.joy) and int(key_list[i].split("_")[3])==int(event.axis) and abs(event.value)<=0.1:  
                            stop=True
            elif not key_list[i].split("_")[0]=="joystick":
                if event.type==pygame.KEYUP:
                    key_name=pygame.key.name(event.key)
                    key_name=key_name.upper()
                    if key_list[i]==key_name:
                        stop=True
            if not stop:
                action=i
            else:
                old_action[i]=False
        if action==0:
            P_UP=True
        elif action==1:
            P_DOWN=True
        elif action==2:
            P_RIGHT=True
        elif action==3:
            P_LEFT=True
        elif action==4:
            P_ATK=True
        elif action==5:
            P_SPE=True
        elif action==6:
            P_SHLD=True
    if P_MENU:
        P_UP=False
        P_DOWN=False
        P_RIGHT=False
        P_LEFT=False
        P_ATK=False
        P_SPE=False
        P_SHLD=False
    if P_air:
        P_SHLD=False
        P_SPE=False
    if not P_air:
        P_DOWN=False
        if P_SHLD:
            P_UP=False
            P_ATK=False
            P_SPE=False
    if P_RIGHT and P_LEFT:
        P_RIGHT=False
        P_LEFT=False
    if P_ATK:
        P_SPE=False
    return [P_UP,P_DOWN,P_RIGHT,P_LEFT,P_ATK,P_SPE,P_SHLD,P_MENU,old_axis,old_action,number,new_time]         #renvoyer l'action à executer et le bouton sur lequel mettre un curseur

def event_key(event,fighters,button,UP,DOWN,RIGHT,LEFT,ATK,SPE,SHLD,MENU,old_axis,old_action,number,new_time,vertical,collide):          #fonction qui gère la détection des touches dans les menus
    timer=0
    if old_action<=3:
        if number==-1:
            new_time=pygame.time.get_ticks()
        elif number==1:
            new_time=pygame.time.get_ticks()
        else:
            timer=pygame.time.get_ticks()-new_time
    key_list=[UP,DOWN,RIGHT,LEFT,ATK,SPE,SHLD,MENU]
    key=0
    action=""
    key3=False
    if event.type==pygame.QUIT:           #si on clique sur la croix, fermer le jeu
        sys.exit(37)
    elif event.type==pygame.MOUSEBUTTONUP:            #faire une action selon le bouton de la souris qui est relâché
        if event.button==1 and collide:
            action=4
        elif event.button==3:
            action=5
            key3=True
        elif event.button==4 and vertical:
            action=0
        elif event.button==5 and vertical:
            action=1
    elif event.type==pygame.JOYBUTTONDOWN:
        for i in range(8):
            if key_list[i].split("_")[0]=="joystick":
                if int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="button" and int(key_list[i].split("_")[3])==int(event.button):
                    action=i
                    old_action=action
                    break
    elif event.type==pygame.JOYHATMOTION:
        for i in range(8):
            if key_list[i].split("_")[0]=="joystick":
                if int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="hat" and str(key_list[i].split("_")[3])==str(event.value):
                    action=i
                    old_action=action
                    break
    elif event.type==pygame.JOYAXISMOTION:
        for i in range(8):
            if key_list[i].split("_")[0]=="joystick":
                if abs(event.value)>=0.9:
                    if int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="+axis" and int(key_list[i].split("_")[3])==int(event.axis) and float(event.value)>0:
                        if not old_axis==i:
                            action=i
                            old_action=action
                        old_axis=i
                        break
                    elif int(key_list[i].split("_")[1])==int(event.joy) and key_list[i].split("_")[2]=="-axis" and int(key_list[i].split("_")[3])==int(event.axis) and float(event.value)<0:
                        if not old_axis==i:
                            action=i
                            old_action=action
                        old_axis=i
                        break
                elif abs(event.value)<=0.1:
                    old_axis=""
                    break
    elif event.type==pygame.KEYDOWN:            #faire une action selon le bouton du clavier qui est enfoncé
        key_name=pygame.key.name(event.key)
        key_name=key_name.upper()
        for i in range(8):
            if key_list[i]==key_name:
                action=i
                old_action=action
                break
    if action==0 or action==1 or action==2 or action==3:
        timer=0
        number=-1
    elif action==4 or action==5 or action==6 or action==7:
        old_action=4
        number=-1
    if action==0:
        button=round(button-1,1)
    elif action==1:
        button=round(button+1,1)
    elif action==2:
        button=round(button+0.1,1)
    elif action==3:
        button=round(button-0.1,1)
    elif action==4 or action==6:
        key=1
    elif action==5:
        key=2
    elif action==7:
        key=2
        key3=True
    elif old_action<=3:
        stop=False
        for i in range(4):
            if key_list[i].split("_")[0]=="joystick" and old_action==i:
                if event.type==pygame.JOYBUTTONUP and key_list[i].split("_")[2]=="button":
                    if int(key_list[i].split("_")[1])==int(event.joy) and int(key_list[i].split("_")[3])==int(event.button):
                        stop=True
                elif event.type==pygame.JOYHATMOTION and key_list[i].split("_")[2]=="hat":
                    if int(key_list[i].split("_")[1])==int(event.joy) and str(event.value)=="(0, 0)":
                        stop=True
                elif event.type==pygame.JOYAXISMOTION:
                    if key_list[i].split("_")[2]=="+axis" or key_list[i].split("_")[2]=="-axis":
                        if int(key_list[i].split("_")[1])==int(event.joy) and int(key_list[i].split("_")[3])==int(event.axis) and abs(event.value)<=0.1:  
                            stop=True
            elif not key_list[i].split("_")[0]=="joystick" and old_action==i:
                if event.type==pygame.KEYUP:
                    key_name=pygame.key.name(event.key)
                    key_name=key_name.upper()
                    if key_list[i]==key_name:
                        stop=True
        if not stop:
            if number<=0:
                if timer<400:
                    number=0
                elif timer>=400:
                    action=old_action
                    number=1
            elif number==1:
                number=2
            elif number==2 and timer>=200:
                action=old_action
                number=1
        else:
            old_action=4
        if action==0:
            button=round(button-1,1)
        elif action==1:
            button=round(button+1,1)
        elif action==2:
            button=round(button+0.1,1)
        elif action==3:
            button=round(button-0.1,1)
    if fighters and key3:
        key=3
    return [key,button,old_axis,old_action,number,new_time]         #renvoyer l'action à executer et le bouton sur lequel mettre un curseur

def fade(image,x,y,t1,transparency1,gain1,t2,transparency2,gain2,ATK,SHLD,old_axis):          #fonction avec le fade_in et le fade_out
    fade_out=False
    key=0
    pygame.time.delay(t1)
    for i in range (transparency1):
        event = pygame.event.poll()
        event_key_list=event_key(event,False,0,"none","none","none","none",ATK,"none",SHLD,"none",old_axis,4,-1,0,False,True)
        key=event_key_list[0]
        old_axis=event_key_list[2]
        if key==1:
            pygame.event.clear()
            fade_out=True
            break
        screen.fill(pygame.Color("black"))
        image.set_alpha(i * gain1)
        screen.blit(image,(x,y))
        pygame.display.update()
        pygame.time.delay(20)
    screen.fill(pygame.Color("black"))
    image.set_alpha(255)
    screen.blit(image,(x,y))
    pygame.display.update()
    if not fade_out:
        key=0
        pygame.time.delay(t2)
        for i in range (transparency2):
            event = pygame.event.poll()
            event_key_list=event_key(event,False,0,"none","none","none","none",ATK,"none",SHLD,"none",old_axis,4,-1,0,False,True)
            key=event_key_list[0]
            old_axis=event_key_list[2]
            if key==1:
                pygame.event.clear()
                break
            screen.fill(pygame.Color("black"))
            image.set_alpha(255 - i * gain2 - 1)
            screen.blit(image,(x,y))
            pygame.display.update()
            pygame.time.delay(20)
    screen.fill(pygame.Color("black"))
    pygame.display.update()
    return old_axis

def fighters_button(P1_select,P2_select,background):
    char=[pygame.transform.flip(pygame.image.load("./fighters/"+str(P1_select)+"/combattant2.png").convert_alpha(),True,False),"fighters/"+str(P2_select)+"/combattant2"]
    xy_list=[[637,45],[981,45],[637,389],[981,389],[637,733],[981,733]]
    for i in range(6):
        char_head=image_adjust("fighters/"+str(i+1)+"/combattant1",xy_list[i][0],xy_list[i][1])
        char_head_rect=char_head[0].get_rect()
        char_head_rect=char_head_rect.move(char_head[1],char_head[2])
        background_piece=background[0].subsurface(char_head_rect[0]-background[1],char_head_rect[1]-background[2],char_head_rect[2],char_head_rect[3])
        screen.blit(background_piece,(char_head_rect[0],char_head_rect[1]))
        screen.blit(char_head[0],(char_head[1],char_head[2]))
        if (P1_select-1)==i and P1_select==P2_select:
            cursor=image_adjust("graphic/button/cursor/combattantJ1J2_curseur",xy_list[i][0],xy_list[i][1])
            screen.blit(cursor[0],(cursor[1],cursor[2]))
        elif (P1_select-1)==i and not P1_select==P2_select:
            cursor=image_adjust("graphic/button/cursor/combattantJ1_curseur",xy_list[i][0],xy_list[i][1])
            screen.blit(cursor[0],(cursor[1],cursor[2]))
        elif (P2_select-1)==i and not P1_select==P2_select:
            cursor=image_adjust("graphic/button/cursor/combattantJ2_curseur",xy_list[i][0],xy_list[i][1])
            screen.blit(cursor[0],(cursor[1],cursor[2]))
    for i in range(2):
        char_adjust=image_adjust(char[i],11+1436*i,0)
        char_rect=char_adjust[0].get_rect()
        char_rect=char_rect.move(char_adjust[1],char_adjust[2])
        background_piece=background[0].subsurface(char_rect[0]-background[1],char_rect[1]-background[2],char_rect[2],char_rect[3])
        screen.blit(background_piece,(char_rect[0],char_rect[1]))
        screen.blit(char_adjust[0],(char_adjust[1],char_adjust[2]))

def fighters_setting(P_select):
    P_adjust=[]
    for i in range(12):
        P_adjust.append(image_adjust("fighters/"+str(P_select)+"/animation/"+str(i),0,0))
    P_hit_adjust=[]
    for i in range(3):
        P_hit_adjust.append(image_adjust("fighters/"+str(P_select)+"/animation/coup"+str(i),0,0))
    P_missile_adjust=image_adjust("fighters/"+str(P_select)+"/animation/missile",0,0)
    P_setting=open("./fighters/"+str(P_select)+"/characteristics.txt").read()
    P_Vspeed=round(float(P_setting.split("|")[1]),1)
    P_Hspeed=round(float(P_setting.split("|")[3]),1)
    P_fall=round(float(P_setting.split("|")[5]),1)
    P_HP=round(float(P_setting.split("|")[7]),1)
    P_SP=round(float(P_setting.split("|")[9]),1)
    P_ATKpunch=round(float(P_setting.split("|")[11]),1)
    P_cdpunch=round(float(P_setting.split("|")[13]),1)
    P_ATKshot=round(float(P_setting.split("|")[15]),1)
    P_cdshot=round(float(P_setting.split("|")[17]),1)
    P_def=round(float(P_setting.split("|")[19]),1)
    P_sentence1=str(P_setting.split("|")[21])
    P_sentence2=str(P_setting.split("|")[23])
    return[P_adjust,P_hit_adjust,P_missile_adjust,P_Vspeed,P_Hspeed,P_fall,P_HP,P_SP,P_ATKpunch,P_cdpunch,P_ATKshot,P_cdshot,P_def,P_sentence1,P_sentence2]

def fight_menu_button(buttonid,rect):         #fonction pour faire apparraître le menu avec un curseur
    button=["Continuer","Continuer_timer","Option","Quitter"]
    button_list=[]
    for i in range(4):
        button_adjust=image_adjust("graphic/button/menu/"+str(button[i]),785,176+226*i)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        button_list += [button_rect]
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
        if i==int(buttonid):
            cursor=image_adjust("graphic/button/cursor/Menu_curseur",785,176+226*i)
            screen.blit(cursor[0],(cursor[1],cursor[2]))  
    if not rect:
        button_list=[]
    return button_list           #renvoyer le rectangle du curseur

def gauge(music,sound,buttonid,background,change,rect):         #fonction qui gère l'apparition des gauges de son et de musique avec leur curseur
    button=["graphic/button/option/Volume_jauge","graphic/button/cursor/Jauge_curseur","graphic/button/cursor/Jauge_curseur2","graphic/button/cursor/Volume_curseur"]
    button_list=[]
    for i in range(2):
        button_adjust=image_adjust(button[0],1500,708+118*i)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
        screen.blit(background_piece,(button_rect[0],button_rect[1]))
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
        button_list += [button_rect]
    if buttonid==2.2:
        a=music
        b=708
    elif buttonid==3.2:
        a=sound
        b=826
    if not change and (buttonid==2.2 or buttonid==3.2):
        button_adjust=image_adjust(button[3],1500,b)
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
    for i in range(2):
        if i==0:
            button_adjust=image_adjust(button[1],1500+music*2.02,708)
        elif i==1:
            button_adjust=image_adjust(button[1],1500+sound*2.02,826)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
        button_list += [button_rect]
    if change and (buttonid==2.2 or buttonid==3.2):
        button_adjust=image_adjust(button[2],1500+a*2.02,b)
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
    if not rect:
        button_list=[]
    return button_list           #renvoyer les rectangles des jauges

def gauge_cursor(music,sound,buttonid,background,gauge_rect,cursor_rect,width,height,screen_mode):
    volume=[round(music/10,1),round(sound/10,1)]
    if buttonid==2.2:
        i=0
    else:
        i=1
    mouse=pygame.mouse.get_pos()[0]
    volume[i]=round(((mouse-gauge_rect[0]-cursor_rect[2]/2.5)/(2.02*background[3]))/10,1)
    if volume[i]<0.0:
        volume[i]=0.0
    elif volume[i]>10.0:
        volume[i]=10.0
    if buttonid==2.2:
        pygame.mixer.music.set_volume(round(volume[0]/10,2))
    gauge(int(volume[0]*10),int(volume[1]*10),buttonid,background,True,False)
    option_button(buttonid,width,height,screen_mode,int(volume[0]*10),int(volume[1]*10),background,False,0)
    pygame.display.update()
    while True:
        pygame.time.wait(1)
        volume_old=volume[i]
        mouse=pygame.mouse.get_pos()[0]
        event = pygame.event.wait()
        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            break
        else:
            volume[i]=round(((mouse-gauge_rect[0]-cursor_rect[2]/2.5)/(2.02*background[3]))/10,1)
            if volume[i]<0.0:
                volume[i]=0.0
            elif volume[i]>10.0:
                volume[i]=10.0
            if buttonid==2.2:
                pygame.mixer.music.set_volume(round(volume[0]/10,2))
        if buttonid==3.2:
            button_sound("nokey",volume_old,volume[i],"none","none",True,int(volume[1]*10))
        option_button(buttonid,width,height,screen_mode,int(volume[0]*10),int(volume[1]*10),background,False,0)
        gauge(int(volume[0]*10),int(volume[1]*10),buttonid,background,True,False)
        pygame.display.update()
    return[int(volume[0]*10),int(volume[1]*10)]

def image_adjust(image,x,y):           #fonction pour ajuster une image par rapport au cadre
    if type(image)==str:
        image=pygame.image.load("./"+str(image)+".png").convert_alpha()
    width=image.get_width()
    height=image.get_height()
    rate=screen_width/1920
    rate_height=screen_height/1080
    if rate<rate_height:          #ajuster l'image de fond au cadre (dont la largeur était trop petite)
        y=int(round(y*rate+(screen_height-1080*rate)/2,0))
        x=int(round(x*rate,0))
    elif rate>rate_height:          #ajuster l'image de fond au cadre (dont la hauteur était trop petite)
        rate=rate_height
        y=int(round(y*rate,0))
        x=int(round(x*rate+(screen_width-1920*rate)/2,0))
    else:          #ajuster l'image de fond au cadre
        y=int(round(y*rate,0))
        x=int(round(x*rate,0))
    image=pygame.transform.scale(image,(int(round(rate*width,0)),int(round(rate*height,0))))
    return [image,x,y,rate]          #renvoyer l'image redimensionnée, ses nouvelles coordonnées et le ratio de redimensionnement

def key_button(buttonid,background,rect):         #fonction pour faire apparraître le menu des commandes avec un curseur
    button_list=[]
    x_list=[420,1090,1544]
    for i in range(3):
        button_adjust=image_adjust("graphic/button/cursor/Option_curseur",x_list[i],150)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
        screen.blit(background_piece,(button_rect[0],button_rect[1]))
        button_list += [button_rect]
        if i==int(round(buttonid-int(buttonid),1)*10):
            screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
    if not rect:
        button_list=[]
    return button_list           #renvoyer le rectangle du curseur

def key_input(sound):
    while True:
        pygame.time.wait(1)
        event=pygame.event.wait()
        stop=False
        key_name=""
        if event.type==pygame.QUIT:
            sys.exit(37)
        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==3 or event.button==1:
                stop=True
                button_sound(2,1,1,"none","none",True,sound)
                break
        elif event.type==pygame.JOYBUTTONDOWN:
            key_name="joystick_"+str(event.joy)+"_button_"+str(event.button)
            button_sound(1,1,1,"none","none",True,sound)
            break
        elif event.type==pygame.JOYHATMOTION:
            if not str(event.value)=="(0, 0)" and not str(event.value)=="(1, 1)" and not str(event.value)=="(-1, 1)" and not str(event.value)=="(1, -1)" and not str(event.value)=="(-1, -1)":
                key_name="joystick_"+str(event.joy)+"_hat_"+str(event.value)
                button_sound(1,1,1,"none","none",True,sound)
                break
        elif event.type==pygame.JOYAXISMOTION:
            if float(event.value)>=0.9:
                key_name="joystick_"+str(event.joy)+"_+axis_"+str(event.axis)
                button_sound(1,1,1,"none","none",True,sound)
                break
            elif float(event.value)<=-0.9:
                key_name="joystick_"+str(event.joy)+"_-axis_"+str(event.axis)
                button_sound(1,1,1,"none","none",True,sound)
                break
        elif event.type==pygame.KEYDOWN:
            key_name=pygame.key.name(event.key)
            key_name=key_name.upper()
            button_sound(1,1,1,"none","none",True,sound)
            break
    return [stop,key_name]
    

def key_input_button(buttonid,background,cursor,rect,key_list):
    button_list=[]
    font=pygame.font.Font(None, int(50*background[3]))
    color=pygame.Color('white')
    for i in range(2):
        for j in range(8):
            button_adjust=image_adjust("graphic/button/cursor/Commande_curseur",531+670*i,300+92*j)
            button_rect=button_adjust[0].get_rect()
            button_rect=button_rect.move(button_adjust[1],button_adjust[2])
            background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
            screen.blit(background_piece,(button_rect[0],button_rect[1]))
            button_list += [button_rect]
            text=key_list[i*8+j]
            txt_surface=font.render(text, True, color)
            if int(button_adjust[0].get_width()-10*background[3])<txt_surface.get_width():
                rate=float(button_adjust[0].get_width()/(txt_surface.get_width()+20*background[3]))
                font=pygame.font.Font(None, int(50*background[3]*rate))
                txt_surface=font.render(text, True, color)
                font=pygame.font.Font(None, int(50*background[3]))
            screen.blit(txt_surface, (int(button_adjust[1]+(button_adjust[0].get_width()-txt_surface.get_width()-5*background[3])),int(button_adjust[2]+(button_adjust[0].get_height()-txt_surface.get_height()-3*background[3]))))
    if cursor:
        button_adjust=image_adjust("graphic/button/cursor/Commande_curseur",531+670*int(round(buttonid-int(buttonid),1)*10),300+92*(int(buttonid)-1))
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
    if not rect:
        button_list=[]
    return button_list           #renvoyer le rectangle du curseur

def map_button(buttonid,background,rect):
    button_list=[]
    xy_list=[[1012,341],[1187,390],[1547,422],[100,739],[635,315]]
    for i in range(5):
        button_adjust=image_adjust("graphic/button/cursor/Carte_curseur",xy_list[i][0],xy_list[i][1])
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
        screen.blit(background_piece,(button_rect[0],button_rect[1]))
        button_list += [button_rect]
        if int(buttonid*10)==i:
            screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))     
    if not rect:
        button_list=[]
    return button_list           #renvoyer le rectangle du curseur

def menu_button(buttonid,rect):         #fonction pour faire apparraître le menu avec un curseur
    button=["Jouer","Option","Quitter"]
    button_list=[]
    for i in range(3):
        button_adjust=image_adjust("graphic/button/menu/"+str(button[i]),785,540+140*i)
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        button_list += [button_rect]
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
        if i==int(buttonid):
            cursor=image_adjust("graphic/button/cursor/Menu_curseur",785,540+140*i)
            screen.blit(cursor[0],(cursor[1],cursor[2]))
    if not rect:
        button_list=[]
    return button_list           #renvoyer le rectangle du curseur

def menu_change(old_axis,screen_width,screen_height,screen_mode,music,sound,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2,old_key_list):          #fonction pour fair apparaître un menu de choix de sauvegarde des options
    window_change_adjust=image_adjust("graphic/button/option/Changement",758,465)
    screen.blit(window_change_adjust[0],(window_change_adjust[1],window_change_adjust[2]))
    button=0.0
    change_list=change_button(button,window_change_adjust,True)
    pygame.display.update()

    old_action=4
    number=-1
    new_time=0
    mouse=pygame.mouse.get_pos()
    pygame.event.clear()
    while True:
        pygame.time.wait(1)
        key=0
        collide=False
        button_old=button
        for i in range(3):
            if change_list[i].collidepoint(mouse):
                if mouse != pygame.mouse.get_pos():
                    collide=True
                    button=round(i/10,1)
                elif button==round(i/10,1):
                    collide=True
                break
        mouse=pygame.mouse.get_pos()          #actualiser la position de la souris
        event=pygame.event.poll()            #détecter des touches et leurs impacts
        event_key_list=event_key(event,False,button,"none","none",old_key_list[0],old_key_list[1],old_key_list[2],old_key_list[3],old_key_list[4],old_key_list[5],old_axis,old_action,number,new_time,False,collide)
        key=event_key_list[0]
        button=event_key_list[1]
        old_axis=event_key_list[2]
        old_action=event_key_list[3]
        number=event_key_list[4]
        new_time=event_key_list[5]
        if button>0.2:          #si le curseur est trop vers la droite, le ramener sur le bouton 1
            button=0.0
        elif button<0.0:            #si le curseur est trop vers la gauche, le ramener sur le bouton 3
            button=0.2
        button_sound(key,button_old,button,0.1,0.2,True,sound)
        change_button(button,window_change_adjust,False)
        pygame.display.update()
        if key==1 and not button==0.2:
            if button==0.0:         #sortir en sauvegardant les changements
                if screen_mode=="Plein écran":
                    screen_mode="Fullscreen"
                elif screen_mode=="Fenêtré sans bordure":
                    screen_mode="Borderless"
                else:
                    screen_mode="Border"
                option=open("Option.txt",'w')
                option.write("Resolution:|"+str(screen_width)+"|"+str(screen_height)+"|\nScreen_mode:|"+str(screen_mode)+"|\nMusic:|"+str(music)+"|\nSound:|"+str(sound)+"|\nConfig:\nP1:\nUP:|"+str(UP1)+"|\nDOWN:|"+str(DOWN1)+"|\nRIGHT:|"+str(RIGHT1)+"|\nLEFT:|"+str(LEFT1)+"|\nATK:|"+str(ATK1)+"|\nSPE:|"+str(SPE1)+"|\nSHLD:|"+str(SHLD1)+"|\nMENU:|"+str(MENU1)+"|\nP2:\nUP:|"+str(UP2)+"|\nDOWN:|"+str(DOWN2)+"|\nRIGHT:|"+str(RIGHT2)+"|\nLEFT:|"+str(LEFT2)+"|\nATK:|"+str(ATK2)+"|\nSPE:|"+str(SPE2)+"|\nSHLD:|"+str(SHLD2)+"|\nMENU:|"+str(MENU2))
                option.close()
                return [1,old_axis]
            elif button==0.1:         #sortir sans sauvegarder les changement
                return [2,old_axis]
        elif key==1 and button==0.2 or key==2:          #ne pas sortir
            return [0,old_axis]

def menu_option(old_axis,screen_width,screen_height,screen_mode,music,sound,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2):            #fonction pour faire apparaître le menu des options
    screen.fill(pygame.Color("black"))
    option_background=image_adjust("graphic/background/Option",0,0)
    screen.blit(option_background[0],(option_background[1],option_background[2]))
    button=0.0
    option_list=option_button(button,screen_width,screen_height,screen_mode,music,sound,option_background,True,0)
    gauge_list=gauge(music,sound,button,option_background,False,True)
    pygame.display.update()

    new_width=screen_width
    new_height=screen_height
    new_screen_mode=screen_mode
    new_music=music
    new_sound=sound
    
    button_width_rect=option_list[0]
    button_height_rect=option_list[1]
    button_preset_rect=option_list[2]
    button_border_rect=option_list[3]
    button_music_rect=option_list[4]
    button_sound_rect=option_list[5]
    button_key_rect=option_list[6]
    button_return_rect=option_list[7]
    gauge_music_rect=gauge_list[0]
    gauge_sound_rect=gauge_list[1]
    cursor_music_rect=gauge_list[2]
    cursor_sound_rect=gauge_list[3]
    mouse = pygame.mouse.get_pos()
    key_changing=0
    old_action=4
    number=-1
    new_time=0
    font=pygame.font.Font(None, int(40*option_background[3]))
    color=pygame.Color('white')
    pygame.event.clear()
    while True:
        pygame.time.wait(1)
        key=0
        changing=0
        collide=False
        button_old=button
        volume_cursor=False
        if button_width_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=0.0
                collide=True
            elif button==0.0:
                collide=True
        elif button_height_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=0.1
                collide=True
            elif button==0.1:
                collide=True
        elif button_preset_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=0.2
                collide=True
            elif button==0.2:
                collide=True
        elif button_border_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=1.1
                collide=True
            elif button==1.1:
                collide=True
        elif button_music_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=2.1
                collide=True
            elif button==2.1:
                collide=True
        elif gauge_music_rect.collidepoint(mouse):
            volume_cursor=True
            if mouse != pygame.mouse.get_pos():
                button=2.2
                collide=True
            elif button==2.2:
                collide=True
        elif button_sound_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=3.1
                collide=True
            elif button==3.1:
                collide=True
        elif gauge_sound_rect.collidepoint(mouse):
            volume_cursor=True
            if mouse != pygame.mouse.get_pos():
                button=3.2
                collide=True
            elif button==3.2:
                collide=True
        elif button_key_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=4.1
                collide=True
            elif button==4.1:
                collide=True
        elif button_return_rect.collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                button=4.2
                collide=True
            elif button==4.2:
                collide=True
        mouse = pygame.mouse.get_pos()          #actualiser la position de la souris
        event = pygame.event.poll()            #détecter des touches et leurs impacts
        event_key_list=event_key(event,False,button,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,True,collide)
        key=event_key_list[0]
        button=event_key_list[1]
        old_axis=event_key_list[2]
        old_action=event_key_list[3]
        number=event_key_list[4]
        new_time=event_key_list[5]
        if button==-1.0:
            button=4.1
        elif button==-0.1:
            button=0.2
        elif button==1.0:
            button=1.1
        elif button==-0.9:
            button=4.1
        elif button==-0.8:
            button=4.2
        elif button==0.3:
            button=0.0
        elif button==1.2:
            button=1.1
        elif button==2.0:
            button=2.2
        elif button==2.3:
            button=2.1
        elif button==3.0:
            button=3.2
        elif button==3.3:
            button=3.1
        elif button==4.0:
            button=4.2
        elif button==4.3:
            button=4.1
        elif button==5.1:
            button=0.1
        elif button==5.2:
            button=0.2
        button_sound(key,button_old,button,4.2,"none",True,new_sound)
        if volume_cursor and event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            button_sound(1,button,button,4.2,"none",True,new_sound)
            volume_list=gauge_cursor(new_music,new_sound,button,option_background,gauge_music_rect,cursor_music_rect,new_width,new_height,new_screen_mode)
            new_music=volume_list[0]
            new_sound=volume_list[1]
        elif key==1 and not button == 4.2:
            if button==0.0 or button==0.1:
                if button==0.0:
                    old_width=''
                    old_height=new_height
                else:
                    old_height=''
                    old_width=new_width
                option_button(button,old_width,old_height,new_screen_mode,new_music,new_sound,option_background,False,0)
                pygame.display.update()
                size=''
                text_surface = font.render(size,True,color)
                stop=False
                while not stop:
                    for event in pygame.event.get():            #détecter des touches et leurs impacts
                        if event.type == pygame.QUIT:
                            sys.exit(37)
                        key=0
                        event_key_list=event_key(event,False,button,"none","none","none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,False,True)
                        key=event_key_list[0]
                        old_axis=event_key_list[2]
                        if key == 1:            #sauvegarder le texte si ce n'est pas un 0 ou du vide
                            if not size=='':
                                if int(size)==0:
                                    size=''
                                    key=2
                            else:
                                key=2
                            stop=True
                        elif key == 2:          #quitter sans sauvegarder le texte
                            size=''
                            stop=True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:         #effacer le dernier caractère
                                 size = size[:-1]
                            if not text_surface.get_width()>button_width_rect[2]-(button_width_rect[2]/35)*2:
                                if event.unicode=="0" or event.unicode=="1" or event.unicode=="2" or event.unicode=="3" or event.unicode=="4" or event.unicode=="5" or event.unicode=="6" or event.unicode=="7" or event.unicode=="8" or event.unicode=="9":
                                    size += event.unicode
                        text_surface = font.render(str(size),True,color)
                        if button==0.0:
                            old_width=size
                        else:
                            old_height=size
                        option_button(button,old_width,old_height,new_screen_mode,new_music,new_sound,option_background,False,0)
                        pygame.display.update()
                if not size=='':
                    if button==0.0:
                        new_width=int(size)
                    else:
                        new_height=int(size)

            elif button==0.2:
                choice_background=image_adjust("graphic/button/option/Préréglages",1564,98)
                option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,1)
                screen.blit(choice_background[0],(choice_background[1],choice_background[2]))
                choice=0
                choice_rect_list=choice_button(choice,choice_background,True,15)
                pygame.display.update()
                choice_background_rect=choice_background[0].get_rect()
                choice_background_rect=choice_background_rect.move(choice_background[1],choice_background[2])
                mouse = pygame.mouse.get_pos()
                while True:
                    pygame.time.wait(1)
                    key=0
                    choice_old=choice
                    if mouse != pygame.mouse.get_pos():
                        for i in range(15):
                            if choice_rect_list[i].collidepoint(mouse):
                                choice=i
                                break
                    mouse = pygame.mouse.get_pos()          #actualiser la position de la souris
                    event = pygame.event.poll()            #détecter des touches et leurs impacts
                    event_key_list=event_key(event,False,choice,UP1,DOWN1,"none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,True,True)
                    key=event_key_list[0]
                    choice=event_key_list[1]
                    old_axis=event_key_list[2]
                    old_action=event_key_list[3]
                    number=event_key_list[4]
                    new_time=event_key_list[5]
                    if choice<0:
                        choice=14
                    elif choice>14:
                        choice=0
                    button_sound(key,choice,choice,"none","none",True,new_sound)
                    choice_button(choice,choice_background,False,15)
                    pygame.display.update()
                    if key==1:
                        if choice_background_rect.collidepoint(mouse) or not event.type == pygame.MOUSEBUTTONUP:
                            choice_list=[[640,480,'4 : 3'],[800,600,'4 : 3'],[1024,768,'4 : 3'],[1280,720,'16 : 6'],[1280,800,'16 : 10'],[1280,960,'4 : 3'],[1280,1024,'5 : 4'],[1366,768,'16 : 9'],[1440,900,'16 : 10'],[1600,900,'16 : 9'],[1600,1200,'4 : 3'],[1680,1050,'16 : 10'],[1920,1080,'16 : 9'],[2880,1620,'16 : 9'],[3840,2160,'16 : 9']]
                            new_width=choice_list[choice][0]
                            new_height=choice_list[choice][1]
                        break
                    elif key==2:
                        break
                option_background_piece=option_background[0].subsurface(choice_background_rect[0]-option_background[1],choice_background_rect[1]-option_background[2],choice_background_rect[2],choice_background_rect[3])
                screen.blit(option_background_piece,(choice_background_rect[0],choice_background_rect[1]))
                option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,0)
                pygame.display.update()
 
            elif button==1.1:
                choice_background=image_adjust("graphic/button/option/Mode",1249,444)
                option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,2)
                screen.blit(choice_background[0],(choice_background[1],choice_background[2]))
                choice=0
                choice_rect_list=choice_button(choice,choice_background,True,3)
                pygame.display.update()
                choice_background_rect=choice_background[0].get_rect()
                choice_background_rect=choice_background_rect.move(choice_background[1],choice_background[2])
                mouse = pygame.mouse.get_pos()
                while True:
                    pygame.time.wait(1)
                    key=0
                    choice_old=choice
                    if mouse != pygame.mouse.get_pos():
                        for i in range(3):
                            if choice_rect_list[i].collidepoint(mouse):
                                choice=i
                                break
                    mouse = pygame.mouse.get_pos()          #actualiser la position de la souris
                    event = pygame.event.poll()            #détecter des touches et leurs impacts
                    event_key_list=event_key(event,False,choice,UP1,DOWN1,"none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,True,True)
                    key=event_key_list[0]
                    choice=event_key_list[1]
                    old_axis=event_key_list[2]
                    old_action=event_key_list[3]
                    number=event_key_list[4]
                    new_time=event_key_list[5]
                    if choice<0:
                        choice=2
                    elif choice>2:
                        choice=0
                    button_sound(key,choice,choice,4.2,"none",True,new_sound)
                    choice_button(choice,choice_background,False,3)
                    pygame.display.update()
                    if key==1:
                        if choice_background_rect.collidepoint(mouse) or not event.type == pygame.MOUSEBUTTONUP:
                            choice_list=["Fenêtré","Fenêtré sans bordure","Plein écran"]
                            new_screen_mode=choice_list[choice]
                        break
                    elif key==2:
                        break
                option_background_piece=option_background[0].subsurface(choice_background_rect[0]-option_background[1],choice_background_rect[1]-option_background[2],choice_background_rect[2],choice_background_rect[3])
                screen.blit(option_background_piece,(choice_background_rect[0],choice_background_rect[1]))
                option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,0)
                pygame.display.update()
                
            if button==2.1 or button==3.1:
                if button==2.1:
                    old_music=''
                    old_sound=new_sound
                else:
                    old_sound=''
                    old_music=new_music
                option_button(button,new_width,new_height,new_screen_mode,old_music,old_sound,option_background,False,0)
                pygame.display.update()
                volume=''
                text_surface = font.render(volume,True,color)
                stop=False
                while not stop:
                    for event in pygame.event.get():            #détecter des touches et leurs impacts
                        if event.type == pygame.QUIT:
                            sys.exit(37)
                        key=0
                        event_key_list=event_key(event,False,button,"none","none","none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,False,True)
                        key=event_key_list[0]
                        old_axis=event_key_list[2]
                        if key==1:            #sauvegarder le texte si ce n'est pas un 0 ou du vide
                            if not volume=='':
                                if int(volume)>100:
                                    volume=100
                                else:
                                    volume=int(volume)
                            else:
                                key=2
                            stop=True
                        elif key == 2:          #quitter sans sauvegarder le texte
                            volume=''
                            stop=True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:         #effacer le dernier caractère
                                 volume = volume[:-1]
                            if not text_surface.get_width()>button_width_rect[2]-(button_width_rect[2]/35)*2:
                                if event.unicode=="0" or event.unicode=="1" or event.unicode=="2" or event.unicode=="3" or event.unicode=="4" or event.unicode=="5" or event.unicode=="6" or event.unicode=="7" or event.unicode=="8" or event.unicode=="9":
                                    volume += event.unicode
                        text_surface = font.render(str(volume),True,color)
                        if button==2.1:
                            old_music=volume
                        else:
                            old_sound=volume
                        option_button(button,new_width,new_height,new_screen_mode,old_music,old_sound,option_background,False,0)
                        pygame.display.update()
                if not volume=='':
                    if button==2.1:
                        new_music=volume
                        pygame.mixer.music.set_volume(round(new_music/100,2))
                    else:
                        new_sound=volume

            elif button==2.2 or button==3.2:
                option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,0)
                gauge(new_music,new_sound,button,option_background,True,False)
                pygame.display.update()
                volume=[round(new_music/10,1),round(new_sound/10,1)]
                if button==2.2:
                    i=0
                else:
                    i=1
                mouse = pygame.mouse.get_pos()
                while True:
                    pygame.time.wait(1)
                    key=0
                    volume_old=volume[i]
                    mouse = pygame.mouse.get_pos()
                    event = pygame.event.poll()
                    event_key_list=event_key(event,False,volume[i],"none","none",RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,False,True)
                    key=event_key_list[0]
                    volume[i]=event_key_list[1]
                    old_axis=event_key_list[2]
                    old_action=event_key_list[3]
                    number=event_key_list[4]
                    new_time=event_key_list[5]
                    if volume[i]<00.0:
                        volume[i]=10.0
                    elif volume[i]>10.0:
                        volume[i]=00.0
                    if button==2.2:
                        pygame.mixer.music.set_volume(round(volume[0]/10,2))
                    if i==1:
                        button_sound("nokey",volume_old,volume[i],"none","none",True,int(volume[1]*10))
                    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        if button==2.2 and gauge_music_rect.collidepoint(mouse):
                            button_sound(1,button,button,"none","none",True,int(volume[1]*10))
                            volume_list=gauge_cursor(int(volume[0]*10),int(volume[1]*10),button,option_background,gauge_music_rect,cursor_music_rect,new_width,new_height,new_screen_mode)
                            new_music=volume_list[0]
                            new_sound=volume_list[1]
                            break
                        elif button==3.2 and gauge_sound_rect.collidepoint(mouse):
                            button_sound(1,button,button,"none","none",True,int(volume[1]*10))
                            volume_list=gauge_cursor(int(volume[0]*10),int(volume[1]*10),button,option_background,gauge_music_rect,cursor_music_rect,new_width,new_height,new_screen_mode)
                            new_music=volume_list[0]
                            new_sound=volume_list[1]
                            break
                    option_button(button,new_width,new_height,new_screen_mode,int(volume[0]*10),int(volume[1]*10),option_background,False,0)
                    gauge(int(volume[0]*10),int(volume[1]*10),button,option_background,True,False)
                    pygame.display.update()
                    if key==1:
                        new_music=int(volume[0]*10)
                        new_sound=int(volume[1]*10)
                        break
                    elif key==2:
                        pygame.mixer.music.set_volume(round(new_music/100,2))
                        break

            elif button == 4.1:
                screen.fill(pygame.Color("black"))
                option_background=image_adjust("graphic/background/Commande",0,0)
                screen.blit(option_background[0],(option_background[1],option_background[2]))
                editkey_button=0.0
                key_list=key_button(editkey_button,option_background,True)
                key_list_name=[UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2]
                key_input_list=key_input_button(editkey_button,option_background,False,True,key_list_name)
                pygame.display.update()
                new_key_list_name=[]
                new_key_list_name=new_key_list_name+key_list_name
                pygame.event.clear()
                while True:
                    pygame.time.wait(1)
                    key=0
                    j=0
                    changing_key=0
                    collide=False
                    collidepoint=0
                    editkey_button_old=editkey_button
                    for i in range(3):
                        if key_list[i].collidepoint(mouse):
                            if mouse != pygame.mouse.get_pos():
                                editkey_button=round(i/10,1)
                                collide=True
                            elif editkey_button==round(i/10,1):
                                collide=True
                            collidepoint=1
                            break
                    if not collidepoint==1:
                        for i in range(16):
                            if key_input_list[i].collidepoint(mouse):
                                collidepoint=2
                                j=i
                                break
                    mouse = pygame.mouse.get_pos()
                    event = pygame.event.poll()
                    event_key_list=event_key(event,False,editkey_button,"none","none",RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,False,collide)
                    key=event_key_list[0]
                    editkey_button=event_key_list[1]
                    old_axis=event_key_list[2]
                    old_action=event_key_list[3]
                    number=event_key_list[4]
                    new_time=event_key_list[5]
                    if editkey_button<0.0:
                        editkey_button=0.2
                    elif editkey_button>0.2:
                        editkey_button=0.0
                    button_sound(key,editkey_button_old,editkey_button,0.2,"none",True,new_sound)
                    if collidepoint==2 and event.type == pygame.MOUSEBUTTONUP and event.button==1:
                        button_sound(1,editkey_button,editkey_button,0.2,"none",True,new_sound)
                        editkey_button=1+j-8*int(j/8)+round((int(j/8))/10,1)
                        old_key_name=new_key_list_name[j]
                        new_key_list_name[j]=""
                        key_button(editkey_button,option_background,False)
                        key_input_button(editkey_button,option_background,True,False,new_key_list_name)
                        pygame.display.update()
                        key_return_list=key_input(new_sound)
                        if not key_return_list[0]:
                            new_key_list_name[j]=key_return_list[1]
                        else:
                            new_key_list_name[j]=old_key_name
                        editkey_button=round(editkey_button-int(editkey_button),1)
                    elif key==1 and not editkey_button==0.2:
                        for i in range(8):
                            new_editkey_button=1+i+editkey_button
                            old_key_name=new_key_list_name[i+8*int(editkey_button*10)]
                            new_key_list_name[i+8*int(editkey_button*10)]=""
                            key_button(new_editkey_button,option_background,False)
                            key_input_button(new_editkey_button,option_background,True,False,new_key_list_name)
                            pygame.display.update()
                            key_return_list=key_input(new_sound)
                            if not key_return_list[0]:
                                new_key_list_name[i+8*int(editkey_button*10)]=key_return_list[1]
                                editkey_button=round(new_editkey_button-int(new_editkey_button),1)
                            else:
                                new_key_list_name[i+8*int(editkey_button*10)]=old_key_name
                                editkey_button=round(new_editkey_button-int(new_editkey_button),1)
                                break
                        
                    elif key == 1 and editkey_button == 0.2 or key == 2:            #s'il y a du changement ouvrir le menu de sauvegarde des options, sinon sortir
                        for i in range(16):
                            if not new_key_list_name[i]==key_list_name[i]:
                                changing_key=1
                                break
                        save_change=0
                        if changing_key==1:
                            old_key_list=[RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1]
                            save_change_list=menu_change(old_axis,screen_width,screen_height,screen_mode,music,sound,new_key_list_name[0],new_key_list_name[1],new_key_list_name[2],new_key_list_name[3],new_key_list_name[4],new_key_list_name[5],new_key_list_name[6],new_key_list_name[7],new_key_list_name[8],new_key_list_name[9],new_key_list_name[10],new_key_list_name[11],new_key_list_name[12],new_key_list_name[13],new_key_list_name[14],new_key_list_name[15],old_key_list)
                            save_change=save_change_list[0]
                            old_axis=save_change_list[1]
                            pygame.event.clear()
                            if save_change>0:
                                break
                            else:
                                screen.fill(pygame.Color("black"))
                                screen.blit(option_background[0],(option_background[1],option_background[2]))
                        else:
                            pygame.event.clear()
                            break
                    key_button(editkey_button,option_background,False)
                    key_input_button(editkey_button,option_background,False,False,new_key_list_name)
                    pygame.display.update()
                if save_change==1:
                    key_changing=1
                    option=open("Option.txt").read()            #appliquer les changements
                
                    UP1=option.split("|")[10]
                    DOWN1=option.split("|")[12]
                    RIGHT1=option.split("|")[14]
                    LEFT1=option.split("|")[16]
                    ATK1=option.split("|")[18]
                    SPE1=option.split("|")[20]
                    SHLD1=option.split("|")[22]
                    MENU1=option.split("|")[24]
                    UP2=option.split("|")[26]
                    DOWN2=option.split("|")[28]
                    RIGHT2=option.split("|")[30]
                    LEFT2=option.split("|")[32]
                    ATK2=option.split("|")[34]
                    SPE2=option.split("|")[36]
                    SHLD2=option.split("|")[38]
                    MENU2=option.split("|")[40]
                screen.fill(pygame.Color("black"))
                option_background=image_adjust("graphic/background/Option",0,0)
                screen.blit(option_background[0],(option_background[1],option_background[2]))
                button=4.1
            
        elif key==1 and button==4.2 or key==2:            #s'il y a du changement ouvrir le menu de sauvegarde des options, sinon sortir
            if not new_screen_mode==screen_mode:
                changing=2
            elif not new_width==screen_width:
                changing=1
            elif not new_height==screen_height:
                changing=1
            elif not new_music==music:
                changing=1
            elif not new_sound==sound:
                changing=1
            if changing>0:
                old_key_list=[RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1]
                save_change_list=menu_change(old_axis,new_width,new_height,new_screen_mode,new_music,new_sound,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2,old_key_list)
                save_change=save_change_list[0]
                old_axis=save_change_list[1]
                pygame.event.clear()
                if save_change==1:
                    return [changing,key_changing,old_axis]
                elif save_change==2:
                    return [0,key_changing,old_axis]
                else:
                    screen.fill(pygame.Color("black"))
                    screen.blit(option_background[0],(option_background[1],option_background[2]))
                    option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,0)
                    gauge(new_music,new_sound,button,option_background,False,False)
            else:
                return [0,key_changing,old_axis]
        option_button(button,new_width,new_height,new_screen_mode,new_music,new_sound,option_background,False,0)
        gauge(new_music,new_sound,button,option_background,False,False)
        pygame.display.update()

def option_button(buttonid,screen_width,screen_height,screen_mode,music,sound,background,rect,choice):           #fonction pour faire apparraître le menu des option des options et un curseur
    xy_list=[[455,48],[977,48],[1564,48],[1249,394],[1140,683],[1140,801],[841,964],[1544,1005]]
    button_list=[]
    font=pygame.font.Font(None, int(40*background[3]))
    color=pygame.Color('white')
    text_list=[str(screen_width),str(screen_height),'custom',str(screen_mode),str(music),str(sound)]
    preset_list=[[640,480,'4 : 3'],[800,600,'4 : 3'],[1024,768,'4 : 3'],[1280,720,'16 : 9'],[1280,800,'16 : 10'],[1280,960,'4 : 3'],[1280,1024,'5 : 4'],[1366,768,'16 : 9'],[1440,900,'16 : 10'],[1600,900,'16 : 9'],[1600,1200,'4 : 3'],[1680,1050,'16 : 10'],[1920,1080,'16 : 9'],[2880,1620,'16 : 9'],[3840,2160,'16 : 9']]
    custom=1
    for j in preset_list:
        if j[0]==screen_width and j[1]==screen_height:
            custom=0
            break
    if choice==1:
        text_list[2]=''
    elif custom==0:
        text_list[2]=str(screen_width)+' x '+str(screen_height)+' ('+j[2]+')'
    if choice==2:
        text_list[3]=''
    for i in range(8):
        button_adjust=image_adjust("graphic/button/cursor/Option_curseur",xy_list[i][0],xy_list[i][1])
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        background_piece=background[0].subsurface(button_rect[0]-background[1],button_rect[1]-background[2],button_rect[2],button_rect[3])
        screen.blit(background_piece,(button_rect[0],button_rect[1]))
        button_list += [button_rect]
        if i<6:
            text=text_list[i]
            text_surface=font.render(text, True, color)
            screen.blit(text_surface,(int(button_adjust[1]+(button_adjust[0].get_width()-text_surface.get_width()-5*button_adjust[3])),int(button_adjust[2]+(button_adjust[0].get_height()-text_surface.get_height()+5*button_adjust[3]))))
    if buttonid==0.0:
        i=0
    elif buttonid==0.1:
        i=1
    elif buttonid==0.2:
        i=2
    elif buttonid==1.1:
        i=3
    elif buttonid==2.1:
        i=4
    elif buttonid==3.1:
        i=5
    elif buttonid==4.1:
        i=6
    elif buttonid==4.2:
        i=7
    if not buttonid==2.2 and not buttonid==3.2:
        button_adjust=image_adjust("graphic/button/cursor/Option_curseur",xy_list[i][0],xy_list[i][1])
        button_rect=button_adjust[0].get_rect()
        button_rect=button_rect.move(button_adjust[1],button_adjust[2])
        screen.blit(button_adjust[0],(button_adjust[1],button_adjust[2]))
    if not rect:
        button_list=[]
    return button_list           #renvoyer le rectangle du curseur

def Player_bar(HPmax,HP,SPmax,SP,ID):
    HPc=(255*(1-HP/HPmax),255*(HP/HPmax),0)
    if HP==0:
        HPc=(69,69,69)
    ID=int(ID-1)
    pygame.draw.rect(screen,(69,69,69),(int(round((9+1596*ID)*ratio+(screen_width-1920*ratio)/2,0)),int(round(9*ratio+(screen_height-1080*ratio)/2,0)),int(304*ratio),int(34*ratio)))
    pygame.draw.rect(screen,HPc,(int(round((11+(1596+int(300-300*HP/HPmax))*ID)*ratio+(screen_width-1920*ratio)/2,0)),int(round(11*ratio+(screen_height-1080*ratio)/2,0)),int(300*HP/HPmax*ratio),int(30*ratio)))

    SPc=(255*(1-SP/SPmax),255*(1-SP/SPmax),255*(SP/SPmax))
    if SP==0:
        SPc=(69,69,69)
    pygame.draw.rect(screen,(69,69,69),(int(round((9+1796*ID)*ratio+(screen_width-1920*ratio)/2,0)),int(round(53*ratio+(screen_height-1080*ratio)/2,0)),int(104*ratio),int(34*ratio)))
    pygame.draw.rect(screen,SPc,(int(round((11+(1796+int(100-100*SP/SPmax))*ID)*ratio+(screen_width-1920*ratio)/2,0)),int(round(55*ratio+(screen_height-1080*ratio)/2,0)),int(100*SP/SPmax*ratio),int(30*ratio)))


def timer_fight(background,foreground,P1,P2,sound,P1_in_anim,P1_hit,P1_direction,P2_in_anim,P2_hit,P2_direction,P1_bullet,P2_bullet,P1_ult,P1_font,P1_sentence1,P1_sentence2,P2_ult,P2_font,P2_sentence1,P2_sentence2):
    second=3
    image_timer_adjust=image_adjust("fighters/timer/3",809,314)
    image_rect=image_timer_adjust[0].get_rect()
    image_rect=image_rect.move(image_timer_adjust[1],image_timer_adjust[2])
    background_piece=background[0].subsurface(image_rect[0]-background[1],image_rect[1]-background[2],image_rect[2],image_rect[3])
    screen.blit(background_piece,(image_rect[0],image_rect[1]))
    for i in range(int(round(len(P1_bullet)/2,0))):
        screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
    screen.blit(pygame.transform.flip(P1[0],P1_direction,False),(int(P1[1]),int(P1[2])))
    if P1_in_anim==4.0:
        P1_hity=P1[2]-P1_hit[1][0].get_height()
        if P1_direction:
            P1_hitx=P1[1]+1*ratio
        else:
            P1_hitx=P1[1]+200*ratio
        P1_hit_rect=P1_hit[1][0].get_rect()
        P1_hit_rect=P1_hit_rect.move(P1_hitx,P1_hity)
        screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
    if P1_in_anim==4.1:
        P1_hity=P1[2]+P1[0].get_height()
        if P1_direction:
            P1_hitx=P1[1]+118*ratio
        else:
            P1_hitx=P1[1]+108*ratio
        P1_hit_rect=P1_hit[2][0].get_rect()
        P1_hit_rect=P1_hit_rect.move(P1_hitx,P1_hity)
        screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
    elif P1_in_anim==4.2:
        if not P1_direction:
            P1_hitx=P1[1]+P1[0].get_width()
        else:
            P1_hitx=P1[1]-P1_hit[0][0].get_width()
        P1_hity=P1[2]+65*ratio
        P1_hit_rect=P1_hit[0][0].get_rect()
        P1_hit_rect=P1_hit_rect.move(P1_hitx,P1_hity)
        screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(P1_hitx,P1_hity))
    for i in range(int(round(len(P2_bullet)/2,0))):
        screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
    screen.blit(pygame.transform.flip(P2[0],P2_direction,False),(int(P2[1]),int(P2[2])))
    if P2_in_anim==4.0:
        P2_hity=P2[2]-P2_hit[1][0].get_height()
        if P2_direction:
            P2_hitx=P2[1]+1*ratio
        else:
            P2_hitx=P2[1]+200*ratio
        P2_hit_rect=P2_hit[1][0].get_rect()
        P2_hit_rect=P2_hit_rect.move(P2_hitx,P2_hity)
        screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
    if P2_in_anim==4.1:
        P2_hity=P2[2]+P2[0].get_height()
        if P2_direction:
            P2_hitx=P2[1]+118*ratio
        else:
            P2_hitx=P2[1]+108*ratio
        P2_hit_rect=P2_hit[2][0].get_rect()
        P2_hit_rect=P2_hit_rect.move(P2_hitx,P2_hity)
        screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
    elif P2_in_anim==4.2:
        if not P2_direction:
            P2_hitx=P2[1]+P2[4][0].get_width()
        else:
            P2_hitx=P2[1]-P2_hit[0][0].get_width()
        P2_hity=P2[2]+65*ratio
        P2_hit_rect=P2_hit[0][0].get_rect()
        P2_hit_rect=P2_hit_rect.move(P2_hitx,P2_hity)
        screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
    screen.blit(foreground[0],(foreground[1],foreground[2]))
    if P1_ult:
        txt_surface=P1_font.render(P1_sentence1, True, color)
        txt_surface2=P1_font.render(P1_sentence2, True, color)
        screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
        screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
    if P2_ult:
        txt_surface=P2_font.render(P2_sentence1, True, color)
        txt_surface2=P2_font.render(P2_sentence2, True, color)
        screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
        screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
    screen.blit(image_timer_adjust[0],(image_timer_adjust[1],image_timer_adjust[2]))
    button_sound(0,1,2,"none","none",False,sound)
    pygame.display.update()
    old_time=pygame.time.get_ticks()
    while not second==0:
        time=pygame.time.get_ticks()-old_time
        if time>=1000:
            second=second-1
            a=2
            if second==0:
                a=1
            image_timer_adjust=image_adjust("fighters/timer/"+str(second),(a-1)*809,314)
            button_sound(2-a,1,a,"none","none",False,sound)
            image_rect=image_timer_adjust[0].get_rect()
            image_rect=image_rect.move(image_timer_adjust[1],image_timer_adjust[2])
            background_piece=background[0].subsurface(image_rect[0]-background[1],image_rect[1]-background[2],image_rect[2],image_rect[3])
            screen.blit(background_piece,(image_rect[0],image_rect[1]))
            for i in range(int(round(len(P1_bullet)/2,0))):
                screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
            screen.blit(pygame.transform.flip(P1[0],P1_direction,False),(int(P1[1]),int(P1[2])))
            if P1_in_anim==4.0:
                screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
            elif P1_in_anim==4.1:
                screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
            elif P1_in_anim==4.2:
                screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
            for i in range(int(round(len(P2_bullet)/2,0))):
                screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
            screen.blit(pygame.transform.flip(P2[0],P2_direction,False),(int(P2[1]),int(P2[2])))
            if P2_in_anim==4.0:
                screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
            elif P2_in_anim==4.1:
                screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
            elif P2_in_anim==4.2:
                screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
            screen.blit(foreground[0],(foreground[1],foreground[2]))
            if P1_ult:
                screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
            if P2_ult:
                screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
            screen.blit(image_timer_adjust[0],(image_timer_adjust[1],image_timer_adjust[2]))
            pygame.display.update()
            old_time=pygame.time.get_ticks()
    while not second==1:
        time=pygame.time.get_ticks()-old_time
        if time>=1000:
            second=1
            screen.blit(background_piece,(image_rect[0],image_rect[1]))
            for i in range(int(round(len(P1_bullet)/2,0))):
                screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
            screen.blit(pygame.transform.flip(P1[0],P1_direction,False),(int(P1[1]),int(P1[2])))
            if P1_in_anim==4.0:
                screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
            elif P1_in_anim==4.1:
                screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
            elif P1_in_anim==4.2:
                screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
            for i in range(int(round(len(P2_bullet)/2,0))):
                screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
            screen.blit(pygame.transform.flip(P2[0],P2_direction,False),(int(P2[1]),int(P2[2])))
            if P2_in_anim==4.0:
                screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
            elif P2_in_anim==4.1:
                screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
            elif P2_in_anim==4.2:
                screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
            screen.blit(foreground[0],(foreground[1],foreground[2]))
            if P1_ult:
                screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
            if P2_ult:
                screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
            pygame.display.update()
        
#------------------------OPTION------------------------#

if not os.path.isfile("./Option.txt"):          #vérifier si le fichier 'Option.txt' existe, sinon le recréer
    option=open("Option.txt",'w')
    option.write("Resolution:|640|480|\nScreen_mode:|Border|\nMusic:|100|\nSound:|100|\nConfig:\nP1:\nUP:|UP|\nDOWN:|DOWN|\nRIGHT:|RIGHT|\nLEFT:|LEFT|\nATK:|W|\nSPE:|D|\nSHLD:|SPACE|\nMENU:|ESCAPE|\nP2:\nUP:|[5]|\nDOWN:|[2]|\nRIGHT:|[3]|\nLEFT:|[1]|\nATK:|[7]|\nSPE:|[4]|\nSHLD:|[0]|\nMENU:|[+]")
    option.close()

icon=pygame.image.load("MechaMecha_World_Championship.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("MechaMecha_World_Championship")

option=open("Option.txt").read()            #copier tout le texte du fichier 'Option.txt' dans une variable

screen_width=int(option.split("|")[1])        #définir la largeur du cadre
screen_height=int(option.split("|")[2])         #définir la hauteur du cadre
if str(option.lower().split("|")[4])=="fullscreen":
    screen_mode="Plein écran"
elif str(option.lower().split("|")[4])=="borderless":
    screen_mode="Fenêtré sans bordure"
else:
    screen_mode="Fenêtré"
if screen_mode=="Plein écran":         #afficher le cadre en pleine écran
    screen=pygame.display.set_mode([screen_width,screen_height], pygame.FULLSCREEN)
elif screen_mode=="Fenêtré sans bordure":         #afficher le cadre sans bordure
    screen=pygame.display.set_mode([screen_width,screen_height], pygame.NOFRAME)
else:         #afficher le cadre avec bordure 
    screen=pygame.display.set_mode([screen_width,screen_height])

music=int(option.split("|")[6])
sound=int(option.split("|")[8])
joysticks=[]
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
joystick_P1=0
str_key_list=[]
for i in range(8):
    strkey=option.split("|")[10+i*2]
    if strkey.split("_")[0]=="joystick":
        strkey="joystick_0_"+str(strkey.split("_")[2])+"_"+str(strkey.split("_")[3])
        joystick_P1=1
    str_key_list.append(strkey)
for i in range(8):
    strkey=option.split("|")[26+i*2]
    if strkey.split("_")[0]=="joystick":
        if joystick_P1==1:
            strkey="joystick_1_"+str(strkey.split("_")[2])+"_"+str(strkey.split("_")[3])
        else:
            strkey="joystick_0_"+str(strkey.split("_")[2])+"_"+str(strkey.split("_")[3])
    str_key_list.append(strkey)
UP1=str_key_list[0]           #attribution des touches
DOWN1=str_key_list[1]
RIGHT1=str_key_list[2]
LEFT1=str_key_list[3]
ATK1=str_key_list[4]
SPE1=str_key_list[5]
SHLD1=str_key_list[6]
MENU1=str_key_list[7]
UP2=str_key_list[8]
DOWN2=str_key_list[9]
RIGHT2=str_key_list[10]
LEFT2=str_key_list[11]
ATK2=str_key_list[12]
SPE2=str_key_list[13]
SHLD2=str_key_list[14]
MENU2=str_key_list[15]
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

#------------------------JEU------------------------#

old_axis=""
background=pygame.image.load("./graphic/background/Pygame.png")         #choisir une image de fond
background=image_adjust(background,0,0)
old_axis=fade(background[0],background[1],background[2],50,64,4,100,64,4,ATK1,SHLD1,old_axis)

background=pygame.image.load("./graphic/background/Logo.png")         #choisir une image de fond
background=image_adjust(background,0,0)
old_axis=fade(background[0],background[1],background[2],500,64,4,100,64,4,ATK1,SHLD1,old_axis)

pygame.time.delay(500)

background=image_adjust("graphic/background/Menu",0,0)
screen.blit(background[0],(background[1],background[2]))
pygame.mixer.music.load("./audio/music/menu.ogg")
pygame.mixer.music.set_volume(round(music/100,2))
pygame.mixer.music.play(-1)
button=0
menu_list=menu_button(button,True)
pygame.display.update()
select_sound=pygame.mixer.Sound("./audio/sound/button/Selection.ogg")

old_action=4
number=-1
new_time=0
mouse=pygame.mouse.get_pos()
pygame.event.clear()
while True:         #boucle du jeu, en sortir cause la fin du jeu
    pygame.time.wait(1)
    key=0
    collide=False
    button_old=button
    for i in range(3):
        if menu_list[i].collidepoint(mouse):
            if mouse != pygame.mouse.get_pos():
                collide=True
                button=i
            elif button==i:
                collide=True
            break
    mouse=pygame.mouse.get_pos()          #Actualiser la position de la souris
    event = pygame.event.poll()            #détecter des touches et leurs impacts
    event_key_list=event_key(event,False,button,UP1,DOWN1,"none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,True,collide)
    key=event_key_list[0]
    button=event_key_list[1]
    old_axis=event_key_list[2]
    old_action=event_key_list[3]
    number=event_key_list[4]
    new_time=event_key_list[5]
    if button>2:          #si le curseur est trop bas, le ramener sur le bouton 1
        button=0
    elif button<0:          #si le curseur est trop haut, le ramener sur le bouton 3
        button=2
    button_sound(key,button_old,button,2,"none",False,sound)
    if button != button_old:
        select_sound.stop()
        select_sound.set_volume(round(sound/100,2))
        select_sound.play()
    elif key==1:
        if button==0:
            background_fighters_adjust=image_adjust("graphic/background/Combattants",0,0)
            screen.blit(background_fighters_adjust[0],(background_fighters_adjust[1],background_fighters_adjust[2]))
            fighters_button(1,1,background_fighters_adjust)
            pygame.display.update()
            background_fighters2_adjust=image_adjust("graphic/background/Combattants2",0,0)

            button_fighters=0.0
            button_fighters2=0.0
            old_action2=4
            number2=-1
            new_time2=0
            old_axis2=""
            P1_validate=False
            P2_validate=False
            pygame.event.clear()
            while True:
                pygame.time.wait(1)
                key_fighters=0
                key_fighters2=2
                button_fighters_old=button_fighters
                button_fighters2_old=button_fighters2
                event=pygame.event.poll()
                fighters_event_list=event_key(event,True,button_fighters,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,False,False)
                if fighters_event_list[0]==3:
                    button_sound(2,1,1,"none","none",True,sound)
                    break
                key_fighters=fighters_event_list[0]
                old_axis=fighters_event_list[2]
                old_action=fighters_event_list[3]
                number=fighters_event_list[4]
                new_time=fighters_event_list[5]
                if not P1_validate:
                    fighters_list=button_menu_fighters(fighters_event_list[1])
                    button_fighters=fighters_list[0]
                    P1_select=fighters_list[1]
                if not P1_validate or not key_fighters==1:
                    button_sound(key_fighters,button_fighters_old,button_fighters,"none","none",False,sound)
                fighters_event_list2=event_key(event,True,button_fighters2,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2,old_axis2,old_action2,number2,new_time2,False,False)
                if fighters_event_list2[0]==3:
                    button_sound(2,1,1,"none","none",True,sound)
                    break
                key_fighters2=fighters_event_list2[0]
                old_axis2=fighters_event_list2[2]
                old_action2=fighters_event_list2[3]
                number2=fighters_event_list2[4]
                new_time2=fighters_event_list2[5]
                if not P2_validate:
                    fighters_list2=button_menu_fighters(fighters_event_list2[1])
                    button_fighters2=fighters_list2[0]
                    P2_select=fighters_list2[1]
                if not P2_validate or not key_fighters2==1:
                    button_sound(key_fighters2,button_fighters2_old,button_fighters2,"none","none",False,sound)
                if key_fighters==1 and not P1_validate:
                    P1_validate=True
                elif key_fighters==2 and P1_validate:
                    P1_validate=False
                if key_fighters2==1 and not P2_validate:
                    P2_validate=True
                elif key_fighters2==2 and P2_validate:
                    P2_validate=False
                if P1_validate and P2_validate:
                    screen.blit(background_fighters2_adjust[0],(background_fighters2_adjust[1],background_fighters2_adjust[2]))
                    pygame.display.update()
                    key_fighters=0
                    stop_fight=False
                    pygame.event.clear()
                    while True:
                        pygame.time.wait(1)
                        event=pygame.event.poll()
                        fighters_event_list=event_key(event,False,0,"none","none","none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,4,-1,0,False,True)
                        key_fighters=fighters_event_list[0]
                        old_axis=fighters_event_list[2]
                        if key_fighters==0:
                            fighters_event_list=event_key(event,False,0,"none","none","none","none",ATK2,SPE2,SHLD2,MENU2,old_axis2,4,-1,0,False,True)
                            key_fighters=fighters_event_list[0]
                            old_axis2=fighters_event_list[2]
                        if key_fighters==1:
                            background_map_adjust=image_adjust("graphic/background/Carte",0,0)
                            screen.blit(background_map_adjust[0],(background_map_adjust[1],background_map_adjust[2]))
                            button_map=0.0
                            map_rect_list=map_button(button_map,background_map_adjust,True)
                            pygame.display.update()
                            key=0
                            mouse=pygame.mouse.get_pos()
                            pygame.event.clear()
                            while True:
                                pygame.time.wait(1)
                                collide=0
                                button_map_old=button_map
                                for i in range(5):
                                    if map_rect_list[i].collidepoint(mouse):
                                        if mouse != pygame.mouse.get_pos():
                                            collide=True
                                            button_map=i
                                        elif button_map==i:
                                            collide=True
                                        break
                                mouse=pygame.mouse.get_pos()
                                event=pygame.event.poll()            #détecter des touches et leurs impacts
                                event_key_list=event_key(event,False,button_map,"none","none",RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,True,collide)
                                key=event_key_list[0]
                                button_map=event_key_list[1]
                                old_axis=event_key_list[2]
                                old_action=event_key_list[3]
                                number=event_key_list[4]
                                new_time=event_key_list[5]
                                if button_map<0.0:
                                    button_map=0.4
                                elif button_map>0.4:
                                    button_map=0.0
                                button_sound(key,button_map_old,button_map,"none","none",True,sound)
                                if key==1:
                                    pygame.mouse.set_visible(False)
                                    pygame.mixer.music.stop()
                                    ratio=background[3]
                                    mapid=int(button_map*10+1)
                                    background_map_fight_adjust=image_adjust("map/"+str(mapid)+"/background",-500,-500)
                                    screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                    P1=pygame.image.load("./fighters/"+str(P1_select)+"/animation/0.png").convert_alpha()
                                    P1_adjust=image_adjust(P1,99,980-P1.get_height())
                                    screen.blit(P1_adjust[0],(P1_adjust[1],P1_adjust[2]))
                                    P2=pygame.transform.flip(pygame.image.load("./fighters/"+str(P2_select)+"/animation/0.png").convert_alpha(),True,False)
                                    P2_adjust=image_adjust(P2,1819-P2.get_width(),980-P2.get_height())
                                    screen.blit(P2_adjust[0],(P2_adjust[1],P2_adjust[2]))
                                    background_map_fight2_adjust=image_adjust("/map/"+str(mapid)+"/foreground",-500,-500)
                                    screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                    P1_list=fighters_setting(P1_select)
                                    P1_HPmax=P1_list[6]
                                    P1_SPmax=P1_list[7]
                                    Player_bar(P1_HPmax,P1_HPmax,P1_SPmax,0,1)
                                    P2_list=fighters_setting(P2_select)
                                    P2_HPmax=P2_list[6]
                                    P2_SPmax=P2_list[7]
                                    Player_bar(P2_HPmax,P2_HPmax,P2_SPmax,0,2)
                                    pygame.display.update()
                                    timer_fight(background_map_fight_adjust,background_map_fight2_adjust,P1_adjust,P2_adjust,sound,0,0,False,0,0,False,[],[],False,"none","none","none",False,"none","none","none")
                                    P1=P1_list[0]
                                    P1_hit=P1_list[1]
                                    P1_missile=P1_list[2]
                                    P1_Vspeed=P1_list[3]
                                    P1_Hspeed=P1_list[4]
                                    P1_fall=P1_list[5]
                                    P1_ATKpunch=P1_list[8]
                                    P1_cdpunch=P1_list[9]
                                    P1_ATKshot=P1_list[10]
                                    P1_cdshot=P1_list[11]
                                    P1_def=P1_list[12]
                                    P1_sentence1=P1_list[13]
                                    P1_sentence2=P1_list[14]
                                    P1_direction=False
                                    P1_air=False
                                    P1_anim=0
                                    P1_x=P1_adjust[1]
                                    P1_y=P1_adjust[2]
                                    P1_HP=P1_HPmax
                                    P1_SP=0
                                    old_axis=""
                                    old_action=[False,False,False,False,False,False,False]
                                    P1_SHLD_old=False
                                    P1_defshield=P1_def
                                    P1_new_time=0
                                    P1_new_time_def=0
                                    P1_new_time_atk=0
                                    P1_ult_new_time=0
                                    P1_cooldown_atk=False
                                    P1_hitx=0
                                    P1_hity=0
                                    P1_new_time_spe=0
                                    P1_timer_spe=0
                                    P1_cooldown_spe=False
                                    P1_bullet=[]
                                    P1_missile_counter=0
                                    P1_font=pygame.font.Font("./fighters/"+str(P1_select)+"/font.ttf", int(100*ratio))
                                    P1_ult=False
                                    
                                    P2=P2_list[0]
                                    P2_hit=P2_list[1]
                                    P2_missile=P2_list[2]
                                    P2_Vspeed=P2_list[3]
                                    P2_Hspeed=P2_list[4]
                                    P2_fall=P2_list[5]
                                    P2_ATKpunch=P2_list[8]
                                    P2_cdpunch=P2_list[9]
                                    P2_ATKshot=P2_list[10]
                                    P2_cdshot=P2_list[11]
                                    P2_def=P2_list[12]
                                    P2_sentence1=P2_list[13]
                                    P2_sentence2=P2_list[14]
                                    P2_direction=True
                                    P2_air=False
                                    P2_anim=0
                                    P2_x=P2_adjust[1]
                                    P2_y=P2_adjust[2]
                                    P2_HP=P2_HPmax
                                    P2_SP=0
                                    old_axis2=""
                                    old_action2=[False,False,False,False,False,False,False]
                                    P2_SHLD_old=False
                                    P2_defshield=P2_def
                                    P2_new_time=0
                                    P2_new_time_def=0
                                    P2_new_time_atk=0
                                    P2_ult_new_time=0
                                    P2_cooldown_atk=False
                                    P2_hitx=0
                                    P2_hity=0
                                    P2_new_time_spe=0
                                    P2_timer_spe=0
                                    P2_cooldown_spe=False
                                    P2_bullet=[]
                                    P2_missile_counter=0
                                    P2_font=pygame.font.Font("./fighters/"+str(P2_select)+"/font.ttf", int(100*ratio))
                                    P2_ult=False
                                    pygame.mixer.music.load("./map/"+str(mapid)+"/theme.ogg")
                                    pygame.mixer.music.play(-1)
                                    sound_screenshot=pygame.mixer.Sound("./audio/sound/game/screenshot.ogg")
                                    sound_punch=pygame.mixer.Sound("./audio/sound/game/punch.ogg")
                                    sound_punch.set_volume(round(sound/100,2))
                                    sound_jetpack=pygame.mixer.Sound("./audio/sound/game/jetpack.ogg")
                                    Sol=int(round(980*ratio+(screen_height-1080*ratio)/2,0))
                                    P1_new_time_anim=0
                                    P1_in_anim=""
                                    P2_new_time_anim=0
                                    P2_in_anim=""
                                    victory=False
                                    color=pygame.Color('orange')
                                    pygame.event.clear()
                                    while True:
                                        pygame.time.wait(1)
                                        P1_direction_old=P1_direction
                                        P2_direction_old=P2_direction
                                        P1_rect=P1[P1_anim][0].get_rect()
                                        P1_rect=P1_rect.move(int(P1_x),int(P1_y))
                                        background_piece=background_map_fight_adjust[0].subsurface(P1_rect[0]-background_map_fight_adjust[1],P1_rect[1]-background_map_fight_adjust[2],P1_rect[2],P1_rect[3])
                                        screen.blit(background_piece,(P1_rect[0],P1_rect[1]))
                                        P2_rect=P2[P2_anim][0].get_rect()
                                        P2_rect=P2_rect.move(int(P2_x),int(P2_y))
                                        background_piece=background_map_fight_adjust[0].subsurface(P2_rect[0]-background_map_fight_adjust[1],P2_rect[1]-background_map_fight_adjust[2],P2_rect[2],P2_rect[3])
                                        screen.blit(background_piece,(P2_rect[0],P2_rect[1]))
                                        if P1_ult:
                                            P1_txt_surface_rect=txt_surface.get_rect()
                                            P1_txt_surface_rect=P1_txt_surface_rect.move(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0)))
                                            background_piece=background_map_fight_adjust[0].subsurface(P1_txt_surface_rect[0]-background_map_fight_adjust[1],P1_txt_surface_rect[1]-background_map_fight_adjust[2],P1_txt_surface_rect[2],P1_txt_surface_rect[3])
                                            screen.blit(background_piece,(P1_txt_surface_rect[0],P1_txt_surface_rect[1]))
                                            P1_txt_surface2_rect=txt_surface2.get_rect()
                                            P1_txt_surface2_rect=P1_txt_surface2_rect.move(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0)))
                                            background_piece=background_map_fight_adjust[0].subsurface(P1_txt_surface2_rect[0]-background_map_fight_adjust[1],P1_txt_surface2_rect[1]-background_map_fight_adjust[2],P1_txt_surface2_rect[2],P1_txt_surface2_rect[3])
                                            screen.blit(background_piece,(P1_txt_surface2_rect[0],P1_txt_surface2_rect[1]))
                                            P2_HP=P2_HP-0.04*(P1_ATKshot/10)
                                            if P2_HP<0:
                                                P2_HP=0
                                        if P2_ult:
                                            P2_txt_surface_rect=txt_surface.get_rect()
                                            P2_txt_surface_rect=P2_txt_surface_rect.move(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0)))
                                            background_piece=background_map_fight_adjust[0].subsurface(P2_txt_surface_rect[0]-background_map_fight_adjust[1],P2_txt_surface_rect[1]-background_map_fight_adjust[2],P2_txt_surface_rect[2],P2_txt_surface_rect[3])
                                            screen.blit(background_piece,(P2_txt_surface_rect[0],P2_txt_surface_rect[1]))
                                            P2_txt_surface2_rect=txt_surface2.get_rect()
                                            P2_txt_surface2_rect=P2_txt_surface2_rect.move(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0)))
                                            background_piece=background_map_fight_adjust[0].subsurface(P2_txt_surface2_rect[0]-background_map_fight_adjust[1],P2_txt_surface2_rect[1]-background_map_fight_adjust[2],P2_txt_surface2_rect[2],P2_txt_surface2_rect[3])
                                            screen.blit(background_piece,(P2_txt_surface2_rect[0],P2_txt_surface2_rect[1]))
                                            P1_HP=P1_HP-0.04*(P2_ATKshot/10)
                                            if P1_HP<0:
                                                P1_HP=0
                                        P1_missile_counter=0
                                        for i in range(int(round(len(P1_bullet)/2,0))):
                                            P1_missile_rect=P1_missile[0].get_rect()
                                            P1_missile_rect=P1_missile_rect.move(int(P1_bullet[(i-P1_missile_counter)*2]),int(round(574*ratio+(screen_height-1080*ratio)/2,0)))
                                            background_piece=background_map_fight_adjust[0].subsurface(P1_missile_rect[0]-background_map_fight_adjust[1],P1_missile_rect[1]-background_map_fight_adjust[2],P1_missile_rect[2],P1_missile_rect[3])
                                            screen.blit(background_piece,(P1_missile_rect[0],P1_missile_rect[1]))
                                            if P1_missile_rect.colliderect(P2_rect):
                                                del(P1_bullet[(i-P1_missile_counter)*2])
                                                del(P1_bullet[(i-P1_missile_counter)*2])
                                                P1_missile_counter=P1_missile_counter+1
                                                if not P2_defshield==0 and not P2_anim==7:
                                                    P2_HP=P2_HP-P1_ATKshot*P2_def*2.5
                                                    P2_SP=P2_SP+0.05
                                                elif P2_defshield==0 and not P2_anim==7:
                                                    P2_HP=P2_HP-P1_ATKshot*4
                                                if P2_HP<0:
                                                    P2_HP=0
                                                if P1_SP>P1_SPmax:
                                                    P1_SP=P1_SPmax
                                                if P2_SP>P2_SPmax:
                                                    P2_SP=P2_SPmax
                                        P2_missile_counter=0
                                        for i in range(int(round(len(P2_bullet)/2,0))):
                                            P2_missile_rect=P2_missile[0].get_rect()
                                            P2_missile_rect=P2_missile_rect.move(int(P2_bullet[(i-P2_missile_counter)*2]),int(round(574*ratio+(screen_height-1080*ratio)/2,0)))
                                            background_piece=background_map_fight_adjust[0].subsurface(P2_missile_rect[0]-background_map_fight_adjust[1],P2_missile_rect[1]-background_map_fight_adjust[2],P2_missile_rect[2],P2_missile_rect[3])
                                            screen.blit(background_piece,(P2_missile_rect[0],P2_missile_rect[1]))
                                            if P2_missile_rect.colliderect(P1_rect):
                                                del(P2_bullet[(i-P2_missile_counter)*2])
                                                del(P2_bullet[(i-P2_missile_counter)*2])
                                                P2_missile_counter=P2_missile_counter+1
                                                if not P1_defshield==0 and not P1_anim==7:
                                                    P1_HP=P1_HP-P2_ATKshot*P1_def*2.5
                                                    P1_SP=P1_SP+0.05
                                                elif P1_defshield==0 and not P1_anim==7:
                                                    P1_HP=P1_HP-P2_ATKshot*4
                                                if P1_HP<0:
                                                    P1_HP=0
                                                if P2_SP>P2_SPmax:
                                                    P2_SP=P2_SPmax
                                                if P1_SP>P1_SPmax:
                                                    P1_SP=P1_SPmax
                                        if P1_in_anim==4.0 or P1_in_anim==4.1 or P1_in_anim==4.2:
                                            background_piece=background_map_fight_adjust[0].subsurface(P1_hit_rect[0]-background_map_fight_adjust[1],P1_hit_rect[1]-background_map_fight_adjust[2],P1_hit_rect[2],P1_hit_rect[3])
                                            screen.blit(background_piece,(P1_hit_rect[0],P1_hit_rect[1]))
                                            if P1_hit_rect.colliderect(P2_rect):
                                                if not P2_defshield==0 and not P2_anim==7:
                                                    P1_SP=P1_SP+0.15
                                                    P2_HP=P2_HP-P1_ATKpunch*P2_def*0.015
                                                    P2_SP=P2_SP+0.05
                                                elif P2_defshield==0 and not P2_anim==7:
                                                    P1_SP=P1_SP+0.4
                                                    P2_HP=P2_HP-P1_ATKpunch*0.03
                                                if P2_HP<0:
                                                    P2_HP=0
                                                if P1_SP>P1_SPmax:
                                                    P1_SP=P1_SPmax
                                                if P2_SP>P2_SPmax:
                                                    P2_SP=P2_SPmax
                                        if P2_in_anim==4.0 or P2_in_anim==4.1 or P2_in_anim==4.2:
                                            background_piece=background_map_fight_adjust[0].subsurface(P2_hit_rect[0]-background_map_fight_adjust[1],P2_hit_rect[1]-background_map_fight_adjust[2],P2_hit_rect[2],P2_hit_rect[3])
                                            screen.blit(background_piece,(P2_hit_rect[0],P2_hit_rect[1]))
                                            if P2_hit_rect.colliderect(P1_rect):
                                                if not P1_defshield==0 and not P1_anim==7:
                                                    P2_SP=P2_SP+0.15
                                                    P1_HP=P1_HP-P2_ATKpunch*P1_def*0.015
                                                    P1_SP=P1_SP+0.05
                                                elif P1_defshield==0 and not P1_anim==7:
                                                    P2_SP=P2_SP+0.4
                                                    P1_HP=P1_HP-P2_ATKpunch*0.03
                                                if P1_HP<0:
                                                    P1_HP=0
                                                if P1_SP>P1_SPmax:
                                                    P1_SP=P1_SPmax
                                                if P2_SP>P2_SPmax:
                                                    P2_SP=P2_SPmax
                                        if P1_HP==0 and P2_HP==0:
                                            font=pygame.font.Font(None, int(50*ratio))
                                            screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                            screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                            Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                            Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                            txt_surface=font.render("Egalite!", True, color)
                                            victory=True
                                        elif P1_HP==0:
                                            screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                            for i in range(int(round(len(P2_bullet)/2,0))):
                                                screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                            screen.blit(pygame.transform.flip(P2[P2_anim][0],P2_direction,False),(P2_x,P2_y))
                                            if P2_in_anim==4.0:
                                                screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(P2_hitx,P2_hity))
                                            elif P2_in_anim==4.1:
                                                screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(P2_hitx,P2_hity))
                                            elif P2_in_anim==4.2:
                                                screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(P2_hitx,P2_hity))
                                            screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                            Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                            Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                            txt_surface=P2_font.render("Le Joueur 2 est vainqueur!", True, color)
                                            victory=True
                                        elif P2_HP==0:
                                            screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                            for i in range(int(round(len(P1_bullet)/2,0))):
                                                screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                            screen.blit(pygame.transform.flip(P1[P1_anim][0],P1_direction,False),(P1_x,P1_y))
                                            if P1_in_anim==4.0:
                                                screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(P1_hitx,P1_hity))
                                            elif P1_in_anim==4.1:
                                                screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(P1_hitx,P1_hity))
                                            elif P1_in_anim==4.2:
                                                screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(P1_hitx,P1_hity))
                                            screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                            Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                            Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                            txt_surface=P1_font.render("Le Joueur 1 est vainqueur!", True, color)
                                            victory=True
                                        if victory:
                                            screen.blit(txt_surface,((screen_width-txt_surface.get_width())/2,(screen_height-txt_surface.get_height())/2))
                                            font=pygame.font.Font(None, int(50*ratio))
                                            txt_surface2=font.render("pressez une touche pour quitter", True, color)
                                            screen.blit(txt_surface2,((screen_width-txt_surface2.get_width())/2,(screen_height-txt_surface2.get_height())/2+100*ratio))
                                            pygame.display.update()
                                            pygame.time.wait(1000)
                                            pygame.event.clear()
                                            while True:
                                                pygame.time.wait(1)
                                                event=pygame.event.wait()
                                                if event.type==pygame.MOUSEBUTTONUP or event.type==pygame.JOYBUTTONDOWN or event.type==pygame.JOYHATMOTION or event.type==pygame.JOYAXISMOTION or event.type==pygame.KEYDOWN:
                                                    stop_fight=True
                                                    break
                                        key_name=""
                                        event=pygame.event.poll()
                                        event_fight_list=event_fight(event,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,P1_air)
                                        P1_UP=event_fight_list[0]
                                        P1_DOWN=event_fight_list[1] 
                                        P1_RIGHT=event_fight_list[2]
                                        P1_LEFT=event_fight_list[3]
                                        P1_ATK=event_fight_list[4]
                                        P1_SPE=event_fight_list[5]
                                        P1_SHLD=event_fight_list[6]
                                        P1_MENU=event_fight_list[7]
                                        old_axis=event_fight_list[8]
                                        old_action=event_fight_list[9]
                                        event_fight2_list=event_fight(event,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2,old_axis2,old_action2,P2_air)
                                        P2_UP=event_fight2_list[0]
                                        P2_DOWN=event_fight2_list[1] 
                                        P2_RIGHT=event_fight2_list[2]
                                        P2_LEFT=event_fight2_list[3]
                                        P2_ATK=event_fight2_list[4]
                                        P2_SPE=event_fight2_list[5]
                                        P2_SHLD=event_fight2_list[6]
                                        P2_MENU=event_fight2_list[7]
                                        old_axis2=event_fight2_list[8]
                                        old_action2=event_fight2_list[9]
                                        if event.type==pygame.KEYDOWN:
                                            key_name=pygame.key.name(event.key)
                                            key_name=key_name.upper()
                                            if key_name=="F12":
                                                stop=False
                                                iphoto=0
                                                while not stop:
                                                    if os.path.isfile("./screenshot/screenshot"+str(iphoto)+".png"):
                                                        iphoto=iphoto+1
                                                    else:
                                                        screen.fill(pygame.Color("black"))
                                                        screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                                        for i in range(int(round(len(P1_bullet)/2,0))):
                                                            screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(pygame.transform.flip(P1[P1_anim][0],P1_direction,False),(P1_x,P1_y))
                                                        if P1_in_anim==4.0:
                                                            screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(P1_hitx,P1_hity))
                                                        elif P1_in_anim==4.1:
                                                            screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(P1_hitx,P1_hity))
                                                        elif P1_in_anim==4.2:
                                                            screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(P1_hitx,P1_hity))
                                                        for i in range(int(round(len(P2_bullet)/2,0))):
                                                            screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(pygame.transform.flip(P2[P2_anim][0],P2_direction,False),(P2_x,P2_y))
                                                        if P2_in_anim==4.0:
                                                            screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(P2_hitx,P2_hity))
                                                        elif P2_in_anim==4.1:
                                                            screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(P2_hitx,P2_hity))
                                                        elif P2_in_anim==4.2:
                                                            screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(P2_hitx,P2_hity))
                                                        screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                                        Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                                        Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                                        if P1_ult:
                                                            screen.blit(txt_surface,((screen_width-txt_surface.get_width())/2,int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                                                            screen.blit(txt_surface2,((screen_width-txt_surface2.get_width())/2,int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
                                                        if P2_ult:
                                                            screen.blit(txt_surface,((screen_width-txt_surface.get_width())/2,int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                            screen.blit(txt_surface2,((screen_width-txt_surface2.get_width())/2,int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                        pygame.image.save(screen, "./screenshot/screenshot"+str(iphoto)+".png")            #prendre une capture d'écran
                                                        sound_screenshot.set_volume(round(sound/100,2))
                                                        sound_screenshot.play()
                                                        P1_rect=P1[P1_anim][0].get_rect()
                                                        P1_rect=P1_rect.move(P1_x,P1_y)
                                                        background_piece=background_map_fight_adjust[0].subsurface(P1_rect[0]-background_map_fight_adjust[1],P1_rect[1]-background_map_fight_adjust[2],P1_rect[2],P1_rect[3])
                                                        screen.blit(background_piece,(P1_rect[0],P1_rect[1]))
                                                        if P1_ult:
                                                            P1_txt_surface_rect=txt_surface.get_rect()
                                                            P1_txt_surface_rect=P1_txt_surface_rect.move((screen_width-txt_surface.get_width())/2,int(round(99*ratio+(screen_height-1080*ratio)/2,0)))
                                                            background_piece=background_map_fight_adjust[0].subsurface(P1_txt_surface_rect[0]-background_map_fight_adjust[1],P1_txt_surface_rect[1]-background_map_fight_adjust[2],P1_txt_surface_rect[2],P1_txt_surface_rect[3])
                                                            screen.blit(background_piece,(P1_txt_surface_rect[0],P1_txt_surface_rect[1]))
                                                            P1_txt_surface2_rect=txt_surface2.get_rect()
                                                            P1_txt_surface2_rect=P1_txt_surface2_rect.move((screen_width-txt_surface2.get_width())/2,int(round(299*ratio+(screen_height-1080*ratio)/2,0)))
                                                            background_piece=background_map_fight_adjust[0].subsurface(P1_txt_surface2_rect[0]-background_map_fight_adjust[1],P1_txt_surface2_rect[1]-background_map_fight_adjust[2],P1_txt_surface2_rect[2],P1_txt_surface2_rect[3])
                                                            screen.blit(background_piece,(P1_txt_surface2_rect[0],P1_txt_surface2_rect[1]))
                                                        if P2_ult:
                                                            P2_txt_surface_rect=txt_surface.get_rect()
                                                            P2_txt_surface_rect=P2_txt_surface_rect.move((screen_width-txt_surface.get_width())/2,int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0)))
                                                            background_piece=background_map_fight_adjust[0].subsurface(P2_txt_surface_rect[0]-background_map_fight_adjust[1],P2_txt_surface_rect[1]-background_map_fight_adjust[2],P2_txt_surface_rect[2],P2_txt_surface_rect[3])
                                                            screen.blit(background_piece,(P2_txt_surface_rect[0],P2_txt_surface_rect[1]))
                                                            P2_txt_surface2_rect=txt_surface2.get_rect()
                                                            P2_txt_surface2_rect=P2_txt_surface2_rect.move((screen_width-txt_surface2.get_width())/2,int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0)))
                                                            background_piece=background_map_fight_adjust[0].subsurface(P2_txt_surface2_rect[0]-background_map_fight_adjust[1],P2_txt_surface2_rect[1]-background_map_fight_adjust[2],P2_txt_surface2_rect[2],P2_txt_surface2_rect[3])
                                                            screen.blit(background_piece,(P2_txt_surface2_rect[0],P2_txt_surface2_rect[1]))
                                                        for i in range(int(round(len(P1_bullet)/2,0))):
                                                            P1_missile_rect=P1_missile[0].get_rect()
                                                            P1_missile_rect=P1_missile_rect.move(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0)))
                                                            background_piece=background_map_fight_adjust[0].subsurface(P1_missile_rect[0]-background_map_fight_adjust[1],P1_missile_rect[1]-background_map_fight_adjust[2],P1_missile_rect[2],P1_missile_rect[3])
                                                            screen.blit(background_piece,(P1_missile_rect[0],P1_missile_rect[1]))
                                                        for i in range(int(round(len(P2_bullet)/2,0))):
                                                            P2_missile_rect=P2_missile[0].get_rect()
                                                            P2_missile_rect=P2_missile_rect.move(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0)))
                                                            background_piece=background_map_fight_adjust[0].subsurface(P2_missile_rect[0]-background_map_fight_adjust[1],P2_missile_rect[1]-background_map_fight_adjust[2],P2_missile_rect[2],P2_missile_rect[3])
                                                            screen.blit(background_piece,(P2_missile_rect[0],P2_missile_rect[1]))
                                                        if P1_in_anim==4.0 or P1_in_anim==4.1 or P1_in_anim==4.2:
                                                            background_piece=background_map_fight_adjust[0].subsurface(P1_hit_rect[0]-background_map_fight_adjust[1],P1_hit_rect[1]-background_map_fight_adjust[2],P1_hit_rect[2],P1_hit_rect[3])
                                                            screen.blit(background_piece,(P1_hit_rect[0],P1_hit_rect[1]))
                                                        P2_rect=P2[P2_anim][0].get_rect()
                                                        P2_rect=P2_rect.move(P2_x,P2_y)
                                                        background_piece=background_map_fight_adjust[0].subsurface(P2_rect[0]-background_map_fight_adjust[1],P2_rect[1]-background_map_fight_adjust[2],P2_rect[2],P2_rect[3])
                                                        screen.blit(background_piece,(P2_rect[0],P2_rect[1]))
                                                        if P2_in_anim==4.0 or P2_in_anim==4.1 or P2_in_anim==4.2:
                                                            background_piece=background_map_fight_adjust[0].subsurface(P2_hit_rect[0]-background_map_fight_adjust[1],P2_hit_rect[1]-background_map_fight_adjust[2],P2_hit_rect[2],P2_hit_rect[3])
                                                            screen.blit(background_piece,(P2_hit_rect[0],P2_hit_rect[1]))
                                                        break
                                        if P1_MENU or P2_MENU:
                                            time_menu=pygame.time.get_ticks()
                                            for i in range(int(round(len(P1_bullet)/2,0))):
                                                screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                            screen.blit(pygame.transform.flip(P1[P1_anim][0],P1_direction,False),(int(P1_x),int(P1_y)))
                                            if P1_in_anim==4.0:
                                                screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                            elif P1_in_anim==4.1:
                                                screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                            elif P1_in_anim==4.2:
                                                screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                            for i in range(int(round(len(P2_bullet)/2,0))):
                                                screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                            screen.blit(pygame.transform.flip(P2[P2_anim][0],P2_direction,False),(int(P2_x),int(P2_y)))
                                            if P2_in_anim==4.0:
                                                screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                            elif P2_in_anim==4.1:
                                                screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                            elif P2_in_anim==4.2:
                                                screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                            screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                            Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                            Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                            if P1_ult:
                                                screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                                                screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
                                            if P2_ult:
                                                screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                            fight_menu_background=image_adjust("graphic/background/Fight_menu",0,0)
                                            screen.blit(fight_menu_background[0],(fight_menu_background[1],fight_menu_background[2]))
                                            button_fight=0
                                            fight_rect_list=fight_menu_button(button_fight,True)
                                            pygame.display.update()
                                            old_axis=""
                                            old_action=4
                                            number=-1
                                            new_time=0
                                            pygame.mouse.set_visible(True)
                                            mouse=pygame.mouse.get_pos()
                                            while True:
                                                pygame.time.wait(1)
                                                key=0
                                                collide=False
                                                button_fight_old=button_fight
                                                for i in range(4):
                                                    if fight_rect_list[i].collidepoint(mouse):
                                                        if mouse!=pygame.mouse.get_pos():
                                                            collide=True
                                                            button_fight=i
                                                        elif button_fight==i:
                                                            collide=True
                                                        break
                                                mouse=pygame.mouse.get_pos()
                                                event=pygame.event.poll()
                                                event_key_list=event_key(event,False,button_fight,UP1,DOWN1,"none","none",ATK1,SPE1,SHLD1,MENU1,old_axis,old_action,number,new_time,True,collide)
                                                key=event_key_list[0]
                                                button_fight=event_key_list[1]
                                                old_axis=event_key_list[2]
                                                old_action=event_key_list[3]
                                                number=event_key_list[4]
                                                new_time=event_key_list[5]
                                                if button_fight<0:
                                                    button_fight=3
                                                elif button_fight>3:
                                                    button_fight=0
                                                if key==2:
                                                    button_sound(1,button_fight,button_fight,"none","none",False,sound)  
                                                button_sound(key,button_fight_old,button_fight,3,"none",False,sound)
                                                if key==1 and button_fight<=1 or key==2:
                                                    color=pygame.Color('orange')
                                                    pygame.mouse.set_visible(False)
                                                    screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                                    for i in range(int(round(len(P1_bullet)/2,0))):
                                                        screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                                    screen.blit(pygame.transform.flip(P1[P1_anim][0],P1_direction,False),(int(P1_x),int(P1_y)))
                                                    if P1_in_anim==4.0:
                                                        screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                                    elif P1_in_anim==4.1:
                                                        screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                                    elif P1_in_anim==4.2:
                                                        screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                                    for i in range(int(round(len(P2_bullet)/2,0))):
                                                        screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                                    screen.blit(pygame.transform.flip(P2[P2_anim][0],P2_direction,False),(int(P2_x),int(P2_y)))
                                                    if P2_in_anim==4.0:
                                                        screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                                    elif P2_in_anim==4.1:
                                                        screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                                    elif P2_in_anim==4.2:
                                                        screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                                    screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                                    Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                                    Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                                    if P1_ult:
                                                        screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(txt_surface2,(int(screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0)))
                                                    if P2_ult:
                                                        screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                    pygame.display.update()
                                                    old_axis=""
                                                    old_action=[False,False,False,False,False,False,False]
                                                    old_axis2=""
                                                    old_action2=[False,False,False,False,False,False,False]
                                                    if key==1 and button_fight==1:
                                                        P1[P1_anim][1]=P1_x
                                                        P1[P1_anim][2]=P1_y
                                                        P2[P2_anim][1]=P2_x
                                                        P2[P2_anim][2]=P2_y
                                                        Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                                        Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                                        timer_fight(background_map_fight_adjust,background_map_fight2_adjust,P1[P1_anim],P2[P2_anim],sound,P1_in_anim,P1_hit,P1_direction,P2_in_anim,P2_hit,P2_direction,P1_bullet,P2_bullet,P1_ult,P1_font,P1_sentence1,P1_sentence2,P2_ult,P2_font,P2_sentence1,P2_sentence2)
                                                    P1_rect=P1[P1_anim][0].get_rect()
                                                    P1_rect=P1_rect.move(int(P1_x),int(P1_y))
                                                    background_piece=background_map_fight_adjust[0].subsurface(P1_rect[0]-background_map_fight_adjust[1],P1_rect[1]-background_map_fight_adjust[2],P1_rect[2],P1_rect[3])
                                                    screen.blit(background_piece,(P1_rect[0],P1_rect[1]))
                                                    P2_rect=P2[P2_anim][0].get_rect()
                                                    P2_rect=P2_rect.move(int(P2_x),int(P2_y))
                                                    background_piece=background_map_fight_adjust[0].subsurface(P2_rect[0]-background_map_fight_adjust[1],P2_rect[1]-background_map_fight_adjust[2],P2_rect[2],P2_rect[3])
                                                    screen.blit(background_piece,(P2_rect[0],P2_rect[1]))
                                                    if P1_ult:
                                                        P1_txt_surface_rect=txt_surface.get_rect()
                                                        P1_txt_surface_rect=P1_txt_surface_rect.move((screen_width-txt_surface.get_width())/2,int(round(99*ratio+(screen_height-1080*ratio)/2,0)))
                                                        background_piece=background_map_fight_adjust[0].subsurface(P1_txt_surface_rect[0]-background_map_fight_adjust[1],P1_txt_surface_rect[1]-background_map_fight_adjust[2],P1_txt_surface_rect[2],P1_txt_surface_rect[3])
                                                        screen.blit(background_piece,(P1_txt_surface_rect[0],P1_txt_surface_rect[1]))
                                                        P1_txt_surface2_rect=txt_surface2.get_rect()
                                                        P1_txt_surface2_rect=P1_txt_surface2_rect.move((screen_width-txt_surface2.get_width())/2,int(round(299*ratio+(screen_height-1080*ratio)/2,0)))
                                                        background_piece=background_map_fight_adjust[0].subsurface(P1_txt_surface2_rect[0]-background_map_fight_adjust[1],P1_txt_surface2_rect[1]-background_map_fight_adjust[2],P1_txt_surface2_rect[2],P1_txt_surface2_rect[3])
                                                        screen.blit(background_piece,(P1_txt_surface2_rect[0],P1_txt_surface2_rect[1]))
                                                    if P2_ult:
                                                        P2_txt_surface_rect=txt_surface.get_rect()
                                                        P2_txt_surface_rect=P2_txt_surface_rect.move((screen_width-txt_surface.get_width())/2,int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0)))
                                                        background_piece=background_map_fight_adjust[0].subsurface(P2_txt_surface_rect[0]-background_map_fight_adjust[1],P2_txt_surface_rect[1]-background_map_fight_adjust[2],P2_txt_surface_rect[2],P2_txt_surface_rect[3])
                                                        screen.blit(background_piece,(P2_txt_surface_rect[0],P2_txt_surface_rect[1]))
                                                        P2_txt_surface2_rect=txt_surface2.get_rect()
                                                        P2_txt_surface2_rect=P2_txt_surface2_rect.move((screen_width-txt_surface2.get_width())/2,int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0)))
                                                        background_piece=background_map_fight_adjust[0].subsurface(P2_txt_surface2_rect[0]-background_map_fight_adjust[1],P2_txt_surface2_rect[1]-background_map_fight_adjust[2],P2_txt_surface2_rect[2],P2_txt_surface2_rect[3])
                                                        screen.blit(background_piece,(P2_txt_surface2_rect[0],P2_txt_surface2_rect[1]))
                                                    for i in range(int(round(len(P1_bullet)/2,0))):
                                                        P1_missile_rect=P1_missile[0].get_rect()
                                                        P1_missile_rect=P1_missile_rect.move(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0)))
                                                        background_piece=background_map_fight_adjust[0].subsurface(P1_missile_rect[0]-background_map_fight_adjust[1],P1_missile_rect[1]-background_map_fight_adjust[2],P1_missile_rect[2],P1_missile_rect[3])
                                                        screen.blit(background_piece,(P1_missile_rect[0],P1_missile_rect[1]))
                                                    for i in range(int(round(len(P2_bullet)/2,0))):
                                                        P2_missile_rect=P2_missile[0].get_rect()
                                                        P2_missile_rect=P2_missile_rect.move(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0)))
                                                        background_piece=background_map_fight_adjust[0].subsurface(P2_missile_rect[0]-background_map_fight_adjust[1],P2_missile_rect[1]-background_map_fight_adjust[2],P2_missile_rect[2],P2_missile_rect[3])
                                                        screen.blit(background_piece,(P2_missile_rect[0],P2_missile_rect[1]))
                                                    if P1_in_anim==4.0 or P1_in_anim==4.1 or P1_in_anim==4.2:
                                                        background_piece=background_map_fight_adjust[0].subsurface(P1_hit_rect[0]-background_map_fight_adjust[1],P1_hit_rect[1]-background_map_fight_adjust[2],P1_hit_rect[2],P1_hit_rect[3])
                                                        screen.blit(background_piece,(P1_hit_rect[0],P1_hit_rect[1]))
                                                    if P2_in_anim==4.0 or P2_in_anim==4.1 or P2_in_anim==4.2:
                                                        background_piece=background_map_fight_adjust[0].subsurface(P2_hit_rect[0]-background_map_fight_adjust[1],P2_hit_rect[1]-background_map_fight_adjust[2],P2_hit_rect[2],P2_hit_rect[3])
                                                        screen.blit(background_piece,(P2_hit_rect[0],P2_hit_rect[1]))
                                                    time_menu=pygame.time.get_ticks()-time_menu
                                                    P1_new_time=P1_new_time+time_menu
                                                    P1_new_time_atk=P1_new_time_atk+time_menu
                                                    P1_new_time_spe=P1_new_time_spe+time_menu
                                                    P1_new_time_def=P1_new_time_def+time_menu
                                                    P1_ult_new_time=P1_ult_new_time+time_menu
                                                    P2_new_time=P2_new_time+time_menu
                                                    P2_new_time_atk=P2_new_time_atk+time_menu
                                                    P2_new_time_spe=P2_new_time_spe+time_menu
                                                    P2_new_time_def=P2_new_time_def+time_menu
                                                    P2_ult_new_time=P2_ult_new_time+time_menu
                                                    break
                                                if key==1 and not button_fight<=1:
                                                    if button_fight==2:
                                                        changing_list=menu_option(old_axis,screen_width,screen_height,screen_mode,music,sound,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2)
                                                        old_axis=changing_list[2]
                                                        option=open("Option.txt").read()
                                                        color=pygame.Color('orange')
                                                        if changing_list[1]==1:
                                                            UP1=option.split("|")[10]
                                                            DOWN1=option.split("|")[12]
                                                            RIGHT1=option.split("|")[14]
                                                            LEFT1=option.split("|")[16]
                                                            ATK1=option.split("|")[18]
                                                            SPE1=option.split("|")[20]
                                                            SHLD1=option.split("|")[22]
                                                            MENU1=option.split("|")[24]
                                                            UP2=option.split("|")[26]
                                                            DOWN2=option.split("|")[28]
                                                            RIGHT2=option.split("|")[30]
                                                            LEFT2=option.split("|")[32]
                                                            ATK2=option.split("|")[34]
                                                            SPE2=option.split("|")[36]
                                                            SHLD2=option.split("|")[38]
                                                            MENU2=option.split("|")[40]
                                                        if changing_list[0]>0:
                                                            P1_x=int(round((P1_x-(screen_width-1920*ratio)/2)/ratio,0))
                                                            P1_y=int(round((P1_y-(screen_height-1080*ratio)/2)/ratio,0))
                                                            P2_x=int(round((P2_x-(screen_width-1920*ratio)/2)/ratio,0))
                                                            P2_y=int(round((P2_y-(screen_height-1080*ratio)/2)/ratio,0))
                                                            Sol=int(round((Sol-(screen_height-1080*ratio)/2)/ratio,0))
                                                            for i in range(int(round(len(P1_bullet)/2,0))):
                                                                P1_bullet[i*2]=int(round((P1_bullet[i*2]-(screen_width-1920*ratio)/2)/ratio,0))
                                                            for i in range(int(round(len(P2_bullet)/2,0))):
                                                                P2_bullet[i*2]=int(round((P2_bullet[i*2]-(screen_width-1920*ratio)/2)/ratio,0))
                                                            screen_width=int(option.split("|")[1])
                                                            screen_height=int(option.split("|")[2])
                                                            if changing_list[0]==2:
                                                                pygame.display.quit()
                                                                pygame.display.init()
                                                                pygame.display.set_icon(icon)
                                                                pygame.display.set_caption("MechaMecha_World_Championship")
                                                            if str(option.lower().split("|")[4])=="fullscreen":
                                                                screen_mode="Plein écran"
                                                            elif str(option.lower().split("|")[4])=="borderless":
                                                                screen_mode="Fenêtré sans bordure"
                                                            else:
                                                                screen_mode="Fenêtré"
                                                            if screen_mode=="Plein écran":
                                                                screen=pygame.display.set_mode([screen_width,screen_height], pygame.FULLSCREEN)
                                                            elif screen_mode=="Fenêtré sans bordure":
                                                                screen=pygame.display.set_mode([screen_width,screen_height], pygame.NOFRAME)
                                                            else:
                                                                screen=pygame.display.set_mode([screen_width,screen_height])
                                                            background_map_fight_adjust=image_adjust("map/"+str(mapid)+"/background",-500,-500)
                                                            background_map_fight2_adjust=image_adjust("/map/"+str(mapid)+"/foreground",-500,-500)
                                                            P1_list=fighters_setting(P1_select)
                                                            P1=P1_list[0]
                                                            P1_hit=P1_list[1]
                                                            P1_missile=P1_list[2]
                                                            P2_list=fighters_setting(P2_select)
                                                            P2=P2_list[0]
                                                            P2_hit=P2_list[1]
                                                            P2_missile=P2_list[2]
                                                            ratio=background_map_fight_adjust[3]
                                                            P1_x=int(round(P1_x*ratio+(screen_width-1920*ratio)/2,0))
                                                            P1_y=int(round(P1_y*ratio+(screen_height-1080*ratio)/2,0))
                                                            P2_x=int(round(P2_x*ratio+(screen_width-1920*ratio)/2,0))
                                                            P2_y=int(round(P2_y*ratio+(screen_height-1080*ratio)/2,0))
                                                            Sol=int(round(Sol*ratio+(screen_height-1080*ratio)/2,0))
                                                            for i in range(int(round(len(P1_bullet)/2,0))):
                                                                P1_bullet[i*2]=int(round(P1_bullet[i*2]*ratio+(screen_width-1920*ratio)/2,0))
                                                            for i in range(int(round(len(P2_bullet)/2,0))):
                                                                P2_bullet[i*2]=int(round(P2_bullet[i*2]*ratio+(screen_width-1920*ratio)/2,0))
                                                            if P1_in_anim==4.0:
                                                                P1_hity=P1_y-P1_hit[1][0].get_height()
                                                                if P1_direction:
                                                                    P1_hitx=P1_x+1*ratio
                                                                else:
                                                                    P1_hitx=P1_x+200*ratio
                                                                P1_hit_rect=P1_hit[1][0].get_rect()
                                                                P1_hit_rect=P1_hit_rect.move(P1_hitx,P1_hity)
                                                            elif P1_in_anim==4.1:
                                                                P1_hity=P1_y+P1[3][0].get_height()
                                                                if P1_direction:
                                                                    P1_hitx=P1_x+118*ratio
                                                                else:
                                                                    P1_hitx=P1_x+108*ratio
                                                                P1_hit_rect=P1_hit[2][0].get_rect()
                                                                P1_hit_rect=P1_hit_rect.move(P1_hitx,P1_hity)
                                                            elif P1_in_anim==4.2:
                                                                if not P1_direction:
                                                                    P1_hitx=P1_x+P1[4][0].get_width()
                                                                else:
                                                                    P1_hitx=P1_x-P1_hit[0][0].get_width()
                                                                P1_hity=P1_y+65*ratio
                                                                P1_hit_rect=P1_hit[0][0].get_rect()
                                                                P1_hit_rect=P1_hit_rect.move(P1_hitx,P1_hity)
                                                            if P2_in_anim==4.0:
                                                                P2_hity=P2_y-P2_hit[1][0].get_height()
                                                                if P2_direction:
                                                                    P2_hitx=P2_x+1*ratio
                                                                else:
                                                                    P2_hitx=P2_x+200*ratio
                                                                P2_hit_rect=P2_hit[1][0].get_rect()
                                                                P2_hit_rect=P2_hit_rect.move(P2_hitx,P2_hity)
                                                            elif P2_in_anim==4.1:
                                                                P2_hity=P2_y+P2[3][0].get_height()
                                                                if P2_direction:
                                                                    P2_hitx=P2_x+118*ratio
                                                                else:
                                                                    P2_hitx=P2_x+108*ratio
                                                                P2_hit_rect=P2_hit[2][0].get_rect()
                                                                P2_hit_rect=P2_hit_rect.move(P2_hitx,P2_hity)
                                                            elif P2_in_anim==4.2:
                                                                if not P2_direction:
                                                                    P2_hitx=P2_x+P2[4][0].get_width()
                                                                else:
                                                                    P2_hitx=P2_x-P2_hit[0][0].get_width()
                                                                P2_hity=P2_y+65*ratio
                                                                P2_hit_rect=P2_hit[0][0].get_rect()
                                                                P2_hit_rect=P2_hit_rect.move(P2_hitx,P2_hity)
                                                            P1_font=pygame.font.Font("./fighters/"+str(P1_select)+"/font.ttf", int(100*ratio))
                                                            P2_font=pygame.font.Font("./fighters/"+str(P2_select)+"/font.ttf", int(100*ratio))
                                                            fight_menu_background=image_adjust("map/"+str(mapid)+"/background",0,0)

                                                            music=int(option.split("|")[6])
                                                            sound=int(option.split("|")[8])
                                                        pygame.mixer.music.set_volume(round(music/100,2))
                                                        button_fight=2
                                                        screen.fill(pygame.Color("black"))
                                                        screen.blit(background_map_fight_adjust[0],(background_map_fight_adjust[1],background_map_fight_adjust[2]))
                                                        for i in range(int(round(len(P1_bullet)/2,0))):
                                                            screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[i*2+1],False),(P1_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(pygame.transform.flip(P1[P1_anim][0],P1_direction,False),(int(P1_x),int(P1_y)))
                                                        if P1_in_anim==4.0:
                                                            screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                                        elif P1_in_anim==4.1:
                                                            screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                                        elif P1_in_anim==4.2:
                                                            screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                                        for i in range(int(round(len(P2_bullet)/2,0))):
                                                            screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[i*2+1],False),(P2_bullet[i*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(pygame.transform.flip(P2[P2_anim][0],P2_direction,False),(int(P2_x),int(P2_y)))
                                                        if P2_in_anim==4.0:
                                                            screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                                        elif P2_in_anim==4.1:
                                                            screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                                        elif P2_in_anim==4.2:
                                                            screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                                        screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                                        Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                                        Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                                        if P1_ult:
                                                            txt_surface=P1_font.render(P1_sentence1, True, color)
                                                            txt_surface2=P1_font.render(P1_sentence2, True, color)
                                                            screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                                                            screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
                                                        if P2_ult:
                                                            txt_surface=P2_font.render(P2_sentence1, True, color)
                                                            txt_surface2=P2_font.render(P2_sentence2, True, color)
                                                            screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                            screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                                        screen.blit(fight_menu_background[0],(fight_menu_background[1],fight_menu_background[2]))
                                                        pygame.display.update()
                                                    elif button_fight==3:
                                                        stop_fight=True
                                                        break
                                                fight_rect_list=fight_menu_button(button_fight,True)
                                                pygame.display.update()
                                        if P1_SHLD and not P1_in_anim==5:
                                            can_shield=True
                                            if not P1_direction and P1_x+P1[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)) and not P1_anim==7:
                                                can_shield=False
                                                P1_SHLD=False
                                            elif P1_direction and P1_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and not P1_anim==7:
                                                can_shield=False
                                                P1_SHLD=False
                                            if P1_defshield==0:
                                                can_shield=False
                                                P1_SHLD=False
                                            if can_shield:
                                                P1_RIGHT=False
                                                P1_LEFT=False
                                                P1_anim=7
                                                if not P1_SHLD_old and P1_SHLD:
                                                    if P1_direction:
                                                        P1_x=P1_x-127*ratio
                                                    else:
                                                        P1_x=P1_x+8*ratio
                                                    P1_y=Sol-P1[P1_anim][0].get_height()
                                                if not P1_in_anim==6:
                                                    P1_new_time=pygame.time.get_ticks()
                                                    P1_in_anim=6
                                                P1_timer=pygame.time.get_ticks()-P1_new_time
                                                if P1_timer>1000:
                                                    P1_in_anim=""
                                                    P1_defshield=round(P1_defshield-0.1,1)
                                                if P1_defshield<0:
                                                    P1_defshield=0
                                        if P1_SHLD_old and not P1_SHLD and P1_anim==7:
                                            P1_in_anim=""
                                            P1_anim=0
                                            P1_new_time_def=pygame.time.get_ticks()
                                            P1_y=Sol-P1[0][0].get_height()
                                            if P1_direction:
                                                P1_x=P1_x+127*ratio
                                            else:
                                                P1_x=P1_x-8*ratio
                                        P1_SHLD_old=P1_SHLD
                                        if not P1_SHLD and not P1_defshield==P1_def:
                                            P1_timer_def=pygame.time.get_ticks()-P1_new_time_def
                                            if P1_defshield==0 and P1_timer_def>5000:
                                                P1_new_time_def=pygame.time.get_ticks()
                                                P1_defshield=round(P1_defshield+0.1,1)
                                            elif not P1_defshield==0 and P1_timer_def>1000:
                                                P1_new_time_def=pygame.time.get_ticks()
                                                P1_defshield=round(P1_defshield+0.1,1)
                                        if P2_SHLD and not P2_in_anim==5:
                                            can_shield=True
                                            if not P2_direction and P2_x+P2[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)) and not P2_anim==7:
                                                can_shield=False
                                                P2_SHLD=False
                                            elif P2_direction and P2_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and not P2_anim==7:
                                                can_shield=False
                                                P2_SHLD=False
                                            if P2_defshield==0:
                                                can_shield=False
                                                P2_SHLD=False
                                            if can_shield:
                                                P2_RIGHT=False
                                                P2_LEFT=False
                                                P2_anim=7
                                                if not P2_SHLD_old and P2_SHLD:
                                                    if P2_direction:
                                                        P2_x=P2_x-127*ratio
                                                    else:
                                                        P2_x=P2_x+8*ratio
                                                    P2_y=Sol-P2[P2_anim][0].get_height()
                                                if not P2_in_anim==6:
                                                    P2_new_time=pygame.time.get_ticks()
                                                    P2_in_anim=6
                                                P2_timer=pygame.time.get_ticks()-P2_new_time
                                                if P2_timer>1000:
                                                    P2_in_anim=""
                                                    P2_defshield=round(P2_defshield-0.1,1)
                                                if P2_defshield<0:
                                                    P2_defshield=0
                                        if P2_SHLD_old and not P2_SHLD and P2_anim==7:
                                            P2_in_anim=""
                                            P2_anim=0
                                            P2_new_time_def=pygame.time.get_ticks()
                                            P2_y=Sol-P2[0][0].get_height()
                                            if P2_direction:
                                                P2_x=P2_x+127*ratio
                                            else:
                                                P2_x=P2_x-8*ratio
                                        P2_SHLD_old=P2_SHLD
                                        if not P2_SHLD and not P2_defshield==P2_def:
                                            P2_timer_def=pygame.time.get_ticks()-P2_new_time_def
                                            if P2_defshield==0 and P2_timer_def>5000:
                                                P2_new_time_def=pygame.time.get_ticks()
                                                P2_defshield=round(P2_defshield+0.1,1)
                                            elif not P2_defshield==0 and P2_timer_def>1000:
                                                P2_new_time_def=pygame.time.get_ticks()
                                                P2_defshield=round(P2_defshield+0.1,1)
                                        if P1_air and not P1_UP and not P1_in_anim==5:
                                            P1_anim=3
                                            P1_y=P1_y+P1_fall*ratio
                                        if P1_UP and not P1_in_anim==5:
                                            P1_air=True
                                            P1_anim=8
                                            if not P1_y-P1_Vspeed*ratio<int(round(0*ratio+(screen_height-1080*ratio)/2,0)):
                                                P1_y=P1_y-P1_Vspeed*ratio
                                            sound_jetpack.set_volume(round(sound/100,2))
                                            sound_jetpack.play()
                                        if P1_RIGHT and not P1_in_anim==5:
                                            P1_direction=False
                                            if not (P1_x+0.5*P1_Hspeed*ratio)>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)-P1[0][0].get_width()):
                                                if not (P1_x+0.5*P1_Hspeed*ratio)>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)-P1[1][0].get_width()) and not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                    if not P1_UP and not P1_air:
                                                        if not P1_in_anim==2:
                                                            P1_new_time=pygame.time.get_ticks()
                                                            P1_in_anim=2
                                                        P1_timer=pygame.time.get_ticks()-P1_new_time
                                                        if P1_timer<150:
                                                            P1_anim=1
                                                        elif P1_timer<300:
                                                            P1_anim=2
                                                        else:
                                                            P1_in_anim=""
                                                    elif not P1_UP and P1_air:
                                                        P1_anim=3
                                                        P1_in_anim=""
                                                else:
                                                    if not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                        P1_in_anim=""
                                                        if not P1_air:
                                                            P1_anim=0
                                                P1_x=P1_x+0.5*P1_Hspeed*ratio      
                                            else:
                                                if not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                    P1_in_anim=""
                                                    if not P1_air:
                                                        P1_anim=0
                                        elif P1_in_anim==2 and not P1_RIGHT:
                                            P1_in_anim=""
                                        if P1_LEFT and not P1_in_anim==5:
                                            P1_direction=True
                                            if not (P1_x-0.5*P1_Hspeed*ratio)<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                if (P1_x+P1[1][0].get_width())>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                    P1_x=P1_x-28*ratio
                                                else:
                                                    if not P1_UP and not P1_air and not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                        if not P1_in_anim==3:
                                                            P1_new_time=pygame.time.get_ticks()
                                                            P1_in_anim=3
                                                        P1_timer=pygame.time.get_ticks()-P1_new_time
                                                        P1_anim_old=P1_anim
                                                        if P1_timer<150:
                                                            P1_anim=1
                                                        elif P1_timer<300:
                                                            P1_anim=2
                                                        else:
                                                            P1_in_anim=""
                                                        if not P1_anim_old==1 and P1_anim==1 and not (P1_x-32*ratio-0.5*P1_Hspeed*ratio)<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                            P1_x=P1_x-32*ratio-0.5*P1_Hspeed*ratio
                                                        elif P1_anim_old==1 and P1_anim==2 and not (P1_x+32*ratio-0.5*P1_Hspeed*ratio)<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                            P1_x=P1_x+32*ratio-0.5*P1_Hspeed*ratio
                                                        else:
                                                            P1_x=P1_x-0.5*P1_Hspeed*ratio
                                                    elif not P1_UP and P1_air and not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                        P1_anim=3
                                                        P1_in_anim=""
                                                        P1_x=P1_x-0.5*P1_Hspeed*ratio
                                                    elif P1_UP:
                                                        if not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                            P1_in_anim=""
                                                        P1_x=P1_x-0.5*P1_Hspeed*ratio
                                                    elif P1_ATK:
                                                        if not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                            P1_in_anim=""
                                                        P1_x=P1_x-0.5*P1_Hspeed*ratio
                                            else:
                                                if not P1_in_anim==4.0 and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                    P1_in_anim=""
                                                    if not P1_air:
                                                        P1_anim=0
                                        elif P1_in_anim==3 and not P1_LEFT:
                                            P1_in_anim=""
                                        if P2_air and not P2_UP and not P2_in_anim==5:
                                            P2_anim=3
                                            P2_y=P2_y+P2_fall*ratio
                                        if P2_UP and not P2_in_anim==5:
                                            P2_air=True
                                            P2_anim=8
                                            if not P2_y-P2_Vspeed*ratio<int(round(0*ratio+(screen_height-1080*ratio)/2,0)):
                                                P2_y=P2_y-P2_Vspeed*ratio
                                            sound_jetpack.set_volume(round(sound/100,2))
                                            sound_jetpack.play()
                                        if P2_RIGHT and not P2_in_anim==5:
                                            P2_direction=False
                                            if not (P2_x+0.5*P2_Hspeed*ratio)>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)-P2[0][0].get_width()):
                                                if not (P2_x+0.5*P2_Hspeed*ratio)>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)-P2[1][0].get_width()) and not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                    if not P2_UP and not P2_air:
                                                        if not P2_in_anim==2:
                                                            P2_new_time=pygame.time.get_ticks()
                                                            P2_in_anim=2
                                                        P2_timer=pygame.time.get_ticks()-P2_new_time
                                                        if P2_timer<150:
                                                            P2_anim=1
                                                        elif P2_timer<300:
                                                            P2_anim=2
                                                        else:
                                                            P2_in_anim=""
                                                    elif not P2_UP and P2_air:
                                                        P2_anim=3
                                                        P2_in_anim=""
                                                else:
                                                    if not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                        P2_in_anim=""
                                                        if not P2_air:
                                                            P2_anim=0
                                                P2_x=P2_x+0.5*P2_Hspeed*ratio      
                                            else:
                                                if not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                    P2_in_anim=""
                                                    if not P2_air:
                                                        P2_anim=0
                                        elif P2_in_anim==2 and not P2_RIGHT:
                                            P2_in_anim=""
                                        if P2_LEFT and not P2_in_anim==5:
                                            P2_direction=True
                                            if not (P2_x-0.5*P2_Hspeed*ratio)<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                if (P2_x+P2[1][0].get_width())>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                    P2_x=P2_x-28*ratio
                                                else:
                                                    if not P2_UP and not P2_air and not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                        if not P2_in_anim==3:
                                                            P2_new_time=pygame.time.get_ticks()
                                                            P2_in_anim=3
                                                        P2_timer=pygame.time.get_ticks()-P2_new_time
                                                        P2_anim_old=P2_anim
                                                        if P2_timer<150:
                                                            P2_anim=1
                                                        elif P2_timer<300:
                                                            P2_anim=2
                                                        else:
                                                            P2_in_anim=""
                                                        if not P2_anim_old==1 and P2_anim==1 and not (P2_x-32*ratio-0.5*P2_Hspeed*ratio)<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                            P2_x=P2_x-32*ratio-0.5*P2_Hspeed*ratio
                                                        elif P2_anim_old==1 and P2_anim==2 and not (P2_x+32*ratio-0.5*P2_Hspeed*ratio)<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                            P2_x=P2_x+32*ratio-0.5*P2_Hspeed*ratio
                                                        else:
                                                            P2_x=P2_x-0.5*P2_Hspeed*ratio
                                                    elif not P2_UP and P2_air and not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                        P2_anim=3
                                                        P2_in_anim=""
                                                        P2_x=P2_x-0.5*P2_Hspeed*ratio
                                                    elif P2_UP:
                                                        if not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                            P2_in_anim=""
                                                        P2_x=P2_x-0.5*P2_Hspeed*ratio
                                                    elif P2_ATK:
                                                        if not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                            P2_in_anim=""
                                                        P2_x=P2_x-0.5*P2_Hspeed*ratio
                                            else:
                                                if not P2_in_anim==4.0 and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                    P2_in_anim=""
                                                    if not P2_air:
                                                        P2_anim=0
                                        elif P2_in_anim==3 and not P2_LEFT:
                                            P2_in_anim=""
                                        if (P1_ATK or P1_in_anim==4.0 or P1_in_anim==4.1 or P1_in_anim==4.2) and not P1_in_anim==5:
                                            if not P1_cooldown_atk:
                                                if (P1_DOWN or P1_in_anim==4.1) and not P1_in_anim==4.0 and not P1_in_anim==4.2:
                                                    if not P1_in_anim==4.1:
                                                        P1_new_time=pygame.time.get_ticks()
                                                        P1_in_anim=4.1
                                                        if P1_UP:
                                                            P1_anim=11
                                                        else:
                                                            P1_anim=10
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P1_in_anim==4.1:
                                                        P1_timer=pygame.time.get_ticks()-P1_new_time
                                                        if P1_timer>150:
                                                            P1_in_anim=""
                                                            P1_anim=3
                                                            P1_new_time_atk=pygame.time.get_ticks()
                                                            P1_cooldown_atk=True
                                                        else:
                                                            if P1_UP:
                                                                P1_anim=11
                                                            else:
                                                                P1_anim=10       
                                                elif (P1_UP or P1_in_anim==4.0) and not P1_in_anim==4.1 and not P1_in_anim==4.2:
                                                    if not P1_in_anim==4.0:
                                                        P1_y=P1_y-56*ratio
                                                        P1_new_time=pygame.time.get_ticks()
                                                        P1_in_anim=4.0
                                                        P1_anim=9
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P1_in_anim==4.0:
                                                        P1_timer=pygame.time.get_ticks()-P1_new_time
                                                        if P1_timer>150:
                                                            P1_in_anim=""
                                                            P1_anim=3
                                                            P1_y=P1_y+56*ratio
                                                            P1_new_time_atk=pygame.time.get_ticks()
                                                            P1_cooldown_atk=True
                                                        else:
                                                            P1_anim=9
                                                else:
                                                    if not P1_direction and not P1_in_anim==4.2 and not P1_x+P1[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        P1_new_time=pygame.time.get_ticks()
                                                        P1_in_anim=4.2
                                                        P1_anim=4
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P1_direction and not P1_in_anim==4.2 and not P1_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and not P1_x+P1[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        if not P1_anim==1:
                                                            P1_x=P1_x-127*ratio
                                                        else:
                                                            P1_x=P1_x-95*ratio
                                                        P1_new_time=pygame.time.get_ticks()
                                                        P1_in_anim=4.2
                                                        P1_anim=4
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P1_in_anim==4.2:
                                                        P1_timer=pygame.time.get_ticks()-P1_new_time
                                                        if P1_timer>150:
                                                            P1_in_anim=""
                                                            if P1_direction:
                                                                if P1_LEFT and not P1_air and not P1_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                                    P1_x=P1_x+95*ratio
                                                                    P1_anim=1
                                                                
                                                                else:
                                                                    P1_x=P1_x+127*ratio
                                                            if P1_air:
                                                                P1_anim=3
                                                            elif P1_RIGHT:
                                                                P1_anim=1
                                                            else:
                                                                P1_anim=0
                                                            P1_new_time_atk=pygame.time.get_ticks()
                                                            P1_cooldown_atk=True
                                                        else:
                                                            P1_anim=4
                                                    if P1_direction_old and not P1_direction and P1_anim==4:
                                                        P1_x=P1_x+126*ratio
                                                    if not P1_direction_old and P1_direction and P1_anim==4:
                                                        P1_x=P1_x-126*ratio
                                        if (P2_ATK or P2_in_anim==4.0 or P2_in_anim==4.1 or P2_in_anim==4.2) and not P2_in_anim==5:
                                            if not P2_cooldown_atk:
                                                if (P2_DOWN or P2_in_anim==4.1) and not P2_in_anim==4.0 and not P2_in_anim==4.2:
                                                    if not P2_in_anim==4.1:
                                                        P2_new_time=pygame.time.get_ticks()
                                                        P2_in_anim=4.1
                                                        if P2_UP:
                                                            P2_anim=11
                                                        else:
                                                            P2_anim=10
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P2_in_anim==4.1:
                                                        P2_timer=pygame.time.get_ticks()-P2_new_time
                                                        if P2_timer>150:
                                                            P2_in_anim=""
                                                            P2_anim=3
                                                            P2_new_time_atk=pygame.time.get_ticks()
                                                            P2_cooldown_atk=True
                                                        else:
                                                            if P2_UP:
                                                                P2_anim=11
                                                            else:
                                                                P2_anim=10       
                                                elif (P2_UP or P2_in_anim==4.0) and not P2_in_anim==4.1 and not P2_in_anim==4.2:
                                                    if not P2_in_anim==4.0:
                                                        P2_y=P2_y-56*ratio
                                                        P2_new_time=pygame.time.get_ticks()
                                                        P2_in_anim=4.0
                                                        P2_anim=9
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P2_in_anim==4.0:
                                                        P2_timer=pygame.time.get_ticks()-P2_new_time
                                                        if P2_timer>150:
                                                            P2_in_anim=""
                                                            P2_anim=3
                                                            P2_y=P2_y+56*ratio
                                                            P2_new_time_atk=pygame.time.get_ticks()
                                                            P2_cooldown_atk=True
                                                        else:
                                                            P2_anim=9
                                                else:
                                                    if not P2_direction and not P2_in_anim==4.2 and not P2_x+P2[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        P2_new_time=pygame.time.get_ticks()
                                                        P2_in_anim=4.2
                                                        P2_anim=4
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P2_direction and not P2_in_anim==4.2 and not P2_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and not P2_x+P2[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        if not P2_anim==1:
                                                            P2_x=P2_x-127*ratio
                                                        else:
                                                            P2_x=P2_x-95*ratio
                                                        P2_new_time=pygame.time.get_ticks()
                                                        P2_in_anim=4.2
                                                        P2_anim=4
                                                        sound_punch.set_volume(round(sound/100,2))
                                                        sound_punch.play()
                                                    elif P2_in_anim==4.2:
                                                        P2_timer=pygame.time.get_ticks()-P2_new_time
                                                        if P2_timer>150:
                                                            P2_in_anim=""
                                                            if P2_direction:
                                                                if P2_LEFT and not P2_air and not P2_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)):
                                                                    P2_x=P2_x+95*ratio
                                                                    P2_anim=1
                                                                
                                                                else:
                                                                    P2_x=P2_x+127*ratio
                                                            if P2_air:
                                                                P2_anim=3
                                                            elif P2_RIGHT:
                                                                P2_anim=1
                                                            else:
                                                                P2_anim=0
                                                            P2_new_time_atk=pygame.time.get_ticks()
                                                            P2_cooldown_atk=True
                                                        else:
                                                            P2_anim=4
                                                    if P2_direction_old and not P2_direction and P2_anim==4:
                                                        P2_x=P2_x+126*ratio
                                                    if not P2_direction_old and P2_direction and P2_anim==4:
                                                        P2_x=P2_x-126*ratio
                                        if P1_SPE and P1_SP>=20 or P1_in_anim==5:
                                            if not P1_cooldown_spe:
                                                if not P1_SP==P1_SPmax:
                                                    if not P1_direction and not P1_in_anim==5 and not P1_x+P1[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        P1_y=P1_y-24*ratio
                                                        P1_new_time=pygame.time.get_ticks()
                                                        P1_in_anim=5
                                                        P1_anim=5
                                                    elif P1_direction and not P1_in_anim==5 and not P1_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and not P1_x+P1[0][0].get_width()-158*ratio>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        if not P1_anim==1:
                                                            P1_x=P1_x-103*ratio
                                                        else:
                                                            P1_x=P1_x-71*ratio
                                                        P1_y=P1_y-24*ratio
                                                        P1_new_time=pygame.time.get_ticks()
                                                        P1_in_anim=5
                                                        P1_anim=5
                                                    elif P1_in_anim==5:
                                                        P1_timer=pygame.time.get_ticks()-P1_new_time
                                                        P1_anim_old=P1_anim
                                                        if P1_timer>=150 and P1_timer<300:
                                                            P1_anim=6
                                                        elif P1_timer>=300 and P1_timer<450:
                                                            P1_anim=5
                                                        elif P1_timer>=450:
                                                            P1_y=P1_y+24*ratio
                                                            P1_in_anim=""
                                                            if P1_direction:
                                                                if P1_LEFT:
                                                                    P1_x=P1_x+71*ratio
                                                                else:
                                                                    P1_x=P1_x+103*ratio
                                                            if P1_RIGHT or P1_LEFT:
                                                                P1_anim=1
                                                            else:
                                                                P1_anim=0
                                                            P1_new_time_spe=pygame.time.get_ticks()
                                                            P1_cooldown_spe=True
                                                        else:
                                                            P1_anim=5
                                                        if P1_anim_old==6 and P1_anim==5:
                                                            if P1_direction:
                                                               P1_x=P1_x+55*ratio
                                                            P1_SP=P1_SP-20
                                                            if P1_SP<0:
                                                                P1_SP=0
                                                        elif P1_anim_old==5 and P1_anim==6:
                                                            if P1_direction:
                                                                P1_x=P1_x-55*ratio
                                                                P1_bullet.append(P1_x)
                                                            else:
                                                                P1_bullet.append(P1_x+P1[6][0].get_width())
                                                            P1_bullet.append(P1_direction)
                                                else:
                                                    P1_SP=0
                                                    P1_ult=True
                                                    P1_ult_new_time=pygame.time.get_ticks()             
                                        if P2_SPE and P2_SP>=20 or P2_in_anim==5:
                                            if not P2_cooldown_spe:
                                                if not P2_SP==P2_SPmax:
                                                    if not P2_direction and not P2_in_anim==5 and not P2_x+P2[0][0].get_width()>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        P2_y=P2_y-24*ratio
                                                        P2_new_time=pygame.time.get_ticks()
                                                        P2_in_anim=5
                                                        P2_anim=5
                                                    elif P2_direction and not P2_in_anim==5 and not P2_x<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and not P2_x+P2[0][0].get_width()-158*ratio>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)):
                                                        if not P2_anim==1:
                                                            P2_x=P2_x-103*ratio
                                                        else:
                                                            P2_x=P2_x-71*ratio
                                                        P2_y=P2_y-24*ratio
                                                        P2_new_time=pygame.time.get_ticks()
                                                        P2_in_anim=5
                                                        P2_anim=5
                                                    elif P2_in_anim==5:
                                                        P2_timer=pygame.time.get_ticks()-P2_new_time
                                                        P2_anim_old=P2_anim
                                                        if P2_timer>=150 and P2_timer<300:
                                                            P2_anim=6
                                                        elif P2_timer>=300 and P2_timer<450:
                                                            P2_anim=5
                                                        elif P2_timer>=450:
                                                            P2_y=P2_y+24*ratio
                                                            P2_in_anim=""
                                                            if P2_direction:
                                                                if P2_LEFT:
                                                                    P2_x=P2_x+71*ratio
                                                                else:
                                                                    P2_x=P2_x+103*ratio
                                                            if P2_RIGHT or P2_LEFT:
                                                                P2_anim=1
                                                            else:
                                                                P2_anim=0
                                                            P2_new_time_spe=pygame.time.get_ticks()
                                                            P2_cooldown_spe=True
                                                        else:
                                                            P2_anim=5
                                                        if P2_anim_old==6 and P2_anim==5:
                                                            if P2_direction:
                                                               P2_x=P2_x+55*ratio
                                                            P2_SP=P2_SP-20
                                                            if P2_SP<0:
                                                                P2_SP=0
                                                        elif P2_anim_old==5 and P2_anim==6:
                                                            if P2_direction:
                                                                P2_x=P2_x-55*ratio
                                                                P2_bullet.append(P2_x)
                                                            else:
                                                                P2_bullet.append(P2_x+P2[6][0].get_width())
                                                            P2_bullet.append(P2_direction)
                                                else:
                                                    P2_SP=0
                                                    P2_ult=True
                                                    P2_ult_new_time=pygame.time.get_ticks()
                                        if P1_in_anim=="" and not P1_UP and not P1_DOWN and not P1_RIGHT and not P1_LEFT and not P1_ATK and not P1_SPE and not P1_SHLD and not P1_MENU and not P1_air:
                                            P1_anim=0
                                        if P2_in_anim=="" and not P2_UP and not P2_DOWN and not P2_RIGHT and not P2_LEFT and not P2_ATK and not P2_SPE and not P2_SHLD and not P2_MENU and not P2_air:
                                            P2_anim=0
                                        P1_timer_atk=pygame.time.get_ticks()-P1_new_time_atk
                                        if P1_timer_atk>1000*P1_cdpunch:
                                            P1_cooldown_atk=False
                                        P2_timer_atk=pygame.time.get_ticks()-P2_new_time_atk
                                        if P2_timer_atk>1000*P2_cdpunch:
                                            P2_cooldown_atk=False
                                        P1_timer_spe=pygame.time.get_ticks()-P1_new_time_spe
                                        if P1_timer_spe>1000*P1_cdshot:
                                            P1_cooldown_spe=False
                                        P2_timer_spe=pygame.time.get_ticks()-P2_new_time_spe
                                        if P2_timer_spe>1000*P2_cdshot:
                                            P2_cooldown_spe=False
                                        P1_timer_ult=pygame.time.get_ticks()-P1_ult_new_time
                                        if P1_timer_ult>3000:
                                            P1_ult=False
                                        P2_timer_ult=pygame.time.get_ticks()-P2_ult_new_time
                                        if P2_timer_ult>3000:
                                            P2_ult=False
                                        if stop_fight:
                                            pygame.event.clear()
                                            break
                                        if P1_y+P1[P1_anim][0].get_height()>=Sol:
                                            P1_air=False
                                            P1_y=Sol-P1[P1_anim][0].get_height()
                                        else:
                                            P1_air=True
                                        if P2_y+P2[P2_anim][0].get_height()>=Sol:
                                            P2_air=False
                                            P2_y=Sol-P2[P2_anim][0].get_height()
                                        else:
                                            P2_air=True
                                        P1_missile_counter=0
                                        for i in range(int(round(len(P1_bullet)/2,0))):
                                            if not P1_bullet[(i-P1_missile_counter)*2]>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)) and not P1_bullet[(i-P1_missile_counter)*2+1] or not P1_bullet[(i-P1_missile_counter)*2]+P1_missile[0].get_width()<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and P1_bullet[(i-P1_missile_counter)*2+1]:
                                                if P1_bullet[(i-P1_missile_counter)*2+1]:
                                                    P1_bullet[(i-P1_missile_counter)*2]=P1_bullet[(i-P1_missile_counter)*2]-(2*ratio*(344*ratio/P1_missile[0].get_width()))
                                                else:
                                                    P1_bullet[(i-P1_missile_counter)*2]=P1_bullet[(i-P1_missile_counter)*2]+(2*ratio*(344*ratio/P1_missile[0].get_width()))
                                                screen.blit(pygame.transform.flip(P1_missile[0],P1_bullet[(i-P1_missile_counter)*2+1],False),(P1_bullet[(i-P1_missile_counter)*2],int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                            else:
                                                del(P1_bullet[(i-P1_missile_counter)*2])
                                                del(P1_bullet[(i-P1_missile_counter)*2])
                                                P1_missile_counter=P1_missile_counter+1
                                        screen.blit(pygame.transform.flip(P1[P1_anim][0],P1_direction,False),(int(P1_x),int(P1_y)))
                                        if P1_in_anim==4.0:
                                            P1_hity=P1_y-P1_hit[1][0].get_height()
                                            if P1_direction:
                                                P1_hitx=P1_x+1*ratio
                                            else:
                                                P1_hitx=P1_x+200*ratio
                                            P1_hit_rect=P1_hit[1][0].get_rect()
                                            P1_hit_rect=P1_hit_rect.move(int(P1_hitx),int(P1_hity))
                                            screen.blit(pygame.transform.flip(P1_hit[1][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                        if P1_in_anim==4.1:
                                            P1_hity=P1_y+P1[3][0].get_height()
                                            if P1_direction:
                                                P1_hitx=P1_x+118*ratio
                                            else:
                                                P1_hitx=P1_x+108*ratio
                                            P1_hit_rect=P1_hit[2][0].get_rect()
                                            P1_hit_rect=P1_hit_rect.move(int(P1_hitx),int(P1_hity))
                                            screen.blit(pygame.transform.flip(P1_hit[2][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                        elif P1_in_anim==4.2:
                                            if not P1_direction:
                                                P1_hitx=P1_x+P1[4][0].get_width()
                                            else:
                                                P1_hitx=P1_x-P1_hit[0][0].get_width()
                                            P1_hity=P1_y+65*ratio
                                            P1_hit_rect=P1_hit[0][0].get_rect()
                                            P1_hit_rect=P1_hit_rect.move(int(P1_hitx),int(P1_hity))
                                            screen.blit(pygame.transform.flip(P1_hit[0][0],P1_direction,False),(int(P1_hitx),int(P1_hity)))
                                        P2_missile_counter=0
                                        for i in range(int(round(len(P2_bullet)/2,0))):
                                            if not P2_bullet[(i-P2_missile_counter)*2]>int(round(1920*ratio+(screen_width-1920*ratio)/2,0)) and not P2_bullet[(i-P2_missile_counter)*2+1] or not P2_bullet[(i-P2_missile_counter)*2]+P2_missile[0].get_width()<int(round(0*ratio+(screen_width-1920*ratio)/2,0)) and P2_bullet[(i-P2_missile_counter)*2+1]:
                                                if P2_bullet[(i-P2_missile_counter)*2+1]:
                                                    P2_bullet[(i-P2_missile_counter)*2]=P2_bullet[(i-P2_missile_counter)*2]-(2*ratio*(344*ratio/P2_missile[0].get_width()))
                                                else:
                                                    P2_bullet[(i-P2_missile_counter)*2]=P2_bullet[(i-P2_missile_counter)*2]+(2*ratio*(344*ratio/P2_missile[0].get_width()))
                                                screen.blit(pygame.transform.flip(P2_missile[0],P2_bullet[(i-P2_missile_counter)*2+1],False),(int(P2_bullet[(i-P2_missile_counter)*2]),int(round(574*ratio+(screen_height-1080*ratio)/2,0))))
                                            else:
                                                del(P2_bullet[(i-P2_missile_counter)*2])
                                                del(P2_bullet[(i-P2_missile_counter)*2])
                                                P2_missile_counter=P2_missile_counter+1
                                        screen.blit(pygame.transform.flip(P2[P2_anim][0],P2_direction,False),(int(P2_x),int(P2_y)))
                                        if P2_in_anim==4.0:
                                            P2_hity=P2_y-P2_hit[1][0].get_height()
                                            if P2_direction:
                                                P2_hitx=P2_x+1*ratio
                                            else:
                                                P2_hitx=P2_x+200*ratio
                                            P2_hit_rect=P2_hit[1][0].get_rect()
                                            P2_hit_rect=P2_hit_rect.move(int(P2_hitx),int(P2_hit))
                                            screen.blit(pygame.transform.flip(P2_hit[1][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                        if P2_in_anim==4.1:
                                            P2_hity=P2_y+P2[3][0].get_height()
                                            if P2_direction:
                                                P2_hitx=P2_x+118*ratio
                                            else:
                                                P2_hitx=P2_x+108*ratio
                                            P2_hit_rect=P2_hit[2][0].get_rect()
                                            P2_hit_rect=P2_hit_rect.move(int(P2_hitx),int(P2_hit))
                                            screen.blit(pygame.transform.flip(P2_hit[2][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                        elif P2_in_anim==4.2:
                                            if not P2_direction:
                                                P2_hitx=P2_x+P2[4][0].get_width()
                                            else:
                                                P2_hitx=P2_x-P2_hit[0][0].get_width()
                                            P2_hity=P2_y+65*ratio
                                            P2_hit_rect=P2_hit[0][0].get_rect()
                                            P2_hit_rect=P2_hit_rect.move(int(P2_hitx),int(P2_hit))
                                            screen.blit(pygame.transform.flip(P2_hit[0][0],P2_direction,False),(int(P2_hitx),int(P2_hity)))
                                        screen.blit(background_map_fight2_adjust[0],(background_map_fight2_adjust[1],background_map_fight2_adjust[2]))
                                        Player_bar(P1_HPmax,P1_HP,P1_SPmax,P1_SP,1)
                                        Player_bar(P2_HPmax,P2_HP,P2_SPmax,P2_SP,2)
                                        if P1_ult:
                                            txt_surface=P1_font.render(P1_sentence1, True, color)
                                            txt_surface2=P1_font.render(P1_sentence2, True, color)
                                            screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(99*ratio+(screen_height-1080*ratio)/2,0))))
                                            screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(299*ratio+(screen_height-1080*ratio)/2,0))))
                                        if P2_ult:
                                            txt_surface=P2_font.render(P2_sentence1, True, color)
                                            txt_surface2=P2_font.render(P2_sentence2, True, color)
                                            screen.blit(txt_surface,(int((screen_width-txt_surface.get_width())/2),int(round(779*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                            screen.blit(txt_surface2,(int((screen_width-txt_surface2.get_width())/2),int(round(979*ratio-txt_surface2.get_height()+(screen_height-1080*ratio)/2,0))))
                                        pygame.display.update()
                                    old_axis=""
                                    old_action=4
                                    number=-1
                                    new_time=0
                                    old_axis2=""
                                    old_action2=4
                                    number2=-1
                                    new_time2=0
                                    pygame.mouse.set_visible(True)
                                    pygame.mixer.music.load("./audio/music/menu.ogg")
                                    pygame.mixer.music.play(-1)
                                if key==2 or stop_fight:
                                    stop_fight=True
                                    pygame.event.clear()
                                    break
                                map_button(button_map,background_map_adjust,False)
                                pygame.display.update()
                        if key_fighters==2 or stop_fight:
                            pygame.event.clear()
                            break
                    P1_validate=False
                    P2_validate=False
                    background_fighters_adjust=image_adjust("graphic/background/Combattants",0,0)
                    screen.blit(background_fighters_adjust[0],(background_fighters_adjust[1],background_fighters_adjust[2]))
                fighters_button(P1_select,P2_select,background_fighters_adjust)
                pygame.display.update()
            pygame.event.clear()
            screen.fill(pygame.Color("black"))
            screen.blit(background[0],(background[1],background[2]))
        elif button==1:
            changing_list=menu_option(old_axis,screen_width,screen_height,screen_mode,music,sound,UP1,DOWN1,RIGHT1,LEFT1,ATK1,SPE1,SHLD1,MENU1,UP2,DOWN2,RIGHT2,LEFT2,ATK2,SPE2,SHLD2,MENU2)
            old_axis=changing_list[2]
            pygame.event.clear()
            option=open("Option.txt").read()
            if changing_list[1]==1:
                UP1=option.split("|")[10]
                DOWN1=option.split("|")[12]
                RIGHT1=option.split("|")[14]
                LEFT1=option.split("|")[16]
                ATK1=option.split("|")[18]
                SPE1=option.split("|")[20]
                SHLD1=option.split("|")[22]
                MENU1=option.split("|")[24]
                UP2=option.split("|")[26]
                DOWN2=option.split("|")[28]
                RIGHT2=option.split("|")[30]
                LEFT2=option.split("|")[32]
                ATK2=option.split("|")[34]
                SPE2=option.split("|")[36]
                SHLD2=option.split("|")[38]
                MENU2=option.split("|")[40]
            if changing_list[0]>0:
                screen_width=int(option.split("|")[1])
                screen_height=int(option.split("|")[2])
                if changing_list[0]==2:
                    pygame.display.quit()
                    pygame.display.init()
                    pygame.display.set_icon(icon)
                    pygame.display.set_caption("MechaMecha_World_Championship")
                if str(option.lower().split("|")[4])=="fullscreen":
                    screen_mode="Plein écran"
                elif str(option.lower().split("|")[4])=="borderless":
                    screen_mode="Fenêtré sans bordure"
                else:
                    screen_mode="Fenêtré"
                if screen_mode=="Plein écran":
                    screen=pygame.display.set_mode([screen_width,screen_height], pygame.FULLSCREEN)
                elif screen_mode=="Fenêtré sans bordure":
                    screen=pygame.display.set_mode([screen_width,screen_height], pygame.NOFRAME)
                else:
                    screen=pygame.display.set_mode([screen_width,screen_height])

                music=int(option.split("|")[6])
                sound=int(option.split("|")[8])

            button=1
            pygame.mixer.music.set_volume(round(music/100,2))
            screen.fill(pygame.Color("black"))
            background=image_adjust("graphic/background/Menu",0,0)
            screen.blit(background[0],(background[1],background[2]))
            menu_list=menu_button(button,True)
        elif button==2:           #quitter le jeu
            while True:
                pygame.time.wait(1)
                pygame.time.Clock().tick(60)
                pygame.time.wait(400)
                break
            sys.exit(37)
    menu_button(button,False)
    pygame.display.update()
