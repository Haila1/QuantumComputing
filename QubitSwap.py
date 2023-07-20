#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:08:49 2023

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

nq = int(input(' Enter number of Qubits  :  '))
qc = QuantumCircuit(nq)
qc.x([10,12])
qc.draw('mpl')

# qc.measure_all()
# job = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024)
# output = job.result().get_counts()
# out = list(output.keys())[0]
# print(out)

for i in range(0,int(nq/2)):
    qc.swap(i, int(nq-i-1))

qc.measure_all()
job = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024)
output = job.result().get_counts()
out = list(output)
print(out)
qc.draw('mpl')
    
    
