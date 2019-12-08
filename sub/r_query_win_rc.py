# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'r_query_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_r_query_Form(object):
    def setupUi(self, r_query_Form):
        r_query_Form.setObjectName("r_query_Form")
        r_query_Form.resize(300, 45)
        r_query_Form.setAccessibleName("")
        self.gridLayout_3 = QtWidgets.QGridLayout(r_query_Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.query_cb = QtWidgets.QComboBox(r_query_Form)
        self.query_cb.setObjectName("query_cb")
        self.query_cb.addItem("")
        self.query_cb.addItem("")
        self.horizontalLayout.addWidget(self.query_cb)
        self.query_le = QtWidgets.QLineEdit(r_query_Form)
        self.query_le.setText("")
        self.query_le.setObjectName("query_le")
        self.horizontalLayout.addWidget(self.query_le)
        self.query_bn = QtWidgets.QPushButton(r_query_Form)
        self.query_bn.setObjectName("query_bn")
        self.horizontalLayout.addWidget(self.query_bn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(r_query_Form)
        QtCore.QMetaObject.connectSlotsByName(r_query_Form)

    def retranslateUi(self, r_query_Form):
        _translate = QtCore.QCoreApplication.translate
        r_query_Form.setWindowTitle(_translate("r_query_Form", "查询"))
        self.query_cb.setItemText(0, _translate("r_query_Form", "编号"))
        self.query_cb.setItemText(1, _translate("r_query_Form", "姓名"))
        self.query_bn.setText(_translate("r_query_Form", "搜索"))

