import pygame
import random

# Configuración inicial de pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batalla RPG Pygame")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Personaje:
    def __init__(self, nombre, x, y, color, vida=100):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.color = color
        self.vida_maxima = vida
        self.vida_actual = vida
        self.ancho = 40
        self.alto = 40
        self.vel = 3

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.alto))
        vida_txt = font.render(f"{self.nombre}: {self.vida_actual}/{self.vida_maxima}", True, BLACK)
        ventana.blit(vida_txt, (self.x - 20, self.y - 25))

    def recibir_dano(self, cantidad):
        self.vida_actual = max(0, self.vida_actual - cantidad)
