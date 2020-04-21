# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from com.ran.bobo.base import gol_var
import delete_rc


def checkNum(num):
    m_num = gol_var.get_value("m_num")
    if num == '.':
        # 包含了小数点
        if m_num.find('.', 0, len(m_num)) != -1 or m_num == '0':
            print(m_num.find('.', 0, len(m_num)))
            return
    if m_num != '0':
        gol_var.set_value("m_num", m_num + num)
    else:
        gol_var.set_value("m_num", num)


def math_result(action):
    result = gol_var.get_value('result')
    m_num = gol_var.get_value('m_num')
    if action == '1':
        try:
            # 包含了小数点
            if m_num.find('.', 0, len(m_num)) != -1 or result.find('.', 0, len(result)) != -1:
                answer = float(m_num) + float(result)
            else:
                answer = int(m_num) + int(result)
            print("结果:" + str(answer))
            gol_var.set_value("result", str(answer))
            gol_var.set_value("m_num", '0')
            # gol_var.set_value("action", '0')
        except Exception as e:
            print(e)
    elif action == '2':
        try:
            # 包含了小数点
            if m_num.find('.', 0, len(m_num)) != -1 or result.find('.', 0, len(result)) != -1:
                if float(result) > 0:
                    answer = float(result) - float(m_num)
                else:
                    answer = float(m_num)
            else:
                if int(result) > 0:
                    answer = int(result) - int(m_num)
                else:
                    answer = int(m_num)
            print("结果:" + str(answer))
            gol_var.set_value("result", str(answer))
            gol_var.set_value("m_num", '0')
            # gol_var.set_value("action", '0')
        except Exception as e:
            print(e)
    elif action == '3':
        try:
            # 包含了小数点
            if m_num.find('.', 0, len(m_num)) != -1 or result.find('.', 0, len(result)) != -1:
                if float(result) > 0:
                    answer = float(result) * float(m_num)
                else:
                    answer = float(m_num)
            else:
                if int(result) > 0:
                    answer = int(result) * int(m_num)
                else:
                    answer = int(m_num)
            print("结果:" + str(answer))
            gol_var.set_value("result", str(answer))
            gol_var.set_value("m_num", '0')
            # gol_var.set_value("action", '0')
        except Exception as e:
            print(e)
    elif action == '4':
        try:
            # 包含了小数点
            if m_num.find('.', 0, len(m_num)) != -1 or result.find('.', 0, len(result)) != -1:
                if float(result) > 0:
                    answer = float(result) / float(m_num)
                else:
                    answer = float(m_num)
            else:
                if int(result) > 0:
                    answer = int(result) / int(m_num)
                else:
                    answer = int(m_num)
            print("结果:" + str(answer))
            gol_var.set_value("result", str(answer))
            gol_var.set_value("m_num", '0')
            # gol_var.set_value("action", '0')
        except Exception as e:
            print(e)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 550)
        MainWindow.setFixedSize(468, 550)
        MainWindow.setStyleSheet("background-color: rgb(66, 83, 99);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 100, 451, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                      "border-radius: 2px; border: 2px groove gray;\n"
                                      "        border-style: outset;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 6, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 6, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 5, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setEnabled(True)
        self.pushButton_16.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 6, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 4, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 5, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 4, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 5, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                        "border-radius: 2px; border: 2px groove gray;\n"
                                        "        border-style: outset;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 5, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 2, 1, 1, 2)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 6, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setEnabled(True)
        self.pushButton_21.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_21.setStyleSheet("image: url(:/newPrefix/delete1.png);\n"
                                         "background-color: rgb(226, 236, 233);\n"
                                         "border-radius: 2px; border: 2px groove gray;\n"
                                         "        border-style: outset;")
        self.pushButton_21.setText("")
        self.pushButton_21.setAutoRepeat(False)
        self.pushButton_21.setFlat(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 2, 3, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 451, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(210, 226, 241);\n"
                                    "border-radius: 5px; \n"
                                    "border: 1px groove gray;\n"
                                    "border-style: inset;\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "padding: 2px;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.push_Button_click)
        self.pushButton_2.clicked.connect(self.push_Button_click)
        self.pushButton_3.clicked.connect(self.push_Button_click)
        self.pushButton_4.clicked.connect(self.push_Button_click)
        self.pushButton_5.clicked.connect(self.push_Button_click)
        self.pushButton_6.clicked.connect(self.push_Button_click)
        self.pushButton_7.clicked.connect(self.push_Button_click)
        self.pushButton_8.clicked.connect(self.push_Button_click)
        self.pushButton_9.clicked.connect(self.push_Button_click)
        self.pushButton_10.clicked.connect(self.push_Button_click)
        self.pushButton_11.clicked.connect(self.push_Button_click)
        self.pushButton_12.clicked.connect(self.push_Button_click)
        self.pushButton_13.clicked.connect(self.push_Button_click)
        self.pushButton_14.clicked.connect(self.push_Button_click)
        self.pushButton_15.clicked.connect(self.push_Button_click)
        self.pushButton_16.clicked.connect(self.push_Button_click)
        self.pushButton_17.clicked.connect(self.push_Button_click)
        self.pushButton_21.clicked.connect(self.back_onClick)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易计算器"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_14.setText(_translate("MainWindow", "."))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.pushButton_9.setText(_translate("MainWindow", "1"))
        self.pushButton_16.setText(_translate("MainWindow", "＋"))
        self.pushButton_4.setText(_translate("MainWindow", "÷"))
        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_8.setText(_translate("MainWindow", "×"))
        self.pushButton_12.setText(_translate("MainWindow", "－"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_10.setText(_translate("MainWindow", "2"))
        self.pushButton_17.setText(_translate("MainWindow", "C"))
        self.pushButton_15.setText(_translate("MainWindow", "="))
        self.lineEdit.setText(_translate("MainWindow", "0"))

    def push_Button_click(self):
        sender = self.sender()
        event = sender.text()
        if event == '0' or event == '1' or event == '2' or event == '3' \
                or event == '4' or event == '5' or event == '6' \
                or event == '7' or event == '8' or event == '9' \
                or event == '.':
            checkNum(event)
        elif event == 'C':
            gol_var.set_value("m_num", '0')
            gol_var.set_value('result', '0')
            self.lineEdit.setText('0')
        elif event == '＋':
            gol_var.set_value("action", '1')
            math_result('1')
        elif event == "－":
            gol_var.set_value("action", '2')
            math_result('2')
        elif event == "×":
            gol_var.set_value("action", '3')
            math_result('3')
        elif event == "÷":
            gol_var.set_value("action", '4')
            math_result('4')
        elif event == "=":
            action = gol_var.get_value("action")
            print("action:" + action)
            math_result(action)

        result = gol_var.get_value("result")
        m_num = gol_var.get_value("m_num")
        if m_num != '0':
            self.lineEdit.setText(m_num)
        else:
            self.lineEdit.setText(result)

    def back_onClick(self):
        m_num = gol_var.get_value("m_num")
        m_num = m_num[:-1]
        gol_var.set_value("m_num", m_num)
        self.lineEdit.setText(m_num)
        if len(m_num) <= 0:
            self.lineEdit.setText('0')
