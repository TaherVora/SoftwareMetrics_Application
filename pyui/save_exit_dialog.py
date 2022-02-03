# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/save_exit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 163)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 91))
        self.label.setObjectName("label")
        self.btn_close_without_save = QtWidgets.QPushButton(Dialog)
        self.btn_close_without_save.setGeometry(QtCore.QRect(30, 120, 151, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close_without_save.sizePolicy().hasHeightForWidth())
        self.btn_close_without_save.setSizePolicy(sizePolicy)
        self.btn_close_without_save.setObjectName("btn_close_without_save")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 120, 176, 30))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Do you want to save the changes to this document <br/>before closing?<br/><br/>If you don\'t save, your changes will be lost.</p></body></html>"))
        self.btn_close_without_save.setText(_translate("Dialog", "Close without Saving "))
