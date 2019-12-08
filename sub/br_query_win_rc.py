# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'br_query_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_br_query_Form(object):
    def setupUi(self, br_query_Form):
        br_query_Form.setObjectName("br_query_Form")
        br_query_Form.resize(400, 91)
        self.gridLayout = QtWidgets.QGridLayout(br_query_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.query_cb = QtWidgets.QComboBox(br_query_Form)
        self.query_cb.setObjectName("query_cb")
        self.query_cb.addItem("")
        self.query_cb.addItem("")
        self.horizontalLayout.addWidget(self.query_cb)
        self.query_le = QtWidgets.QLineEdit(br_query_Form)
        self.query_le.setText("")
        self.query_le.setObjectName("query_le")
        self.horizontalLayout.addWidget(self.query_le)
        self.query_bn = QtWidgets.QPushButton(br_query_Form)
        self.query_bn.setObjectName("query_bn")
        self.horizontalLayout.addWidget(self.query_bn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_rb = QtWidgets.QRadioButton(br_query_Form)
        self.all_rb.setChecked(True)
        self.all_rb.setObjectName("all_rb")
        self.verticalLayout.addWidget(self.all_rb)
        self.notre_rb = QtWidgets.QRadioButton(br_query_Form)
        self.notre_rb.setObjectName("notre_rb")
        self.verticalLayout.addWidget(self.notre_rb)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(br_query_Form)
        QtCore.QMetaObject.connectSlotsByName(br_query_Form)

    def retranslateUi(self, br_query_Form):
        _translate = QtCore.QCoreApplication.translate
        br_query_Form.setWindowTitle(_translate("br_query_Form", "查询"))
        self.query_cb.setItemText(0, _translate("br_query_Form", "读者编号"))
        self.query_cb.setItemText(1, _translate("br_query_Form", "图书序号"))
        self.query_bn.setText(_translate("br_query_Form", "搜索"))
        self.all_rb.setText(_translate("br_query_Form", "查询全部记录"))
        self.notre_rb.setText(_translate("br_query_Form", "查询未还记录"))

