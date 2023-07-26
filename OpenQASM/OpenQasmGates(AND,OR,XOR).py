#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:26:15 2023

@author: ha
"""



from qiskit import *
from qiskit import Aer, qiskit, qasm3, execute



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


#we can name it any thing 
# in this code we named it openQasm
AND =  '''

OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [3]   qr;



//bit [number of bits] bit name
bit [3] cr;


//reset Qubit;
reset qr;

//gates
x qr[0];
x qr[1];

//barrier 
barrier qr;

//
ccx qr[0],qr[1],qr[2];


// measure all (must be the same size)
cr[2] = measure qr[2]; 


'''
OR = '''

OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [3]   qr;



//bit [number of bits] bit name
bit [3] cr;


//reset Qubit;
reset qr;

//gates
x qr[0];
x qr[1];

//barrier 
barrier qr;

//
ccx qr[0],qr[1],qr[2];
cx qr[0],qr[2];
cx qr[1],qr[2];


// measure all (must be the same size)
cr[2] = measure qr[2]; 


'''
XOR = '''

OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [3]   qr;



//bit [number of bits] bit name
bit [3] cr;


//reset Qubit;
reset qr;

//gates
x qr[0];
x qr[1];

//barrier 
barrier qr;

//
cx qr[0],qr[1];
cx qr[1],qr[2];


// measure all (must be the same size)
cr[2] = measure qr[2]; 


'''


OQ = input('what Truth Table do you want (AND , OR , XOR )  :')
O = globals()[OQ.upper()]

qc = qiskit.qasm3.loads(O)

qc.draw('mpl')

backend = execute(qc, Aer.get_backend('qasm_simulator')).result()
count = backend.get_counts()

print(count)


