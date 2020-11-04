#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys, design, pickle 
from atable import Active_Table
#from serial import Serial 

class PB5:
  Port    = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyUSB2', '/dev/ttyS0', '/dev/ttyS1', 'COM1', 'COM1', 'COM3']
  Trigger = ['Internal', 'Single', 'External', 'External Gated']
  Pulse   = {'Pulse'     :['ON', 'OFF'],
             'Polarity'  :['Negative', 'Positive'],
             'Pulse Top' :['Flat', 'Tail'],
             'Rise Time' :[0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0],
             'Fall Time' :[0.5, 1.0, 2.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0],
             'Attenuate' :[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],
             'Clamp'     :['OFF', 'ON']}
  Tell    = ['SET TRIIGGER MODE {}',   'TRIGGER ONE PULSE',     'SET THRESHOLD {:.1f}',    'SET PULSE ON {:1d}',
             'SET AMPLITUDE {:.3f}',   'SET REP RATE {:d}',     'SET WIDTH {:d}',          'SET DELAY {:d}',
             'SET RISE TIME {:d}',     'SET FALL TIME {:d}',    'SET TAIL PULSE {:1d}',    'SET POLARITY POSITIVE {:1d}',
             'SET ATTENUATION {:d}',   'SET DISPLAY keV {:1d}', 'SET EQUIVALENT keV {:d}', 'CLAMP BASELINE {:1d}',
             'SET RAMP STARTV {:.3f}', 'SET RAMP STOPV {:.3f}', 'SET RAMP STARTeV {:.3f}', 'SET RAMP STOPeV {:.3f}',
             'SET RAMP TIME {:d}',     'SET RAMP CYCLES {:d}',  'EXECUTE RAMP', 'RECALL FACTORY DEFAULTS', 'HELP']

  def __init__(self): self.Read_Parameters()

  def Save_Parameters(self):
    with open('settings.pickle', 'wb') as fp: pickle.dump(self.config, fp)
    
  def Read_Parameters(self):
    try:     
      with open('settings.pickle', 'rb') as fp: self.config = pickle.load(fp)
    except FileNotFoundError: 
      self.config  = {'Port':1, 'Trigger':0, 'Frequency':100, 'Delay':0.25, 'Threshold':5.0, 
                      'Polarity':0, 'Pulse Top':0, 'Width':0.1, 'Rise Time':0, 'Fall Time':0, 'Amplitude':1.0, 'Attenuate':6, 'Clamp':0,
                      'Ramp Start':1.0, 'Ramp Stop':2.0, 'Ramp Time':30, 'Ramp Cycles':10, 
                      'Volt':1.0,
                      'Time':1.0,
                      'Volts':[0.5*(i+1) for i in range(16)],
                      'Probs':[100./16.  for i in range(16)],
                      'OnOff':[True      for i in range(16)]
                      }

class Application(QtWidgets.QMainWindow, design.Ui_MainWindow, Active_Table):
  def __init__(self): 
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('BNC PB-5 Pulser Control')
    self.actionExit.triggered.connect(self.close)
    self.timer = QTimer()
    self.PB5 = PB5()
    self.nrows = 16
    self.Init_Widgets()
    Active_Table.__init__(self)
    self.Read_Configuration()

    self.actionSave_Settings.triggered.connect(self.Save_Configuration)
    self.actionLoad_Settings.triggered.connect(self.Read_Configuration)
