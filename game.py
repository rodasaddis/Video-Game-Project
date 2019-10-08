#Rodas Addis, rha6aq
#William Mosberg, wkm7fy

import pygame
import gamebox


camera = gamebox.Camera(800,600)
lives = 5

frogger_images = gamebox.load_sprite_sheet(
    'frogger.png',
    8, 12)
frogger = gamebox.from_image(400, 575, frogger_images[0])
game_over = gamebox.from_text(400, 300, "GAME OVER", 150, "red", bold=True)
tick_counter = 0
game_on = False
screen = True
touching = True
log1 = []
center_x = [400, 150, 700]
for i in center_x:
    log = gamebox.from_image(i, 225, 'https://www.trestlewood.com/image/780a/29608/BlogHeadingBoard.png')
    log.width = 120
    log1.append(log)

log2 = []
center_x_2 = [200, 700]
for i in center_x_2:
    log_2 = gamebox.from_image(i, 175, 'https://www.trestlewood.com/image/780a/29608/BlogHeadingBoard.png')
    log_2.width = 120
    log2.append(log_2)


log3 = []
center_x_3 = [200, 700]
for i in center_x_3:
    log_3 = gamebox.from_image(i, 125, 'https://www.trestlewood.com/image/780a/29608/BlogHeadingBoard.png')
    log_3.width = 120
    log3.append(log_3)


log4 = []
center_x_4 = [200, 700]
for i in center_x_4:
    log_4 = gamebox.from_image(i, 75, 'https://www.trestlewood.com/image/780a/29608/BlogHeadingBoard.png')
    log_4.width = 120
    log4.append(log_4)

center_x = [400,150,300,700]
car_lane_one = []
for i in center_x:
    car = gamebox.from_image(i, 525, 'http://www.clker.com/cliparts/z/G/i/D/h/6/brown-car-md.png')
    car.width = 80
    car_lane_one.append(car)

lane_two = [100, 300, 450, 550]
car_lane_two = []
for i in lane_two:
    car_2 =gamebox.from_image(i,475,"https://images.superiorthan.com/posts/large/Duolingo-1w4Dn81480251882.png")
    car_2.width = 75
    car_lane_two.append(car_2)

lane_three = [150, 350, 730]
car_lane_three = []
for i in lane_three:
    car_three = gamebox.from_image(i, 425, "https://i2.wp.com/www.stickpng.com/assets/images/5890d8d0b2cb5b18709ca61f.png")
    car_three.width = 60
    car_lane_three.append(car_three)

lane_four = [200, 550]
car_lane_four = []
for i in lane_four:
    car_four = gamebox.from_image(i, 375, "https://images.superiorthan.com/posts/large/Duolingo-1w4Dn81480251882.png")
    car_four.width = 80
    car_lane_four.append(car_four)

lane_five = [200, 700, 50]
car_lane_five = []
for i in lane_five:
    car_five = gamebox.from_image(i, 325, "https://i2.wp.com/www.stickpng.com/assets/images/5890d8d0b2cb5b18709ca61f.png")
    car_five.width = 60
    car_lane_five.append(car_five)


def start_screen(keys):
    """
    function that displays the star screen
    """
    global game_on, screen

    camera.clear('black')
    camera.draw(gamebox.from_text(400, 100, "FR0GG3R", 100, "green", bold=True))
    camera.draw(gamebox.from_text(400, 150, "Rodas Addis, rha6aq & William Mosberg, wkm7fy", 20, "white", italic=True))
    camera.draw(gamebox.from_text(400, 300, "use the arrow keys to move", 25, "green", italic=True))
    camera.draw(gamebox.from_text(400, 260, "avoid obstacles and keep in mind your frog can't swim", 25, "green", italic=True))
    camera.draw(gamebox.from_text(400, 220, "reach the other side within the time limit! you have 5 lives-- don't try to go off the screen >:)", 25, "green", italic=True))
    camera.draw(gamebox.from_text(400, 340," don't try to go off the screen >:)",25, "green", italic=True))
    camera.draw(gamebox.from_text(400, 400, "PRESS SPACE TO START", 80, "red",bold=True))
    if pygame.K_SPACE in keys:
        screen = False
        game_on = True



