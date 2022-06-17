# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QSpinBox

#創建性別清單
class GenderSpinBox(QSpinBox):

    # constructor
    def __init__(self, parent=None):
        super(GenderSpinBox, self).__init__(parent)

        # 性別清單
        strings = ['男性', '女性', '變性', '中性', '雙性', '其他']

        # calling setStrings method
        self.setStrings(strings)

    # method setString
    # similar to set value method
    def setStrings(self, strings):
        # making strings list
        strings = list(strings)

        # making tuple from the string list
        self._strings = tuple(strings)

        # creating a dictionary
        self._values = dict(zip(strings, range(len(strings))))

        # setting range to it the spin box
        self.setRange(0, len(strings) - 1)

    # overwriting the textFromValue method
    def textFromValue(self, value):
        # returning string from index
        # _string = tuple
        return self._strings[value]




#創建血型清單
class BloodTypeSpinBox(QSpinBox):

    # constructor
    def __init__(self, parent=None):
        super(BloodTypeSpinBox, self).__init__(parent)

        # 血型清單
        strings = ['O', 'AB', 'A', 'B']

        # calling setStrings method
        self.setStrings(strings)

    # method setString
    # similar to set value method
    def setStrings(self, strings):
        # making strings list
        strings = list(strings)

        # making tuple from the string list
        self._strings = tuple(strings)

        # creating a dictionary
        self._values = dict(zip(strings, range(len(strings))))

        # setting range to it the spin box
        self.setRange(0, len(strings) - 1)

    # overwriting the textFromValue method
    def textFromValue(self, value):
        # returning string from index
        # _string = tuple
        return self._strings[value]




class LoginDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(500, 90, 121, 121))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText('取消')
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('確定')
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.closed)

        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 291, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(72, 49))
        self.label.setMaximumSize(QtCore.QSize(72, 49))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(150, 50))
        self.textEdit.setMaximumSize(QtCore.QSize(150, 50))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 140, 291, 52))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(72, 49))
        self.label_3.setMaximumSize(QtCore.QSize(72, 49))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setMinimumSize(QtCore.QSize(150, 50))
        self.dateEdit.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 200, 291, 52))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setMinimumSize(QtCore.QSize(72, 49))
        self.label_4.setMaximumSize(QtCore.QSize(72, 49))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox = BloodTypeSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox.setMinimumSize(QtCore.QSize(150, 50))
        self.spinBox.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 260, 291, 52))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setMinimumSize(QtCore.QSize(72, 49))
        self.label_2.setMaximumSize(QtCore.QSize(72, 49))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_2 = GenderSpinBox(self.horizontalLayoutWidget_4)
        self.spinBox_2.setMinimumSize(QtCore.QSize(150, 50))
        self.spinBox_2.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 621, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeEvent(self, event):
        import sys
        sys.exit()


    def closed(self):
        import sys
        sys.exit()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "男女朋友翻譯機"))
        self.label.setText(_translate("Dialog", "姓名："))
        self.label_3.setText(_translate("Dialog", "生日："))
        self.label_4.setText(_translate("Dialog", "血型："))
        self.label_2.setText(_translate("Dialog", "性別："))
        self.label_5.setText(_translate("Dialog", "登入畫面"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoginDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
