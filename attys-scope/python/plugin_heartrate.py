#!/usr/bin/python3
"""
Requires pyqtgraph.

Copyright (c) 2018-2022, Bernd Porr <mail@berndporr.me.uk>
see LICENSE file.

Plots heartrate

It's a demo how use the callback based approach and filtering.
"""

channel = 7 # 1st ADC unfiltered

import time
import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets
import numpy as np
from scipy import signal
import iir_filter
from attys_scope_plugin_comm import AttysScopeReader
import ecg_analysis
from PyQt5.QtCore import *

app = pg.mkQApp()

class QtPanningPlot:

    def __init__(self,title):
        self.mw = QtWidgets.QMainWindow()
        self.mw.setWindowTitle('HR')
        self.mw.resize(800,600)
        self.cw = QtWidgets.QWidget()
        self.mw.setCentralWidget(self.cw)
        self.l = QtWidgets.QVBoxLayout()
        self.cw.setLayout(self.l)
        self.pw = pg.PlotWidget()
        self.l.addWidget(self.pw)
        self.pw.setYRange(0,200)
        self.pw.setXRange(0,60)
        self.pw.setLabel('bottom', 't/sec')
        self.plt = self.pw.plot()
        self.data = []
        # any additional initalisation code goes here (filters etc)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.qlabelHR = QtWidgets.QLabel()
        self.qlabelHR.setStyleSheet("background-color:black; color:white; font-size: 48px;");
        self.qlabelHR.setAlignment(Qt.AlignCenter);
        self.l.addWidget(self.qlabelHR)
        self.mw.show()
        
    def update(self):
        self.data=self.data[-60:]
        if self.data:
            self.plt.setData(np.hstack(self.data))

    def addData(self,d):
        self.qlabelHR.setText("{:10.1f} BPM".format(d))
        self.data.append(d)
        
qtPanningPlot1 = QtPanningPlot("Heartrate")

# will be properly set in the callback
heartrate_detector = False

def hasHR(bpm):
    qtPanningPlot1.addData(bpm)
    print(time.time(),bpm,flush=True)

# init the detector once we know the sampling rate
def callbackFs(fs):
    global heartrate_detector
    heartrate_detector = ecg_analysis.heartrate_detector(fs,hasHR)

# process data with the filters set up
def callbackData(data):
    v = data[channel]
    heartrate_detector.detect(v)
    
attysScopeReader = AttysScopeReader(callbackData,callbackFs)
attysScopeReader.start()

# showing all the windows
app.exec_()

attysScopeReader.stop()

print("Finished")