def move_frog(keys):
    """
    allows user to move the frog using the arrow keys
    """
    if pygame.K_UP in keys:
        frogger.y -= 50
    if pygame.K_DOWN in keys:
        frogger.y += 50
    if pygame.K_RIGHT in keys:
        frogger.x += 50
    if pygame.K_LEFT in keys:
        frogger.x -= 50
    keys.clear()
lane_position = 50
lane_y = 500

def draw_scenery():
    """
    draws the background screen

    """
    global lane_position, lane_y

    camera.draw(gamebox.from_color(400, 450, "black", 800, 300))
    highway = camera.draw(gamebox.from_color(400, 575, 'sienna', 800, 50))
    camera.draw(gamebox.from_color(400, 275, "sienna", 800, 50))
    water = camera.draw(gamebox.from_color(400, 150, "blue", 800, 200))

def highway_lines():
    """
    makes lines for the highways
    """
    global lane_position, lane_y
    lst = []
    for number in range(0, 800, 50):
        number += 20
        lst.append(number)


    for element in lst:
        camera.draw(gamebox.from_color(element, 500, "white", 30, 5))
        camera.draw(gamebox.from_color(element, 450, "white", 30, 5))
        camera.draw(gamebox.from_color(element, 400, "white", 30, 5))
        camera.draw(gamebox.from_color(element, 350, "white", 30, 5))

def cars():
    """
    draws the cars per the highway lanes
    """
    global car_lane_one, car_lane_two, car_lane_three,car_lane_four, car_lane_five,frogger

    for c in car_lane_one:
        c.x += 7
        camera.draw(c)
        if c.x > 800:
            c.x = 0


    for a in car_lane_two:
        a.x -= 5
        camera.draw(a)
        if a.x < 0:
            a.x = 800

    for r in car_lane_three:
        r.x -= 5
        camera.draw(r)
        if r.x < 0:
           r.x = 800

    for r in car_lane_four:
        r.x -= 6
        camera.draw(r)
        if r.x < 0:
           r.x = 800

    for r in car_lane_five:
        r.x -= 7
        camera.draw(r)
        if r.x < 0:
           r.x = 800


def logs():
    """
   draws the logs for the water
    """
    global log1, log2, log3, frogger
    for thing in log1:
        thing.x -= 7
        camera.draw(thing)
        if thing.x < -100:
            thing.x = 800
        if frogger.touches(thing):
            frogger.x -= 7


    for l0g in log2:
        l0g.x += 8
        camera.draw(l0g)
        if l0g.x > 800:
            l0g.x = 0
        if frogger.touches(l0g):
            frogger.x += 8

    for stuff in log3:
        stuff.x -= 15
        camera.draw(stuff)
        if stuff.x < -100:
            stuff.x = 800
        if frogger.touches(stuff):
            frogger.x -= 15

    for loog in log4:
        loog.x += 12
        camera.draw(loog)
        if loog.x > 800:
            loog.x = 0
        if frogger.touches(loog):
            frogger.x += 12

massive_lst = []
for all in log4, log3, log2, log1:
    massive_lst.append(all)


