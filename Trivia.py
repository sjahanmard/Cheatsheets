# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trivia1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
import json
import pandas as pd
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 460)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
#widget (starting page)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 661, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("triviaphoto.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.btnstart = QtWidgets.QPushButton(self.widget)
        self.btnstart.setGeometry(QtCore.QRect(190, 330, 261, 41))
        self.btnstart.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btnstart.setObjectName("btnstart")
        self.btnstart.setText("Start")
        self.btnstart.clicked.connect(self.starting)
        
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btnstart.setFont(font)

        

#widget 1 (gaming page)
    
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.widget1.setObjectName("widget1")
        
        self.lbq = QtWidgets.QLabel(self.widget1)
        self.lbq.setGeometry(QtCore.QRect(110, 40, 430, 231))
        self.lbq.setWordWrap(True)
        self.lbq.setObjectName("lbq")
        self.lbq.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(30)
        self.lbq.setFont(font)

        self.btn1 = QtWidgets.QPushButton(self.widget1)
        self.btn1.setGeometry(QtCore.QRect(40, 260, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.btn1.setFont(font)
        
        self.btn1.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btn1.setObjectName("pushButton")
        self.btn2 = QtWidgets.QPushButton(self.widget1)
        self.btn2.setGeometry(QtCore.QRect(350, 259, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.widget1)
        self.btn3.setGeometry(QtCore.QRect(350, 319, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.widget1)
        self.btn4.setGeometry(QtCore.QRect(40, 320, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btn4.setObjectName("btn4")
        self.lbscore = QtWidgets.QLabel(self.widget1)
        self.lbscore.setGeometry(QtCore.QRect(10, 10, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lbscore.setFont(font)
        self.lbscore.setStyleSheet('text-color:black;border-radius: 35PX;background-color:pink;border: 2px solid purple')
        self.lbscore.setObjectName("lbscore")

        self.lbq.setText(" ")
        self.btn1.setText(" ")
        self.btn2.setText(" ")
        self.btn3.setText(" ")
        self.btn4.setText(" ")
        self.score=0
        self.lbscore.setText(str(self.score))
        
        









#widget 2 (winning window)        
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.widget2.setObjectName("widget2")
        self.lbhappy = QtWidgets.QLabel(self.widget2)
        self.lbhappy.setGeometry(QtCore.QRect(0, 0, 661, 461))
        self.lbhappy.setText("")
        self.lbhappy.setPixmap(QtGui.QPixmap("won.jpg"))
        self.lbhappy.setScaledContents(True)
        self.lbhappy.setObjectName("lbhappy")
        self.btnnew = QtWidgets.QPushButton(self.widget2)
        self.btnnew.setGeometry(QtCore.QRect(190, 340, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btnnew.setFont(font)
        self.btnnew.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btnnew.setObjectName("pushButton")
        self.lbwon = QtWidgets.QLabel(self.widget2)
        self.lbwon.setGeometry(QtCore.QRect(90, 262, 500, 51))
        self.lbwon.setObjectName("lbwon")
        self.lbwon.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbwon.setFont(font)
        self.lbwon.setStyleSheet('color: purple')
        self.btnnew.setText("New Game")
        self.lbwon.setText("Congratulations, you WON!!")
        
#widget 3 (losing window)        
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.widget3.setObjectName("widget3")
        self.lbsad = QtWidgets.QLabel(self.widget3)
        self.lbsad.setGeometry(QtCore.QRect(0, 0, 661, 461))
        self.lbsad.setText("")
        self.lbsad.setPixmap(QtGui.QPixmap("sad.jpg"))
        self.lbsad.setScaledContents(True)
        self.lbsad.setObjectName("lbsad")
        self.btntry = QtWidgets.QPushButton(self.widget3)
        self.btntry.setGeometry(QtCore.QRect(190, 340, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btntry.setFont(font)
        self.btntry.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid purple;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color:pink;\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background:#ffaaff;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: orange;\n"
                                        "    }")
        self.btntry.setObjectName("pushButton")
        self.lblost = QtWidgets.QLabel(self.widget3)
        self.lblost.setGeometry(QtCore.QRect(80, 30, 500, 200))
        self.lblost.setObjectName("lbwon")
        self.lblost.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.lblost.setFont(font)
        self.lblost.setStyleSheet('color: red')
        self.btntry.setText("Try Again")
        self.lblost.setText( "U LOST!!")
    













        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    
        self.widget1.hide()
        self.widget2.hide()
        self.widget3.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        
        self.btntry.setText(_translate("MainWindow", "Try Again"))
        self.lblost.setText(_translate("MainWindow", "U LOST!!"))
        
    def starting(self):
        self.score = 0 
        self.lbscore.setText(str(self.score))
        self.widget.hide()
        self.widget2.hide()
        self.widget3.hide()
        self.widget1.show()

    
        with urlopen ("https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple") as webpage:
            data = json.loads(webpage.read().decode())
            df = pd.DataFrame(data['results'])
            self.question=[]
            self.correctanswer=[]
            incorrectanswers=[]
            self.allanswers=[]

#for i in range (50):
                
#question[i].append(df['question'][i])
#correctanswer[i]  = df['correct_answer'][i]
#incorrectanswers[i]  = df['incorrect_answers'][i]
#allanswers[i]  = incorrectanswers[i]  + [correctanswer[i]]

#if u write the code like this U will get the IndexError list Index our of range
#why?because there is no Index defined for question so U will ahve to write it like this:
            for i in range (50):
                
                self.question.append(df['question'][i])
                self.correctanswer.append(df['correct_answer'][i])
                incorrectanswers.append( df['incorrect_answers'][i])
                self.allanswers.append(incorrectanswers[i]  + [self.correctanswer[i]])
                formatting = [("#039;", "'"),("&'", "'"),("&quot;", '"'),("&lt;", "<"),("&gt;", ">")]

#replace corrputed charecters in the string
                for tuple in formatting:
                    self.question[i] = self.question[i].replace(tuple[0], tuple[1])
                    self.correctanswer[i] = self.correctanswer[i].replace(tuple[0], tuple[1])
                for tuple in formatting:
                    for n in range(4):
                        self.allanswers[i][n] = self.allanswers[i][n].replace(tuple[0], tuple[1])
                random.shuffle(self.allanswers[i])
        
        print ('1')

        self.excelling()

    def excelling(self): 
        print ('2')
   
        self.btn1.clicked.connect(lambda: self.checking(self.allanswers[-1][0]))
        self.btn2.clicked.connect(lambda: self.checking(self.allanswers[-1][1]))
        self.btn3.clicked.connect(lambda: self.checking(self.allanswers[-1][2]))
        self.btn4.clicked.connect(lambda: self.checking(self.allanswers[-1][3]))
        print ('3')
        self.lbq.setText(self.question[-1])
        self.btn1.setText(self.allanswers[-1][0])
        self.btn2.setText(self.allanswers[-1][1])
        self.btn3.setText(self.allanswers[-1][2])
        self.btn4.setText(self.allanswers[-1][3])
    
        print ('4')
        print (self.correctanswer[-1])
        
    def checking(self, chosenanswer):
        print (chosenanswer)
        print ('5')
        if self.correctanswer[-1] == chosenanswer:
            self.score += 10            
            self.lbscore.setText(str(self.score))
            self.correctanswer.pop()
            self.allanswers.pop()
            self.question.pop()
            self.btn1.clicked.disconnect()
            self.btn2.clicked.disconnect()
            self.btn3.clicked.disconnect()
            self.btn4.clicked.disconnect()

            
            print ('6')
            if self.score == 100:
                self.won()
                
            self.excelling()
        else:
            self.failed()
        
    def won(self):
        self.widget1.hide()
        self.widget2.show()
        self.btnnew.clicked.connect(self.starting)
        
    def failed(self):
        self.widget1.hide()
        self.widget3.show()
        self.btntry.clicked.connect(self.starting)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        














if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    