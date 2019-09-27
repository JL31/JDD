# coding: utf-8

"""
    Script de conversion du fichier ui du dossier courant
"""

# =================================================================================================
# PARAMETRES GLOBAUX
# =================================================================================================

__author__ = 'Julien LEPAIN'
__email__ = 'julien.lepain@altran.com'
__version__ = '1.0'
__maintainer__ = 'Julien LEPAIN'
__date__ = '24/09/2019'
__status__ = 'dev'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

from JDD.IHM.main_windows.conversion_ui_to_py import conversion
from glob import glob
# from os import getcwd
from os.path import basename, dirname

# ==================================================================================================
# INITIALISATIONS
# ==================================================================================================

# ==================================================================================================
# CLASSES
# ==================================================================================================

# ==================================================================================================
# FONCTIONS
# ==================================================================================================

# ==================================================================================================
# UTILISATION
# ==================================================================================================

if __name__ == "__main__":

    # fichier_a_convertir = glob(getcwd() + "\*.ui")
    fichier_a_convertir = glob(dirname(__file__) + "\*.ui")

    nombre_de_fichiers_ui = len(fichier_a_convertir)

    if nombre_de_fichiers_ui > 1:

        msg = "Le dossier ne doit contenir qu'un seul fichier ui, il en contient {} :\n\n".format(nombre_de_fichiers_ui)
        for fichier in fichier_a_convertir:

            msg += "- {}\n".format(basename(fichier))

        raise ValueError(msg)

    conversion(*fichier_a_convertir)
