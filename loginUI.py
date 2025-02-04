# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import test


class LoginUI_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 250, 400))
        self.label.setStyleSheet("border-image: url(:/newPrefix/kookmin_background.jpg);\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 250, 400))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
                                   "")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 0, 250, 400))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 255);\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.loginLabel = QtWidgets.QLabel(Dialog)
        self.loginLabel.setGeometry(QtCore.QRect(330, 40, 100, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.loginLabel.setObjectName("loginLabel")
        self.emailLineEdit = QtWidgets.QLineEdit(Dialog)
        self.emailLineEdit.setGeometry(QtCore.QRect(280, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                         "border:none;\n"
                                         "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                         "color: rgba(0, 0, 0, 240);\n"
                                         "padding-bottom:7px;")
        self.emailLineEdit.setText("")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.pwLineEdit = QtWidgets.QLineEdit(Dialog)
        self.pwLineEdit.setGeometry(QtCore.QRect(280, 180, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pwLineEdit.setFont(font)
        self.pwLineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                      "color: rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.pwLineEdit.setText("")
        self.pwLineEdit.setObjectName("pwLineEdit")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(280, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 250, 90))
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0, 70);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 90, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(280, 330, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.signupButton = QtWidgets.QPushButton(Dialog)
        self.signupButton.setGeometry(QtCore.QRect(410, 330, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setUnderline(True)
        self.signupButton.setFont(font)
        self.signupButton.setStyleSheet("text-decoration: underline;")
        self.signupButton.setObjectName("signupButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginLabel.setText(_translate("Dialog", "Sign In"))
        self.emailLineEdit.setPlaceholderText(
            _translate("Dialog", "Email Address"))
        self.pwLineEdit.setPlaceholderText(_translate("Dialog", "Password"))
        self.loginButton.setText(_translate("Dialog", "Sign In"))
        self.label_6.setText(_translate("Dialog", "KookO Talk"))
        self.label_7.setText(_translate(
            "Dialog", "Don\'t you have any account?"))
        self.signupButton.setText(_translate("Dialog", "Sign Up"))
