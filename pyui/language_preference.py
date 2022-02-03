# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/language_preference.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(143, 427)
        Dialog.setAcceptDrops(True)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 15, 116, 404))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton1.setObjectName("radioButton1")
        self.verticalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton2.setObjectName("radioButton2")
        self.verticalLayout.addWidget(self.radioButton2)
        self.radioButton3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton3.setObjectName("radioButton3")
        self.verticalLayout.addWidget(self.radioButton3)
        self.radioButton4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton4.setObjectName("radioButton4")
        self.verticalLayout.addWidget(self.radioButton4)
        self.radioButton5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton5.setObjectName("radioButton5")
        self.verticalLayout.addWidget(self.radioButton5)
        self.radioButton6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton6.setObjectName("radioButton6")
        self.verticalLayout.addWidget(self.radioButton6)
        self.radioButton7 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton7.setObjectName("radioButton7")
        self.verticalLayout.addWidget(self.radioButton7)
        self.radioButton8 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton8.setObjectName("radioButton8")
        self.verticalLayout.addWidget(self.radioButton8)
        self.radioButton9 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton9.setObjectName("radioButton9")
        self.verticalLayout.addWidget(self.radioButton9)
        self.radioButton10 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton10.setObjectName("radioButton10")
        self.verticalLayout.addWidget(self.radioButton10)
        self.radioButton11 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton11.setObjectName("radioButton11")
        self.verticalLayout.addWidget(self.radioButton11)
        self.radioButton12 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton12.setObjectName("radioButton12")
        self.verticalLayout.addWidget(self.radioButton12)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Language "))
        self.radioButton1.setText(_translate("Dialog", "Assembler"))
        self.radioButton1.setProperty("score", _translate("Dialog", "209"))
        self.radioButton2.setText(_translate("Dialog", "Ada 95"))
        self.radioButton2.setProperty("score", _translate("Dialog", "154"))
        self.radioButton3.setText(_translate("Dialog", "C"))
        self.radioButton3.setProperty("score", _translate("Dialog", "148"))
        self.radioButton4.setText(_translate("Dialog", "C++"))
        self.radioButton4.setProperty("score", _translate("Dialog", "59"))
        self.radioButton5.setText(_translate("Dialog", "C#"))
        self.radioButton5.setProperty("score", _translate("Dialog", "58"))
        self.radioButton6.setText(_translate("Dialog", "COBOL"))
        self.radioButton6.setProperty("score", _translate("Dialog", "80"))
        self.radioButton7.setText(_translate("Dialog", "FORTRAN"))
        self.radioButton7.setProperty("score", _translate("Dialog", "90"))
        self.radioButton8.setText(_translate("Dialog", "HTML"))
        self.radioButton8.setProperty("score", _translate("Dialog", "43"))
        self.radioButton9.setText(_translate("Dialog", "JAVA"))
        self.radioButton9.setProperty("score", _translate("Dialog", "55"))
        self.radioButton10.setText(_translate("Dialog", "JAVASCRIPT"))
        self.radioButton10.setProperty("score", _translate("Dialog", "54"))
        self.radioButton11.setText(_translate("Dialog", "VBSCRIPT"))
        self.radioButton11.setProperty("score", _translate("Dialog", "38"))
        self.radioButton12.setText(_translate("Dialog", "Visual Basic"))
        self.radioButton12.setProperty("score", _translate("Dialog", "50"))
        self.pushButton.setText(_translate("Dialog", "Done"))
