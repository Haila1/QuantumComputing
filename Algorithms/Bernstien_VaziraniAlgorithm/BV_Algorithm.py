#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:40:16 2023

@author: ha
"""



import numpy as np
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ, BasicAer, qiskit
import random

key = input('input key :  ')
n = len(key)
qc = QuantumCircuit(n+1,n)

def oracle(oq):
    for i in range(n):
        
        if key[i] == '0':
            oq.i(i)
        else:
            oq.cx(i,n)
            
    #gate = oq.to_gate(label = 'oracle ')   
    return oq
 
def BV_Algo(qc):
    qc.x(n)
    qc.h(range(0,n+1))
    qc.barrier(range(0,n+1))
    
    
    oq = QuantumCircuit(n+1)
    oq=oracle(oq)
    
    qc = qc.compose(oq)
    
    qc.barrier(range(0,n+1))
    qc.h(range(0,n))
    qc.measure(range(0,n), range(0,n))
    job = execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output)[0]
    s = out[::-1]
    #cercuit titling 
    qctitle = qc.draw('mpl')
    qctitle.axes[0].set_title(" BV Algorithm ")
    
    print(f'output:  {s}')

BV_Algo(qc)
