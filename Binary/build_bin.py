# coding=utf-8

"""
    Ce script est utilisé pour générer un fichier EXE pour le script principal
    Le projet doit être structuré de la manière suivante :

    Dossier parent
                   |
                   |__Binary (dossier)
                   |     |
                   |     |__build_bin.py (ce script)
                   |
                   |__donnees (dossier)
                   |
                   |__Sources du package (dossier)
                   |
                   |__main.py

    Ce fichier EXE sera généré dans le dossier Binary
"""

__author__ = 'Julien LEPAIN'
__email__ = ''
__version__ = '1.0'
__date__ = '30/09/2019'
__status = 'prod'

# ==================================================================================================
# IMPORTS
# ==================================================================================================

import os
import shutil
import glob

# ==================================================================================================
# INITIALISATIONS
# ==================================================================================================

# nom du fichier exe généré (sans extension)
EXE_NAME = "JDD"

# Nom du scripot main (sans extension)
MAIN_SCRIPT_NAME = "main"

# Nom du package dans lequel les sources peuvent être récupérées
SOURCE_PACKAGE_NAME = "JDD"

# Emplacement de l'exécutable de Python
EMPLACEMENT_EXE_PYTHON = "C:\my_pythons\Anaconda3"

# Nom de l'icône
NOM_FICHIER_ICONE = "Icone_JDD.ico"

# Nom du fichier de données
NOM_FICHIER_DE_DONNEES = "numeros_et_noms_des_departements"

# Emplacement du fichier de données
EMPLACEMENT_FICHIER_DE_DONNEES = "donnees"


# ==================================================================================================
# CLASSES
# ==================================================================================================

# ==================================================================================================
# FONCTIONS
# ==================================================================================================


# ===================================================================================================================================================================
def generate_exe(exe_name, main_script_name, source_package_name, emplacement_exe_python, nom_fichier_icone, nom_fichier_de_donnees, emplacement_fichier_de_donnees):
    """
        Cette fonction génère le fichier exécutable

        :param exe_name: le nom du fichier exécutable généré (sans extension)
        :type exe_name: str

        :param main_script_name: le nom du script principal (sans extension)
        :type main_script_name: str

        :param source_package_name: le nom du package dans lequel se trouvent les sources
        :type source_package_name: str

        :param emplacement_exe_python: l'emplacement auquel se trouve l'exécutable Python
        :type emplacement_exe_python: str

        :param nom_fichier_icone: nom du fichier icône à utiliser
        :type nom_fichier_icone: str

        :param nom_fichier_de_donnees: nom du fichier icône à utiliser
        :type nom_fichier_de_donnees: str

        :param emplacement_fichier_de_donnees: emplacement dans lequel se trouvera le fichier de données lors de l'exécution
        :type emplacement_fichier_de_donnees: str
    """

    # Création des dossiers et des emplacements des fichiers
    # ======================================================

    bin_dir_path = os.path.dirname(os.path.abspath(__file__))
    tool_dir_path = os.path.dirname(bin_dir_path)
    sources_dir_path = os.path.join(tool_dir_path, source_package_name)
    data_dir_path = os.path.join(tool_dir_path, emplacement_fichier_de_donnees)
    tmp_dir_path = os.path.join(bin_dir_path, 'tmp')
    target_dir_path = os.path.join(tmp_dir_path, source_package_name)
    data_tmp_dir_path = os.path.join(tmp_dir_path, emplacement_fichier_de_donnees)
    source_script_path = os.path.join(tool_dir_path, main_script_name + ".py")
    target_script_path = os.path.join(tmp_dir_path, main_script_name + ".py")
    donnees_source = os.path.join(data_tmp_dir_path, nom_fichier_de_donnees)

    # Suppression du fichier exécutable
    # =================================

    for f in glob.glob(os.path.join(bin_dir_path, '*.exe')):

        os.remove(f)

    # Suppression du dossier tmp
    # ==========================

    if os.path.isdir(tmp_dir_path):

        shutil.rmtree(tmp_dir_path)

    os.mkdir(tmp_dir_path)
    shutil.copytree(sources_dir_path, target_dir_path)
    shutil.copytree(data_dir_path, data_tmp_dir_path)
    shutil.copy(source_script_path, target_script_path)

    # Génération du fichier exécutable
    # ================================

    os.chdir(tmp_dir_path)

    cmd = (r'{exe}\Scripts\pyinstaller'
           ' --paths C:\\my_pythons\\Anaconda3\\Lib\\site-packages\\PyQt5\\Qt\\bin'
           # ' --paths C:\\my_pythons\\Anaconda3\\Lib\\site-packages\\scipy\\extra-dll'
           # ' --hidden-import scipy._lib.messagestream'
           # ' --hidden-import numpy._distributor_init'
           # ' --hidden-import scipy._distributor_init'
           ' --exclude PyQt4'
           ' --windowed'
           ' --icon="../{icone}" -F'
           ' --add-data "{};{}"'
           ' --add-data "{nom};{emplacement}"'
           ' {main}.py').format(exe=emplacement_exe_python,
                                icone=nom_fichier_icone,
                                nom=donnees_source,
                                emplacement=emplacement_fichier_de_donnees,
                                main=main_script_name)
    os.system(cmd)

    # Déplacement du fichier exécutable dans le dossier bin
    # =====================================================

    shutil.move(r"dist\%s.exe" % main_script_name, os.path.join(bin_dir_path, exe_name + '.exe'))

    # Redéfinition du dossier courant
    # ===============================

    os.chdir(bin_dir_path)

    # Suppression du dossier tmp
    # ==========================

    shutil.rmtree(tmp_dir_path)

# ==================================================================================================
# UTILISATION
# ==================================================================================================


if __name__ == "__main__":

    generate_exe(EXE_NAME, MAIN_SCRIPT_NAME, SOURCE_PACKAGE_NAME, EMPLACEMENT_EXE_PYTHON, NOM_FICHIER_ICONE, NOM_FICHIER_DE_DONNEES, EMPLACEMENT_FICHIER_DE_DONNEES)
