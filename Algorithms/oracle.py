#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 20:13:22 2023

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
        qc.i([0,1])
        print(f'case1: constant zero: ')
    if c==2:
        qc.i(0)
        qc.x(1)
        print(f'case2: constant 1:  ')

    if c==3:
        qc.cx(0, 1)
        print(f'case3: balanced:  ')

    if c==4:
         qc.cx(0, 1)
         qc.x(1)
         print(f'case4: balanced:  ')
    
    return qc
 


def output(qc , c):
    qc.barrier([0,1])
    c = c
    qc.h(0)
    qc.measure(0, 0)
    job = execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output)[0]
    #cercuit titling 
    qctitle = qc.draw('mpl')
    qctitle.axes[0].set_title(f"case {c} oracle ")
    
    return out 

qc = QuantumCircuit(2,1)
qc.x(1)  
qc.h([0,1])
qc.barrier([0,1])

c =  random.randint(1, 4)

qcc=oracle(qc , c)
qc.compose(qcc)
out=output(qc , c)

print(f'output:  {out}')



