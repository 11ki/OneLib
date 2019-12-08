from PyQt5.QtGui import QIntValidator

from main_win_rc import *
from sub_win_rc import *
from lib_bll import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMenu, QHeaderView
import sys

class login_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_login_Form()
        self.sub.setupUi(self)
        self.sub.user_le.setValidator(QIntValidator(0, 999999999, self))
        self.setAttribute(Qt.WA_DeleteOnClose)

class main_win(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.main_ui.r_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_ui.b_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_ui.rt_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_ui.br_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def closeEvent(self, *args, **kwargs):
        sys.exit(app.exec_())

class user_room(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_user_room_Form()
        self.sub.setupUi(self)

class r_query_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_r_query_Form()
        self.sub.setupUi(self)

class b_query_win(r_query_win):
    def __init__(self):
        r_query_win.__init__(self)
        self.sub.query_cb.setItemText(1, "书名")

class br_query_win(r_query_win):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_br_query_Form()
        self.sub.setupUi(self)

class r_br_query_win(r_query_win):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_r_br_query_Form()
        self.sub.setupUi(self)

class r_insert_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_r_insert_Form()
        self.sub.setupUi(self)
        # self.setAttribute(Qt.WA_DeleteOnClose)
        self.sub.id_le.setValidator(QIntValidator(0, 999999999, self))

    def closeEvent(self, QCloseEvent):
        self.sub.id_le.clear()
        self.sub.name_le.clear()
        self.sub.sex_cb.setCurrentIndex(0)
        self.sub.type_cb.setCurrentIndex(3)
        self.sub.dept_le.clear()
        self.sub.phone_le.clear()
        self.sub.email_le.clear()
        self.sub.psw_le.clear()
        self.sub.roles_cb.setCurrentIndex(0)

class b_insert_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_b_insert_Form()
        self.sub.setupUi(self)
        self.sub.id_le.setValidator(QIntValidator(0, 999999999, self))
        self.sub.pages_le.setValidator(QIntValidator(0, 999999999, self))
        self.sql = SQLServer()
        result = self.sql.ExecQuery("TB_Book", "1 = 1")
        result.sort(key=lambda x:x[0], reverse=True)
        self.sub.id_le.setText(str(result[0][0]+1))

class r_ud_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_r_ud_Form()
        self.sub.setupUi(self)

class b_ud_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_b_ud_Form()
        self.sub.setupUi(self)

class psw_change_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_psw_change_Form()
        self.sub.setupUi(self)
    def closeEvent(self, QCloseEvent):
        self.sub.old_psw_le.clear()
        self.sub.new_psw_le.clear()
        self.sub.check_psw_le.clear()
        self.sub.old_psw_echo.setText("...")
        self.sub.new_psw_echo.setText("...")
        self.sub.check_psw_echo.setText("...")

class b_book_win(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_br_book_Form()
        self.sub.setupUi(self)
        self.sub.r_id_le.setValidator(QIntValidator(0, 999999999, self))
        self.sub.b_id_le.setValidator(QIntValidator(0, 999999999, self))

    def closeEvent(self, QCloseEvent):
        self.sub.r_id_le.clear()
        self.sub.b_id_le.clear()

class r_book_win(b_book_win):
    def __init__(self):
        QDialog.__init__(self)
        self.sub = Ui_br_book_Form()
        self.sub.setupUi(self)

        # self.sub.br_id_le.setEnabled(True)
        self.sub.br_id_le.setVisible(False)
        self.sub.br_id_label.setVisible(False)
        self.setWindowTitle("还书")
        self.sub.a_id_label.setText("还书操作员：")
        self.sub.br_book_btn.setText("确认还书")
    def closeEvent(self, QCloseEvent):
        self.sub.r_id_le.clear()
        self.sub.b_id_le.clear()
        self.sub.br_id_le.clear()

class connect_win:
    def __init__(self):
        self.login = login_win()
        self.window = main_win()
        self.ur = user_room()
        self.pswc = psw_change_win()
        self.rq = r_query_win()
        self.ri = r_insert_win()
        self.rbrq = r_br_query_win()
        self.rud = r_ud_win()
        self.bq = b_query_win()
        self.brq = br_query_win()
        self.bi =b_insert_win()
        self.bud = b_ud_win()
        self.bbk = b_book_win()
        self.rbk = r_book_win()
        self.sql = SQLServer()
        self.bll = Business_Logic(self.window, self.login, self.ur, self.rq, self.bq, self.brq, self.rbrq, self.ri, self.bi, self.rud, self.bud, self.bbk, self.rbk,self.pswc)
        update_data_thread = UpdateData()

        # print(self.window.main_ui.tabWidget.currentWidget().objectName())
        # self.r_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #启动更新线程
        update_data_thread.update_date.connect(self.bll.update_item_data)  # 链接信号
        update_data_thread.start()

        self.connect()
        self.login.show()

    def connect(self):
        # 右键
        # self.window.main_ui.r_tw.customContextMenuRequested.connect(lambda: self.bll.custom_right_menu("r_tw"))
        # self.window.main_ui.b_tw.customContextMenuRequested.connect(lambda: self.bll.custom_right_menu("b_tw"))
        # self.window.main_ui.rt_tw.customContextMenuRequested.connect(lambda: self.bll.custom_right_menu("rt_tw"))
        #关闭标签页
        # self.window.main_ui.tabWidget.tabCloseRequested['int'].connect(bll.close_tab)
        self.window.main_ui.r_tw.cellDoubleClicked['int','int'].connect(self.bll.r_ud)
        self.window.main_ui.b_tw.cellDoubleClicked['int','int'].connect(self.bll.b_ud)
        self.window.main_ui.r_tw.itemEntered['QTableWidgetItem*'].connect(self.bll.outSelect)
        self.window.main_ui.b_tw.itemEntered['QTableWidgetItem*'].connect(self.bll.outSelect)
        self.window.main_ui.rt_tw.itemEntered['QTableWidgetItem*'].connect(self.bll.outSelect)
        self.window.main_ui.br_tw.itemEntered['QTableWidgetItem*'].connect(self.bll.outSelect)
        self.window.main_ui.action_update.triggered.connect(self.bll.table_ini)
        self.rq.sub.query_bn.clicked.connect(self.bll.r_query)
        self.bq.sub.query_bn.clicked.connect(self.bll.b_query)
        self.brq.sub.query_bn.clicked.connect(self.bll.br_query)
        self.rbrq.sub.query_bn.clicked.connect(self.bll.r_br_query)
        self.rbrq.sub.q_all_btn.clicked.connect(self.bll.r_br_q_all)
        self.login.sub.login_btn.clicked.connect(self.bll.login_manage)
        self.ri.sub.insert_btn.clicked.connect(self.bll.r_insert)
        self.bi.sub.insert_btn.clicked.connect(self.bll.b_insert)
        self.rud.sub.update_btn.clicked.connect(self.bll.r_ud_u)
        self.bud.sub.update_btn.clicked.connect(self.bll.b_ud_u)
        self.rud.sub.delete_btn.clicked.connect(self.bll.r_ud_d)
        self.bud.sub.delete_btn.clicked.connect(self.bll.b_ud_d)
        self.bbk.sub.br_book_btn.clicked.connect(self.bll.b_book)
        self.rbk.sub.br_book_btn.clicked.connect(self.bll.r_book)
        # 通过menul联结不同窗口
        self.window.main_ui.rd_query.triggered.connect(self.bll.query_show)
        self.window.main_ui.rd_insert.triggered.connect(self.bll.insert_show)
        self.window.main_ui.action_room.triggered.connect(self.ur.show)
        self.window.main_ui.action_borrow.triggered.connect(self.bll.b_book_ini)
        self.window.main_ui.action_return.triggered.connect(self.bll.r_book_ini)
        self.ur.sub.psw_change_btn.clicked.connect(self.pswc.show)
        self.pswc.sub.psw_change_btn.clicked.connect(self.bll.psw_change)
        # window.main_ui.bk_query.triggered.connect(bq.show)

if __name__=='__main__':
    app = QApplication(sys.argv)
    win = connect_win()
    sys.exit(app.exec_())
