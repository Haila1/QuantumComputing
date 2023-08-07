#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:05:46 2023

@author: ha
"""

import numpy as np
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ, BasicAer, qiskit
from qiskit.visualization import plot_histogram
import random

# NOTE: the histogram will give 0s and the KEY, the output will be 0s or the KEY 


key = input('inter key :  ')
n = len(key)
qc = QuantumCircuit(n+1,n)

def oracle(oq):
    for i in range(n):
        
        if key[i] == '0':
            oq.i(i)
        else:
            oq.cz(i,n)
            
    gate = oq.to_gate(label = 'oracle ')   
    return gate
 
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
    plot_histogram(output)
    print(f'output:  {s}')

BV_Algo(qc)
