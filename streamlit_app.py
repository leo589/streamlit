import streamlit as st
import pygame
import time
import numpy as np
from PIL import Image

# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Cores
WHITE = (255, 255, 255)

# Carregar imagens
mario_img = pygame.image.load("mario.png")  # Coloque a imagem de Mario na mesma pasta que o script
background_img = pygame.image.load("background.png")  # Coloque o background na mesma pasta que o script

# Posições iniciais
mario_x, mario_y = WIDTH // 2, HEIGHT // 2

# Função para mover o Mario
def move_mario(keys, x, y):
    speed = 5
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    return x, y

# Função para renderizar a tela
def render_screen(x, y):
    screen.blit(background_img, (0, 0))
    screen.blit(mario_img, (x, y))
    pygame.display.flip()

# Título do Streamlit
st.title("Jogo do Mario com Streamlit")

# Placeholder para o jogo
game_placeholder = st.empty()

# Loop do jogo
running = True
while running:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    mario_x, mario_y = move_mario(keys, mario_x, mario_y)

    # Renderizar a tela
    render_screen(mario_x, mario_y)

    # Transformar a tela em imagem para exibir no Streamlit
    screen_array = pygame.surfarray.array3d(pygame.display.get_surface())
    screen_array = np.transpose(screen_array, (1, 0, 2))
    img = Image.fromarray(screen_array)
    
    # Exibir a imagem no Streamlit
    game_placeholder.image(img)

    # Delay para limitar a taxa de quadros
    time.sleep(0.033)  # Aproximadamente 30 FPS

pygame.quit()
