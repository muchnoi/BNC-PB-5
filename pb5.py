#!/usr/bin/env python3
from PyQt5  import QtWidgets
from PyQt5.QtCore import QTimer
import sys, design  

class PB5:
  Trigger = {'Mode':['Internal', 'Single', 'External', 'External Gated'], 'Threshold':5.0, 'Frequency':10.0, 'Delay':0.0 }
  Pulse   = {'Polarity':['positive', 'negative'],
             'Rise Time' : [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0],
             'Fall Time' : [0.5, 1.0, 2.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0],
             'Attenuate' : [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],
             'Clamp'     : ['ON', 'OFF']} 


class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
  def __init__(self): 
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('BNC PB-5 Pulser Control')
    self.timerA = QTimer()
    self.actionExit.triggered.connect(self.close)
    self.PB5 = PB5
    self.trigger_init()
    self.pulse_init()
    
  def trigger_init(self):
    for v in self.PB5.Trigger['Mode']: self.TriggerModeBox.addItem(v)
    
  def pulse_init(self):
    for v in self.PB5.Pulse['Polarity'] : self.PolarityBox.addItem('Polarity: {:}'.format(v))
    for v in self.PB5.Pulse['Rise Time']: self.RiseTimeBox.addItem('Rise Time: {:.2f} μs'.format(v))
    for v in self.PB5.Pulse['Fall Time']: self.FallTimeBox.addItem('Decay Time: {:.1f} μs'.format(v))
    for v in self.PB5.Pulse['Attenuate']: self.AttenuationBox.addItem('Attenuation: {:d} x'.format(v))
    for v in self.PB5.Pulse['Clamp']:     self.ClampBox.addItem('Clamp: {:}'.format(v))
    
  
   
  def closeEvent(self, event):
#    if self.tabs.DPP.Connection:
#      print("Close connection: ")
    event.accept()
#    else: event.ignore()

  def about(self):
    QtWidgets.QMessageBox.about(self, "About Application", "The <b>Application</b> example")

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
  

