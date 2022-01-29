# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ailever.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Education_widget = QtWidgets.QWidget()
        self.Education_widget.setObjectName("Education_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Education_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Education_tabwidget = QtWidgets.QTabWidget(self.Education_widget)
        self.Education_tabwidget.setObjectName("Education_tabwidget")
        self.Statistics_widget = QtWidgets.QWidget()
        self.Statistics_widget.setObjectName("Statistics_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Statistics_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Statistics_tabwidget = QtWidgets.QTabWidget(self.Statistics_widget)
        self.Statistics_tabwidget.setObjectName("Statistics_tabwidget")
        self.Descriptive_widget = QtWidgets.QWidget()
        self.Descriptive_widget.setObjectName("Descriptive_widget")
        self.Statistics_tabwidget.addTab(self.Descriptive_widget, "")
        self.Inferential_widget = QtWidgets.QWidget()
        self.Inferential_widget.setObjectName("Inferential_widget")
        self.Statistics_tabwidget.addTab(self.Inferential_widget, "")
        self.Regression_widget = QtWidgets.QWidget()
        self.Regression_widget.setObjectName("Regression_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Regression_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Statistics_tabwidget.addTab(self.Regression_widget, "")
        self.Forecast_widget = QtWidgets.QWidget()
        self.Forecast_widget.setObjectName("Forecast_widget")
        self.Statistics_tabwidget.addTab(self.Forecast_widget, "")
        self.verticalLayout_4.addWidget(self.Statistics_tabwidget)
        self.Education_tabwidget.addTab(self.Statistics_widget, "")
        self.DeepLearning_widget = QtWidgets.QWidget()
        self.DeepLearning_widget.setObjectName("DeepLearning_widget")
        self.Education_tabwidget.addTab(self.DeepLearning_widget, "")
        self.ReinforcementLearning_widget = QtWidgets.QWidget()
        self.ReinforcementLearning_widget.setObjectName("ReinforcementLearning_widget")
        self.Education_tabwidget.addTab(self.ReinforcementLearning_widget, "")
        self.verticalLayout.addWidget(self.Education_tabwidget)
        self.tabWidget.addTab(self.Education_widget, "")
        self.StockMarket_widget = QtWidgets.QWidget()
        self.StockMarket_widget.setObjectName("StockMarket_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.StockMarket_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.StockMarket_tabwidget = QtWidgets.QTabWidget(self.StockMarket_widget)
        self.StockMarket_tabwidget.setObjectName("StockMarket_tabwidget")
        self.DatasetDescription_widget = QtWidgets.QWidget()
        self.DatasetDescription_widget.setObjectName("DatasetDescription_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.DatasetDescription_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.DatasetDescription_scrollarea = QtWidgets.QScrollArea(self.DatasetDescription_widget)
        self.DatasetDescription_scrollarea.setWidgetResizable(True)
        self.DatasetDescription_scrollarea.setObjectName("DatasetDescription_scrollarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 750, 475))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setGeometry(QtCore.QRect(90, 300, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(60, 360, 681, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(340, 20, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 260, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setGeometry(QtCore.QRect(70, 220, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(550, 260, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.DatasetDescription_scrollarea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.DatasetDescription_scrollarea)
        self.StockMarket_tabwidget.addTab(self.DatasetDescription_widget, "")
        self.ResidualAnalysis_widget = QtWidgets.QWidget()
        self.ResidualAnalysis_widget.setObjectName("ResidualAnalysis_widget")
        self.StockMarket_tabwidget.addTab(self.ResidualAnalysis_widget, "")
        self.verticalLayout_3.addWidget(self.StockMarket_tabwidget)
        self.tabWidget.addTab(self.StockMarket_widget, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.Education_tabwidget.setCurrentIndex(0)
        self.Statistics_tabwidget.setCurrentIndex(3)
        self.StockMarket_tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ailever Eyes"))
        self.Statistics_tabwidget.setTabText(self.Statistics_tabwidget.indexOf(self.Descriptive_widget), _translate("MainWindow", "Descriptive"))
        self.Statistics_tabwidget.setTabText(self.Statistics_tabwidget.indexOf(self.Inferential_widget), _translate("MainWindow", "Inferential"))
        self.Statistics_tabwidget.setTabText(self.Statistics_tabwidget.indexOf(self.Regression_widget), _translate("MainWindow", "Regression"))
        self.Statistics_tabwidget.setTabText(self.Statistics_tabwidget.indexOf(self.Forecast_widget), _translate("MainWindow", "Forecast"))
        self.Education_tabwidget.setTabText(self.Education_tabwidget.indexOf(self.Statistics_widget), _translate("MainWindow", "Statistics"))
        self.Education_tabwidget.setTabText(self.Education_tabwidget.indexOf(self.DeepLearning_widget), _translate("MainWindow", "Deep Learning"))
        self.Education_tabwidget.setTabText(self.Education_tabwidget.indexOf(self.ReinforcementLearning_widget), _translate("MainWindow", "Reinforcement Learning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Education_widget), _translate("MainWindow", "Education"))
        self.StockMarket_tabwidget.setTabText(self.StockMarket_tabwidget.indexOf(self.DatasetDescription_widget), _translate("MainWindow", "Dataset Description"))
        self.StockMarket_tabwidget.setTabText(self.StockMarket_tabwidget.indexOf(self.ResidualAnalysis_widget), _translate("MainWindow", "Residual Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StockMarket_widget), _translate("MainWindow", "Stock Market"))
