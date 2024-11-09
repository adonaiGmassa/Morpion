# bibliothèque utilisée
import pygame
import sys

# Dimensions de la fenêtre
LARGUR = 300
HAUTEUR = 400
LARGEUR_CASE = 100
LARGEUR_BOUTON = 100
HAUTEUR_BOUTON = 40
HAUTEUR_PLATEAU = 300  # La partie haute de l'écran pour le plateau (300 pixels)
HAUTEUR_INTERFACE = 100  # La partie basse de l'écran pour l'interface (100 pixels)

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (213, 50, 80)
BLEU = (50, 150, 255)
VERT = (0, 255, 0)
ROSE = (255, 0, 0)

# Initialiser Pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGUR, HAUTEUR))
pygame.display.set_caption("Morpion")

# Fonction pour dessiner un bouton
def dessiner_bouton(x, y, largeur, hauteur, texte, couleur):

    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur))
    pygame.draw.rect(fenetre, NOIR, (x, y, largeur, hauteur), 2)
    font = pygame.font.Font(None, 36)
    label = font.render(texte, True, NOIR)
    fenetre.blit(label, (x + 10, y + 10))

# Fonction pour réinitialiser le plateau
def reinitialiser_plateau():

    return [[" " for _ in range(3)] for _ in range(3)]

# Créer le plateau
plateau = reinitialiser_plateau()
tour = "X"  # Le joueur qui commence
jeu_en_cours = True

# Fonction pour dessiner le plateau
def DESSINER_PLATEAU():

    fenetre.fill(BLANC)  # Mettre l'arrière-plan en blanc

    for i in range(1, 3):  # Dessine les lignes du plateau

        # Dessine une ligne horizontale
        pygame.draw.line(fenetre, NOIR, (0, i * LARGEUR_CASE), (LARGUR, i * LARGEUR_CASE), 2)
        # Dessine une ligne verticale
        pygame.draw.line(fenetre, NOIR, (i * LARGEUR_CASE, 0), (i * LARGEUR_CASE, HAUTEUR_PLATEAU), 2)

    for i in range(3):

        for j in range(3):
            
            if plateau[i][j] == "X":
                
                pygame.draw.line(fenetre, ROUGE, (j * LARGEUR_CASE + 20, i * LARGEUR_CASE + 20),
                                 (j * LARGEUR_CASE + 80, i * LARGEUR_CASE + 80), 2)
                
                pygame.draw.line(fenetre, ROUGE, (j * LARGEUR_CASE + 80, i * LARGEUR_CASE + 20),
                                 (j * LARGEUR_CASE + 20, i * LARGEUR_CASE + 80), 2)
            
            elif plateau[i][j] == "O":
                
                pygame.draw.circle(fenetre, NOIR, (j * LARGEUR_CASE + 50, i * LARGEUR_CASE + 50), 40, 2)

    # Dessiner la ligne de séparation entre le plateau et le bouton
    pygame.draw.line(fenetre, NOIR, (0, HAUTEUR_PLATEAU), (LARGUR, HAUTEUR_PLATEAU), 3)

    # Dessiner le bouton Recommencer dans la partie inférieure de l'écran
    dessiner_bouton(100, HAUTEUR_PLATEAU + (HAUTEUR_INTERFACE - HAUTEUR_BOUTON) // 2,
                    LARGEUR_BOUTON, HAUTEUR_BOUTON, "Recommencer", BLEU)

# Fonction pour dessiner l'écran de fin de jeu
def dessiner_fin_jeu(message):

    # Afficher le message de fin de jeu
    fenetre.fill(BLANC)
    font = pygame.font.Font(None, 48)
    label = font.render(message, True, NOIR)
    fenetre.blit(label, (50, 100))

    # Dessiner les boutons de choix (Recommencer et Quitter)
    dessiner_bouton(50, 250, LARGEUR_BOUTON, HAUTEUR_BOUTON, "Recommencer", VERT)
    dessiner_bouton(150, 250, LARGEUR_BOUTON, HAUTEUR_BOUTON, "Quitter", ROSE)

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
    
    if jeu_en_cours:
        
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

            if jeu_en_cours:
                
                # Vérifier si le clic est dans la zone du plateau
                if 0 <= ligne < 3 and 0 <= colonne < 3 and y < HAUTEUR_PLATEAU and plateau[ligne][colonne] == " ":
                    
                    plateau[ligne][colonne] = tour
                    gagnant = victoire()
                    
                    if gagnant:
                        
                        print(f"Le joueur {gagnant} a gagné !")
                        jeu_en_cours = False  # Fin du jeu
                        dessiner_fin_jeu(f"Le joueur {gagnant} a gagné !")
                        pygame.display.flip()

                    # Changer de tour
                    tour = "O" if tour == "X" else "X"

            # Vérifier si le clic est dans la zone du bouton "Recommencer"
            if not jeu_en_cours:

                # Vérifier si "Recommencer" est cliqué
                if 50 <= x <= 150 and 250 <= y <= 290:
                    
                    plateau = reinitialiser_plateau()  # Réinitialiser le plateau
                    tour = "X"  # Le joueur X recommence
                    jeu_en_cours = True  # Relancer le jeu

                # Vérifier si "Quitter" est cliqué
                if 150 <= x <= 250 and 250 <= y <= 290:
                    
                    pygame.quit()  # Quitter le jeu
                    sys.exit()



