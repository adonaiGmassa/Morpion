# bibliothèque utilisée
import pygame
import sys

# Dimensions de la fenêtre
LARGUR = 300
HAUTEUR = 300
LARGEUR_CASE = 100
LARGEUR_BOUTON = 100
HAUTEUR_BOUTON = 40

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (213, 50, 80)
BLEU = (50, 150, 255)

# Initialiser Pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGUR, HAUTEUR))
pygame.display.set_caption("Morpion")

# Créer le plateau
plateau = [[" " for _ in range(3)] for _ in range(3)]
tour = "X"  # Le joueur qui commence
jeu_en_cours = True


# Fonction pour dessiner le plateau
def DESSINER_PLATEAU():

    fenetre.fill(BLANC)  # Mettre l'arrière-plan blanc

    for i in range(1, 3):  # Dessine les lignes du plateau 
        # Dessine une ligne horizontale
        pygame.draw.line(fenetre, NOIR, (0, i * LARGEUR_CASE), (LARGUR, i * LARGEUR_CASE), 2)
        # Dessine une ligne verticale
        pygame.draw.line(fenetre, NOIR, (i * LARGEUR_CASE, 0), (i * LARGEUR_CASE, HAUTEUR), 2)

    for i in range(3):
        for j in range(3):
            if plateau[i][j] == "X":
                pygame.draw.line(fenetre, ROUGE, (j * LARGEUR_CASE + 20, i * LARGEUR_CASE + 20),
                                 (j * LARGEUR_CASE + 80, i * LARGEUR_CASE + 80), 2)
                pygame.draw.line(fenetre, ROUGE, (j * LARGEUR_CASE + 80, i * LARGEUR_CASE + 20),
                                 (j * LARGEUR_CASE + 20, i * LARGEUR_CASE + 80), 2)
            elif plateau[i][j] == "O":
                pygame.draw.circle(fenetre, NOIR, (j * LARGEUR_CASE + 50, i * LARGEUR_CASE + 50), 40, 2)

    # Dessiner le bouton Recommencer
    dessiner_bouton(100, 250, LARGEUR_BOUTON, HAUTEUR_BOUTON, "Recommencer")

# Fonction pour dessiner un bouton
def dessiner_bouton(x, y, largeur, hauteur, texte):

    pygame.draw.rect(fenetre, BLEU, (x, y, largeur, hauteur))
    pygame.draw.rect(fenetre, NOIR, (x, y, largeur, hauteur), 2)
    font = pygame.font.Font(None, 36)
    label = font.render(texte, True, NOIR)
    fenetre.blit(label, (x + 10, y + 10))

# Vérifier la victoire
def victoire():

    # Parcourt les lignes du plateau
    for i in range(3):

        # Vérifie si les trois cases de la ligne i sont identiques et non vides
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":

            return plateau[i][0]
            
        # Vérifie si les trois cases de la colonne i sont identiques et non vides
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":

            return plateau[0][i]
    
    # Vérifie si les trois cases de la diagonale principale sont identiques et non vides
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ":
        return plateau[0][0]

    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return plateau[0][2]

    # Si aucune victoire n'est trouvée, retourne None
    return None

# Boucle principale du jeu
while jeu_en_cours:

    DESSINER_PLATEAU()
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            
            x, y = event.pos
            colonne = x // LARGEUR_CASE
            ligne = y // LARGEUR_CASE

            # Vérifier si le clic est dans la zone du plateau
            if 0 <= ligne < 3 and 0 <= colonne < 3 and plateau[ligne][colonne] == " ":

                plateau[ligne][colonne] = tour
                gagnant = victoire()
                
                if gagnant:

                    print(f"Le joueur {gagnant} a gagné !")
                    jeu_en_cours = False  # Fin du jeu

                # Changer de tour
                tour = "O" if tour == "X" else "X"



pygame.quit()

