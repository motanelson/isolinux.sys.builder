import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boneco Anatômico 3D Simulado")

# Cores
BLACK = (0, 0, 0)
imagecounter=0
# Carregar a imagem do boneco anatômico
boneco_images=[]
boneco_images=boneco_images+[pygame.image.load("boneco.png").convert_alpha()]  # Substitua pelo caminho da sua imagem
boneco_images=boneco_images+[pygame.image.load("boneco1.png").convert_alpha()]  # Substitua pelo caminho da sua imagem
boneco_images=boneco_images+[pygame.image.load("boneco2.png").convert_alpha()]  # Substitua pelo caminho da sua imagem

boneco_image = boneco_images[0]
boneco_original_width = boneco_image.get_width()
boneco_original_height = boneco_image.get_height()

# Posição inicial do boneco
x = 0
z = 100  # Controle da "profundidade"
z_min = 50
z_max = 500
scale_factor = 10

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar entrada do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        z = min(z_max, z + 1)
    if keys[pygame.K_DOWN]:
        z = max(z_min, z - 1)
    if x<-(z*0.1):
        x=-(z*0.1)
    if x>(z*0.1):
        x=(z*0.1)

    # Calcular parâmetros com base em z
    scale = 1 / (z*0.1) * scale_factor
    scaled_width = int(boneco_original_width * scale)
    scaled_height = int(boneco_original_height * scale)
    center_x = screen_width // 2 + int(x * scale * 20)
    center_y = screen_height // 2 + int((z*0.1) * scale * 10)

    # Redimensionar a imagem do boneco
    boneco_scaled = pygame.transform.scale(boneco_image, (scaled_width, scaled_height))

    # Limpar tela
    screen.fill(BLACK)

    # Desenhar o boneco
    boneco_rect = boneco_scaled.get_rect(center=(center_x, center_y))
    screen.blit(boneco_scaled, boneco_rect)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(1000)
    imagecounter=imagecounter+1
    if imagecounter>2:
        imagecounter=0
    boneco_image = boneco_images[imagecounter]
# Sair do Pygame
pygame.quit()
