# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/tab_calculate_ucp.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(686, 593)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(11, 11, 571, 551))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inp_loc_pm = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_loc_pm.sizePolicy().hasHeightForWidth())
        self.inp_loc_pm.setSizePolicy(sizePolicy)
        self.inp_loc_pm.setMinimumSize(QtCore.QSize(150, 0))
        self.inp_loc_pm.setMaximumSize(QtCore.QSize(250, 16777215))
        self.inp_loc_pm.setObjectName("inp_loc_pm")
        self.gridLayout.addWidget(self.inp_loc_pm, 6, 1, 1, 1)
        self.label_ucp_result = QtWidgets.QLabel(self.widget)
        self.label_ucp_result.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_ucp_result.setObjectName("label_ucp_result")
        self.gridLayout.addWidget(self.label_ucp_result, 10, 1, 1, 1)
        self.label_est_pm = QtWidgets.QLabel(self.widget)
        self.label_est_pm.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_est_pm.setObjectName("label_est_pm")
        self.gridLayout.addWidget(self.label_est_pm, 13, 1, 1, 1)
        self.btn_calc_uaw = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calc_uaw.sizePolicy().hasHeightForWidth())
        self.btn_calc_uaw.setSizePolicy(sizePolicy)
        self.btn_calc_uaw.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btn_calc_uaw.setObjectName("btn_calc_uaw")
        self.gridLayout.addWidget(self.btn_calc_uaw, 4, 0, 1, 1)
        self.label_uucw_result = QtWidgets.QLabel(self.widget)
        self.label_uucw_result.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_uucw_result.setObjectName("label_uucw_result")
        self.gridLayout.addWidget(self.label_uucw_result, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.btn_calc_ecf = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calc_ecf.sizePolicy().hasHeightForWidth())
        self.btn_calc_ecf.setSizePolicy(sizePolicy)
        self.btn_calc_ecf.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btn_calc_ecf.setObjectName("btn_calc_ecf")
        self.gridLayout.addWidget(self.btn_calc_ecf, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.btn_calc_uucw = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calc_uucw.sizePolicy().hasHeightForWidth())
        self.btn_calc_uucw.setSizePolicy(sizePolicy)
        self.btn_calc_uucw.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btn_calc_uucw.setObjectName("btn_calc_uucw")
        self.gridLayout.addWidget(self.btn_calc_uucw, 3, 0, 1, 1)
        self.label_tcp_result = QtWidgets.QLabel(self.widget)
        self.label_tcp_result.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_tcp_result.setObjectName("label_tcp_result")
        self.gridLayout.addWidget(self.label_tcp_result, 1, 1, 1, 1)
        self.label_uucp_result = QtWidgets.QLabel(self.widget)
        self.label_uucp_result.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_uucp_result.setObjectName("label_uucp_result")
        self.gridLayout.addWidget(self.label_uucp_result, 9, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.inp_loc_ucp = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_loc_ucp.sizePolicy().hasHeightForWidth())
        self.inp_loc_ucp.setSizePolicy(sizePolicy)
        self.inp_loc_ucp.setMinimumSize(QtCore.QSize(150, 0))
        self.inp_loc_ucp.setMaximumSize(QtCore.QSize(250, 16777215))
        self.inp_loc_ucp.setObjectName("inp_loc_ucp")
        self.gridLayout.addWidget(self.inp_loc_ucp, 7, 1, 1, 1)
        self.inp_pf = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_pf.sizePolicy().hasHeightForWidth())
        self.inp_pf.setSizePolicy(sizePolicy)
        self.inp_pf.setMinimumSize(QtCore.QSize(150, 0))
        self.inp_pf.setMaximumSize(QtCore.QSize(250, 16777215))
        self.inp_pf.setStyleSheet("<body><p align-text=center>20</p></body>")
        self.inp_pf.setObjectName("inp_pf")
        self.gridLayout.addWidget(self.inp_pf, 5, 1, 1, 1)
        self.label_uaw_result = QtWidgets.QLabel(self.widget)
        self.label_uaw_result.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_uaw_result.setObjectName("label_uaw_result")
        self.gridLayout.addWidget(self.label_uaw_result, 4, 1, 1, 1)
        self.label_est_loc = QtWidgets.QLabel(self.widget)
        self.label_est_loc.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_est_loc.setObjectName("label_est_loc")
        self.gridLayout.addWidget(self.label_est_loc, 12, 1, 1, 1)
        self.label_est_hours = QtWidgets.QLabel(self.widget)
        self.label_est_hours.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_est_hours.setObjectName("label_est_hours")
        self.gridLayout.addWidget(self.label_est_hours, 11, 1, 1, 1)
        self.label_ecf_result = QtWidgets.QLabel(self.widget)
        self.label_ecf_result.setStyleSheet("background-color: rgb(217, 212, 255);")
        self.label_ecf_result.setObjectName("label_ecf_result")
        self.gridLayout.addWidget(self.label_ecf_result, 2, 1, 1, 1)
        self.btn_calc_tcp = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calc_tcp.sizePolicy().hasHeightForWidth())
        self.btn_calc_tcp.setSizePolicy(sizePolicy)
        self.btn_calc_tcp.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_calc_tcp.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btn_calc_tcp.setObjectName("btn_calc_tcp")
        self.gridLayout.addWidget(self.btn_calc_tcp, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_calc_metrics = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calc_metrics.sizePolicy().hasHeightForWidth())
        self.btn_calc_metrics.setSizePolicy(sizePolicy)
        self.btn_calc_metrics.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btn_calc_metrics.setObjectName("btn_calc_metrics")
        self.gridLayout.addWidget(self.btn_calc_metrics, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculate UCP"))
        self.inp_loc_pm.setText(_translate("Form", "700"))
        self.label_ucp_result.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_est_pm.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.btn_calc_uaw.setText(_translate("Form", "Calculate UAW"))
        self.label_uucw_result.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">LOC per PM</span></p></body></html>"))
        self.btn_calc_ecf.setText(_translate("Form", "Calculate ECF"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PF<br/></span>Productivity Factor</p></body></html>"))
        self.btn_calc_uucw.setText(_translate("Form", "Calculate UUCW"))
        self.label_tcp_result.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_uucp_result.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">LOC per UCP</span></p></body></html>"))
        self.inp_loc_ucp.setText(_translate("Form", "100"))
        self.inp_pf.setText(_translate("Form", "20"))
        self.label_uaw_result.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_est_loc.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_est_hours.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.label_ecf_result.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.btn_calc_tcp.setText(_translate("Form", "Calculate TCP"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Use Case Point</span></p></body></html>"))
        self.btn_calc_metrics.setText(_translate("Form", "Calculate Metrics"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">UUCP<br/></span>(UUCP = UUCW + UAW)</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Total UCP<br/></span>(UCP = TCP * ECF * UUCP * PF)</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Estimated Hours</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Estimated LOC</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Estimated PM</span></p></body></html>"))
