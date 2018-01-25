Fonctionnalités
Version du 25.01.2018
Mission du site:

Remplacer les plateformes de réseautage entre professeurs particuliers et élèves.

Cibler spécifiquement :
-les élèves secondaires en Belgique francophone
-les étudiants de polytech de l'ULB, UCL, Ulg

En uploadant le programme de cours de chaque année pour permettre à 
l'élève de facilement identifier la matière qui lui fait défaut et au 
professeur de plus facilement identifier les lacunes de son étudiant.

Processus:

En tant qu'étudiant/élève:

Description des pages web:
(1)
Nom de la page : home
Affiché à l'écran :
Deux cases :
(2) Je cherche un professeur
(6) Je donne des cours particuliers


(2)
Nom de la page : choixEtudiant
Affiché à l'écran :
Deux cases :
(3) Je publie une annonce
() Je regarde la liste des professeurs

(3)
Nom de la page : newAnnonce
Affiché à l'écran :
Formulaire nouvelle annonce:

Nom
Prénom
adresse_email
Password
telephone
DescriptionAnnonce

Niveau=choose in [Primaire,Secondaire,Universitaire]
if secondaire :
	annee_scolaire=choose in [1,2,3,4,5,6]
	Matière déficiente=choose in [matière[niveau][annee_scolaire]]
elif universitaire :
	Université=choose in [ULB,UCL,Ulg]
	if ULB:
		cursus=choose in [polytech,solvay,bioingé,médecine]
	else:
		cursus=polytech
	niveau= [BA1,BA2,BA3,MA1]
	Matière déficiente=choose in [matière[niveau][cursus][niveau]]

Valider--> voir annonce (5)


(4)Nom de la page : ListeAnnonce
Affiché à l'écran :
Liste des annonces avec options de recherche

(5)
Nom de la page : AnnonceDetail
Affiché à l'écran :

(a)Details de l'annonce

(b)Formulaire de contact de l'élève:
Envoie un email à annonce.email
ProfesseurLogged_in
Texte
Liste des lacunes de l'élèves en tickbox pour preciser les compétences du prof face aux demandes de l'annonce


(6)
Nom de la page : choixProf
Affiché à l'écran :
Deux cases :
(7) Je m'enregistre sur OpenProf
() Je suis déja enregistré sur OpenProf

(7)
Nom de la page : newProf
Affiché à l'écran :
Formulaire nouveau Prof:

Nom
Prénom
adresse_email
Password
telephone

DescriptionProf
Situation=
NiveauEtudes=choose in [en_Bachelier,en_Master,Prof_secondaire,Assistant]

Valider--> voir annonce (9)


(8)Nom de la page : ListeProf
Affiché à l'écran :
Liste des Prof avec options de recherche

(9)
Nom de la page : ProfDetail
Affiché à l'écran :

(a)Details de l'annonce

(b)Formulaire de contact de l'élève:
Envoi un email à annonce.email
ProfesseurLogged_in
Texte
Liste des lacunes de l'élèves en tickbox pour preciser les compétences du prof face aux demandes de l'annonce

(10)
Nom de la page : Connexion
Affiché à l'écran :
Formulaire Connexion
adresse_email
Password
[Valider]
