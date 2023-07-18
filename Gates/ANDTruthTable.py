#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:06:27 2023

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


def ANDTruthTable(qc,i,j):
    if i == 0 and j==1:
        qc.x(1)
    elif i==1 and j==0:
        qc.x(0)
    elif i==1 and j==1:
        qc.x(0)
        qc.x(1)
        
    qc.ccx(0, 1, 2)
    qc.measure(2, 0)
    job = qiskit.execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output.keys())[0]
        
    return  out



#nq = int(input('number of qubits :  '))
qc = QuantumCircuit(3 ,1)

for i in range(0,2):
    for j in range(0,2):
        qc = QuantumCircuit(3 ,1)
        out = ANDTruthTable(qc,i,j)
        print(f'{i} {j}  :  {out}')
        #ß®print(qc.draw('mpl'))
        