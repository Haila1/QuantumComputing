#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:35:13 2023

@author: ha
"""

#TruthTables

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


def ORTruthTable(qc,i,j):
    if i == 0 and j==1:
        qc.x(1)
    elif i==1 and j==0:
        qc.x(0)
    elif i==1 and j==1:
        qc.x(0)
        qc.x(1)
        
    qc.ccx(0,1,2)
    qc.cx(0,2)
    qc.cx(1,2)
    qc.measure(2, 0)
    job = qiskit.execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output.keys())[0]
        
    return  out


def XORTruthTable(qc,i,j):
    if i == 0 and j==1:
        qc.x(1)
    elif i==1 and j==0:
        qc.x(0)
    elif i==1 and j==1:
        qc.x(0)
        qc.x(1)
        
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.measure(2, 0)
    job = qiskit.execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output.keys())[0]
        
    return  out



def NANDTruthTable(qc,i,j):
    if i == 0 and j==1:
        qc.x(1)
    elif i==1 and j==0:
        qc.x(0)
    elif i==1 and j==1:
        qc.x(0)
        qc.x(1)
        
    qc.ccx(0, 1, 2)
    qc.x(2)
    qc.measure(2, 0)
    job = qiskit.execute(qc, Aer.get_backend('qasm_simulator'))
    output = job.result().get_counts()
    out = list(output.keys())[0]
        
    return  out




qc = QuantumCircuit(3 ,1)
tt = input('what Truth Table do you want (AND , OR , XOR , NAND) :  ')


if tt== 'AND':
    for i in range(0,2):
        for j in range(0,2):
            qc = QuantumCircuit(3 ,1)
            out = ANDTruthTable(qc,i,j)
            print(f'{i} {j}  :  {out}')
            #print(qc.draw('mpl'))

if tt=='NAND':
    for i in range(0,2):
        for j in range(0,2):
            qc = QuantumCircuit(3 ,1)
            out = NANDTruthTable(qc,i,j)
            print(f'{i} {j}  :  {out}')
            #print(qc.draw('mpl'))

if tt=='OR':
    for i in range(0,2):
        for j in range(0,2):
            qc = QuantumCircuit(3 ,1)
            out = ORTruthTable(qc,i,j)
            print(f'{i} {j}  :  {out}')
            #print(qc.draw('mpl'))
        
    
if tt=='XOR':
    for i in range(0,2):
        for j in range(0,2):
            qc = QuantumCircuit(3 ,1)
            out = XORTruthTable(qc,i,j)
            print(f'{i} {j}  :  {out}')
            #print(qc.draw('mpl'))
        
            

    
    
