import pygame
pygame.init()
import math
from random import randint
import sys
# Zaheer
# January 6th, 2020
# Link's Boss Fight

# Making the screen dimensions
WIDTH = 820
HEIGHT = 760

# Loading the main background
BACKGROUND = pygame.image.load("Arena.png")
BACKGROUND2 = pygame.image.load("Arena2.png")
BACKGROUND3 = pygame.image.load("Arena3.png")
background = BACKGROUND

# Making all the colors that will be used
in_game_color = (24,8,130)
END_TEXT_COLOR = (230,214,0)
WIN_COLOR = (252,219,3)
secret = False
shield = False

# Making booleans for pausing and replaying
pause = False
replay = True

# Allowing the user to re-run the program
# After they win or lose
while replay == True:
    
    # All of link's different images
    link = pygame.image.load("link_right.png")
    LINK_RIGHT = pygame.image.load("link_right.png")
    LINK_LEFT = pygame.image.load("link_left.png")
    LINK_UP = pygame.image.load("link_up.png")
    LINK_DOWN = pygame.image.load("link_down.png")
    LINK_UPRIGHT = pygame.image.load("link_upright.png")
    LINK_UPLEFT = pygame.image.load("link_upleft.png")
    LINK_DOWNRIGHT = pygame.image.load("link_downright.png")
    LINK_DOWNLEFT = pygame.image.load("link_downleft.png")

    # Link shield variables and images
    shieldx = 2000
    shieldy = 2000
    shield_symbol = pygame.image.load("shield_symbol.png")
    SHIELD_BAR = pygame.image.load("shield_bar.png")
    SHIELD_BAR2 = pygame.image.load("shield_bar2.png")
    SHIELD_BAR3 = pygame.image.load("shield_bar3.png")
    SHIELD_BAR4 = pygame.image.load("shield_bar4.png")
    SHIELD_BAR5 = pygame.image.load("shield_bar5.png")
    SHIELD_BAR6 = pygame.image.load("shield_bar6.png")
    shield_bar = SHIELD_BAR
    SHIELD_RIGHT = pygame.image.load("shield_right.png")
    SHIELD_LEFT = pygame.image.load("shield_left.png")
    SHIELD_DOWN = pygame.image.load("shield_down.png")
    SHIELD_UP = pygame.image.load("shield.png")
    SHIELD_UPRIGHT = pygame.image.load("shield_upright.png")
    SHIELD_UPLEFT = pygame.image.load("shield_upleft.png")
    SHIELD_DOWNRIGHT = pygame.image.load("shield_downright.png")
    SHIELD_DOWNLEFT = pygame.image.load("shield_downleft.png")
    link_shield = SHIELD_UP
    link_shieldRect = link_shield.get_rect()
    
    # Link's x and y speeds
    LINKX_SPEED = 7
    LINKY_SPEED = 7
    
    # Making buffed speeds for when
    # Link consumes speed potion
    BUFFEDX_SPEED = 12
    BUFFEDY_SPEED = 12
    
    # Making the collision detection rectangle
    # For link and declaring his health, start location,
    # And health
    linkRect = link.get_rect()
    linkx = 200
    linky = 400
    linkx_speed = LINKX_SPEED 
    linky_speed = LINKY_SPEED 
    link_health = 10

    # Loading potions
    health_potion = pygame.image.load("red_potion.png")
    speed_potion = pygame.image.load("green_potion.png")
    damage_potion = pygame.image.load("yellow_potion.png")
    shield_potion = pygame.image.load("blue_potion.png")

    # Giving potions a location
    healthx = 180
    healthy = 450
    speedx = 380
    speedy = 455
    damagex = 580
    damagey = 460
    bluex = 380
    bluey = 550
    
    # Making potion collision detection rectangles
    health_potionRect = health_potion.get_rect()
    speed_potionRect = speed_potion.get_rect()
    damage_potionRect = damage_potion.get_rect()
    shield_potionRect = shield_potion.get_rect()
    # Loading win and lose pictures
    win_picture = pygame.image.load("happy_win1.png")
    lose_picture = pygame.image.load("defeated link1.png")

    # Loading the pause overlay
    pause_overlay = pygame.image.load("pause.png")

    # All Sword Variables
    sword = pygame.image.load("link_up_sword.png")
    swordx = -1000
    swordy = -1000
    attack = False
    swordRect = sword.get_rect()
    swordW = swordRect.width
    swordH = swordRect.height
    
    # Loading all the sword images
    SWORD_UP = pygame.image.load("link_up_sword.png")
    SWORD_UP_BUFF = pygame.image.load("link_up_sword_buff.png")
    SWORD_DOWN = pygame.image.load("link_down_sword.png")
    SWORD_DOWN_BUFF = pygame.image.load("link_down_sword_buff.png")
    SWORD_LEFT = pygame.image.load("link_left_sword.png")
    SWORD_LEFT_BUFF = pygame.image.load("link_left_sword_buff.png")
    SWORD_RIGHT = pygame.image.load("link_right_sword.png")
    SWORD_RIGHT_BUFF = pygame.image.load("link_right_sword_buff.png")

    # Loading the heart and declaring all heart locations
    heart_image = pygame.image.load("link_heart.png")

    heartx1 = 50
    heartx2 = 90
    heartx3 = 130
    heartx4 = 170
    heartx5 = 210
    heartx6 = 250
    heartx7 = 290
    heartx8 = 330
    heartx9 = 370
    heartx10 = 410
    hearty = 3

    # Enemy Variables
    Ganondorf = pygame.image.load("enemy.png")
    ganonx = 340
    ganony = 120
    ganon_health = 20

    # Loading all boss health bar images
    barx = 190
    boss_bar = pygame.image.load("boss_bar.png")
    BOSS_BAR1 = pygame.image.load("boss_bar1.png")
    BOSS_BAR2 = pygame.image.load("boss_bar2.png")
    BOSS_BAR3 = pygame.image.load("boss_bar3.png")
    BOSS_BAR4 = pygame.image.load("boss_bar4.png")
    BOSS_BAR5 = pygame.image.load("boss_bar5.png")
    BOSS_BAR6 = pygame.image.load("boss_bar6.png")
    BOSS_BAR7 = pygame.image.load("boss_bar7.png")
    BOSS_BAR8 = pygame.image.load("boss_bar8.png")
    BOSS_BAR9 = pygame.image.load("boss_bar9.png")
    BOSS_BAR10 = pygame.image.load("boss_bar10.png")
    BOSS_BAR11 = pygame.image.load("boss_bar11.png")
    BOSS_BAR12 = pygame.image.load("boss_bar12.png")
    BOSS_BAR13 = pygame.image.load("boss_bar13.png")
    BOSS_BAR14 = pygame.image.load("boss_bar14.png")
    BOSS_BAR15 = pygame.image.load("boss_bar15.png")
    BOSS_BAR16 = pygame.image.load("boss_bar16.png")
    BOSS_BAR17 = pygame.image.load("boss_bar17.png")
    BOSS_BAR18 = pygame.image.load("boss_bar18.png")
    BOSS_BAR19 = pygame.image.load("boss_bar19.png")
    BOSS_BAR20 = pygame.image.load("boss_bar20.png")

    # Making the enemy collision detection rectangle
    ganonRect = Ganondorf.get_rect()

    # Making all the Fireball variables
    fireball = pygame.image.load("fireball.png")
    firex = -1000
    firey = -1000
    active = False
    fireRect = fireball.get_rect()
    fireH = fireRect.height
    fireW = fireRect.width
    FIREBALL_SPEED = 15

    # Loading all the different texts that will be used
    game_over = pygame.image.load("game over.png")
    congratulations = pygame.image.load("congratulations.png")
    defeated = pygame.image.load("defeated.png")
    ganondorf_word = pygame.image.load("ganondorf.png")
    rerun = pygame.image.load("re-run_text.png")

    # Allowing the start screen to function
    inPlay = False
    
    # Loading the starting screen
    starting_screen = pygame.image.load("starting_screen.png")

    #----------------------Starting The Game-----------------------------#

    # Creating the starting screen
    while inPlay == False:
        
        # Getting rid of buffs from previous games
        shield_health = 5
        damage_buff = False
        secret = False
        pause = False
        # Making the background the main arena
        background = BACKGROUND
        
        # Playing the music
        pygame.mixer.music.load("zelda.mp3")
        pygame.mixer.music.play(-1)
        pygame.event.get()
        keys = pygame.key.get_pressed()
        game_window = pygame.display.set_mode((WIDTH,HEIGHT))
        game_window.blit(starting_screen,(0,0))

        # Starting the game if the user presses SPACE
        if keys[pygame.K_SPACE] and inPlay == False:
            inPlay = True
        pygame.display.flip()
        
    # Starting the infinite loop with everything
    while inPlay == True:
        
        # Getting keyboard input
        pygame.event.get()
        keys = pygame.key.get_pressed()

        # Making the character move when the arrow keys
        # Are clicked and making boundaries for the enemy
        if keys[pygame.K_LEFT]:
            linkx = linkx - linkx_speed
            link = LINK_LEFT
            if linkx<480 and linky<280 and linkx>400 and (background == BACKGROUND or background == BACKGROUND2):
                linkx = 480
           
        if keys[pygame.K_RIGHT]:
            linkx = linkx + linkx_speed
            link = LINK_RIGHT
            if linkx>280 and linky<280 and linkx<400 and (background == BACKGROUND or background == BACKGROUND2):
                linkx = 280
            
        if keys[pygame.K_UP]:
            linky = linky - linky_speed
            link = LINK_UP
            if linky<299 and linkx>317 and linkx<460 and (background == BACKGROUND or background == BACKGROUND2):
                linky = 300

        # Changing Link's orientation if he goes diagonal
        if keys[pygame.K_DOWN]:
            linky = linky + linky_speed
            link = LINK_DOWN
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            link = LINK_UPRIGHT
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            link = LINK_DOWNRIGHT
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            link = LINK_UPLEFT
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            link = LINK_DOWNLEFT

        # Arena Boundaries
        if linkx >639:
            linkx = 640
        if linkx <107:
            linkx = 108 
        if linky < 67 and secret == False:
            linky = 68
        if linky > 564 and secret == False:
            linky = 565
            
        # Creating collision rectangles for link and ganondorf
        linkRect = pygame.Rect(linkx + 10,linky,40,50)
        ganonRect = pygame.Rect(ganonx,ganony,70,100)

        # Making the fireball able to come onscreen and Rach the player
        if active == False:
            
            # Making the fireball shoot from the enemy's hand
            firex = ganonx + 50
            firey = ganony - 5
            
            # Finding the rise and the run to find the hypotenuse
            slope_run = linkx - firex
            slope_rise = linky - firey
            
            # Calculating the hypotenuse with the rise and run so the fireball
            # Can reach the character
            hypotenuse = math.sqrt(slope_run**2 + slope_rise**2)
            firex_speed = slope_run/hypotenuse*FIREBALL_SPEED
            firey_speed = slope_rise/hypotenuse*FIREBALL_SPEED
            active = True
            
        # Making the collision rectangle for the fireball and
        # Adding the x and y speeds to the fireball
        if active == True:
            firex = firex + firex_speed
            firey = firey + firey_speed
            fireRect = pygame.Rect(int(firex),int(firey),fireW,fireH)
           
            
        # Making link lose a heart if link gets hit with a fireball and
        # Making the fireball get sent again
        if fireRect.colliderect(linkRect):
            link_health = link_health - 1
            active = False
        
        # Getting the fireball to start being fired again once off-screen
        elif firex<=0 or firex>=WIDTH or firey <=0 or firey>= HEIGHT:
            active = False


    #-------------------------- Link attack features-------------------------------------#
        # Creating the collision detection rectangle
        # For Link's sword
        swordRect = pygame.Rect(swordx,swordy,swordW,swordH)
        link_shieldRect = pygame.Rect(shieldx,shieldy,70,50)
        if attack == False:
            swordx = -1000
            swordy = -1000
        if shield == False:
            shieldx = 2000
            shieldy = 2000
            
        # Making the sword appear in different directions
        # Based on what the user clicks (WASD)
        if keys[pygame.K_w]:
            sword = SWORD_UP
            swordx = linkx - 19
            swordy = linky - 160
            link = LINK_UP
            attack  = True
            if damage_buff == True:
                sword = SWORD_UP_BUFF
        if keys[pygame.K_a]:
            sword = SWORD_LEFT
            swordx = linkx - 150
            swordy = linky
            link = LINK_LEFT
            attack  = True
            if damage_buff == True:
                sword = SWORD_LEFT_BUFF
        if keys[pygame.K_d]:
            sword = SWORD_RIGHT
            swordx = linkx + 40
            swordy = linky
            link = LINK_RIGHT
            attack  = True
            if damage_buff == True:
                sword = SWORD_RIGHT_BUFF
        if keys[pygame.K_s]:
            sword = SWORD_DOWN
            swordx = linkx + 14
            swordy = linky + 60
            link = LINK_DOWN
            attack  = True
            if damage_buff == True:
                sword = SWORD_DOWN_BUFF
                
        # Making the shield appear if the user clicks 'f'
        if keys[pygame.K_f] and shield_health>0 and pause == False:
            shield = True
            
            # Making the shield face where Link is facing
            if link == LINK_UP:
                link_shield = SHIELD_UP
                shieldx = linkx - 30
                shieldy = linky - 40
            if link == LINK_RIGHT:
                link_shield = SHIELD_RIGHT
                shieldx = linkx + 60
                shieldy = linky - 20
            if link == LINK_LEFT:
                link_shield = SHIELD_LEFT
                shieldx = linkx - 30
                shieldy = linky - 20
            if link == LINK_DOWN:
                link_shield = SHIELD_DOWN
                shieldy = linky + 70
                shieldx = linkx - 20
            if link == LINK_UPRIGHT:
                link_shield = SHIELD_UPRIGHT
                shieldx = linkx + 30
                shieldy = linky - 40
            if link == LINK_UPLEFT:
                link_shield = SHIELD_UPLEFT
                shieldx = linkx - 50
                shieldy = linky - 40
            if link == LINK_DOWNRIGHT:
                link_shield = SHIELD_DOWNRIGHT
                shieldx = linkx + 20
                shieldy = linky + 20
            if link == LINK_DOWNLEFT:
                link_shield = SHIELD_DOWNLEFT
                shieldx = linkx - 40
                shieldy = linky + 30
            
        # Making the shield take hits from the fireballs
        # Rather than Link taking the damage
        if link_shieldRect.colliderect(fireRect):
            shield_health = shield_health - 1
            active = False
            
        # Making the shield "break" once it runs
        # out of durability
        if shield_health == 0:
            shieldx = 3000
            shield_bar = SHIELD_BAR6
        if shield == True:
            shield = False
            
        # Making the sword not appear if
        # WASD are not clicked
        if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s]:
            attack = False
            
        # Allowing the attack to be reset
        if attack == True:
            attack = False

        # Making the enemy lose health if the player attacks him
        # And teleporting the character on a random location
        # After hitting the enemy (to get rid of spamming)
        if swordRect.colliderect(ganonRect) and damage_buff == False:
            ganon_health = ganon_health - 1
            attack = False
            swordx = -1000
            linky = randint(450,600)
            linkx = randint(200,600)
        # Making the sword do double damage if
        # Damage potion is consumed
        if swordRect.colliderect(ganonRect) and damage_buff == True:
             ganon_health = ganon_health - 2
             attack = False
             swordx = -1000
             linky = randint(450,600)
             linkx = randint(200,600)

        # Loading and playing the victory music if
        # You defeat the enemy with more than 1 heart
        if ganon_health <=2 and ganon_health>0:
            pygame.mixer.music.load("victory.mp3")
            pygame.mixer.music.play(0)


        # Changing the shield health bar
        # After it takes hits from the fireball
        if shield_health == 5:
            shield_bar = SHIELD_BAR
        if shield_health == 4:
            shield_bar = SHIELD_BAR2
        if shield_health == 3:
            shield_bar = SHIELD_BAR3
        if shield_health == 2:
            shield_bar = SHIELD_BAR4
        if shield_health == 1:
            shield_bar = SHIELD_BAR5
        
    #------------------------------------------------------------------------------------#
        # Making the hearts disappear when link gets hit
        if link_health == 10:
            heartx1 = 50
            heartx2 = 90
            heartx3 = 130
            heartx4 = 170
            heartx5 = 210
            heartx6 = 250
            heartx7 = 290
            heartx8 = 330
            heartx9 = 370
            heartx10 = 410
        if link_health == 9:
            heartx10 = -1000
        if link_health == 8:
            heartx9 = -1000
        if link_health == 7:
            heartx8 = -1000
        if link_health == 6:
            heartx7 = -1000
        if link_health == 5:
            heartx6 = -1000
        if link_health == 4:
            heartx5 = -1000
        if link_health == 3:
            heartx4 = -1000
        if link_health == 2:
            heartx3 = -1000
        if link_health == 1:
            heartx2 = -1000
        if link_health == 1:
            heartx2 = -1000
            
            # Loading and playing the death music
            # Once you lose all your hearts
            pygame.mixer.music.load("death.mp3")
            pygame.mixer.music.play(0)

        # Changing the boss bar depending
        # On how much health he has
        if ganon_health == 19:
            boss_bar = BOSS_BAR1
        if ganon_health == 18:
            boss_bar = BOSS_BAR2
        if ganon_health == 17:
            boss_bar = BOSS_BAR3
        if ganon_health == 16:
            boss_bar = BOSS_BAR4
        if ganon_health == 15:
            boss_bar = BOSS_BAR5
        if ganon_health == 14:
            boss_bar = BOSS_BAR6
        if ganon_health == 13:
            boss_bar = BOSS_BAR7
        if ganon_health == 12:
            boss_bar = BOSS_BAR8
        if ganon_health == 11:
            boss_bar = BOSS_BAR9
        if ganon_health == 10:
            boss_bar = BOSS_BAR10
        if ganon_health == 9:
            boss_bar = BOSS_BAR11
        if ganon_health == 8:
            boss_bar = BOSS_BAR12
        if ganon_health == 7:
            boss_bar = BOSS_BAR13
        if ganon_health == 6:
            boss_bar = BOSS_BAR14
        if ganon_health == 5:
            boss_bar = BOSS_BAR15
        if ganon_health == 4:
            boss_bar = BOSS_BAR16
        if ganon_health == 3:
            boss_bar = BOSS_BAR17
        if ganon_health == 2:
            boss_bar = BOSS_BAR18
        if ganon_health == 1:
            boss_bar = BOSS_BAR19
            
        # Drawing background color behind the arena image
        game_window.fill(in_game_color)
        game_window.blit(background,(0,-10,))

        # Making the door open when you hit it with the sword
        if keys[pygame.K_s] and linkx>350 and linkx<400 and linky > 500 and background == BACKGROUND:
            background = BACKGROUND2
            secret = True
            
        # Allowing you to enter another room
        if linky>HEIGHT:
            linky = 50
            background = BACKGROUND3
            ganonx = -1000
            
        # Updating boundaries once the door is open
        if background == BACKGROUND2:
            if linkx < 330 and linky > 570:
                linky = 570
            if linkx > 420 and linky > 570:
                linky = 570
            if linky<100:
                linky = 100
                
        # Making boundaries for the other room and making the potions visible
        # Also, getting rid of the fireballs and boss health bar
        if background == BACKGROUND3:
            firex = -100
            barx = -1000

            # Making all the potions appear once you enter the
            # secret room with collision detection
            game_window.blit(health_potion,(healthx,healthy))
            health_potionRect = pygame.Rect(healthx,healthy,50,50)
            
            game_window.blit(speed_potion,(speedx,speedy))
            speed_potionRect = pygame.Rect(speedx,speedy,50,50)
            
            game_window.blit(damage_potion,(damagex,damagey))
            damage_potionRect = pygame.Rect(damagex,damagey,50,50)

            game_window.blit(shield_potion,(bluex,bluey))
            shield_potionRect = pygame.Rect(bluex,bluey,50,50)

            # Updating boundaries for the new room
            if linky > 564:
                linky = 565
            if linkx<330 and linky<100:
                linky = 100
            if linkx>420 and linky<100:
                linky = 100
                
            # Letting you go back to the main room
            # If you go through the door
            if linky<0:
                linky = 500
                background = BACKGROUND2
                ganonx = 340
                ganony = 120
                barx = 190
                
            # Allowing Link to consume the potions with collision detection
            # Each potion has a special buff
            if linkRect.colliderect(health_potionRect) and keys[pygame.K_SPACE]:
                link_health = 10
                healthx = -1000
                
            # Speed buff potion
            if linkRect.colliderect(speed_potionRect) and keys[pygame.K_SPACE]:
                linkx_speed = BUFFEDX_SPEED
                linky_speed = BUFFEDY_SPEED
                speedx = -1000
                
            # Damage buff potion
            if linkRect.colliderect(damage_potionRect) and keys[pygame.K_SPACE]:
                damage_buff = True
                damagex = -1000
                
            # Shield durability potion
            if linkRect.colliderect(shield_potionRect) and keys[pygame.K_SPACE]:
                shield_health = 5
                bluex = -1000
    
        # Ending the game if link loses all oh his hearts
        if link_health == 0:
            heartx1 = -1000
            linkx = -1000
            linky = -1000
            ganonx = -1000
            shieldx = 3000
            game_window.blit(game_over,(140,150))
            game_window.blit(rerun,(140,550))
            
            # Putting the sword off-screen
            swordx = -1000
            swordy = -1000
            
            # Creating the lose image
            game_window.blit(lose_picture,(200,300))
            
            # Allowing the user to re-run the program if they wish
            # By pressing r
            replay = False
            if keys[pygame.K_r]:
                inPlay = False
                replay = True

        # Ending the game if ganondorf loses all of his health
        if ganon_health <1:
            ganonx = -1000
            linkx = -10000
            shieldx = 3000
            # Creating the win text and re-run text
            game_window.blit(congratulations,(170,125))
            game_window.blit(defeated,(150,175))
            game_window.blit(ganondorf_word,(260,225))
            game_window.blit(rerun,(140,550))
            
            # Putting the sword off-screen
            swordx = -1000
            swordy = -1000
            firex = -1000
            
            # Making the boss bar empty
            boss_bar = BOSS_BAR20
            
            # Creating the win picture
            game_window.blit(win_picture,(270,300))
            
            # Allowing the user to re-run the program if they wish
            # By pressing r
            replay = False
            
            # Allowing the user to restart while paused
            if keys[pygame.K_r]:
                inPlay = False
                replay = True
                
        # Creating all the hearts for Link
        game_window.blit(heart_image,(heartx1,hearty))
        game_window.blit(heart_image,(heartx2,hearty))
        game_window.blit(heart_image,(heartx3,hearty))
        game_window.blit(heart_image,(heartx4,hearty))
        game_window.blit(heart_image,(heartx5,hearty))
        game_window.blit(heart_image,(heartx6,hearty))
        game_window.blit(heart_image,(heartx7,hearty))
        game_window.blit(heart_image,(heartx8,hearty))
        game_window.blit(heart_image,(heartx9,hearty))
        game_window.blit(heart_image,(heartx10,hearty))
        
        # Putting ganondorf and his health bar on the screen
        game_window.blit(Ganondorf,(ganonx,ganony))
        game_window.blit(boss_bar,(barx,45))

        # Making the fireball come on-screen if
        # it is being activated
        if active == True:
            game_window.blit(fireball,(int(firex),int(firey)))
            
        # Creating Link, his sword, his shield, and the shield bar
        game_window.blit(sword,(swordx,swordy))
        game_window.blit(link,(linkx,linky))
        game_window.blit(link_shield,(shieldx,shieldy))
        game_window.blit(shield_bar,(700,200))
        game_window.blit(shield_symbol,(725,130))
        
        # Pause feature
        if keys[pygame.K_ESCAPE]:
            pause = True
            
        if pause == True:
            replay = False
            
            # Allowing the user to re-run
            if keys[pygame.K_r]:
                inPlay = False
                replay = True
            
            # Not allowing Link to move while paused
            linkx_speed = 0
            linky_speed = 0
            
            # Not allowing the sword on-screen while paused
            swordx = -1000
            swordy = -1000
            
            # Stopping the fireball when paused
            firex_speed = 0
            firey_speed = 0
            
            # Creating the pause overlay 
            game_window.blit(pause_overlay,(-20,0))

        # Allowing the user to un-pause the
        # Game by pressing 'p'
        if keys[pygame.K_p]:
            pause = False

            if speedx>0:
                
                # Giving link his speed back
                linkx_speed = LINKX_SPEED 
                linky_speed = LINKY_SPEED
            elif speedx<0:
                linkx_speed = BUFFEDX_SPEED
                linky_speed = BUFFEDY_SPEED
                
            # Giving the fireball it's speed back
            firex_speed = slope_run/hypotenuse*FIREBALL_SPEED
            firey_speed = slope_rise/hypotenuse*FIREBALL_SPEED
        
        # Making a feature so you can leave the game
        # If you press ESCAPE and 'q'
        if keys[pygame.K_ESCAPE] and keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
           
        pygame.display.flip()



































