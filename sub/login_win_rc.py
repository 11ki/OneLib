# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_Form(object):
    def setupUi(self, login_Form):
        login_Form.setObjectName("login_Form")
        login_Form.resize(280, 277)
        self.gridLayout_2 = QtWidgets.QGridLayout(login_Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lib_le = QtWidgets.QLabel(login_Form)
        self.lib_le.setText("")
        self.lib_le.setPixmap(QtGui.QPixmap(":/Icon/lib.png"))
        self.lib_le.setAlignment(QtCore.Qt.AlignCenter)
        self.lib_le.setObjectName("lib_le")
        self.gridLayout.addWidget(self.lib_le, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(login_Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icon/user.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(login_Form)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Icon/password.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.user_le = QtWidgets.QLineEdit(login_Form)
        self.user_le.setObjectName("user_le")
        self.verticalLayout_2.addWidget(self.user_le)
        self.password_le = QtWidgets.QLineEdit(login_Form)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.verticalLayout_2.addWidget(self.password_le)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_btn = QtWidgets.QPushButton(login_Form)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_2.addWidget(self.login_btn)
        self.re_btn = QtWidgets.QPushButton(login_Form)
        self.re_btn.setObjectName("re_btn")
        self.horizontalLayout_2.addWidget(self.re_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.prompt_le = QtWidgets.QLabel(login_Form)
        self.prompt_le.setAlignment(QtCore.Qt.AlignCenter)
        self.prompt_le.setObjectName("prompt_le")
        self.gridLayout.addWidget(self.prompt_le, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(login_Form)
        self.re_btn.clicked.connect(self.user_le.clear)
        self.re_btn.clicked.connect(self.password_le.clear)
        QtCore.QMetaObject.connectSlotsByName(login_Form)

    def retranslateUi(self, login_Form):
        _translate = QtCore.QCoreApplication.translate
        login_Form.setWindowTitle(_translate("login_Form", "用户登录"))
        self.user_le.setPlaceholderText(_translate("login_Form", "读者编号/借书证号"))
        self.password_le.setPlaceholderText(_translate("login_Form", "密码"))
        self.login_btn.setText(_translate("login_Form", "登陆"))
        self.re_btn.setText(_translate("login_Form", "重置"))
        self.prompt_le.setText(_translate("login_Form", "欢迎登陆图书管理系统！"))

import img_rcc_rc
