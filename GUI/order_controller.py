from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, Qt, QDate, QDateTime
from order_ui import Ui_MainWindow
from order import order_controller

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
        self.ui.buttonBox.accepted.connect(self.order)
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.comboBox_restaurant.currentIndexChanged.connect(self.changeRes)
    def order(self):
        ac = self.ui.line_account.text()
        pw = self.ui.line_password.text()
        peoples = self.ui.comboBox_peoples.currentText()
        store = self.ui.comboBox_store.currentText()
        eat_time = self.ui.comboBox_eat_time.currentText()
        order_date = self.ui.dateEdit_order_date.date().toString('yyyy-MM-dd')
        restaurant = self.ui.comboBox_restaurant.currentText()

        # print('restaurant ' + restaurant, type(restaurant))
        # print('ac ' + ac, type(ac))
        # print('pw ' + pw, type(pw))
        # print('peoples ' + peoples, type(peoples))
        # print('store ' + store, type(store))
        # print('eat_time ' + eat_time, type(eat_time))
        # print('order_date ' + order_date, type(order_date))
        # print("\n")
        self.order_controller = order_controller(
            restaurant = restaurant,
            ac = ac,
            pw = pw,
            peoples = peoples,
            store = store,
            eat_time = eat_time,
            order_date = order_date
        )
        
        self.order_controller.order()
    def showTime(self):
        current_time = QDateTime.currentDateTime()
        label_time = current_time.toString('yyyy-MM-dd hh:mm:ss')
        self.ui.label_timer.setText(label_time)
    def changeRes(self):
        restaurant = self.ui.comboBox_restaurant.currentText()

        if restaurant == '旭集':
            self.ui.comboBox_store.removeItem(0)
            self.ui.comboBox_store.removeItem(1)
            self.ui.comboBox_store.setItemText(0, "旭集信義店")
        elif restaurant == '饗饗':
            self.ui.comboBox_store.removeItem(0)
            self.ui.comboBox_store.addItems(["微風店", "新莊店"])

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())