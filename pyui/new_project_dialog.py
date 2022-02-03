# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/new_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-150, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(78, 10, 251, 20))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 29, 381, 214))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.projectNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.projectNameLabel)
        self.projectNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.projectNameLineEdit.setObjectName("projectNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.projectNameLineEdit)
        self.productNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.productNameLabel.setObjectName("productNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.productNameLabel)
        self.productNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.productNameLineEdit.setObjectName("productNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productNameLineEdit)
        self.creatorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.creatorLabel.setObjectName("creatorLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.creatorLabel)
        self.creatorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.creatorLineEdit.setObjectName("creatorLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.creatorLineEdit)
        self.commentsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.commentsLabel.setObjectName("commentsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.commentsLabel)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.textEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CECS 543 Metrics Suite New Project"))
        self.label.setText(_translate("Dialog", "CECS 543 Metrics Suite New Project"))
        self.projectNameLabel.setText(_translate("Dialog", "Project Name:"))
        self.productNameLabel.setText(_translate("Dialog", "Product Name:"))
        self.creatorLabel.setText(_translate("Dialog", "Creator:"))
        self.commentsLabel.setText(_translate("Dialog", "Comments"))