def death():
    """allows for the game to end if frog dies"""
    global log4, log3, log2, log1, lives, game_over

    if frogger.y == 225:
        if frogger.touches(log1[0]) is False and frogger.touches(log1[1]) is False and frogger.touches(log1[2]) is False:
            lives -= 1
            if lives != 0:
                frogger.y = 275
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 175:
        if frogger.touches(log2[0]) is False and frogger.touches(log2[1]) is False:
            lives -= 1
            if lives != 0:
                frogger.y = 275
                frogger.x = 400

            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 125:
        if frogger.touches(log3[0]) is False and frogger.touches(log3[1]) is False:
            lives -= 1
            if lives != 0:
                frogger.y = 275
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 75:
        if frogger.touches(log4[0]) is False and frogger.touches(log4[1]) is False:
            lives -= 1
            if lives != 0:
                frogger.y = 275
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 525:
        if frogger.touches(car_lane_one[0]) is True or frogger.touches(car_lane_one[1]) is True or frogger.touches(car_lane_one[2]) or frogger.touches(car_lane_one[2]) or frogger.touches(car_lane_one[3]):
            lives -= 1
            if lives != 0:
                frogger.y = 575
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 475:
        if frogger.touches(car_lane_two[0]) is True or frogger.touches(car_lane_two[1]) is True or frogger.touches(car_lane_two[2]) or frogger.touches(car_lane_two[2]) or frogger.touches(car_lane_two[3]):
            lives -= 1
            if lives != 0:
                frogger.y = 575
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 425:
        if frogger.touches(car_lane_three[0]) is True or frogger.touches(car_lane_three[1]) is True or frogger.touches(car_lane_three[2]):
            lives -= 1
            if lives != 0:
                frogger.y = 575
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 375:
        if frogger.touches(car_lane_four[0]) is True or frogger.touches(car_lane_four[1]):
            lives -= 1
            if lives != 0:
                frogger.y = 575
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.y == 325:
        if frogger.touches(car_lane_five[0]) or frogger.touches(car_lane_five[1]) or frogger.touches(car_lane_five[2]):
            lives -= 1
            if lives != 0:
                frogger.y = 575
                frogger.x = 400
            else:
                camera.draw(game_over)
                gamebox.pause()

    if frogger.x > 800 or frogger.x < 0 or frogger.y > 600:
        lives -= 1
        if lives != 0:
            if frogger.y > 275:
                frogger.y = 575
                frogger.x = 400
            else:
                frogger.y = 275
                frogger.x = 400
        else:
            camera.draw(game_over)
            gamebox.pause()


def win():
    """displays wining screen"""
    global frogger
    if frogger.y == 25:
        camera.draw(gamebox.from_text(400, 300, "YOU WIN!!!!!!!", 140, "yellow", bold=True, ))
        gamebox.pause()

def health_bar():
    """makes health bar"""
    global lives
    camera.draw(gamebox.from_text(620,25,"health:",30,"green",bold=True,))
    if lives == 5:
        health_bar = gamebox.from_color(730, 25, "red", 100, 30)
        camera.draw(health_bar)
    if lives == 4:
        health_bar = gamebox.from_color(720, 25, "red", 80, 30)
        camera.draw(health_bar)
    if lives == 3:
        health_bar = gamebox.from_color(710, 25, "red", 60, 30)
        camera.draw(health_bar)
    if lives == 2:
        health_bar = gamebox.from_color(700, 25, "red", 40, 30)
        camera.draw(health_bar)
    if lives == 1:
        health_bar = gamebox.from_color(690, 25, "red", 20, 30)
        camera.draw(health_bar)
    if lives == 0:
        health_bar = gamebox.from_color(680, 25, "red", 0, 30)
        camera.draw(health_bar)

def time():
    """function that displays a timer countdown"""
    global game_on, tick_counter, game_over
    clock = 60
    if game_on:
        clock -= tick_counter//30
        clock_image = gamebox.from_text(75, 25, "time: " + str(clock), 30, "green", bold=True)
        camera.draw(clock_image)
        if clock == 0:
            camera.draw(game_over)
            gamebox.pause()

def tick(keys):
    """"
this is the tick function
"""
    global tick_counter
    tick_counter += 1
    if game_on is False:
        start_screen(keys)
    if game_on:
        camera.clear("sienna")
        frogger.image = frogger_images[tick_counter//2 % 12]
        move_frog(keys)
        draw_scenery()
        highway_lines()
        cars()
        logs()
        death()
        win()
        camera.draw(frogger)
        health_bar()
        time()
    camera.display()


gamebox.timer_loop(30, tick)