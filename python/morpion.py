# bibliothèque utilisée
import pygame
import sys

# Dimensions de la fenêtre
LARGUR = 300
HAUTEUR = 300
LARGEUR_CASE = 100

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (213, 50, 80)

# Initialiser Pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGUR, HAUTEUR))
pygame.display.set_caption("Morpion")

# Créer le plateau
plateau = [
    [" " 
     for _ in range(3)
    ] 
    for _ in range(3)
]

