# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jlepain/PycharmProjects/Perso/JDD/JDD/IHM/choice_window\choice.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(440, 300))
        Dialog.setMaximumSize(QtCore.QSize(440, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(415, 0))
        self.label_3.setMaximumSize(QtCore.QSize(415, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bouton_nom_vers_num = QtWidgets.QPushButton(Dialog)
        self.bouton_nom_vers_num.setMinimumSize(QtCore.QSize(70, 70))
        self.bouton_nom_vers_num.setMaximumSize(QtCore.QSize(70, 70))
        self.bouton_nom_vers_num.setObjectName("bouton_nom_vers_num")
        self.horizontalLayout.addWidget(self.bouton_nom_vers_num)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bouton_num_vers_nom = QtWidgets.QPushButton(Dialog)
        self.bouton_num_vers_nom.setMinimumSize(QtCore.QSize(70, 70))
        self.bouton_num_vers_nom.setMaximumSize(QtCore.QSize(70, 70))
        self.bouton_num_vers_nom.setObjectName("bouton_num_vers_nom")
        self.horizontalLayout.addWidget(self.bouton_num_vers_nom)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.bouton_quitter = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_quitter.sizePolicy().hasHeightForWidth())
        self.bouton_quitter.setSizePolicy(sizePolicy)
        self.bouton_quitter.setMinimumSize(QtCore.QSize(70, 70))
        self.bouton_quitter.setMaximumSize(QtCore.QSize(70, 70))
        self.bouton_quitter.setObjectName("bouton_quitter")
        self.horizontalLayout_2.addWidget(self.bouton_quitter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choix du jeu"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">Bienvenue dans le jeu des départements</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Choisissez le type de jeu auquel vous voulez jouer :"))
        self.bouton_nom_vers_num.setText(_translate("Dialog", "Trouver le\n"
"numéro"))
        self.bouton_num_vers_nom.setText(_translate("Dialog", "Trouver le\n"
"nom"))
        self.bouton_quitter.setText(_translate("Dialog", "Quitter"))

