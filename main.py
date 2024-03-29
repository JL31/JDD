#!/usr/bin/python3
# coding: utf-8

"""
    Script qui permet de lancer l'application
"""

# =================================================================================================
# PARAMETRES GLOBAUX
# =================================================================================================

__author__ = 'Julien LEPAIN'
__email__ = ''
__version__ = '1.0'
__maintainer__ = 'Julien LEPAIN'
__date__ = '24/09/2019'
__status__ = 'prod'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from JDD.IHM.choice_window.choice_windows import ChoiceWindow

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

    application = QApplication(argv)
    main = ChoiceWindow(application)
    main.show()

    exit(application.exec())
