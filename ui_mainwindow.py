# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 553)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 531))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setMovable(False)
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.frame = QFrame(self.searchTab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(570, 10, 211, 161))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.cityLine = QLineEdit(self.frame)
        self.cityLine.setObjectName(u"cityLine")
        self.cityLine.setGeometry(QRect(20, 30, 171, 20))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 171, 16))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 171, 16))
        self.pagesLine = QLineEdit(self.frame)
        self.pagesLine.setObjectName(u"pagesLine")
        self.pagesLine.setGeometry(QRect(110, 80, 81, 20))
        self.scanButton = QPushButton(self.frame)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setGeometry(QRect(20, 120, 171, 23))
        self.pagesLineStart = QLineEdit(self.frame)
        self.pagesLineStart.setObjectName(u"pagesLineStart")
        self.pagesLineStart.setGeometry(QRect(20, 80, 81, 20))
        self.frame_2 = QFrame(self.searchTab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(570, 180, 211, 151))
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.validButton = QPushButton(self.frame_2)
        self.validButton.setObjectName(u"validButton")
        self.validButton.setGeometry(QRect(20, 20, 81, 23))
        self.manualButton = QPushButton(self.frame_2)
        self.manualButton.setObjectName(u"manualButton")
        self.manualButton.setEnabled(False)
        self.manualButton.setGeometry(QRect(20, 50, 171, 23))
        self.savehostsButton = QPushButton(self.frame_2)
        self.savehostsButton.setObjectName(u"savehostsButton")
        self.savehostsButton.setGeometry(QRect(20, 80, 171, 23))
        self.loadhostsButton = QPushButton(self.frame_2)
        self.loadhostsButton.setObjectName(u"loadhostsButton")
        self.loadhostsButton.setGeometry(QRect(20, 110, 171, 23))
        self.clonesButton = QPushButton(self.frame_2)
        self.clonesButton.setObjectName(u"clonesButton")
        self.clonesButton.setGeometry(QRect(110, 20, 81, 23))
        self.frame_3 = QFrame(self.searchTab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(570, 340, 211, 151))
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.removeButton = QPushButton(self.frame_3)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setEnabled(True)
        self.removeButton.setGeometry(QRect(20, 20, 171, 23))
        self.checkButton = QPushButton(self.frame_3)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setEnabled(True)
        self.checkButton.setGeometry(QRect(20, 50, 171, 23))
        self.openButton = QPushButton(self.frame_3)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setGeometry(QRect(20, 80, 171, 23))
        self.clearnButton = QPushButton(self.frame_3)
        self.clearnButton.setObjectName(u"clearnButton")
        self.clearnButton.setGeometry(QRect(20, 110, 171, 23))
        self.testButton = QPushButton(self.frame_3)
        self.testButton.setObjectName(u"testButton")
        self.testButton.setEnabled(False)
        self.testButton.setGeometry(QRect(0, 0, 41, 23))
        self.qtHostList = QTableWidget(self.searchTab)
        if (self.qtHostList.columnCount() < 3):
            self.qtHostList.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.qtHostList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.qtHostList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.qtHostList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.qtHostList.rowCount() < 1):
            self.qtHostList.setRowCount(1)
        self.qtHostList.setObjectName(u"qtHostList")
        self.qtHostList.setGeometry(QRect(10, 30, 551, 461))
        self.qtHostList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.qtHostList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.qtHostList.setRowCount(1)
        self.qtHostList.setColumnCount(3)
        self.qtHostList.horizontalHeader().setVisible(False)
        self.qtHostList.horizontalHeader().setMinimumSectionSize(30)
        self.qtHostList.horizontalHeader().setDefaultSectionSize(120)
        self.qtHostList.horizontalHeader().setStretchLastSection(True)
        self.qtHostList.verticalHeader().setVisible(False)
        self.qtHostList.verticalHeader().setMinimumSectionSize(20)
        self.qtHostList.verticalHeader().setDefaultSectionSize(20)
        self.hostcountLabel = QLabel(self.searchTab)
        self.hostcountLabel.setObjectName(u"hostcountLabel")
        self.hostcountLabel.setGeometry(QRect(10, 10, 210, 13))
        self.tabWidget.addTab(self.searchTab, "")
        self.exploreTab = QWidget()
        self.exploreTab.setObjectName(u"exploreTab")
        self.frame_4 = QFrame(self.exploreTab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(570, 10, 211, 171))
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.winscpButton = QPushButton(self.frame_4)
        self.winscpButton.setObjectName(u"winscpButton")
        self.winscpButton.setGeometry(QRect(20, 20, 171, 23))
        self.removesButton = QPushButton(self.frame_4)
        self.removesButton.setObjectName(u"removesButton")
        self.removesButton.setGeometry(QRect(20, 50, 171, 23))
        self.favButton = QPushButton(self.frame_4)
        self.favButton.setObjectName(u"favButton")
        self.favButton.setGeometry(QRect(20, 110, 171, 23))
        self.selectInListButton = QPushButton(self.frame_4)
        self.selectInListButton.setObjectName(u"selectInListButton")
        self.selectInListButton.setGeometry(QRect(20, 80, 171, 23))
        self.qtFileList = QListWidget(self.exploreTab)
        self.qtFileList.setObjectName(u"qtFileList")
        self.qtFileList.setGeometry(QRect(10, 30, 551, 461))
        self.curhostLabel = QLabel(self.exploreTab)
        self.curhostLabel.setObjectName(u"curhostLabel")
        self.curhostLabel.setGeometry(QRect(10, 10, 550, 13))
        self.frame_5 = QFrame(self.exploreTab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(570, 190, 211, 101))
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.ipinputLine = QLineEdit(self.frame_5)
        self.ipinputLine.setObjectName(u"ipinputLine")
        self.ipinputLine.setGeometry(QRect(20, 30, 171, 20))
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 50, 13))
        self.ipinputButton = QPushButton(self.frame_5)
        self.ipinputButton.setObjectName(u"ipinputButton")
        self.ipinputButton.setGeometry(QRect(20, 60, 171, 23))
        self.frame_6 = QFrame(self.exploreTab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(570, 300, 211, 51))
        self.frame_6.setFrameShape(QFrame.WinPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.refreshButton = QPushButton(self.frame_6)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(20, 10, 171, 23))
        self.tabWidget.addTab(self.exploreTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.verticalLayout = QVBoxLayout(self.settingsTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cfgList = QTableWidget(self.settingsTab)
        if (self.cfgList.columnCount() < 2):
            self.cfgList.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cfgList.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cfgList.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.cfgList.rowCount() < 2):
            self.cfgList.setRowCount(2)
        self.cfgList.setObjectName(u"cfgList")
        self.cfgList.setFrameShape(QFrame.WinPanel)
        self.cfgList.setWordWrap(False)
        self.cfgList.setRowCount(2)
        self.cfgList.setColumnCount(2)
        self.cfgList.horizontalHeader().setVisible(False)
        self.cfgList.horizontalHeader().setDefaultSectionSize(145)
        self.cfgList.horizontalHeader().setStretchLastSection(True)
        self.cfgList.verticalHeader().setVisible(False)
        self.cfgList.verticalHeader().setMinimumSectionSize(29)

        self.verticalLayout.addWidget(self.cfgList)

        self.cfg_apply = QPushButton(self.settingsTab)
        self.cfg_apply.setObjectName(u"cfg_apply")

        self.verticalLayout.addWidget(self.cfg_apply)

        self.cfg_cancel = QPushButton(self.settingsTab)
        self.cfg_cancel.setObjectName(u"cfg_cancel")

        self.verticalLayout.addWidget(self.cfg_cancel)

        self.tabWidget.addTab(self.settingsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMouseTracking(False)
        self.statusBar.setAutoFillBackground(False)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cityLine.setText(QCoreApplication.translate("MainWindow", u"Nizhnevartovsk", None))
        self.cityLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"London", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.pagesLine.setInputMask("")
        self.pagesLine.setText("")
        self.pagesLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.scanButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pagesLineStart.setInputMask("")
        self.pagesLineStart.setText("")
        self.pagesLineStart.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.validButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u044f", None))
        self.manualButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.savehostsButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0445\u043e\u0441\u0442\u043e\u0432", None))
        self.loadhostsButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0445\u043e\u0441\u0442\u043e\u0432", None))
        self.clonesButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u044b", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439", None))
        self.clearnButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"test", None))
        ___qtablewidgetitem = self.qtHostList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IP-\u0430\u0434\u0440\u0435\u0441\u0430", None));
        ___qtablewidgetitem1 = self.qtHostList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem2 = self.qtHostList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440", None));
        self.hostcountLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0445\u043e\u0441\u0442\u043e\u0432: 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.winscpButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 WinSCP", None))
        self.removesButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.favButton.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0438\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.selectInListButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432 \u0441\u043f\u0438\u0441\u043a\u0435", None))
        self.curhostLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0445\u043e\u0441\u0442: 0.0.0.0", None))
        self.ipinputLine.setText(QCoreApplication.translate("MainWindow", u"0.0.0.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.ipinputButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exploreTab), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        ___qtablewidgetitem3 = self.cfgList.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None));
        ___qtablewidgetitem4 = self.cfgList.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        self.cfg_apply.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.cfg_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.statusBar.setToolTip(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0448\u0435\u043b \u043d\u0430\u0445\u0443\u0439", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

