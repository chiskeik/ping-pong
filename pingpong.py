# importación e inicialización:

import pygame, sys, random # importa las librerías necesarias.
pygame.init() # inicializa pygame.

# configuración de la pantalla:

width, height = 800, 600 # ancho y alto de la pantalla respectivamente.
font = pygame.font.SysFont("consolas", width//20) # fuente para el texto.
screen = pygame.display.set_mode((width, height)) # crea la pantalla.
pygame.display.set_caption("ping pong!") # título del juego.
clock = pygame.time.Clock() # reloj para controlar los FPS.

# bucle principal del juego:

# paddles

player = pygame.Rect(width-60, height/2-50, 10, 100) # paddle del jugador.
opponent = pygame.Rect(50, height/2-50, 10, 100) # paddle del oponente.
player_score, opponent_score = 0, 0 # puntajes iniciales del jugador y del oponente.

# pelotica

ball = pygame.Rect(width/2-10, height/2-10, 20, 20)
x_speed, y_speed = 1, 1 # velocidad de la pelota

while True:

    keys_pressed = pygame.key.get_pressed() # revisa las teclas que presiona el usuario.
    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 2 # mueve el paddle del jugador hacia arriba.
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < height:
            player.bottom += 2 # mueve el paddle del jugador hacia arriba.

    for event in pygame.event.get(): # revisa y procesa las acciones del usuario.
        if event.type == pygame.QUIT: # si el usuario cierra la ventana.
            pygame.quit() # cierra pygame.
            sys.exit() # cierra el programa.

    if ball.y >= height:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1
    if ball.x <= 0:
        player_score += 1
        ball.center = (width/2, height/2) # coloca la pelota en el centro tras ganar un punto
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if ball.x >= width:
        opponent_score += 1
        ball.center = (width/2, height/2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top - ball.width, player.bottom + ball.width):
        x_speed = -1
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(opponent.top - ball.width, opponent.bottom + ball.width):
        x_speed = 1

    ball.x += x_speed*1.5
    ball.y += y_speed*1.5

    if opponent.y < ball.y:
        opponent.top += 1
    if opponent.bottom > ball.y:
        opponent.bottom -= 1

    player_score_text = font.render(str(player_score), True, "light pink")
    opponent_score_text = font.render(str(opponent_score), True, "light pink")

    fondo = pygame.image.load("assets/descarga.jpg")
    fondo = pygame.transform.scale(fondo, (width, height))

    screen.blit(fondo, (0, 0)) # dibuja el fondo.

    pygame.draw.rect(screen, "light pink", player)
    pygame.draw.rect(screen, "light pink", opponent)
    pygame.draw.circle(screen, "light pink", ball.center, 10)

    fondo = pygame.image.load("assets/descarga.jpg")
    fondo = pygame.transform.scale(fondo, (width, height))

    screen.blit(player_score_text, (width/2 + 50,50))
    screen.blit(opponent_score_text, (width/2 - 50,50))
    pygame.display.update() # actualiza la pantalla.
    clock.tick(300) # limita los FPS a 300.
