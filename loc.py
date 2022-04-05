import obspy as ob
import numpy as np
import mpl_interactions.ipyplot as iplt
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor, Button
import os
import pandas as pd
from random import rand

def rdata(p):
 global data
 data = ob.read(p, debug_headers=True)
 ndat = len(p)/3
 print(data)

def gtrazas(d):
 global times
 fig = plt.figure()
 gs = fig.add_gridspec(len(d), hspace=0)
 axs = gs.subplots(sharex=True,sharey=True)
 
 for i in np.linspace(0,len(d)-1,len(d)).astype(int):
  axs[i].plot(d[i].times("timestamp"), d[i].data,color='k', label=d[i].stats.station + " " + d[i].stats.channel)
  axs[i].legend(loc='upper left')
  axis.append(np.array(axs[i].get_position()))
 
 for ax in axs:
  ax.label_outer()

 clicks = MultiCursor(fig.canvas, axs, horizOn=False, vertOn=True, color='blue',lw=0.5)

 fig.autofmt_xdate()
 fig.canvas.mpl_connect('key_press_event', onclick)
 
 plt.show()
 
def onclick(event):
 if event.key == 'P':
  p.append(event.xdata)
  pa.append(np.array(event.inaxes.get_position()))
  plt.plot(event.xdata, event.ydata) 
  plt.text(event.xdata, event.ydata, "P")
  plt.draw()
 if event.key ==  'S':
  s.append(event.xdata)
  sa.append(np.array(event.inaxes.get_position()))
  plt.scatter(event.xdata, event.ydata) 
  plt.text(event.xdata, event.ydata, "P")
  fig.canvas.draw()

def sannealing(ppa):
 clati = 16.39 - 90
 loni = -98.1274
 to = p[1]
 platmax = 2
 platmin = -2
 plonmax = 4
 plonmin = -4

 while True:
  for j in np.linspace(0,2,3).astype(int):
   for i in np.linspace(0,2,3).astype(int):
    save = 
   

axis = []
hist = []
while True:
 opc = str(input("LOC> "))
 hist.append(opc)

 if opc[0] == "r":
  path = opc[2:]
  print(opc[2:]) 
  rdata(path)

 if opc[0] == "p":
  p = []
  pa = []
  ppa = []
  if data is None:
   print("No se han leido datos")
  else:
   gtrazas(data)
   for j in np.linspace(0,len(pa)-1,len(pa)).astype(int):
    for i in np.linspace(0,len(axis)-1,len(axis)).astype(int):
     #asd = abs(sum(pa[j][:,1] - axis[i][:,1]))
     #print(asd)
     if abs(sum(pa[j][:,1] - axis[i][:,1])) < 0.1:
      print("hola")
      ppa.append((p[j],data[i].stats.station))
   print(ppa)  


 if opc[0:2] == "ls":
  print(os.listdir())
 
 if opc[0:2] == "cd":
  os.chdir(opc[3:])

 if opc[:] == "h":
  print(hist)

 if opc[:] == "t":
  print(times)

 if opc[:] == "q":
  break