#    self.tabWidget.setCurrentWidget(self.settings_tab)
    
  def closeEvent(self, event):
    event.accept()

  def about(self):
    QtWidgets.QMessageBox.about(self, "About Application", "The <b>Application</b> example")
 
  def Save_Configuration(self):
    self.PB5.config['Port']        = self.SerialPortBox.currentIndex()
    self.PB5.config['Trigger']     = self.TriggerModeBox.currentIndex()
    self.PB5.config['Frequency']   = self.FrequencyBox.value()
    self.PB5.config['Delay']       = self.DelayBox.value()
    self.PB5.config['Threshold']   = self.ThresholdBox.value()
    self.PB5.config['Polarity']    = self.PolarityBox.currentIndex()
    self.PB5.config['Pulse Top']   = self.PulseTopBox.currentIndex()
    self.PB5.config['Width']       = self.WidthBox.value()
    self.PB5.config['Rise Time']   = self.RiseTimeBox.currentIndex()
    self.PB5.config['Fall Time']   = self.FallTimeBox.currentIndex()
    self.PB5.config['Amplitude']   = self.Volts[0]
    self.PB5.config['Attenuate']   = self.AttenuateBox.currentIndex()
    self.PB5.config['Clamp']       = self.ClampBox.currentIndex()
    self.PB5.config['Ramp Start']  = self.Volts[1]
    self.PB5.config['Ramp Stop']   = self.Volts[2]
    self.PB5.config['Ramp Time']   = self.RampTimeBox.value()
    self.PB5.config['Ramp Cycles'] = self.RampCyclBox.value()
    self.PB5.config['Volt']        = self.Volt
    self.PB5.config['Time']        = self.Time
    self.PB5.config['Volts']       = self.A[2]
    self.PB5.config['Probs']       = self.W[2]
    self.PB5.config['OnOff']       = self.C[1]
#    print('SAVE')
#    for el in self.PB5.config.items(): print (el)
    self.PB5.Save_Parameters()
  
  def Read_Configuration(self):
    self.allow_connection = False
    self.PB5.Read_Parameters()
