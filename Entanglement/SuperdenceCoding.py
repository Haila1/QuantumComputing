#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:08:57 2023

@author: ha
"""


# Importing standard Qiskit libraries
from qiskit import qiskit
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.providers.aer import QasmSimulator
from qiskit.quantum_info import *

qcc = QuantumCircuit(2,2)    
  
def encoding():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0,1)
    #qc.draw('mpl')
    qc = qc.to_gate(label = 'encoding')
    return qc   

def decoding():
    qc = QuantumCircuit(2)
    qc.cx(0,1)
    qc.h(0)
    #qc.draw('mpl')
    qc = qc.to_gate(label = 'decoding')
    return qc

def massage(m):
    if m == '00':
        qcc.i(0)
    elif m == '10':
        qcc.x(0)    
    elif m == '01':
        qcc.z(0)
    elif m == '11':
        qcc.x(0)
        qcc.z(0)
    else: 
        print('error massage,')
        x=input('if you want to abort input [A] or shift to retray: ')
        if x == 'A':
           raise Exception("error, input not valid ")
        else:
           massage(input('input valid massage:  ') )
            

qcc = qcc.compose(encoding())
massage(input('input massage:  '))
qcc = qcc.compose(decoding())

qcc.measure([0,1],[0,1])
job = execute(qcc, Aer.get_backend('qasm_simulator'))
output = job.result().get_counts()
out = list(output.keys())[0]
print(f'output : {out}')
qctitle = qcc.draw('mpl')
qctitle.axes[0].set_title("Superdence Coding ")