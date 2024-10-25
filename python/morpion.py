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

# Fonction pour dessiner le plateau
def DESSINER_PLATEAU():
    fenetre.fill(BLANC)  # Mettre l'arrière-plan blanc
    for i in range(1, 3):# Dessine les lignes du plateau 
        # Dessine une ligne horizontale
        pygame.draw.line(fenetre, NOIR, (0, i * LARGEUR_CASE), (LARGUR, i * LARGEUR_CASE), 2)
        # Dessine une ligne verticale
        pygame.draw.line(fenetre, NOIR, (i * LARGEUR_CASE, 0), (i * LARGEUR_CASE, HAUTEUR), 2)
        
        # Parcourt chaque ligne du plateau
        for i in range(3):
    
            # Parcourt chaque colonne du plateau
            for j in range(3):

                # Vérifie si la case contient un "X"
                if plateau[i][j] == "X":

                    # Dessine la première diagonale du "X"
                    pygame.draw.line(
                        fenetre, ROUGE,
                        (j * LARGEUR_CASE + 20, i * LARGEUR_CASE + 20),
                        (j * LARGEUR_CASE + 80, i * LARGEUR_CASE + 80), 2
                        )  

                    # Dessine la deuxième diagonale du "X"
                    pygame.draw.line(
                        fenetre, ROUGE,
                        (j * LARGEUR_CASE + 80, i * LARGEUR_CASE + 20),
                        (j * LARGEUR_CASE + 20, i * LARGEUR_CASE + 80),2
                        ) 
                
                # Vérifie si la case contient un "O"
                elif plateau[i][j] == "O":
                    # Dessine un cercle pour le "O"
                    pygame.draw.circle(fenetre, NOIR, (j * LARGEUR_CASE + 50, i * LARGEUR_CASE + 50),40,2)  

# Vérifier la victoire
def victoire():

    # Parcourt les lignes du plateau
    for i in range(3):

        # Vérifie si les trois cases de la ligne i sont identiques et non vides
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":
            # Si oui, retourne le symbole (X ou O) qui a gagné
            return plateau[i][0]

        # Vérifie si les trois cases de la colonne i sont identiques et non vides
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":
            # Si oui, retourne le symbole (X ou O) qui a gagné
            return plateau[0][i]

    # Vérifie si les trois cases de la diagonale principale sont identiques et non vides
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ":
        return plateau[0][0]# Si oui, retourne le symbole (X ou O) qui a gagné

    # Vérifie si les trois cases de la diagonale secondaire sont identiques et non vides
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return plateau[0][2]# Si oui, retourne le symbole (X ou O) qui a gagné

    # Si aucune victoire n'est trouvée, retourne None
    return None
