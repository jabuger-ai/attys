# -*- coding: utf-8 -*-
"""
@author: Bernd Porr, mail@berndporr.me.uk

Plots the frequency spectrum of the 1st selected channel in
attys-scope (and its filtering).
Start from within attys-scope.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.signal as signal
import collections
from attys_scope_plugin_comm import AttysScopeReader


# sampling rate, updated in callback
fs = False

# update rate in ms
updateRate = 1000

# time window in sec
timeWindow = 3

# Title for the Channel:
titleChannel = "cross correlation"

# From data Column:
channel_attys1 = 11
channel_attys2 = 11+20

# do abs
doAbs = True
if doAbs:
    titleChannel = "abs("+titleChannel+")"

ringbuffer = collections.deque([], 1000)

# now let's plot the data
fig, ax = plt.subplots(1,1)
ax.set_xlabel('')
ax.set_ylabel('Amplitude/V^2')
ax.set_xlabel('time/secs')
ax.set_title(titleChannel)

# empty axes
e = np.array([1,2])
line, = ax.plot(e,e)

# receives the data from the generator below
def update(data):
    global ringbuffer
    global channel
    global line
    global ax, fig
    global titlePlot
    # axis
    crosscorr = signal.correlate(np.array(ringbuffer)[:,channel_attys1], np.array(ringbuffer)[:,channel_attys2])
    if doAbs:
        crosscorr = np.abs(crosscorr)
    tmin = -len(crosscorr)/fs/2
    tmax = len(crosscorr)/fs/2
    t = np.linspace(tmin,tmax,len(crosscorr))
    line.set_data(t,crosscorr)
    # set new max
    ax.set_ylim(crosscorr.min()*1.2,crosscorr.max()*1.2)
    ax.set_xlim(tmin,tmax)
    # return the line
    return line

def callbackFs(_fs):
    global fs
    fs = _fs
    global ringbuffer
    ringbuffer = collections.deque([], fs*timeWindow)

def callbackData(data):
    global ringbuffer
    ringbuffer.append(data)
    
attysScopeReader = AttysScopeReader(callbackData,callbackFs)
attysScopeReader.start()

# start the animation
ani = animation.FuncAnimation(fig, update, interval=updateRate)

# show it
plt.show()

attysScopeReader.stop()

print("finished")
