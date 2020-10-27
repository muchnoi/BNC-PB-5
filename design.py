# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QGroupBox { border: 1px solid grey;   border-radius: 10px;   font-weight: bold; font-size: 12pt; color: black; padding:8px; margin:8px; background-color: #F0F0F0;}\n"
"QGroupBox::title {  subcontrol-origin: margin;   subcontrol-position: top center;    padding:  0 5px;  }\n"
"QSpinBox {             background-color: #FFFFFF; }\n"
"QDoubleSpinBox {background-color: #FFFFFF;} ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.SerialPortBox = QtWidgets.QComboBox(self.groupBox)
        self.SerialPortBox.setGeometry(QtCore.QRect(30, 90, 221, 24))
        self.SerialPortBox.setObjectName("SerialPortBox")
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PulseGroupBox = QtWidgets.QGroupBox(self.frame_2)
        self.PulseGroupBox.setObjectName("PulseGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PulseGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PolarityBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.PolarityBox.setObjectName("PolarityBox")
        self.verticalLayout.addWidget(self.PolarityBox)
        self.RiseTimeBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.RiseTimeBox.setObjectName("RiseTimeBox")
        self.verticalLayout.addWidget(self.RiseTimeBox)
        self.FallTimeBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.FallTimeBox.setObjectName("FallTimeBox")
        self.verticalLayout.addWidget(self.FallTimeBox)
        self.AmplitudeBox = QtWidgets.QDoubleSpinBox(self.PulseGroupBox)
        self.AmplitudeBox.setDecimals(4)
        self.AmplitudeBox.setMaximum(10.0)
        self.AmplitudeBox.setSingleStep(0.25)
        self.AmplitudeBox.setObjectName("AmplitudeBox")
        self.verticalLayout.addWidget(self.AmplitudeBox)
        self.AttenuationBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.AttenuationBox.setObjectName("AttenuationBox")
        self.verticalLayout.addWidget(self.AttenuationBox)
        self.ClampBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.ClampBox.setObjectName("ClampBox")
        self.verticalLayout.addWidget(self.ClampBox)
        self.horizontalLayout.addWidget(self.PulseGroupBox)
        self.TriggerGroupBox = QtWidgets.QGroupBox(self.frame_2)
        self.TriggerGroupBox.setObjectName("TriggerGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TriggerGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TriggerModeBox = QtWidgets.QComboBox(self.TriggerGroupBox)
        self.TriggerModeBox.setObjectName("TriggerModeBox")
        self.verticalLayout_2.addWidget(self.TriggerModeBox)
        self.FrequencyBox = QtWidgets.QSpinBox(self.TriggerGroupBox)
        self.FrequencyBox.setObjectName("FrequencyBox")
        self.verticalLayout_2.addWidget(self.FrequencyBox)
        self.DelayBox = QtWidgets.QDoubleSpinBox(self.TriggerGroupBox)
        self.DelayBox.setObjectName("DelayBox")
        self.verticalLayout_2.addWidget(self.DelayBox)
        self.ThresholdBox = QtWidgets.QDoubleSpinBox(self.TriggerGroupBox)
        self.ThresholdBox.setMaximum(10.0)
        self.ThresholdBox.setObjectName("ThresholdBox")
        self.verticalLayout_2.addWidget(self.ThresholdBox)
        self.TriggerButton = QtWidgets.QPushButton(self.TriggerGroupBox)
        self.TriggerButton.setObjectName("TriggerButton")
        self.verticalLayout_2.addWidget(self.TriggerButton)
        self.horizontalLayout.addWidget(self.TriggerGroupBox)
        self.RampGroupBox = QtWidgets.QGroupBox(self.frame_2)
        self.RampGroupBox.setObjectName("RampGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.RampGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RampStartBox = QtWidgets.QDoubleSpinBox(self.RampGroupBox)
        self.RampStartBox.setDecimals(3)
        self.RampStartBox.setObjectName("RampStartBox")
        self.verticalLayout_3.addWidget(self.RampStartBox)
        self.RampStopBox = QtWidgets.QDoubleSpinBox(self.RampGroupBox)
        self.RampStopBox.setDecimals(3)
        self.RampStopBox.setObjectName("RampStopBox")
        self.verticalLayout_3.addWidget(self.RampStopBox)
        self.RampTimeBox = QtWidgets.QSpinBox(self.RampGroupBox)
        self.RampTimeBox.setMinimum(30)
        self.RampTimeBox.setMaximum(900)
        self.RampTimeBox.setSingleStep(10)
        self.RampTimeBox.setObjectName("RampTimeBox")
        self.verticalLayout_3.addWidget(self.RampTimeBox)
        self.RampNumberBox = QtWidgets.QSpinBox(self.RampGroupBox)
        self.RampNumberBox.setMinimum(1)
        self.RampNumberBox.setMaximum(999)
        self.RampNumberBox.setObjectName("RampNumberBox")
        self.verticalLayout_3.addWidget(self.RampNumberBox)
        self.RampButton = QtWidgets.QPushButton(self.RampGroupBox)
        self.RampButton.setObjectName("RampButton")
        self.verticalLayout_3.addWidget(self.RampButton)
        self.horizontalLayout.addWidget(self.RampGroupBox)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionLoad_Settings = QtWidgets.QAction(MainWindow)
        self.actionLoad_Settings.setObjectName("actionLoad_Settings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionLoad_Settings)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Connection Settings"))
        self.PulseGroupBox.setTitle(_translate("MainWindow", "Pulse Settings"))
        self.AmplitudeBox.setPrefix(_translate("MainWindow", "Amplitude: "))
        self.TriggerGroupBox.setTitle(_translate("MainWindow", "Trigger Settings"))
        self.FrequencyBox.setSuffix(_translate("MainWindow", " Hz"))
        self.FrequencyBox.setPrefix(_translate("MainWindow", "Frequency: "))
        self.DelayBox.setPrefix(_translate("MainWindow", "Delay: "))
        self.ThresholdBox.setPrefix(_translate("MainWindow", "Threshold: "))
        self.TriggerButton.setText(_translate("MainWindow", "One Pulse Trigger"))
        self.RampGroupBox.setTitle(_translate("MainWindow", "Ramp Settings"))
        self.RampStartBox.setPrefix(_translate("MainWindow", "Start: "))
        self.RampStartBox.setSuffix(_translate("MainWindow", " V"))
        self.RampStopBox.setPrefix(_translate("MainWindow", "Stop: "))
        self.RampStopBox.setSuffix(_translate("MainWindow", " V"))
        self.RampTimeBox.setSuffix(_translate("MainWindow", " s"))
        self.RampTimeBox.setPrefix(_translate("MainWindow", "Time: "))
        self.RampNumberBox.setPrefix(_translate("MainWindow", "N of cycles: "))
        self.RampButton.setText(_translate("MainWindow", "Execute Ramp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Manual"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Auto"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings"))
        self.actionLoad_Settings.setText(_translate("MainWindow", "Load Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))