# coding: utf-8

"""
    Module de gestion d'un jeu de type : à partir du numéro trouve le nom du département
"""

# =================================================================================================
# PARAMETRES GLOBAUX
# =================================================================================================

__author__ = 'Julien LEPAIN'
__email__ = 'julien.lepain@altran.com'
__version__ = '1.0'
__maintainer__ = 'Julien LEPAIN'
__date__ = '25/09/2019'
__status__ = 'prod'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

from random import randint
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# ==================================================================================================
# INITIALISATIONS
# ==================================================================================================

# ==================================================================================================
# CLASSES
# ==================================================================================================


# =======================
class NumVersNom(object):
    """
        Classe de gestion des méthode dans le cas d'un jeu de type : à partir du numéro trouve le nom du département

        :ivar __context: instance de la classe MainWindow
        :type __context: JDD.IHM.main_windows.main_windows.MainWindow
    """

    # ==========================
    def __init__(self, context):
        """
            Constructeur de la classe

            :param context: instance de la classe MainWindow
            :type context: JDD.IHM.main_windows.main_windows.MainWindow
        """

        self.__context = context
        self.__context.label_titre.setText("Trouvez le nom du département associé au\nnuméro proposé")
        newfont = QFont("MS Shell Dlg 2", 12, QFont.Bold)
        self.__context.label_titre.setFont(newfont)
        self.__context.label_titre.setAlignment(Qt.AlignCenter)

    # ===================================
    def verification_de_la_reponse(self):
        """
            Méthode qui permet de vérifier la réponse donnée par le joueur
        """

        reponse = self.__context.LE_reponse.text()

        if reponse:

            reponse = self.__context.transformation_de_la_reponse(reponse)

        if reponse == self.__context.transformation_de_la_reponse(self.__context.get_departement_actuel()):

            self.__context.incrementer_score()
            self.__context.mise_a_jour_score()
            self.__context.label_verif.setText("Bien")

        else:

            self.__context.label_verif.setText("Mauvaise réponse ! Solution : {}".format(self.__context.get_departement_actuel()))

        self.__context.initialisation_nouvelle_question()

    # ==================================
    def choisir_donnee_a_afficher(self):
        """
            Méthode qui permet de choisir la donnée à afficher
        """

        if not self.__context.get_numeros_deja_affiches():

            nouveau_numero = str(randint(1, 101))
            self.__context.set_numero_actuel(nouveau_numero)
            self.__context.set_numeros_deja_affiches(self.__context.get_numero_actuel())

        else:

            condition = True

            while condition:

                nouveau_numero = str(randint(1, 101))
                self.__context.set_numero_actuel(nouveau_numero)

                if self.__context.get_numero_actuel() not in self.__context.get_numeros_deja_affiches():

                    self.__context.set_numeros_deja_affiches(self.__context.get_numero_actuel())
                    condition = False

        self.__context.set_departement_actuel(self.__context.get_dico_departements()[self.__context.get_numero_actuel()][1])
        self.__context.label_question.setText(self.__context.get_dico_departements()[self.__context.get_numero_actuel()][0])

# ==================================================================================================
# FONCTIONS
# ==================================================================================================

# ==================================================================================================
# UTILISATION
# ==================================================================================================

if __name__ == "__main__":
    pass
