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
__date__ = '27/09/2019'
__status__ = 'prod'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

from PyQt5.QtWidgets import QDialog
from JDD.IHM.choice_window.ui_choice import Ui_Dialog
from JDD.IHM.main_windows.main_windows import MainWindow

# ==================================================================================================
# INITIALISATIONS
# ==================================================================================================

# ==================================================================================================
# CLASSES
# ==================================================================================================


# =====================================
class ChoiceWindow(QDialog, Ui_Dialog):
    """
        Classe qui permet de charger l'interface de choix du type de jeu

        :ivar __application: application
        :type __application: PyQt5.QtWidgets.QApplication

        :ivar __jeu_choisi: type de jeu choisi par l'utilisateur
        :type __jeu_choisi: str

        :ivar __instance_du_jeu_choisi: instance d'un object MainWindow correspondant au jeu choisi par le joueur
        :type __instance_du_jeu_choisi: None | JDD.IHM.main_windows.main_windows.MainWindow
    """

    # ==============================
    def __init__(self, application):
        """
            Constructeur de la classe

            :param application: application
            :type application: PyQt5.QtWidgets.QApplication
        """

        # Initialisation en tant que QMainWindow
        QDialog.__init__(self)

        # Initialisation graphique
        self.setupUi(self)

        # Initialisation des variables d'instance
        self.__application = application

        # Initialisation des autres variables d'instance
        self.__jeu_choisi = ""
        self.__instance_du_jeu_choisi = None

        # Connexion des widgets
        self.connexions()

    # ===================
    def connexions(self):
        """
            Méthode qui permet de faire les connexions entre les widgets et les actions
        """

        self.bouton_num_vers_nom.clicked.connect(self.charger_num_vers_nom)
        self.bouton_nom_vers_num.clicked.connect(self.charger_nom_vers_num)
        self.bouton_quitter.clicked.connect(self.quitter)

    # =============================
    def charger_num_vers_nom(self):
        """
            Méthode qui permet de
        """

        self.__jeu_choisi = "num_vers_nom"
        self.lancer_le_jeu_choisi()

    # =============================
    def charger_nom_vers_num(self):
        """
            Méthode qui permet de
        """

        self.__jeu_choisi = "nom_vers_num"
        self.lancer_le_jeu_choisi()

    # =============================
    def lancer_le_jeu_choisi(self):
        """
            Méthode qui permet de lancer le jeu choisi
        """

        self.hide()
        self.__instance_du_jeu_choisi = MainWindow(self.__application, self.__jeu_choisi, self)
        self.__instance_du_jeu_choisi.show()

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
