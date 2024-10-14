// Récupération de l'élément HTML avec l'ID "plateau" pour y afficher le jeu
const PLATEAU = document.getElementById("plateau");

// Variable pour suivre le joueur actuel (X ou O)
let joueurActuel = "X";

// Tableau pour garder l'état du jeu, initialisé avec des chaînes vides
let etatDuJeu = ["", "", "", "", "", "", "", "", ""];

// Fonction pour créer le plateau de jeu
function creerPlateau() {
    // Boucle pour créer 9 cellules (3x3) pour le jeu
    for (let i = 0; i < 9; i++) {
        // Création d'un nouvel élément div pour chaque cellule
        const CELLULE = document.createElement("div");
        
        // Ajout de la classe "cellule" à chaque div pour le style
        CELLULE.classList.add("cellule");
        
        // Définition de l'attribut "data-index" pour identifier chaque cellule
        CELLULE.setAttribute("data-index", i);
        
        // Ajout d'un écouteur d'événements pour gérer le clic sur la cellule
        CELLULE.addEventListener("click", gererClic);
        
        // Ajout de la cellule au plateau
        PLATEAU.appendChild(CELLULE);
    }
}

creerPlateau();