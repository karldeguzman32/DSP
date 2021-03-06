# -*- coding: utf-8 -*-
"""Lab02_DSPy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AmG_vz3Mtg6hRfgZZCkrz3eTLWPtwbkx
"""

import numpy as np
import scipy.signal as sig
from matplotlib import pyplot as plt

def disc_plot(x, y, title, func_name='f[n]'):
  plt.figure(figsize=(10,7))
  plt.title(title)
  plt.xlabel("n")
  plt.ylabel(func_name)
  plt.stem(x,y,use_line_collection=True)
  plt.grid()
  plt.show()

class GenerateSignal():
  def impulse_signal(min, max):
    N = np.arange(min, max+1)
    delta_sig = sig.unit_impulse(N.shape, idx='mid')
    disc_plot(N, delta_sig, "Impulse Signal")
    return delta_sig

  def unit_signal(min, max):
    N = np.arange(min, max+1)
    unit_step = np.ones(N.shape)
    unit_step[N<0]=0
    disc_plot(N, unit_step, ' Unit Signal')
    return unit_step
  
  def ramp_signal(min, max):
    N = np.arange(min, max+1)
    unit_step = np.ones(N.shape)
    unit_step[N<0]=0
    ramp_step = N * unit_step
    disc_plot(N, ramp_step, 'Ramp Signal')
    return ramp_step
  
  def exponential_decay(min, max, alpha):
    N = np.arange(min, max+1)
    unit_step = np.ones(N.shape)
    unit_step[N<0]=0
    exp_decay = (alpha**N) * unit_step
    disc_plot(N, exp_decay, 'Exponential Decay')
    return exp_decay

  def exponential_growth(min,max, alpha):
    N = np.arange(min, max+1)
    unit_step = np.ones(N.shape)
    unit_step[N<0]=0
    exp_growth = (N**alpha)*unit_step
    disc_plot(N, exp_growth, 'Exponential Growth')
    return exp_growth

  def sigmoid(min,max):
    N = np.arange(min, max+1)
    z = np.exp(-N)
    sig = 1/(1+z)
    disc_plot(N, sig, 'Sigmoid')   
    return sig
  
  def leaky_relu(min, max):
    N = np.arange(min, max+1)
    unit_step = np.ones(N.shape)
    unit_step[N<0]*=0.01
    l_relu = N*unit_step
    disc_plot(N, l_relu, 'Leaky Relu')
    return l_relu
  
  def elu(min, max, alpha):
    N = np.arange(min, max+1)
    z = np.exp(N)
    unit_step = np.ones(N.shape)
    unit_step[N<0] = (z[z<1] - 1)*alpha
    unit_step[N>=0] = N[N>=0]
    disc_plot(N, unit_step, 'ELU')
    return unit_step