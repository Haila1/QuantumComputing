#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:04:12 2023

@author: ha
"""

import numpy as np

# Importing standard Qiskit libraries
from qiskit import qiskit
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ, BasicAer
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.visualization import plot_histogram

from qiskit.providers.aer import QasmSimulator
from math import *
from qiskit.quantum_info import *

def ANDgate(qc):
    
    qc.ccx(0, 1, 2)
    qc.measure(2,0)

    return  qc.draw('mpl')

def ORgate(qc):
    qc.ccx(0,1,2)
    qc.cx(0,2)
    qc.cx(1,2)
    qc.measure(2,0)
    
    return qc # or qc.draw('mpl')
    
def XORgate(qc):
    qc.cx(0,2)
    qc.cx(1,2)
    qc.measure(2,0)
    
    return qc # or qc.draw('mpl')

def NANDgate(qc):
    qc.ccx(0, 1, 2)
    qc.x(2)
    qc.measure(2,0)

    return  qc # or qc.draw('mpl')

def NORgate(qc):
    qc.ccx(0,1,2)
    qc.cx(0,2)
    qc.cx(1,2)
    qc.x(2)
    qc.measure(2,0)
    
    return qc # or qc.draw('mpl')

qc = QuantumCircuit(3,1)
print(ANDgate(qc))
# print(ORgate(qc))
# print(XORgate(qc))
# print(NANDgate(qc))
# print(NORgate(qc))


