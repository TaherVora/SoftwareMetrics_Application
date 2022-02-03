# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/tab_smi.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(767, 585)
        self.btn_add_row = QtWidgets.QPushButton(Form)
        self.btn_add_row.setGeometry(QtCore.QRect(130, 520, 95, 30))
        self.btn_add_row.setObjectName("btn_add_row")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 50, 221, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(100, 100, 551, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.btn_compute_idx = QtWidgets.QPushButton(Form)
        self.btn_compute_idx.setGeometry(QtCore.QRect(270, 520, 111, 30))
        self.btn_compute_idx.setObjectName("btn_compute_idx")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_add_row.setText(_translate("Form", "Add Row"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Software Maturity Index</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "SMI"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Modules Added"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Modules Modified"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Modules Deleted"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Total Modules"))
        self.btn_compute_idx.setText(_translate("Form", "Compute Index"))
