# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ecf_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 851, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 8, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 4, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 4, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 4, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 3, 3, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout.addWidget(self.comboBox_6, 6, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 4, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout.addWidget(self.comboBox_8, 8, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 6, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 6, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 4, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 5, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 8, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 7, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 5, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.layoutWidget)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout.addWidget(self.comboBox_7, 7, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 6, 4, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 6, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 5, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget)
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 8, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.layoutWidget)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 8, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 400, 176, 30))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Environment Complexity Factor (ECF)"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Description</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Perceived Impact</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_12.setText(_translate("Dialog", "E1"))
        self.label_23.setText(_translate("Dialog", "Object Oriented Experience"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p>Lead analyst capability</p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Total Factor</span></p></body></html>"))
        self.label_27.setText(_translate("Dialog", "E4"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "5"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_6.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_6.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_6.setItemText(5, _translate("Dialog", "5"))
        self.label_22.setText(_translate("Dialog", "E3"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_8.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_8.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_8.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_8.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_8.setItemText(5, _translate("Dialog", "5"))
        self.label_38.setText(_translate("Dialog", "Stable Requirements"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "5"))
        self.label_37.setText(_translate("Dialog", "E6"))
        self.comboBox.setItemText(0, _translate("Dialog", "0"))
        self.comboBox.setItemText(1, _translate("Dialog", "1"))
        self.comboBox.setItemText(2, _translate("Dialog", "2"))
        self.comboBox.setItemText(3, _translate("Dialog", "3"))
        self.comboBox.setItemText(4, _translate("Dialog", "4"))
        self.comboBox.setItemText(5, _translate("Dialog", "5"))
        self.label_18.setText(_translate("Dialog", "Application Experience"))
        self.label_13.setText(_translate("Dialog", "Familiarity with UML"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "5"))
        self.label_32.setText(_translate("Dialog", "<html><head/><body><p>E5</p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Environmental Factor</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "E2"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "5"))
        self.label_42.setText(_translate("Dialog", "E7"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Weight</span></p></body></html>"))
        self.label_43.setText(_translate("Dialog", "Part-time workers"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Calculated Factor</span><br/><span style=\" font-size:9pt; color:#707070;\">(weight*perceived impact)</span></p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_7.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_7.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_7.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_7.setItemText(5, _translate("Dialog", "5"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.label_33.setText(_translate("Dialog", "<html><head/><body><p>Motivation</p></body></html>"))
        self.label_48.setText(_translate("Dialog", "<html><head/><body><p>Difficult Programming<br/>language</p></body></html>"))
        self.label_47.setText(_translate("Dialog", "E8"))
