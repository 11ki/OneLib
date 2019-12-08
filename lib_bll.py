import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint
from PyQt5.QtGui import QPalette
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QMenu, QMessageBox, QToolTip
from lib_dal import *
import sys
import os

#业务逻辑
class Business_Logic:
    def __init__(self, window, login, ur, rq, bq, brq, rbrq, ri, bi, rud, bud, bbk, rbk, pswc):
        self.user_id = None
        self.user_name = None
        self.user_role = None

        self.sql = SQLServer()
        self.window = window
        self.ur = ur
        self.pswc = pswc
        self.rq = rq
        self.bq = bq
        self.brq = brq
        self.rbrq = rbrq
        self.ri = ri
        self.bi = bi
        self.rud = rud
        self.bud = bud
        self.bbk = bbk
        self.rbk = rbk
        self.login = login

        self.pe_red = QPalette()
        self.pe_red.setColor(QPalette.WindowText,Qt.red)

    def msg(self, widget, context):
        echo = QMessageBox.information(widget, "提示", context, QMessageBox.Yes)

    def w_msg(self, widget, context):
        # echo = QMessageBox.warning(widget, "确认", context, QMessageBox.Yes, QMessageBox.No)
        # if echo == QMessageBox.Yes:
        #     print('Y')
        # elif echo == QMessageBox.No:
        #     print('N')
        echo = QMessageBox(QMessageBox.Warning, "确认", context, QMessageBox.NoButton, widget)
        y_btn = echo.addButton("确定", QMessageBox.AcceptRole)
        n_btn = echo.addButton("取消", QMessageBox.RejectRole)
        echo.exec_()
        if echo.clickedButton() == y_btn:
            return 1
        elif echo.clickedButton() == n_btn:
            return 0

    #登陆管理
    def login_manage(self):
        rdid = self.login.sub.user_le.text()
        rdid = "rdID=\'" + rdid + "\'"
        result = self.sql.ExecQuery("TB_Reader", rdid)
        if len(result) == 0:
            self.login.sub.prompt_le.setText("")
            self.login.sub.prompt_le.setText("无此用户！")
            self.login.sub.prompt_le.setPalette(self.pe_red)
            # xy = QPoint(self.login.geometry().x()+self.login.sub.user_le.x(),self.login.geometry().y()+self.login.sub.user_le.y())
            # QToolTip.showText(xy, "无此用户！")
            self.login.sub.password_le.clear()
        elif result[0][9] == "挂失":
            self.login.sub.prompt_le.setText("")
            self.login.sub.prompt_le.setText("此账号已挂失！")
            self.login.sub.prompt_le.setPalette(self.pe_red)
            self.login.sub.password_le.clear()
        elif result[0][9] == "注销":
            self.login.sub.prompt_le.setText("")
            self.login.sub.prompt_le.setText("此账号已注销！")
            self.login.sub.prompt_le.setPalette(self.pe_red)
            self.login.sub.password_le.clear()
        elif result[0][11] != self.login.sub.password_le.text():
            self.login.sub.prompt_le.setText("")
            self.login.sub.prompt_le.setText("密码错误！")
            self.login.sub.prompt_le.setPalette(self.pe_red)
            self.login.sub.password_le.clear()
        elif result[0][11] == self.login.sub.password_le.text():
            self.user_id = result[0][0]
            self.user_name = result[0][1]
            self.user_role = result[0][12]
            self.user_load(result[0][12])

    def user_load(self, role):
        self.login.close()
        self.window.main_ui.statusBar.showMessage("Hi！" + self.user_name + "同学，欢迎来到图书管理系统")
        self.ur_load()
        self.table_ini()
        if role == 0: #读者
            self.close_tab(0)
            self.close_tab(1)
            self.window.main_ui.rd_insert.setVisible(False)
            self.window.main_ui.action_borrow.setVisible(False)
            self.window.main_ui.action_return.setVisible(False)
            # self.window.main_ui.action_update.setVisible(False)
        elif role == 1: #借书证管理
            self.window.main_ui.action_borrow.setVisible(False)
            self.window.main_ui.action_return.setVisible(False)
        elif role == 2: #图书管理
            self.close_tab(0)
            self.close_tab(1)
            self.window.main_ui.action_borrow.setVisible(False)
            self.window.main_ui.action_return.setVisible(False)
        elif role == 4: #借阅管理
            self.close_tab(0)
            self.close_tab(1)
            self.window.main_ui.rd_insert.setVisible(False)
        self.window.show()

    def ur_load(self):
        column = "rdName = \'" + self.user_name + "\'"
        result = self.sql.ExecQuery("TB_Reader", column)
        self.ur.sub.id.setText(str(result[0][0]))
        self.ur.sub.name.setText(result[0][1])
        self.ur.sub.sex.setText(result[0][2])
        if result[0][3] == 0:
            self.ur.sub.type.setText('校职工')
        elif result[0][3] == 1:
            self.ur.sub.type.setText('博士生')
        elif result[0][3] == 2:
            self.ur.sub.type.setText('硕士生')
        elif result[0][3] == 3:
            self.ur.sub.type.setText('本科生')
        elif result[0][3] == 4:
            self.ur.sub.type.setText('专科生')
        self.ur.sub.dept.setText(result[0][4])
        self.ur.sub.phone.setText(str(result[0][5]))
        self.ur.sub.email.setText(result[0][6])
        self.ur.sub.date.setText(str(result[0][7]).split('.')[0])
        self.ur.sub.status.setText(str(result[0][9]))
        self.ur.sub.qty.setText(str(result[0][10]))
        if result[0][12] == 0:
            self.ur.sub.roles.setText('读者')
        elif result[0][12] == 1:
            self.ur.sub.roles.setText('借书证管理员')
        elif result[0][12] == 2:
            self.ur.sub.roles.setText('图书管理员')
        elif result[0][12] == 4:
            self.ur.sub.roles.setText('借阅管理员')
        elif result[0][12] == 8:
            self.ur.sub.roles.setText('系统管理员')

    def psw_change(self):
        column = "rdName = \'" + self.user_name + "\'"
        result = self.sql.ExecQuery("TB_Reader", column)
        if result[0][11] == self.pswc.sub.old_psw_le.text():
            if self.pswc.sub.new_psw_le.text() == self.pswc.sub.check_psw_le.text():
                self.sql.ExecUpdate("TB_Reader", "rdPwd = \'" + self.pswc.sub.new_psw_le.text() + "\'" , column)
                self.pswc.close()
                self.msg(self.ur, "密码更换成功！请重新登陆！")
                # python = sys.executable
                # os.execl(python, sys.executable, *sys.argv)
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                self.pswc.sub.new_psw_echo.setText("...")
                self.pswc.sub.old_psw_echo.setText("...")
                self.pswc.sub.check_psw_echo.setText("密码不匹配")
                self.pswc.sub.check_psw_echo.setPalette(self.pe_red)
                self.pswc.sub.check_psw_le.clear()
        else:
            self.pswc.sub.new_psw_echo.setText("...")
            self.pswc.sub.check_psw_echo.setText("...")
            self.pswc.sub.old_psw_echo.setText("密码错误")
            self.pswc.sub.old_psw_echo.setPalette(self.pe_red)
            self.pswc.sub.old_psw_le.clear()

    #右键菜单
    # def custom_right_menu(self, tw_name):
    #     menu = QMenu()
    #     add_ = menu.addAction("修改")
    #     del_ = menu.addAction("删除")
    #     # action = menu.exec_(self.main_ui.r_tw.mapToGlobal(pos))
    #     action = menu.exec_(QtGui.QCursor.pos())
    #     if action == add_:
    #         if tw_name == "r_tw":
    #             print('1')
    #         elif tw_name == "b_tw":
    #             print('2')
    #         elif tw_name == "rt_tw":
    #             print('3')
    #     elif action == del_:
    #         if tw_name == "r_tw":
    #             print('1')
    #         elif tw_name == "b_tw":
    #             print('2')
    #         elif tw_name == "rt_tw":
    #             print('3')

    def close_tab(self,index):
        self.window.main_ui.tabWidget.removeTab(index)

    #提示
    def outSelect(self, Item=None):
        if Item == None:
            return
        # print(Item.text())
        self.window.main_ui.tabWidget.setToolTip(Item.text())

    def update_item_data(self, *data):
        if data[0] == "r_tw":
            self.window.main_ui.r_tw.setItem(data[1], data[2], QTableWidgetItem(data[3]))
        elif data[0] == "b_tw":
            self.window.main_ui.b_tw.setItem(data[1], data[2], QTableWidgetItem(data[3]))
        elif data[0] == "rt_tw":
            self.window.main_ui.rt_tw.setItem(data[1], data[2], QTableWidgetItem(data[3]))
        elif data[0] == "br_tw":
            self.window.main_ui.br_tw.setItem(data[1], data[2], QTableWidgetItem(data[3]))

    def table_ini(self):
        column = "rdName = \'" + self.user_name + "\'"
        result = self.sql.ExecQuery("TB_Reader", column)
        if result[0][12] == 8 or result[0][12] == 1:
            result = self.sql.ExecQuery("TB_Reader", "1=1")
            self.window.main_ui.r_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("r_tw", m, n, str(result[m][n]))

            result = self.sql.ExecQuery("TB_Book", "1=1")
            self.window.main_ui.b_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("b_tw", m, n, str(result[m][n]))

            result = self.sql.ExecQuery("TB_ReaderType", "1=1")
            self.window.main_ui.rt_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("rt_tw", m, n, str(result[m][n]))

            result = self.sql.ExecQuery("TB_Borrow", "1=1")
            self.window.main_ui.br_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("br_tw", m, n, str(result[m][n]))
        elif result[0][12] == 0 or result[0][12] == 2 or result[0][12] == 4:
            result = self.sql.ExecQuery("TB_Book", "1=1")
            self.window.main_ui.b_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("b_tw", m, n, str(result[m][n]))

            result = self.sql.ExecQuery("TB_Borrow", "rdID = " + str(self.user_id))
            self.window.main_ui.br_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("br_tw", m, n, str(result[m][n]))

    def query_show(self):
        cw_name = self.window.main_ui.tabWidget.currentWidget().objectName()
        if cw_name == "r_tab":
            self.rq.show()
        elif cw_name == "b_tab":
            self.bq.show()
        elif cw_name == "br_tab":
            if self.user_role == 4 or self.user_role == 8:
                self.brq.show()
            else:
                self.rbrq.show()

    def insert_show(self):
        cw_name = self.window.main_ui.tabWidget.currentWidget().objectName()
        if cw_name == "r_tab":
            if self.user_role == 1 or self.user_role == 8:
                self.ri.show()
        elif cw_name == "b_tab":
            if self.user_role == 2 or self.user_role == 8:
                self.bi.show()

    def r_query(self):
        if self.rq.sub.query_cb.currentIndex() == 0 :
            cn = "rdID LIKE \'%" + self.rq.sub.query_le.text() + "%\'"
        else:
            cn = "rdName LIKE \'%" + self.rq.sub.query_le.text() + "%\'"
        result = self.sql.ExecQuery("TB_Reader", cn)
        if result == 0:
            self.msg(self.bq, "输入有误！")
        else:
            self.window.main_ui.r_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("r_tw", m, n, str(result[m][n]))

    def b_query(self):
        if self.bq.sub.query_cb.currentIndex() == 0 :
            cn = "bkCode LIKE \'%" + self.bq.sub.query_le.text() + "%\'"
        else:
            cn = "bkName LIKE \'%" + self.bq.sub.query_le.text() + "%\'"
        result = self.sql.ExecQuery("TB_Book", cn)
        if result == 0:
            self.msg(self.bq, "输入有误！")
        else:
            self.window.main_ui.b_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("b_tw", m, n, str(result[m][n]))

    def br_query(self):
        if self.brq.sub.query_cb.currentIndex() == 0 :
            if self.brq.sub.all_rb.isChecked() == True:
                cn = "rdID = " + self.brq.sub.query_le.text()
            else:
                cn = "rdID = " + self.brq.sub.query_le.text() + " AND lsHasReturn = 0"
        else:
            if self.brq.sub.all_rb.isChecked() == True:
                cn = "bkID = " + self.brq.sub.query_le.text()
            else:
                cn = "bkID = " + self.brq.sub.query_le.text() + " AND lsHasReturn = 0"
        result = self.sql.ExecQuery("TB_Borrow", cn)
        if len(result) == 0:
            self.msg(self.brq, "未找到相关记录！")
        else:
            self.window.main_ui.br_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("br_tw", m, n, str(result[m][n]))

    def r_br_query(self):
        if self.rbrq.sub.all_rb.isChecked() == True:
            cn = "rdID = " + str(self.user_id) + " AND bkID = " + self.rbrq.sub.query_le.text()
        else:
            cn = "rdID = " + str(self.user_id) + " AND bkID = " + self.rbrq.sub.query_le.text() + " AND lsHasReturn = 0"
        result = self.sql.ExecQuery("TB_Borrow", cn)
        if len(result) == 0:
            self.msg(self.rbrq, "未找到相关记录！")
        else:
            self.window.main_ui.br_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("br_tw", m, n, str(result[m][n]))

    def r_br_q_all(self):
        cn = "rdID = " + str(self.user_id) + " AND lsHasReturn = 0"
        result = self.sql.ExecQuery("TB_Borrow", cn)
        if len(result) == 0:
            self.msg(self.rbrq, "未找到相关记录！")
        else:
            self.window.main_ui.br_tw.setRowCount(len(result))
            for m in range(len(result)):
                for n in range(len(result[0])):
                    self.update_item_data("br_tw", m, n, str(result[m][n]))

    def r_insert(self):
        rdID = self.ri.sub.id_le.text()
        rdName = "\'" + self.ri.sub.name_le.text() + "\'"
        rdSex = "\'" + self.ri.sub.sex_cb.currentText() + "\'"
        rdType = str(self.ri.sub.type_cb.currentIndex())
        rdDept = "\'" + self.ri.sub.dept_le.text() + "\'"
        rdPhone = "\'" + self.ri.sub.phone_le.text() + "\'"
        rdEmail = "\'" + self.ri.sub.email_le.text() + "\'"
        rdDateReg = "GETDATE()"
        rdPhoto = "NULL"
        rdStatus = "\'" + self.ri.sub.status_le.text() + "\'"
        rdBorrowQty = "0"
        if self.ri.sub.psw_le.text() == '':
            rdPwd = "\'123\'"
        else:
            rdPwd = "\'" + self.ri.sub.psw_le.text() + "\'"
        if self.ri.sub.roles_cb.currentIndex() == 0:
            rdAdminRoles = " 0"
        elif self.ri.sub.roles_cb.currentIndex() == 1:
            rdAdminRoles = "1"
        elif self.ri.sub.roles_cb.currentIndex() == 2:
            rdAdminRoles = "2"
        elif self.ri.sub.roles_cb.currentIndex() == 3:
            rdAdminRoles = "4"
        else:
            rdAdminRoles = "8"
        result = self.sql.ExecInsert("TB_Reader", rdID, rdName, rdSex, rdType, rdDept, rdPhone, rdEmail, rdDateReg, rdPhoto, rdStatus, rdBorrowQty, rdPwd, rdAdminRoles)
        if result == 2627:
            self.msg(self.ri, "用户已存在！")
        else:
            self.msg(self.ri, "添加成功！")
            self.table_ini()

    def b_insert(self):
        bkID = self.bi.sub.id_le.text()
        bkCode = "\'" + self.bi.sub.code_le.text() + "\'"
        bkName = "\'" + self.bi.sub.name_le.text() + "\'"
        bkAuthor = "\'" + self.bi.sub.author_le.text() + "\'"
        bkPress = "\'" + self.bi.sub.press_le.text() + "\'"
        bkDatePress = "\'" + self.bi.sub.datepress_le.text() + "\'"
        bkISBN = "\'" + self.bi.sub.ISBN_le.text() + "\'"
        bkLanguage = str(self.bi.sub.language_cb.currentIndex())
        bkPages = str(self.bi.sub.pages_le.text())
        bkPrice = self.bi.sub.price_le.text()
        bkDateln = "GETDATE()"
        bkBrief = "\'" + self.bi.sub.brief_le.text() + "\'"
        bkCover = "NULL"
        bkStatus = "\'" + self.bi.sub.status_cb.currentText() + "\'"
        result = self.sql.ExecInsert("TB_Book", bkID, bkCode, bkName, bkAuthor, bkPress, bkDatePress, bkISBN, bkLanguage, bkPages, bkPrice, bkDateln, bkBrief, bkCover, bkStatus)
        # if result == 2627:
        #     self.msg(self.bi, "图书已存在！")
        # else:
        self.msg(self.bi, "添加成功！")
        self.table_ini()

    def r_ud(self, row):
        column = "rdID = " + str(self.window.main_ui.r_tw.item(row, 0).text())
        result = self.sql.ExecQuery("TB_Reader", column)
        self.rud.sub.id_le.setText(str(result[0][0]))
        self.rud.sub.name_le.setText(str(result[0][1]))
        if result[0][2] == "男":
            self.rud.sub.sex_cb.setCurrentIndex(0)
        elif result[0][2] == "女":
            self.rud.sub.sex_cb.setCurrentIndex(1)
        self.rud.sub.type_cb.setCurrentIndex(result[0][3])
        self.rud.sub.dept_le.setText(str(result[0][4]))
        self.rud.sub.phone_le.setText(str(result[0][5]))
        self.rud.sub.email_le.setText(str(result[0][6]))
        self.rud.sub.date_le.setText(str(result[0][7]).split('.')[0])
        if result[0][9] == "有效":
            self.rud.sub.status_cb.setCurrentIndex(0)
        elif result[0][9] == "挂失":
            self.rud.sub.status_cb.setCurrentIndex(1)
        elif result[0][9] == "注销":
            self.rud.sub.status_cb.setCurrentIndex(2)
        self.rud.sub.bwqty_le.setText(str(result[0][10]))
        self.rud.sub.psw_le.setText(result[0][11])
        if result[0][12] == 4:
            self.rud.sub.roles_cb.setCurrentIndex(3)
        elif result[0][12] == 8:
            self.rud.sub.roles_cb.setCurrentIndex(4)
        else:
            self.rud.sub.roles_cb.setCurrentIndex(result[0][12])
        self.rud.show()

    def b_ud(self, row):
        if self.user_role == 0 or self.user_role == 1 or self.user_role == 4:
            self.bud.sub.code_le.setEnabled(False)
            self.bud.sub.name_le.setEnabled(False)
            self.bud.sub.author_le.setEnabled(False)
            self.bud.sub.press_le.setEnabled(False)
            self.bud.sub.datepress_le.setEnabled(False)
            self.bud.sub.ISBN_le.setEnabled(False)
            self.bud.sub.language_cb.setEnabled(False)
            self.bud.sub.pages_le.setEnabled(False)
            self.bud.sub.price_le.setEnabled(False)
            self.bud.sub.dateln_le.setEnabled(False)
            self.bud.sub.dateln_cb.setVisible(False)
            self.bud.sub.brief_le.setEnabled(False)
            self.bud.sub.status_cb.setEnabled(False)
            self.bud.sub.update_btn.setVisible(False)
            self.bud.sub.delete_btn.setVisible(False)
            self.bud.sub.load_photo_btn.setVisible(False)
        column = "bkID = " + str(self.window.main_ui.b_tw.item(row, 0).text())
        result = self.sql.ExecQuery("TB_Book", column)
        self.bud.sub.id_le.setText(str(result[0][0]))
        self.bud.sub.code_le.setText(str(result[0][1]))
        self.bud.sub.name_le.setText(str(result[0][2]))
        self.bud.sub.author_le.setText(str(result[0][3]))
        self.bud.sub.press_le.setText(str(result[0][4]))
        self.bud.sub.datepress_le.setText(str(result[0][5]))
        self.bud.sub.ISBN_le.setText(str(result[0][6]))
        self.bud.sub.language_cb.setCurrentIndex(result[0][7])
        self.bud.sub.pages_le.setText(str(result[0][8]))
        self.bud.sub.price_le.setText(str(result[0][9]))
        self.bud.sub.dateln_le.setText(str(result[0][10]).split('.')[0])
        self.bud.sub.brief_le.setText(str(result[0][11]))
        if result[0][13] == "在馆":
            self.bud.sub.status_cb.setCurrentIndex(0)
        elif result[0][13] == "借出":
            self.bud.sub.status_cb.setCurrentIndex(1)
        elif result[0][13] == "遗失":
            self.bud.sub.status_cb.setCurrentIndex(2)
        elif result[0][13] == "变卖":
            self.bud.sub.status_cb.setCurrentIndex(3)
        elif result[0][13] == "销毁":
            self.bud.sub.status_cb.setCurrentIndex(4)
        self.bud.show()

    def r_ud_u(self):
        rdID = "rdID = " + self.rud.sub.id_le.text()
        rdName = "rdName = \'" + self.rud.sub.name_le.text() + "\'"
        rdSex = "rdSex =\'" + self.rud.sub.sex_cb.currentText() + "\'"
        rdType = "rdType = " + str(self.rud.sub.type_cb.currentIndex())
        rdDept = "rdDept = \'" + self.rud.sub.dept_le.text() + "\'"
        rdPhone = "rdPhone = \'" + self.rud.sub.phone_le.text() + "\'"
        rdEmail = "rdEmail = \'" + self.rud.sub.email_le.text() + "\'"
        rdStatus = "rdStatus = \'" + self.rud.sub.status_cb.currentText() + "\'"
        if self.rud.sub.psw_le.text() == "":
            self.msg(self.rud, "密码不能为空！")
            return
        else:
            rdPwd = "rdPwd = \'" + self.rud.sub.psw_le.text() + "\'"
        if self.rud.sub.roles_cb.currentIndex() == 3:
            rdAdminRoles = "rdAdminRoles = 4"
        elif self.rud.sub.roles_cb.currentIndex() == 4:
            rdAdminRoles = "rdAdminRoles = 8"
        else:
            rdAdminRoles = "rdAdminRoles = " + str(self.rud.sub.roles_cb.currentIndex())
        if self.rud.sub.date_cb.isChecked() == True:
            rdDateReg = "rdDateReg = GETDATE()"
            self.sql.ExecUpdate("TB_Reader", rdName, rdSex, rdType, rdDept, rdPhone, rdEmail, rdDateReg, rdStatus, rdPwd, rdAdminRoles, rdID)
        else:
            self.sql.ExecUpdate("TB_Reader", rdName, rdSex, rdType, rdDept, rdPhone, rdEmail, rdStatus, rdPwd, rdAdminRoles, rdID)
        self.msg(self.rud, "更新成功！")
        self.table_ini()

    def b_ud_u(self):
        bkID = "bkID = " + self.bud.sub.id_le.text()
        bkCode = "bkCode = \'" + self.bud.sub.code_le.text() + "\'"
        bkName = "bkName = \'" + self.bud.sub.name_le.text() + "\'"
        bkAuthor = "bkAuthor =\'" + self.bud.sub.author_le.text() + "\'"
        bkPress = "bkPress = " + self.bud.sub.press_le.text()
        bkDatePress = "bkDatePress = \'" + self.bud.sub.datepress_le.text() + "\'"
        bkISBN = "bkISBN = \'" + self.bud.sub.ISBN_le.text() + "\'"
        bkLanguage = "bkLanguage = " + str(self.bud.sub.language_cb.currentIndex())
        bkPages = "bkPages = " + self.bud.sub.pages_le.text()
        bkPrice = "bkPrice = " + self.bud.sub.price_le.text()
        bkBrief = "bkBrief = \'" + self.bud.sub.brief_le.text() + "\'"
        bkStatus = "bkStatus = \'" + self.bud.sub.status_cb.currentText() + "\'"
        if self.bud.sub.dateln_cb.isChecked() == True:
            bkDateln = "bkDateln = GETDATE()"
            self.sql.ExecUpdate("TB_Book", bkCode, bkName, bkAuthor, bkPress, bkDatePress, bkISBN, bkLanguage, bkPages, bkPrice, bkDateln, bkBrief, bkStatus, bkID)
        else:
            self.sql.ExecUpdate("TB_Book", bkCode, bkName, bkAuthor, bkPress, bkDatePress, bkISBN, bkLanguage, bkPages, bkPrice, bkBrief, bkStatus, bkID)
        self.msg(self.rud, "更新成功！")
        self.table_ini()

    def r_ud_d(self):
        rdID = "rdID = " + self.rud.sub.id_le.text()
        if self.rud.sub.bwqty_le.text() != "0":
            self.msg(self.rud, "此用户有未归还图书，无法删除！")
            return
        echo = self.w_msg(self.rud, "确认删除此用户？")
        if echo == 1:
            self.sql.ExecDelete("TB_Reader", rdID)
            self.rud.close()
            self.table_ini()
        else:
            return

    def b_ud_d(self):
        bkID = "bkID = " + self.bud.sub.id_le.text()
        echo = self.w_msg(self.rud, "确认删除此书？")
        if echo == 1:
            self.sql.ExecDelete("TB_Book", bkID)
            self.bud.close()
            self.table_ini()
        else:
            return

    def b_book_ini(self):
        result = self.sql.ExecQuery("TB_Borrow", "1=1")
        if len(result) == 0:
            self.bbk.sub.br_id_le.setText("0")
        else:
            result.sort(key=lambda x: x[0], reverse=True)
            self.bbk.sub.br_id_le.setText(str(result[0][0]+1))
        self.bbk.sub.a_id_le.setText(self.user_name)
        self.bbk.show()

    def r_book_ini(self):
        self.rbk.sub.a_id_le.setText(self.user_name)
        self.rbk.show()

    def b_book(self):
        br_id = self.bbk.sub.br_id_le.text()
        r_id = self.bbk.sub.r_id_le.text()
        b_id = self.bbk.sub.b_id_le.text()
        a_id = self.bbk.sub.a_id_le.text()
        result = self.sql.ExecBorrow(br_id, r_id, b_id, a_id)
        if result != None:
            self.msg(self.bbk, result)
        else:
            self.table_ini()
            self.msg(self.bbk, "借书成功！")

    def r_book(self):
        # br_id = self.rbk.sub.br_id_le.text()
        r_id = self.rbk.sub.r_id_le.text()
        b_id = self.rbk.sub.b_id_le.text()
        a_id = self.rbk.sub.a_id_le.text()
        result = self.sql.ExecReturn(r_id, b_id, a_id)
        if result != None:
            self.msg(self.rbk, result)
        else:
            self.table_ini()
            self.msg(self.rbk, "还书成功！")

#更新线程
class UpdateData(QThread):
    update_date = pyqtSignal(str) # 自定义信号

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            time.sleep(1)

if __name__=='__main__':
    Business_Logic()