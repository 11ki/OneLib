# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b_book.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_br_book_Form(object):
    def setupUi(self, br_book_Form):
        br_book_Form.setObjectName("br_book_Form")
        br_book_Form.resize(250, 151)
        self.gridLayout = QtWidgets.QGridLayout(br_book_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.br_id_label = QtWidgets.QLabel(br_book_Form)
        self.br_id_label.setObjectName("br_id_label")
        self.verticalLayout.addWidget(self.br_id_label)
        self.r_id_label = QtWidgets.QLabel(br_book_Form)
        self.r_id_label.setObjectName("r_id_label")
        self.verticalLayout.addWidget(self.r_id_label)
        self.b_id_label = QtWidgets.QLabel(br_book_Form)
        self.b_id_label.setObjectName("b_id_label")
        self.verticalLayout.addWidget(self.b_id_label)
        self.a_id_label = QtWidgets.QLabel(br_book_Form)
        self.a_id_label.setObjectName("a_id_label")
        self.verticalLayout.addWidget(self.a_id_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.br_id_le = QtWidgets.QLineEdit(br_book_Form)
        self.br_id_le.setEnabled(False)
        self.br_id_le.setObjectName("br_id_le")
        self.verticalLayout_2.addWidget(self.br_id_le)
        self.r_id_le = QtWidgets.QLineEdit(br_book_Form)
        self.r_id_le.setObjectName("r_id_le")
        self.verticalLayout_2.addWidget(self.r_id_le)
        self.b_id_le = QtWidgets.QLineEdit(br_book_Form)
        self.b_id_le.setObjectName("b_id_le")
        self.verticalLayout_2.addWidget(self.b_id_le)
        self.a_id_le = QtWidgets.QLineEdit(br_book_Form)
        self.a_id_le.setEnabled(False)
        self.a_id_le.setObjectName("a_id_le")
        self.verticalLayout_2.addWidget(self.a_id_le)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.br_book_btn = QtWidgets.QPushButton(br_book_Form)
        self.br_book_btn.setObjectName("br_book_btn")
        self.verticalLayout_3.addWidget(self.br_book_btn)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(br_book_Form)
        QtCore.QMetaObject.connectSlotsByName(br_book_Form)

    def retranslateUi(self, br_book_Form):
        _translate = QtCore.QCoreApplication.translate
        br_book_Form.setWindowTitle(_translate("br_book_Form", "借书"))
        self.br_id_label.setText(_translate("br_book_Form", "借书序号："))
        self.r_id_label.setText(_translate("br_book_Form", "读者编号："))
        self.b_id_label.setText(_translate("br_book_Form", "图书序号："))
        self.a_id_label.setText(_translate("br_book_Form", "借书操作员："))
        self.br_book_btn.setText(_translate("br_book_Form", "确认借书"))

