#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 19:22:20 2023

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



gate = QuantumCircuit(2)

def case1(gate):
    gate.i([0,1])
    gate = gate.to_gate(label = 'constant zero:')
    print(f'case1: constant zero: ')
    
    return gate
    
def case2(gate):
    gate.i(0)
    gate.x(1)
    gate = gate.to_gate(label = 'constant one')
    print(f'case2: constant 1:  ')
   
    return gate

def case3(gate):
    gate.cx(0, 1)
    gate = gate.to_gate(label = 'balanced:')
    print(f'case3: balanced:  ')
    return gate

def case4(gate):
    gate.cx(0, 1)
    gate.x(1)
    gate = gate.to_gate(label = 'balanced:')
    print(f'case4: balanced:  ')
    return gate
    

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



#random number between 1 and 4
c =  random.randint(1, 4)

#funcction call
if c==1:
    gate=case1(gate)
if c==2:
    gate=case2(gate)
if c==3:
    gate=case3(gate)
if c==4:
    gate=case4(gate)

#composing 2 cercuits
qc=qc.compose(gate)

#output 
out=output(qc , c)

print(f'output:  {out}')






