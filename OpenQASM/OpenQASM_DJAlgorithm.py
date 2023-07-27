#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:11:50 2023

@author: ha
"""
import numpy as np

# Importing standard Qiskit libraries
from qiskit import qiskit
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *

from qiskit.providers.aer import QasmSimulator
from math import *
from qiskit.quantum_info import *

#Quantum Project 3: Deutsch-Jozsa Algorithm
#Task 1: 
#     Steps:
#     1-by Study the Deutsch-Jozsa algorithm you understand its working principles and the role of the oracle.
#     2-Design a quantum circuit to create a balanced oracle for the problem.
#     3-Clearly explain the design choices and the reasoning behind them in your code comments.
#     4-Test the oracle using various inputs to verify its balanced behavior.

DJ = '''
OPENQASM 3;

include "stdgates.inc";

gate DJ() q0, q1, q2{
    cx q0,q2;
    cx q1,q2;
     }


qubit [3] qr;
bit [3] cr;

reset qr;
x qr[2];

barrier qr;
h qr;
//function using
DJ() qr[0], qr[1], qr[2];
barrier qr;
h qr[0];
h qr[1]; 

barrier qr;

cr[0] = measure qr[0];
cr[1] = measure qr[1];



'''

qc=qiskit.qasm3.loads(DJ)
qc.draw('mpl')

#backend = execute(qc, Aer.get_backend('qasm_simulator')).result()       -> qasm_simulator error -> no if in qasm_simulator
backend = execute(qc, Aer.get_backend('aer_simulator')).result()
count = backend.get_counts()

print(count)