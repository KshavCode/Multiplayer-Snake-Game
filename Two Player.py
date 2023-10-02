import pygame 
import random
import os


x = pygame.init()
pygame.mixer.init()
snah, snaw = 25, 25
snahh, snaww = 25, 25

pygame.font.get_fonts()
font = pygame.font.SysFont('arialblue', 60)

def tex(text, greenor, x, y) : 
    screen_text = font.render(text, True, greenor)
    win.blit(screen_text, [x,y])


def plot(win, greenor, snake1_list, snah) :
    for x,y in snake1_list : 
        pygame.draw.rect(win, greenor, [x, y, snaw, snah])

win = pygame.display.set_mode((1350,750), pygame.FULLSCREEN)
pygame.display.set_caption("Something, I don't know")
pygame.display.update()
clock = pygame.time.Clock()
bg = pygame.image.load("vs1.jpg")
bg = pygame.transform.scale(bg, (3500, 3700)).convert_alpha()
start = pygame.image.load("start.png")
start = pygame.transform.scale(start, (620,70)).convert_alpha()
start2 = pygame.image.load("loadvs.png")
start2 = pygame.transform.scale(start2, (800, 80))
p1r = pygame.image.load("p1.png")
p1r = pygame.transform.scale(p1r, (500, 60))
p2r = pygame.image.load("p2.png")
p2r = pygame.transform.scale(p2r, (500, 60))

def loadscreen() : 
    exit_game = False 
    pygame.mixer.music.load("game sound2.mp3")
    pygame.mixer.music.play()
    p1 = False
    p2 = False
    while not exit_game : 
        win.fill((0, 255, 0))
        win.blit(bg, (0,0))
        win.blit(start, (370, 450))
        win.blit(start2, (290, 330))
        

        if p1 == True : 
            win.blit(p2r, (0, 600))
            pygame.display.update()
        if p2 == True : 
            win.blit(p1r, (800, 600))
            pygame.display.update()
        
        if p1 == True and p2 == True : 
            exit_game = True
            pygame.time.wait(1000)
            gameloop()   
             
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_w :  
                    p1 = True 
                if event.key == pygame.K_UP : 
                    p2 = True
                if event.key == pygame.K_ESCAPE : 
                    quit()
                         
        pygame.display.update()
        clock.tick(60)

def gameloop() : 
    bground =  (0, 14, 22)
    blue = (117, 230, 247)
    snax, snay = 1200, 400
    snaxx, snayy = 100, 400
    velx = 0 
    vely = 0
    velxx = 0 
    velyy = 0
    foodx = random.randint(0, 1300)
    foody = random.randint(50, 700)
    foodimg = pygame.image.load("apple.png")
    foodimg = pygame.transform.scale(foodimg, (25, 25)).convert_alpha()
    score1 = 0 
    score2 = 0
    exit_game = False 
    game_over = False 
    snake1_list = []
    snake1_length = 1
    snake2_list = [100]
    snake2_length = 1
    winner = None
    
    pygame.mixer.music.load("ingame music2.mp3")
    pygame.mixer.music.play()
    
    if(not os.path.exists("hhighscore.txt")) : 
      with open("hhighscore.txt", "w") as b : 
        b.write("0")
    with open("hhighscore.txt", "r") as f :
        high = f.read()
    
    while not exit_game :
        if game_over : 
            win.fill((25,0,51))
            gover = pygame.image.load("over.png")
            gover = pygame.transform.scale(gover, (650,90)).convert_alpha()
            win.blit(gover, (320,100))
            tex(f"{winner} wins!", (153, 255, 255), 300, 300)
            tex(f"Player 1 score (arrow) : {score1}", (204,204,255), 300, 400)
            tex(f"Player 2 score (wasd) : {score2}", (204,204,255), 300, 450)
            tex("Press Enter to restart", (255,255,204), 450, 600)
            tex("Press Esc to quit", (255,255,204), 450, 650)
            with open("hhighscore.txt", "w") as t: 
                t.write(str(high))     
            
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_RETURN : 
                        gameloop()
                        
                    if event.key == pygame.K_ESCAPE : 
                        quit()
        else : 
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_ESCAPE : 
                        quit()

                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_d : 
                        velxx = 5
                        velyy = 0
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_a : 
                        velxx = -5
                        velyy = 0 
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_w : 
                        velyy = -5
                        velxx = 0 
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_s : 
                        velyy = 5 
                        velxx = 0
        
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_RIGHT : 
                        velx = 5
                        vely = 0 
                    if event.key == pygame.K_LEFT : 
                        velx = -5
                        vely = 0  
                    if event.key == pygame.K_UP : 
                        vely = -5
                        velx = 0 
                    if event.key == pygame.K_DOWN : 
                        vely = 5 
                        velx = 0
        
            snax = snax + velx 
            snay = snay + vely  
            snaxx = snaxx + velxx
            snayy = snayy + velyy
            
            if abs(snax - foodx) < 25 and abs(snay - foody) < 25 : 
                score1 += 1 
                foodx = random.randint(0, 900)
                foody = random.randint(0,700)
                snake1_length += 5
            if abs(snaxx - foodx) < 25 and abs(snayy - foody) < 25 : 
                score2 += 1 
                foodx = random.randint(30, 900)
                foody = random.randint(30,700)
                snake2_length += 5

            win.fill(bground)
            win.blit(foodimg, (foodx, foody))
            tex(f"Score = {score2}", (192, 186, 204), 20, 10)
            tex(f"Score = {score1}", blue, 1120,10)
            tex(f"High Score = {high}", (250, 228, 91), 510, 15)
            if int(high) < score1 : 
                high = score1
            elif int(high) < score2 : 
                high = score2

            head = []
            head.append(snax)
            head.append(snay)    
            snake1_list.append(head)
            
            head2 = []
            head2.append(snaxx)
            head2.append(snayy)    
            snake2_list.append(head2)

            if len(snake1_list) > snake1_length : 
                del snake1_list[0]
            if len(snake2_list) > snake2_length : 
                del snake2_list[0]

            if snax < 0 : 
                snax = 1350
            elif snax > 1350 : 
                snax = 0
            if snay > 750 : 
                snay = 0 
            elif snay < 0 : 
                snay = 750
            
            if snaxx < 0 : 
                snaxx = 1350
            elif snaxx > 1350 : 
                snaxx = 0
            if snayy > 750 : 
                snayy = 0 
            elif snayy < 0 : 
                snayy = 750

            
            if head2 in snake1_list[:-1] :
                game_over = True
                winner = "Player 1"
            if head in snake2_list[:-1] : 
                game_over = True
                winner = "Player 2"
            
            plot(win, blue, snake1_list, snah)
            plot(win, (192, 186, 204), snake2_list, snahh)

        pygame.display.update()
        clock.tick(60)
    
    
    
    
loadscreen()
    
    
    