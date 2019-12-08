# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'r_br_query_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_r_br_query_Form(object):
    def setupUi(self, r_br_query_Form):
        r_br_query_Form.setObjectName("r_br_query_Form")
        r_br_query_Form.resize(400, 129)
        self.gridLayout = QtWidgets.QGridLayout(r_br_query_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(r_br_query_Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.query_le = QtWidgets.QLineEdit(r_br_query_Form)
        self.query_le.setText("")
        self.query_le.setObjectName("query_le")
        self.horizontalLayout.addWidget(self.query_le)
        self.query_bn = QtWidgets.QPushButton(r_br_query_Form)
        self.query_bn.setObjectName("query_bn")
        self.horizontalLayout.addWidget(self.query_bn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_rb = QtWidgets.QRadioButton(r_br_query_Form)
        self.all_rb.setChecked(True)
        self.all_rb.setObjectName("all_rb")
        self.verticalLayout.addWidget(self.all_rb)
        self.notre_rb = QtWidgets.QRadioButton(r_br_query_Form)
        self.notre_rb.setObjectName("notre_rb")
        self.verticalLayout.addWidget(self.notre_rb)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(r_br_query_Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.q_all_btn = QtWidgets.QPushButton(r_br_query_Form)
        self.q_all_btn.setObjectName("q_all_btn")
        self.verticalLayout_2.addWidget(self.q_all_btn)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(r_br_query_Form)
        QtCore.QMetaObject.connectSlotsByName(r_br_query_Form)

    def retranslateUi(self, r_br_query_Form):
        _translate = QtCore.QCoreApplication.translate
        r_br_query_Form.setWindowTitle(_translate("r_br_query_Form", "查询"))
        self.label.setText(_translate("r_br_query_Form", "图书序号："))
        self.query_bn.setText(_translate("r_br_query_Form", "搜索"))
        self.all_rb.setText(_translate("r_br_query_Form", "查询全部记录"))
        self.notre_rb.setText(_translate("r_br_query_Form", "查询未还记录"))
        self.q_all_btn.setText(_translate("r_br_query_Form", "一键查询全部未还图书"))

