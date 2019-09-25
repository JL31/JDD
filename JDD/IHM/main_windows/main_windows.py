# coding: utf-8

"""
    Module de gestion de la fenêtre principale du jeu
"""

# =================================================================================================
# PARAMETRES GLOBAUX
# =================================================================================================

__author__ = 'Julien LEPAIN'
__email__ = ''
__version__ = '1.0'
__maintainer__ = 'Julien LEPAIN'
__date__ = '24/09/2019'
__status__ = 'dev'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from JDD.IHM.main_windows.ui_main import Ui_MainWindow
from random import randint
from os.path import join
from unidecode import unidecode

# ==================================================================================================
# INITIALISATIONS
# ==================================================================================================

# ==================================================================================================
# CLASSES
# ==================================================================================================


# ===========================================
class MainWindow(QMainWindow, Ui_MainWindow):
    """
        Classe qui permet de charger l'interface

        :ivar __application: application
        :type __application: PyQt5.QtWidgets.QApplication

        :ivar __fichier_des_donnees: nom du fichier contenant les données
        :type __fichier_des_donnees: str

        :ivar __emplacement_du_fichier_de_donnees: emplacement absolu du fichier contenant les données
        :type __emplacement_du_fichier_de_donnees: str

        :ivar __dico_departements: dictionnaire contenant les numéros et les noms des départements
        :type __dico_departements: dict

        :ivar __numero_actuel: numéro du département actuel
        :type __numero_actuel: str

        :ivar __departement_actuel: nom du département actuel
        :type __departement_actuel: str

        :ivar __numeros_deja_affiches: liste des numéros déjà affichés
        :type __numeros_deja_affiches: list[str]

        :ivar __score: score du joueur
        :type __score: int

        :ivar __nombre_de_tours: nombre de tours effectués
        :type __nombre_de_tours: int

        :ivar __partie_terminee: permet de savoir si la partie est terminée ou non (True si terminée, False sinon)
        :type __partie_terminee: bool
    """

    # ==============================
    def __init__(self, application):
        """
            Constructeur de la classe

            :param application: application
            :type application: PyQt5.QtWidgets.QApplication
        """

        # Initialisation en tant que QMainWindow
        QMainWindow.__init__(self)

        # Initialisation graphique
        self.setupUi(self)

        # Initialisation des variables d'instance
        self.__application = application

        # Initialisation des autres variables d'instance
        self.__fichier_des_donnees = "numeros_et_noms_des_departements"
        self.__emplacement_du_fichier_de_donnees = join("donnees", self.__fichier_des_donnees)
        self.__dico_departements = {}
        self.__numero_actuel = ""
        self.__departement_actuel = ""

        self.__numeros_deja_affiches = []
        self.__score = 0
        self.__nombre_de_tours = 1
        self.__partie_terminee = False

        # lancement des initilisations
        self.initialisations()

    # ========================
    def initialisations(self):
        """
            Méthode qui permet de réaliser quelques initialisations :
            - alignement horizontal dans le QLineEdit,
            - peuplement du dictionnaire qui va contenir les numéros et les noms des départements,
            - connexion des boutons,
            - initialisation de la donnée à afficher,
            - initialisation du score.
        """

        # Alignement horizontal dans le TextEdit
        self.LE_reponse.setAlignment(Qt.AlignCenter)

        # Peuplement du dictionnaire qui va contenir les numéros et les noms des départements
        self.chargement_des_departements()

        # Connexion des boutons
        self.connexions()

        # Initialisation de la donnée à afficher
        self.choisir_donnee_a_afficher()

        # Initialisation du score
        self.mise_a_jour_score()

    # ======================================
    def reinitilisations_de_variables(self):
        """
            Méthode qui permet de réinitialiser les valeurs de certaines variables
        """

        self.__numeros_deja_affiches = []
        self.__score = 0
        self.__nombre_de_tours = 1
        self.__partie_terminee = False

        self.LE_reponse.setEnabled(True)
        self.bouton_solution.setDisabled(False)

        self.label_question.setText("")
        self.LE_reponse.setText("")
        self.label_verif.setText("")

    # ====================================
    def incrementer_nombre_de_tours(self):
        """
            Méthode qui permet d'incrémenter de 1 le nombre de tours
        """

        self.__nombre_de_tours += 1

    # ===================================
    def verification_statut_partie(self):
        """
            Méthode qui permet de savoir si la partie est terminée ou non
        """

        if self.__nombre_de_tours == len(self.__dico_departements):

            self.__partie_terminee = True

            if self.__score == len(self.__dico_departements):

                msg = "Félicitations, vous avez gagné !"

            else:

                msg = "Vous avez perdu"

            self.label_verif.setText(msg)

            self.LE_reponse.setEnabled(False)
            self.bouton_solution.setDisabled(True)

    # ==========================
    def mise_a_jour_score(self):
        """
            Méthode qui permet de mettre à jour le score
        """

        score = "Votre socre est de : {}/{}".format(self.__score, len(self.__dico_departements))
        self.label_score.setText(score)

    # =======================================
    @staticmethod
    def transformation_de_la_reponse(chaine):
        """
            Fonction qui permet de transformer une chaîne de caractères pour :

            - enlever les accents,
            - enlever les tirets,
            - enlever les apostrophes,
            - mettre en minuscule.

            :param chaine: la chaîne de caractères à transformer
            :type chaine: str

            :return: la chaîne de caractères transformée
            :rtype: str
        """

        chaine = unidecode(chaine)
        chaine = chaine.replace("-", " ")
        chaine = chaine.replace("'", " ")
        chaine = chaine.lower()
        
        return chaine

    # ====================================
    def chargement_des_departements(self):
        """
            Méthode qui permet de charger les numéros des départements et les noms associés à chaque numéro dans le dictionnaire "__dico_departements"
            La méthode va lire le contenu du fichier "numeros_et_noms_des_departements" situé dans le dossier "donnees"
        """
        
        try:

            with open(self.__emplacement_du_fichier_de_donnees, 'r', encoding="utf-8") as file:

                donnees = file.readlines()

        except OSError:

            msg = "Le fichier {} contenant les données n'existe pas dans le dossier donnees".format(self.__fichier_des_donnees, )
            raise OSError(msg)

        else:

            for element in donnees:

                cle = element.split(";")[0]
                numero = element.split(";")[1]
                nom = element.split(";")[2].strip()
                self.__dico_departements[cle] = (numero, nom)

    # ===================
    def connexions(self):
        """
            Méthode qui permet de faire les connexions entre les widgets et les actions
        """

        self.LE_reponse.returnPressed.connect(self.verification_de_la_reponse)
        self.bouton_solution.clicked.connect(self.afficher_solution)
        self.bouton_nouvelle_partie.clicked.connect(self.lancement_nouvelle_partie)
        self.bouton_quitter.clicked.connect(self.quitter)

    # =========================================
    def initialisation_nouvelle_question(self):
        """
            Méthode qui permet de réaliser une série d'actions à chaque nouvelle question
        """

        self.incrementer_nombre_de_tours()

        self.verification_statut_partie()

        if not self.__partie_terminee:

            self.LE_reponse.setText("")
            self.choisir_donnee_a_afficher()

    # ===================================
    def verification_de_la_reponse(self):
        """
            Méthode qui permet de vérifier la réponse donnée par le joueur
        """

        reponse = self.LE_reponse.text()

        if reponse:

            reponse = self.transformation_de_la_reponse(reponse)

        if reponse == self.transformation_de_la_reponse(self.__departement_actuel):

            self.__score += 1
            self.mise_a_jour_score()
            self.label_verif.setText("Bien")

        else:

            self.label_verif.setText("Mauvaise réponse ! Solution : {}".format(self.__departement_actuel))

        self.initialisation_nouvelle_question()

    # ==========================
    def afficher_solution(self):
        """
            Méthode qui permet d'afficher la solution dans le QLineEdit
        """

        self.label_verif.setText("La réponse était :\n {} - {}".format(self.__dico_departements[self.__numero_actuel][0], self.__departement_actuel))
        self.initialisation_nouvelle_question()

    # ==================================
    def choisir_donnee_a_afficher(self):
        """
            Méthode qui permet de choisir la donnée à afficher
        """

        if not self.__numeros_deja_affiches:

            self.__numero_actuel = str(randint(1, 101))
            self.__numeros_deja_affiches.append(self.__numero_actuel)

        else:

            condition = True

            while condition:

                self.__numero_actuel = str(randint(1, 101))

                if self.__numero_actuel not in self.__numeros_deja_affiches:

                    self.__numeros_deja_affiches.append(self.__numero_actuel)
                    condition = False

        self.__departement_actuel = self.__dico_departements[self.__numero_actuel][1]
        self.label_question.setText(self.__dico_departements[self.__numero_actuel][0])

    # ==================================
    def lancement_nouvelle_partie(self):
        """
            Méthode qui permet de lancer une nouvelle partie
        """

        self.reinitilisations_de_variables()
        self.mise_a_jour_score()
        self.choisir_donnee_a_afficher()

    # ================
    def quitter(self):
        """
            Méthode qui permet de quitter l'application
        """

        self.__application.exit(0)

# ==================================================================================================
# FONCTIONS
# ==================================================================================================

# ==================================================================================================
# UTILISATION
# ==================================================================================================

if __name__ == "__main__":
    pass
