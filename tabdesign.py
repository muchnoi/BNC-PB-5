# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabdesign.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 675)
        MainWindow.setStyleSheet("QGroupBox { border: 1px solid grey;   border-radius: 10px;   font-weight: bold; font-size: 11pt; color: black; padding:8px; margin:8px; background-color: #F0F0F0;}\n"
"QGroupBox::title {  subcontrol-origin: margin;   subcontrol-position: top center;    padding:  0 5px;  }\n"
"QSpinBox {             background-color: #FFFFFF; }\n"
"QDoubleSpinBox {background-color: #FFFFFF;} ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setObjectName("Tabs")
        self.tabManual = QtWidgets.QWidget()
        self.tabManual.setObjectName("tabManual")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabManual)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.tabManual)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SerialPortBox = QtWidgets.QComboBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialPortBox.sizePolicy().hasHeightForWidth())
        self.SerialPortBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SerialPortBox.setFont(font)
        self.SerialPortBox.setObjectName("SerialPortBox")
        self.verticalLayout_6.addWidget(self.SerialPortBox)
        self.PulseGroupBox = QtWidgets.QGroupBox(self.frame_5)
        self.PulseGroupBox.setObjectName("PulseGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PulseGroupBox)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.PulseGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(4, 8, 4, 8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PulseOnButton = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PulseOnButton.sizePolicy().hasHeightForWidth())
        self.PulseOnButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PulseOnButton.setFont(font)
        self.PulseOnButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PulseOnButton.setObjectName("PulseOnButton")
        self.horizontalLayout_5.addWidget(self.PulseOnButton)
        self.PulseOffButton = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PulseOffButton.sizePolicy().hasHeightForWidth())
        self.PulseOffButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PulseOffButton.setFont(font)
        self.PulseOffButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PulseOffButton.setObjectName("PulseOffButton")
        self.horizontalLayout_5.addWidget(self.PulseOffButton)
        self.verticalLayout.addWidget(self.frame)
        self.PolarityBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.PolarityBox.setObjectName("PolarityBox")
        self.verticalLayout.addWidget(self.PolarityBox)
        self.AttenuateBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.AttenuateBox.setObjectName("AttenuateBox")
        self.verticalLayout.addWidget(self.AttenuateBox)
        self.AmplitudeBox = QtWidgets.QDoubleSpinBox(self.PulseGroupBox)
        self.AmplitudeBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AmplitudeBox.setDecimals(3)
        self.AmplitudeBox.setMaximum(10.0)
        self.AmplitudeBox.setSingleStep(0.25)
        self.AmplitudeBox.setObjectName("AmplitudeBox")
        self.verticalLayout.addWidget(self.AmplitudeBox)
        self.PulseTopBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.PulseTopBox.setObjectName("PulseTopBox")
        self.verticalLayout.addWidget(self.PulseTopBox)
        self.RiseTimeBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.RiseTimeBox.setObjectName("RiseTimeBox")
        self.verticalLayout.addWidget(self.RiseTimeBox)
        self.FallTimeBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.FallTimeBox.setObjectName("FallTimeBox")
        self.verticalLayout.addWidget(self.FallTimeBox)
        self.WidthBox = QtWidgets.QDoubleSpinBox(self.PulseGroupBox)
        self.WidthBox.setDecimals(3)
        self.WidthBox.setMinimum(0.1)
        self.WidthBox.setMaximum(10000.0)
        self.WidthBox.setObjectName("WidthBox")
        self.verticalLayout.addWidget(self.WidthBox)
        self.ClampBox = QtWidgets.QComboBox(self.PulseGroupBox)
        self.ClampBox.setObjectName("ClampBox")
        self.verticalLayout.addWidget(self.ClampBox)
        self.keVBox = QtWidgets.QDoubleSpinBox(self.PulseGroupBox)
        self.keVBox.setMinimum(1.0)
        self.keVBox.setMaximum(10000.0)
        self.keVBox.setSingleStep(10.0)
        self.keVBox.setProperty("value", 1.0)
        self.keVBox.setObjectName("keVBox")
        self.verticalLayout.addWidget(self.keVBox)
        self.verticalLayout_6.addWidget(self.PulseGroupBox)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.tabManual)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ConnectCheckBox = QtWidgets.QCheckBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectCheckBox.sizePolicy().hasHeightForWidth())
        self.ConnectCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ConnectCheckBox.setFont(font)
        self.ConnectCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ConnectCheckBox.setObjectName("ConnectCheckBox")
        self.verticalLayout_8.addWidget(self.ConnectCheckBox, 0, QtCore.Qt.AlignHCenter)
        self.TriggerGroupBox = QtWidgets.QGroupBox(self.frame_7)
        self.TriggerGroupBox.setObjectName("TriggerGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TriggerGroupBox)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TriggerModeBox = QtWidgets.QComboBox(self.TriggerGroupBox)
        self.TriggerModeBox.setObjectName("TriggerModeBox")
        self.verticalLayout_2.addWidget(self.TriggerModeBox)
        self.FrequencyBox = QtWidgets.QSpinBox(self.TriggerGroupBox)
        self.FrequencyBox.setMinimum(2)
        self.FrequencyBox.setMaximum(500000)
        self.FrequencyBox.setSingleStep(10)
        self.FrequencyBox.setObjectName("FrequencyBox")
        self.verticalLayout_2.addWidget(self.FrequencyBox)
        self.DelayBox = QtWidgets.QDoubleSpinBox(self.TriggerGroupBox)
        self.DelayBox.setMinimum(0.25)
        self.DelayBox.setMaximum(10000.0)
        self.DelayBox.setObjectName("DelayBox")
        self.verticalLayout_2.addWidget(self.DelayBox)
        self.ThresholdBox = QtWidgets.QDoubleSpinBox(self.TriggerGroupBox)
        self.ThresholdBox.setDecimals(1)
        self.ThresholdBox.setMinimum(0.1)
        self.ThresholdBox.setMaximum(3.5)
        self.ThresholdBox.setSingleStep(0.5)
        self.ThresholdBox.setProperty("value", 1.0)
        self.ThresholdBox.setObjectName("ThresholdBox")
        self.verticalLayout_2.addWidget(self.ThresholdBox)
        self.TriggerButton = QtWidgets.QPushButton(self.TriggerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TriggerButton.sizePolicy().hasHeightForWidth())
        self.TriggerButton.setSizePolicy(sizePolicy)
        self.TriggerButton.setMinimumSize(QtCore.QSize(0, 0))
        self.TriggerButton.setAutoDefault(True)
        self.TriggerButton.setObjectName("TriggerButton")
        self.verticalLayout_2.addWidget(self.TriggerButton)
        self.verticalLayout_8.addWidget(self.TriggerGroupBox)
        self.RampGroupBox = QtWidgets.QGroupBox(self.frame_7)
        self.RampGroupBox.setObjectName("RampGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.RampGroupBox)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(4)
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
        self.RampCyclBox = QtWidgets.QSpinBox(self.RampGroupBox)
        self.RampCyclBox.setMinimum(1)
        self.RampCyclBox.setMaximum(999)
        self.RampCyclBox.setObjectName("RampCyclBox")
        self.verticalLayout_3.addWidget(self.RampCyclBox)
        self.RampButton = QtWidgets.QPushButton(self.RampGroupBox)
        self.RampButton.setMinimumSize(QtCore.QSize(0, 0))
        self.RampButton.setAutoDefault(True)
        self.RampButton.setObjectName("RampButton")
        self.verticalLayout_3.addWidget(self.RampButton)
        self.verticalLayout_8.addWidget(self.RampGroupBox)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.Tabs.addTab(self.tabManual, "")
        self.tabRandom = QtWidgets.QWidget()
        self.tabRandom.setObjectName("tabRandom")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabRandom)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.tabRandom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.RandomButton = QtWidgets.QPushButton(self.frame_3)
        self.RandomButton.setObjectName("RandomButton")
        self.horizontalLayout_4.addWidget(self.RandomButton)
        self.TimerBox = QtWidgets.QSpinBox(self.frame_3)
        self.TimerBox.setMinimum(1)
        self.TimerBox.setMaximum(10)
        self.TimerBox.setObjectName("TimerBox")
        self.horizontalLayout_4.addWidget(self.TimerBox)
        self.ResetButton = QtWidgets.QPushButton(self.frame_3)
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout_4.addWidget(self.ResetButton)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.listframe = QtWidgets.QFrame(self.tabRandom)
        self.listframe.setStyleSheet("")
        self.listframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listframe.setObjectName("listframe")
        self.verticalLayout_4.addWidget(self.listframe)
        self.Tabs.addTab(self.tabRandom, "")
        self.verticalLayout_5.addWidget(self.Tabs)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 16, 16))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 20))
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
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.PulseOnButton, self.PulseOffButton)
        MainWindow.setTabOrder(self.PulseOffButton, self.PolarityBox)
        MainWindow.setTabOrder(self.PolarityBox, self.AttenuateBox)
        MainWindow.setTabOrder(self.AttenuateBox, self.AmplitudeBox)
        MainWindow.setTabOrder(self.AmplitudeBox, self.PulseTopBox)
        MainWindow.setTabOrder(self.PulseTopBox, self.RiseTimeBox)
        MainWindow.setTabOrder(self.RiseTimeBox, self.FallTimeBox)
        MainWindow.setTabOrder(self.FallTimeBox, self.WidthBox)
        MainWindow.setTabOrder(self.WidthBox, self.ClampBox)
        MainWindow.setTabOrder(self.ClampBox, self.keVBox)
        MainWindow.setTabOrder(self.keVBox, self.TriggerModeBox)
        MainWindow.setTabOrder(self.TriggerModeBox, self.FrequencyBox)
        MainWindow.setTabOrder(self.FrequencyBox, self.DelayBox)
        MainWindow.setTabOrder(self.DelayBox, self.ThresholdBox)
        MainWindow.setTabOrder(self.ThresholdBox, self.TriggerButton)
        MainWindow.setTabOrder(self.TriggerButton, self.RampStartBox)
        MainWindow.setTabOrder(self.RampStartBox, self.RampStopBox)
        MainWindow.setTabOrder(self.RampStopBox, self.RampTimeBox)
        MainWindow.setTabOrder(self.RampTimeBox, self.RampCyclBox)
        MainWindow.setTabOrder(self.RampCyclBox, self.RampButton)
        MainWindow.setTabOrder(self.RampButton, self.RandomButton)
        MainWindow.setTabOrder(self.RandomButton, self.TimerBox)
        MainWindow.setTabOrder(self.TimerBox, self.ResetButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PulseGroupBox.setTitle(_translate("MainWindow", "Pulse Settings"))
        self.PulseOnButton.setText(_translate("MainWindow", "Pulse: ON"))
        self.PulseOffButton.setText(_translate("MainWindow", "OFF"))
        self.AmplitudeBox.setPrefix(_translate("MainWindow", "Amplitude: "))
        self.AmplitudeBox.setSuffix(_translate("MainWindow", " V"))
        self.WidthBox.setPrefix(_translate("MainWindow", "Width: "))
        self.WidthBox.setSuffix(_translate("MainWindow", " μs"))
        self.keVBox.setPrefix(_translate("MainWindow", "1 V = "))
        self.keVBox.setSuffix(_translate("MainWindow", " keV"))
        self.ConnectCheckBox.setText(_translate("MainWindow", "Connection:"))
        self.TriggerGroupBox.setTitle(_translate("MainWindow", "Trigger"))
        self.FrequencyBox.setSuffix(_translate("MainWindow", " Hz"))
        self.FrequencyBox.setPrefix(_translate("MainWindow", "Rep. Rate: "))
        self.DelayBox.setPrefix(_translate("MainWindow", "Delay: "))
        self.DelayBox.setSuffix(_translate("MainWindow", " μs"))
        self.ThresholdBox.setPrefix(_translate("MainWindow", "Threshold: "))
        self.ThresholdBox.setSuffix(_translate("MainWindow", " V"))
        self.TriggerButton.setText(_translate("MainWindow", "Single Trigger"))
        self.RampGroupBox.setTitle(_translate("MainWindow", "Ramp Settings"))
        self.RampStartBox.setPrefix(_translate("MainWindow", "Start: "))
        self.RampStartBox.setSuffix(_translate("MainWindow", " V"))
        self.RampStopBox.setPrefix(_translate("MainWindow", "Stop: "))
        self.RampStopBox.setSuffix(_translate("MainWindow", " V"))
        self.RampTimeBox.setSuffix(_translate("MainWindow", " s"))
        self.RampTimeBox.setPrefix(_translate("MainWindow", "Time: "))
        self.RampCyclBox.setPrefix(_translate("MainWindow", "N cycles: "))
        self.RampButton.setText(_translate("MainWindow", "Execute Ramp"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabManual), _translate("MainWindow", "Manual Control"))
        self.RandomButton.setText(_translate("MainWindow", "Start"))
        self.TimerBox.setSuffix(_translate("MainWindow", " s"))
        self.TimerBox.setPrefix(_translate("MainWindow", "Cycle t = "))
        self.ResetButton.setText(_translate("MainWindow", "Weights Reset"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabRandom), _translate("MainWindow", "Random Mode"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings"))
        self.actionSave_Settings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad_Settings.setText(_translate("MainWindow", "Load Settings"))
        self.actionLoad_Settings.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
