import pygame
import math

# Função para desenhar a imagem em triângulos com pontos
def draw_triangles_with_points(screen, image):
    screen_heights=screen_height
    half_width = screen_width // 2
    for x in range(half_width):
        left_height = int(screen_height * (x / half_width))
        right_height = int(screen_height * ((half_width - x) / half_width))

        # Parte esquerda do triângulo (encolhendo)
        for y in range(left_height):
            scaled_y = int(y / (left_height + 1) * image_height)
            color = image.get_at((int(half_width-x / half_width * image_width), scaled_y))
            screen.set_at((half_width + x, (screen_height - left_height) // 2 + y), color)

        # Parte direita do triângulo (encolhendo)
        for y in range(right_height):
            scaled_y = int(y / (right_height + 1) * image_height)
            color = image.get_at((int(( x / half_width) * image_width), scaled_y))
            screen.set_at(( x, (screen_height - right_height) // 2 + y), color)

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
image_path = "imagem.png"  # Substitua pelo caminho do seu arquivo PNG
image = pygame.image.load(image_path).convert_alpha()
image = pygame.transform.scale(image, (400, 600))  # Redimensionar para 400x600
image_width = image.get_width()
image_height = image.get_height()

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
z = 10  # Controle da "profundidade"
z_min = 5
z_max = 120
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
        z = z + 5
    if keys[pygame.K_DOWN]:
        z =  z - 5
    if keys[pygame.K_SPACE]:
        print(str(z))

    if x<-((z_max-z)*0.2):
        x=-((z_max-z)*0.2)
    if x>(z_max-z)*0.2:
        x=(z_max-z)*0.2
    if z>z_max:
        z=z_max
    if z<z_min:
        z=z_min

    # Calcular parâmetros com base em z
    scale = 1 / z * scale_factor
    scaled_width = int(boneco_original_width * scale)
    scaled_height = int(boneco_original_height * scale)
    center_x = screen_width // 2 + int(x * scale * 20)
    center_y = screen_height // (2.7) + int(z * scale * 10)

    # Redimensionar a imagem do boneco
    boneco_scaled = pygame.transform.scale(boneco_image, (scaled_width, scaled_height))

    # Limpar tela
    screen.fill(BLACK)
    # Desenhar os triângulos com pontos
    draw_triangles_with_points(screen, image)
    # Desenhar o boneco
    boneco_rect = boneco_scaled.get_rect(center=(center_x, center_y))
    screen.blit(boneco_scaled, boneco_rect)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(6)
    imagecounter=imagecounter+1
    if imagecounter>2:
        imagecounter=0
    boneco_image = boneco_images[imagecounter]
# Sair do Pygame
pygame.quit()
