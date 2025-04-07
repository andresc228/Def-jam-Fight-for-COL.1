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

    def curar(self, cantidad):
        self.vida_actual = min(self.vida_maxima, self.vida_actual + cantidad)

    def esta_vivo(self):
        return self.vida_actual > 0

    def mover_aleatoriamente(self):
        direccion = random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
        if direccion == 'arriba':
            self.y = max(0, self.y - self.vel)
        elif direccion == 'abajo':
            self.y = min(HEIGHT - self.alto, self.y + self.vel)
        elif direccion == 'izquierda':
            self.x = max(0, self.x - self.vel)
        elif direccion == 'derecha':
            self.x = min(WIDTH - self.ancho, self.x + self.vel)

    def ataque_lejano(self, objetivo):
        if abs(self.x - objetivo.x) < 200 and abs(self.y - objetivo.y) < 200:
            objetivo.recibir_dano(10)

    def ataque_cercano(self, objetivo):
        if abs(self.x - objetivo.x) < 60 and abs(self.y - objetivo.y) < 60:
            objetivo.recibir_dano(20)

    # Personajes disponibles
personajes_disponibles = [
        Personaje("Guerrero", 100, 300, BLUE),
        Personaje("Mago", 100, 300, GREEN),
        Personaje("Arquero", 100, 300, (150, 0, 255))
    ]

enemigos_disponibles = [
        Personaje("Orco", 600, 300, RED),
        Personaje("Esqueleto", 600, 300, (200, 0, 0))
    ]

print("Selecciona tu personaje:")
for idx, pj in enumerate(personajes_disponibles):
        print(f"{idx + 1}. {pj.nombre}")
indice_jugador = int(input("Número: ")) - 1
jugador = personajes_disponibles[indice_jugador]

print("Selecciona tu enemigo:")
for idx, en in enumerate(enemigos_disponibles):
        print(f"{idx + 1}. {en.nombre}")
indice_enemigo = int(input("Número: ")) - 1
enemigo = enemigos_disponibles[indice_enemigo]
