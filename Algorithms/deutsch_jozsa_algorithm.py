#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:23:36 2023

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
import random




def oracle(qc , c):
    
    if c==1:
        oq.i(range(0,n))
        gate = oq.to_gate(label = 'constant')
        
        print('constant: ')
        

        
    if c==2:
        oq.cx(range(0,n),n)
        gate = oq.to_gate(label = 'balanced:')
        print('balanced: ')


    return gate
 


def output(qc , c):
    qc.barrier(range(0,n+1))
    c = c
    qc.h(range(0,n))
    qc.measure(range(0,n), range(0,n))
    job = execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output)[0]
    #cercuit titling 
    qctitle = qc.draw('mpl')
    qctitle.axes[0].set_title(f" case {c} oracle ")
    
    return out 


n = int(input('inter number of n:   '))
c = random.randint(1, 2)

qc = QuantumCircuit(n+1,n)
oq = QuantumCircuit(n+1)
qc.x(n)
qc.h(range(0,n+1))
qc.barrier(range(0,n+1))


oq=oracle(oq , c)
qc= qc.compose(oq)
out=output(qc , c)

print(f'output:  {out}')



