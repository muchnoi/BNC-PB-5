from PyQt5 import QtCore, QtWidgets
from random import choices

class Active_Table:
  def __init__(self):
    self.active_rows = self.nrows
    self.ResetButton.clicked.connect(self.Reset)
    self.RandomButton.clicked.connect(self.StartStop)
    self.TimerBox.valueChanged.connect(self.CycleT)
    self.RNG = range(self.nrows)
    self.C = [[QtWidgets.QCheckBox()      for i in self.RNG], [0  for i in self.RNG]]
    self.A = [[QtWidgets.QDoubleSpinBox() for i in self.RNG], [0. for i in self.RNG], [0. for i in self.RNG]]
    self.W = [[QtWidgets.QDoubleSpinBox() for i in self.RNG], [0. for i in self.RNG], [0. for i in self.RNG]]
    self.R = [ QtWidgets.QRadioButton()   for i in self.RNG]
    layout = QtWidgets.QGridLayout()
    layout.setColumnStretch(0, 2)
    layout.setColumnStretch(1, 5)
    layout.setColumnStretch(2, 5)
    layout.setColumnStretch(3, 1)
    for i in self.RNG:
      self.C[0][i].setText('{:1X})'.format(i))
      self.C[0][i].setLayoutDirection(QtCore.Qt.RightToLeft)
      self.A[0][i].setPrefix('A = ');    self.A[0][i].setSuffix(' V');    self.A[0][i].setDecimals(3)
      self.A[0][i].setMinimum(0.0);      self.A[0][i].setMaximum(10.0)
      self.W[0][i].setPrefix('P = '); self.W[0][i].setSuffix(' %'); self.W[0][i].setDecimals(2)
      self.W[0][i].setMinimum(0.0); self.W[0][i].setMaximum(50.0)
      self.R[i].setDisabled(True)
      layout.addWidget(self.C[0][i], i, 0, alignment=QtCore.Qt.AlignRight)
      layout.addWidget(self.A[0][i],    i, 1)
      layout.addWidget(self.W[0][i], i, 2)
      layout.addWidget(self.R[i],    i, 3, alignment=QtCore.Qt.AlignRight)
      self.C[0][i].stateChanged.connect(self.Select)
      self.A[0][i].valueChanged.connect(self.Amplitudes)
      self.W[0][i].valueChanged.connect(self.Weights)
    widget = self.listframe
    widget.setLayout(layout)
    self.hide = [self.ResetButton, self.TimerBox, self.PulseGroupBox, self.TriggerGroupBox, self.RampGroupBox, self.ConnectionGroupBox]
    

  def FillTables(self):
    self.TimerBox.setValue(self.Time)
    for i in self.RNG:
      self.C[0][i].blockSignals(True); self.C[0][i].setChecked(self.C[1][i]);         self.C[0][i].blockSignals(False)
      self.A[0][i].blockSignals(True); self.A[0][i].setValue(self.A[2][i]*self.Volt); self.A[0][i].blockSignals(False)   
      self.SetProb(i, self.W[2][i])
    
  def CycleT(self):
    self.Time = self.TimerBox.value()
      
  def StartStop(self):
    button  = self.RandomButton.text()
    if  'Start' in button: 
      cumulative = 0.0
      self.population = []
      self.cumweights = []
      for i in self.RNG:
        if self.C[1][i]:
          cumulative += self.W[2][i]
          self.population.append(i)
          self.cumweights.append(cumulative)
      self.RandomButton.setText('Stop')
      self.timer.start(1000*self.Time)
      self.timer.timeout.connect(self.Switch)
      for el in self.hide: el.setEnabled(False)
    elif 'Stop' in button: 
      self.RandomButton.setText('Start')
      self.timer.timeout.disconnect(self.Switch)
      self.timer.stop()
      for el in self.hide: el.setEnabled(True)

  def Switch(self):
    i = choices(self.population, cum_weights=self.cumweights, k=1)[0]
    self.R[i].setChecked(True)
    self.exchange(4,  float('{:5.3f}'.format(self.A[2][i])))
    
  
  def Select(self):
    for i in self.RNG:
      if self.C[1][i] != self.C[0][i].isChecked():
        self.C[1][i]   = self.C[0][i].isChecked()
        self.active_rows += (2*self.C[1][i] - 1)
        break
    if self.W[0][i].value()!=0.0:  self.W[0][i].setValue(0.0)

  def Reset(self):
    for i in self.RNG:
      if self.C[1][i]: V = 100./self.active_rows
      else:            V = 0.0
      self.SetProb(i, V) 
    
  def SetProb(self, i, V):      
    self.W[2][i] = V
    V = float('{:.2f}'.format(V))
    self.W[0][i].blockSignals(True)
    self.W[0][i].setValue(V);  self.W[1][i] = V
    self.W[0][i].blockSignals(False)

  def Weights(self):
    for i in self.RNG:
      if self.W[0][i].value() != self.W[1][i]:
        V, POINT, ISON  = self.W[0][i].value(), i, self.C[1][i]
        DELTA              = V - self.W[2][i]
        self.W[1][i]       = V
        self.W[2][i]       = V
        break
    DELTA = DELTA/(self.active_rows - ISON)
    for i in self.RNG:
      if i!=POINT and self.C[1][i]:
        self.SetProb(i, self.W[2][i] - DELTA) 
    
  def Amplitudes(self, value):
    for i in self.RNG:
      if self.A[1][i] != self.A[0][i].value():
        self.A[1][i]   = self.A[0][i].value()
        self.A[2][i]   = self.A[2][i]/self.Volt

