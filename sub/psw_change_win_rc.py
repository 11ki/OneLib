# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psw_change_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_psw_change_Form(object):
    def setupUi(self, psw_change_Form):
        psw_change_Form.setObjectName("psw_change_Form")
        psw_change_Form.resize(265, 125)
        self.gridLayout = QtWidgets.QGridLayout(psw_change_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(psw_change_Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(psw_change_Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(psw_change_Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.old_psw_le = QtWidgets.QLineEdit(psw_change_Form)
        self.old_psw_le.setMaxLength(20)
        self.old_psw_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_psw_le.setObjectName("old_psw_le")
        self.verticalLayout_2.addWidget(self.old_psw_le)
        self.new_psw_le = QtWidgets.QLineEdit(psw_change_Form)
        self.new_psw_le.setMaxLength(20)
        self.new_psw_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_psw_le.setObjectName("new_psw_le")
        self.verticalLayout_2.addWidget(self.new_psw_le)
        self.check_psw_le = QtWidgets.QLineEdit(psw_change_Form)
        self.check_psw_le.setMaxLength(20)
        self.check_psw_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.check_psw_le.setObjectName("check_psw_le")
        self.verticalLayout_2.addWidget(self.check_psw_le)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.old_psw_echo = QtWidgets.QLabel(psw_change_Form)
        self.old_psw_echo.setObjectName("old_psw_echo")
        self.verticalLayout_3.addWidget(self.old_psw_echo)
        self.new_psw_echo = QtWidgets.QLabel(psw_change_Form)
        self.new_psw_echo.setObjectName("new_psw_echo")
        self.verticalLayout_3.addWidget(self.new_psw_echo)
        self.check_psw_echo = QtWidgets.QLabel(psw_change_Form)
        self.check_psw_echo.setObjectName("check_psw_echo")
        self.verticalLayout_3.addWidget(self.check_psw_echo)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.psw_change_btn = QtWidgets.QPushButton(psw_change_Form)
        self.psw_change_btn.setObjectName("psw_change_btn")
        self.verticalLayout_4.addWidget(self.psw_change_btn)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(psw_change_Form)
        QtCore.QMetaObject.connectSlotsByName(psw_change_Form)

    def retranslateUi(self, psw_change_Form):
        _translate = QtCore.QCoreApplication.translate
        psw_change_Form.setWindowTitle(_translate("psw_change_Form", "更换密码"))
        self.label.setText(_translate("psw_change_Form", "旧密码："))
        self.label_2.setText(_translate("psw_change_Form", "新密码："))
        self.label_3.setText(_translate("psw_change_Form", "再次确认："))
        self.old_psw_echo.setText(_translate("psw_change_Form", "..."))
        self.new_psw_echo.setText(_translate("psw_change_Form", "..."))
        self.check_psw_echo.setText(_translate("psw_change_Form", "..."))
        self.psw_change_btn.setText(_translate("psw_change_Form", "更换密码"))

