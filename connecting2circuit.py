#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:41:42 2023

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



qc1 = QuantumCircuit(2)
qc1.x(0)
qc1.draw('mpl')

qc2 = QuantumCircuit(2)
qc2.h(1)
qc2.draw('mpl')

qc3 = QuantumCircuit(2)
qc3 = qc1.compose(qc2)
qc3.draw('mpl')