#    print('READ')
#    for el in self.PB5.config.items(): print (el)
    self.Volt                         = self.PB5.config['Volt']
    self.Time                         = self.PB5.config['Time']
    self.A[2]                         = self.PB5.config['Volts'] # volts no kev
    self.W[2]                         = self.PB5.config['Probs'] # float weights
    self.C[1]                         = self.PB5.config['OnOff'] 
    self.Dimension_Widgets = [self.AmplitudeBox, self.RampStartBox, self.RampStopBox] + self.A[0]
    self.Volts = [self.PB5.config['Amplitude'], self.PB5.config['Ramp Start'], self.PB5.config['Ramp Stop']]
    self.SerialPortBox.blockSignals(True)
    self.SerialPortBox.setCurrentIndex( self.PB5.config['Port'])
    self.SerialPortBox.blockSignals(False)
    self.TriggerModeBox.setCurrentIndex(self.PB5.config['Trigger'])
    self.FrequencyBox.setValue(         self.PB5.config['Frequency'])
    self.DelayBox.setValue(             self.PB5.config['Delay'])
    self.ThresholdBox.setValue(         self.PB5.config['Threshold'])
    self.PolarityBox.setCurrentIndex(   self.PB5.config['Polarity'])
    self.PulseTopBox.setCurrentIndex(   self.PB5.config['Pulse Top'])
    self.WidthBox.setValue(             self.PB5.config['Width'])
    self.RiseTimeBox.setCurrentIndex(   self.PB5.config['Rise Time'])
    self.FallTimeBox.setCurrentIndex(   self.PB5.config['Fall Time'])
    self.AttenuateBox.setCurrentIndex(  self.PB5.config['Attenuate'])
    self.ClampBox.setCurrentIndex(      self.PB5.config['Clamp'])
    self.RampTimeBox.setValue(          self.PB5.config['Ramp Time'])
    self.RampCyclBox.setValue(          self.PB5.config['Ramp Cycles'])
    self.AmplitudeBox.blockSignals(True); self.AmplitudeBox.setValue(self.PB5.config['Amplitude']*self.Volt);  self.AmplitudeBox.blockSignals(False)
    self.RampStartBox.blockSignals(True); self.RampStartBox.setValue(self.PB5.config['Ramp Start']*self.Volt); self.RampStartBox.blockSignals(False)
    self.RampStopBox.blockSignals( True); self.RampStopBox.setValue(self.PB5.config['Ramp Stop']*self.Volt);   self.RampStopBox.blockSignals(False)
    self.keVBox.blockSignals(      True); self.keVBox.setValue(self.PB5.config['Volt']);                       self.keVBox.blockSignals(False)
    self.FillTables()
    self.Units(self.Volt)
    self.serial_connection(self.SerialPortBox.currentIndex())
 
  def Init_Widgets(self):
    for v in self.PB5.Port:               self.SerialPortBox.addItem('Serial port: {}'.format(v))
    for v in self.PB5.Trigger:            self.TriggerModeBox.addItem(v)
    for v in self.PB5.Pulse['Polarity'] : self.PolarityBox.addItem('Polarity: {}'.format(v))
    for v in self.PB5.Pulse['Pulse Top']: self.PulseTopBox.addItem('Pulse top: {}'.format(v))
    for v in self.PB5.Pulse['Rise Time']: self.RiseTimeBox.addItem('Rise Time: {:.2f} μs'.format(v))
    for v in self.PB5.Pulse['Fall Time']: self.FallTimeBox.addItem('Decay Time: {:.1f} μs'.format(v))
    for v in self.PB5.Pulse['Attenuate']: self.AttenuateBox.addItem('Attenuation: {:d} x'.format(v))
    for v in self.PB5.Pulse['Clamp']:     self.ClampBox.addItem('Clamp Baseline: {:}'.format(v))
    self.SerialPortBox.currentIndexChanged.connect(self.serial_connection)
    self.TriggerButton.clicked.connect(           lambda x: self.exchange(1,  ''))
    self.ThresholdBox.valueChanged.connect(       lambda x: self.exchange(2,  self.ThresholdBox.value()))
    self.PulseOnButton.clicked.connect(           lambda x: self.exchange(3,  1))
    self.PulseOffButton.clicked.connect(          lambda x: self.exchange(3,  0))
    self.AmplitudeBox.valueChanged.connect(       lambda x: self.changeex(4,  0, self.AmplitudeBox.value()))
    self.FrequencyBox.valueChanged.connect(       lambda x: self.exchange(5,  self.FrequencyBox.value()))
    self.WidthBox.valueChanged.connect(           lambda x: self.exchange(6,  int(1000*self.WidthBox.value())))
    self.keVBox.valueChanged.connect(self.Units)
    self.DelayBox.valueChanged.connect(           lambda x: self.exchange(7,  int(1000*self.DelayBox.value())))
    self.RiseTimeBox.currentIndexChanged.connect( lambda x: self.exchange(8,  int(1000*self.PB5.Pulse['Rise Time'][self.RiseTimeBox.currentIndex()])))
    self.FallTimeBox.currentIndexChanged.connect( lambda x: self.exchange(9,  int(1000*self.PB5.Pulse['Fall Time'][self.FallTimeBox.currentIndex()])))
    self.PulseTopBox.currentIndexChanged.connect( lambda x: self.exchange(10, self.PulseTopBox.currentIndex()))
    self.PolarityBox.currentIndexChanged.connect( lambda x: self.exchange(11, self.PolarityBox.currentIndex()))
    self.AttenuateBox.currentIndexChanged.connect(lambda x: self.exchange(12, self.PB5.Pulse['Attenuate'][self.AttenuateBox.currentIndex()]))
    self.ClampBox.currentIndexChanged.connect(    lambda x: self.exchange(15, self.ClampBox.currentIndex()))
    self.RampStartBox.valueChanged.connect(       lambda x: self.changeex(16, 1, self.RampStartBox.value()))
    self.RampStopBox.valueChanged.connect(        lambda x: self.changeex(17, 2, self.RampStopBox.value()))
    self.RampTimeBox.valueChanged.connect(        lambda x: self.exchange(20, int(self.RampTimeBox.value())))
    self.RampCyclBox.valueChanged.connect(        lambda x: self.exchange(21, int(self.RampCyclBox.value())))
    self.RampButton.clicked.connect(              lambda x: self.exchange(22, ''))
    self.TriggerModeBox.currentIndexChanged.connect(self.trigger_mode)

  def changeex(self, command, vindex, value):
    self.Volts[vindex] = value/self.Volt
    self.exchange(command, self.Volts[vindex])

  def Units(self, k):
    for Wgt in self.Dimension_Widgets:
      Wgt.blockSignals(True)
      Wgt.setMaximum(10.0*k)
      if k == 1.0: Wgt.setSuffix(' V');   Wgt.setDecimals(3); Wgt.setSingleStep(0.1)
      else:        Wgt.setSuffix(' keV'); Wgt.setDecimals(1); Wgt.setSingleStep(1.0)
      Wgt.setValue(k * (self.Volts+self.A[2])[self.Dimension_Widgets.index(Wgt)])
      Wgt.blockSignals(False)
    self.Volt = k
    

  def serial_connection(self, index):
