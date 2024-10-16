<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark.Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            color: black; /* Texte noir pour contraste */
            padding: 50px;
            margin: 0;
            height: 100vh; /* Remplit la hauteur de la fenêtre */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-image: url('https://cdn.discordapp.com/attachments/1295073134898057266/1296157211109621821/IMG_5309.jpg?ex=671143f8&is=670ff278&hm=7f6e698ccfe181959fdd1b96580835421a0042385c977985f70573b24c72f1ef&');
            background-size: cover; /* Couvre tout l'écran */
            background-position: center; /* Centre l'image */
            filter: brightness(0.7); /* Assombrit l'image de fond pour améliorer la lisibilité */
        }
        .note {
            font-size: 2em; /* Taille du texte de la note */
            color: white; /* Couleur du texte de la note */
            margin-bottom: 20px;
            font-weight: bold; /* Gras pour mettre en valeur */
        }
        h2 {
            font-size: 1.8em;
            margin: 10px 0;
            font-weight: normal;
            color: white; /* Texte blanc */
        }
        .profile-pic {
            width: 150px; /* Ajustez la taille de la photo de profil */
            border-radius: 50%;
            border: 5px solid #23272A; /* Bordure noire */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3); /* Ombre portée */
            margin-bottom: 20px;
        }
        .button {
            background-color: #23272A; /* Couleur de fond noire pour le bouton */
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 30px; /* Bouton arrondi */
            cursor: pointer;
            text-decoration: none;
            font-size: 18px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); /* Ombre portée du bouton */
            transition: background-color 0.3s, transform 0.3s; /* Effet de transition */
        }
        .button:hover {
            background-color: #DC143C; /* Couleur rouge plus foncé pour le survol */
            transform: translateY(-2px); /* Effet de survol */
        }
    </style>
</head>
<body>
    <div class="note">y my hacker</div> <!-- Ajout de la note -->
    <img src="https://cdn.discordapp.com/attachments/1295073134898057266/1296155515721879664/IMG_5251.jpg?ex=67114264&is=670ff0e4&hm=e82fbd5dcf6d83d19f00bbeb0dc7679315b9ff5b24533044e82fc3b1e4ef38cb&" alt="Photo de Profil" class="profile-pic">
    <h2>N4S</h2>
    <p>Mes liens de réseaux sociaux :</p>
    <a href="https://discord.gg/Vc3QrAvdz9" class="button">DarkTool</a> <!-- Lien mis à jour -->
</body>
</html>