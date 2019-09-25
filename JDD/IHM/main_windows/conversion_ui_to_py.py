# coding: utf-8

__author__ = 'Julien LEPAIN'
__email__ = 'julien.lepain@altran.com'
__version__ = '1.0'
__maintainer__ = 'Julien LEPAIN'
__date__ = '29/04/2019'
__status__ = 'prod'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

from sys import argv
from os import system, sep
from os.path import basename, dirname

# ==================================================================================================
# INITIALISATIONS
# ==================================================================================================

EMPLACEMENT_EXE_PYTHON = "C:\my_pythons\Anaconda3\python.exe"

# ==================================================================================================
# CLASSES
# ==================================================================================================

# ==================================================================================================
# FONCTIONS
# ==================================================================================================


# ==================================
def conversion(nom_du_fichier=None):
    """
        Fonction qui permet de convertir un fichier ui généré par QtDesigner en fichier source python

        :param nom_du_fichier: nom du fichier à convertir
        :type nom_du_fichier: None | str
    """

    if not nom_du_fichier:

        nom_du_fichier_ui = argv[1]

    else:

        nom_du_fichier_ui = basename(nom_du_fichier)

    nom_du_fichier_ui = nom_du_fichier_ui.split(".")[0]

    # commande = "{0} -m PyQt5.uic.pyuic {1}.ui -o ui_{1}.py".format(EMPLACEMENT_EXE_PYTHON, nom_du_fichier_ui)
    commande = "{0} -m PyQt5.uic.pyuic {1}{2}{3}.ui -o {1}{2}ui_{3}.py".format(EMPLACEMENT_EXE_PYTHON, dirname(nom_du_fichier), sep, nom_du_fichier_ui)

    system(commande)

# ==================================================================================================
# UTILISATION
# ==================================================================================================


if __name__ == "__main__":
    
    conversion()