#    self.link = serial.Serial() 
    self.link = self.PB5.Port[index]
    print ('link=', self.link)
    self.allow_connection = True
    self.exchange(3, 0)
    self.PulseOffButton.setChecked(True)
#    self.PulseOffClone.setChecked(True)
    if self.connection:
      self.trigger_mode(self.PB5.config['Trigger'])
      self.exchange(2,  self.ThresholdBox.value())
      self.changeex(4,  0, self.AmplitudeBox.value())
      self.exchange(5,  self.FrequencyBox.value())
      self.exchange(6,  int(1000*self.WidthBox.value()))
      self.exchange(7,  int(1000*self.DelayBox.value()))
      self.exchange(8,  int(1000*self.PB5.Pulse['Rise Time'][self.RiseTimeBox.currentIndex()]))
      self.exchange(9,  int(1000*self.PB5.Pulse['Fall Time'][self.FallTimeBox.currentIndex()]))
      self.exchange(10, self.PulseTopBox.currentIndex())
      self.exchange(11, self.PolarityBox.currentIndex())
      self.exchange(12, self.PB5.Pulse['Attenuate'][self.AttenuateBox.currentIndex()])
      self.exchange(15, self.ClampBox.currentIndex())
      self.changeex(16, 1, self.RampStartBox.value())
      self.changeex(17, 2, self.RampStopBox.value())
      self.exchange(20, int(self.RampTimeBox.value()))
      self.exchange(21, int(self.RampCyclBox.value()))
      self.PulseGroupBox.setEnabled(True)
      self.TriggerGroupBox.setEnabled(True)
      self.RampGroupBox.setEnabled(True)
      self.RandomGroupBox.setEnabled(True)
      self.ConnectCheckBox.setChecked(True)
    else:
      self.PulseGroupBox.setEnabled(False)
      self.TriggerGroupBox.setEnabled(False)
      self.RampGroupBox.setEnabled(False)
      self.RandomGroupBox.setEnabled(False)
      self.ConnectCheckBox.setChecked(False)
        
    
  def trigger_mode(self, index):
    M = ['INTERNAL', 'ONE PULSE', 'EXTERNAL', 'GATED']
    self.FrequencyBox.setEnabled( index == 0)
    self.ThresholdBox.setEnabled( index >= 2)
    self.TriggerButton.setEnabled(index == 1)
    self.exchange(0, M[index])
  
  
  def exchange(self, key, value):
    if self.SerialPortBox.currentIndex() == 0 and self.allow_connection:
      self.connection = True
      command = self.PB5.Tell[key].format(value)  
      print (command)
    else:
      self.connection = False
      self.PulseOffButton.setChecked(True)
#      self.PulseOffClone.setChecked(True)
#    self.statusBar().showMessage(command)

def main():
  try:
    app    = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()
  except:
    window.closeEvent()
#    window.tabs.__del__()
  print("Good Bye!")
  
if __name__ == '__main__':  main()  

