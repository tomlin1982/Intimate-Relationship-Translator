#這是一個簡單的GUI範例

# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QDialog

from snownlp import SnowNLP
from snownlp import sentiment

from Login import LoginDialog

#LoginDialog 載入
class LoginDlg(QDialog, LoginDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)
        self.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))

        self.mylogin = LoginDlg()
        self.mylogin.exec()

        if self.mylogin.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked:
            self.myname = self.mylogin.textEdit.toPlainText()
            print(self.myname)
            self.birthday_value = self.mylogin.dateEdit.date().toString('yyyy-MM-dd')
            print(self.birthday_value)
            self.mybloodtype = self.mylogin.spinBox.text()
            print(self.mybloodtype)
            self.mygendertype  = self.mylogin.spinBox_2.text()
            print(self.mygendertype)



        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 331, 481))
        self.groupBox.setObjectName("groupBox")

        #對話輸入的面板
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 311, 431))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")

        #確定按鈕
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 90, 150, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonClicked_plain)

        #分析按鈕
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 150, 150, 50))
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.buttonCLick_analysis)
        self.pushButton_2.setDisabled(True)

        #清除按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 500, 150, 50))
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.buttonClicked_clear)
        self.pushButton_3.setDisabled(True)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 50))
        self.label_2.setMaximumSize(QtCore.QSize(70, 50))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 50))
        self.label.setMaximumSize(QtCore.QSize(100, 50))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(70, 50))
        self.label_3.setMaximumSize(QtCore.QSize(70, 50))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 50))
        self.label_4.setMaximumSize(QtCore.QSize(150, 50))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(70, 50))
        self.label_5.setMaximumSize(QtCore.QSize(70, 50))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(100, 50))
        self.label_6.setMaximumSize(QtCore.QSize(100, 50))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(70, 50))
        self.label_7.setMaximumSize(QtCore.QSize(70, 50))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(100, 50))
        self.label_8.setMaximumSize(QtCore.QSize(100, 50))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)

        #顯示對話與分析詞語的面板
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(350, 110, 271, 431))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setDisabled(True)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label.setText(self.myname)
        self.label_4.setText(self.birthday_value)
        self.label_6.setText(self.mybloodtype)
        self.label_8.setText(self.mygendertype)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buttonClicked_plain(self):
        msg = self.textEdit.toPlainText()
        self.textBrowser.setText(msg)
        print(msg)

        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)

    def buttonCLick_analysis(self):
        msg = self.textEdit.toPlainText()
        self.textBrowser.clear()
        self.textBrowser.setText("重點詞語\n=========\n")
        # print(type(msg))
        #snownlp 情感分析工具初步分析
        s = SnowNLP(msg)
        # print(s.sentiments)
        # print(type(s.sentiments))
        # print(s.keywords(5))
        # print(type(s.keywords(5)))
        # print(s.summary(5))
        # print(type(s.summary(5)))
        for mykeyword in s.summary(5):
            self.textBrowser.append(mykeyword)
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(False)

    def buttonClicked_clear(self):
        self.textEdit.clear()
        self.textBrowser.clear()

        self.pushButton.setDisabled(False)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "男女朋友翻譯機"))
        self.groupBox.setTitle(_translate("MainWindow", "男/女朋友對話輸入"))
        self.textEdit.setDocumentTitle(_translate("MainWindow", "我的文字"))
        self.pushButton.setText(_translate("MainWindow", "確定"))
        self.pushButton_2.setText(_translate("MainWindow", "分析"))
        self.pushButton_3.setText(_translate("MainWindow", "清空對話"))
        self.label_2.setText(_translate("MainWindow", "姓名："))
        self.label_3.setText(_translate("MainWindow", "生日："))
        self.label_5.setText(_translate("MainWindow", "血型："))
        self.label_7.setText(_translate("MainWindow", "性別："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
