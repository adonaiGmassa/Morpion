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
        const CELLULE = document.createElement("div");
        CELLULE.classList.add("cellule");
        CELLULE.setAttribute("data-index", i);
        CELLULE.addEventListener("click", gererClic);
        PLATEAU.appendChild(CELLULE);
    }
}

// Fonction pour gérer le clic sur une cellule
function gererClic(event) {
    const INDEX = event.target.getAttribute("data-index");

    // Vérifier si la cellule est déjà remplie ou si le jeu est terminé
    if (etatDuJeu[INDEX] !== "" || verifierVictoire()) {
        return;
    }

    // Mettre à jour l'état du jeu
    etatDuJeu[INDEX] = joueurActuel;
    event.target.textContent = joueurActuel;

    // Vérifier la victoire
    if (verifierVictoire()) {
        setTimeout(() =>  afficherMessageVictoire(), 10);
    } else {
        // Changer de joueur
        joueurActuel = joueurActuel === "X" ? "O" : "X";
    }
}

// Fonction pour vérifier la victoire
function verifierVictoire() {
    const COMBINAISON_GAGNANTES = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    return COMBINAISON_GAGNANTES.some(combinaison => {
        const [a, b, c] = combinaison;
        return etatDuJeu[a] && etatDuJeu[a] === etatDuJeu[b] && etatDuJeu[a] === etatDuJeu[c];
    });
}

// Fonction pour réinitialiser le jeu
function reinitialiser() {
    etatDuJeu = ["", "", "", "", "", "", "", "", ""];
    joueurActuel = "X";
    const CELLULES = PLATEAU.children;
    for (let cellule of CELLULES) {
        cellule.textContent = "";
    }
}

// Fonction pour afficher un message de victoire
function afficherMessageVictoire() {
    const  MESSAGE = `Le joueur ${joueurActuel} a gagné!`;
    const MESSAGE_CONTAINER = document.createElement("div");
    MESSAGE_CONTAINER.classList.add("message-victoire");
    MESSAGE_CONTAINER.textContent = MESSAGE;
    document.body.appendChild(MESSAGE_CONTAINER);
}

// Initialiser le plateau
creerPlateau();
