#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:06:04 2023

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


qc1 = QuantumCircuit(1,1)
ket = [0,1]
qc1.initialize(ket, 0)
qc1.draw('mpl')

job = execute(qc1, Aer.get_backend('statevector_simulator'))
output = job.result().get_statevector()
#print(Aer.backends())

plot_state_qsphere(output)
plot_bloch_multivector(output)

