from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 170)
        Dialog.setMinimumSize(QtCore.QSize(438, 170))
        Dialog.setMaximumSize(QtCore.QSize(438, 170))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.text = QtWidgets.QLabel(Dialog)
        self.text.setGeometry(QtCore.QRect(9, 9, 401, 41))
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.through5m = QtWidgets.QPushButton(Dialog)
        self.through5m.setGeometry(QtCore.QRect(20, 60, 113, 32))
        self.through5m.setObjectName("through5m")
        self.through15m = QtWidgets.QPushButton(Dialog)
        self.through15m.setGeometry(QtCore.QRect(20, 110, 113, 32))
        self.through15m.setObjectName("through15m")
        self.through1h = QtWidgets.QPushButton(Dialog)
        self.through1h.setGeometry(QtCore.QRect(160, 110, 113, 32))
        self.through1h.setObjectName("through1h")
        self.through30m = QtWidgets.QPushButton(Dialog)
        self.through30m.setGeometry(QtCore.QRect(160, 60, 113, 32))
        self.through30m.setObjectName("through30m")
        self.through2h = QtWidgets.QPushButton(Dialog)
        self.through2h.setGeometry(QtCore.QRect(300, 60, 113, 32))
        self.through2h.setObjectName("through2h")
        self.btn_completed = QtWidgets.QPushButton(Dialog)
        self.btn_completed.setGeometry(QtCore.QRect(300, 110, 113, 32))
        self.btn_completed.setDefault(True)
        self.btn_completed.setObjectName("btn_completed")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ㅤ"))
        self.text.setText(_translate("Dialog", "None"))
        self.through5m.setText(_translate("Dialog", "5 Minutes"))
        self.through15m.setText(_translate("Dialog", "15 Minutes"))
        self.through1h.setText(_translate("Dialog", "1 hour"))
        self.through30m.setText(_translate("Dialog", "30 Minutes"))
        self.through2h.setText(_translate("Dialog", "2 Hours"))
        self.btn_completed.setText(_translate("Dialog", "Completed"))

# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
