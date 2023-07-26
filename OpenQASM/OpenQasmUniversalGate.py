#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:03:27 2023

@author: ha
"""



from qiskit import *
from qiskit import Aer, qiskit, qasm3, execute

OQ='''


OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [2]   qr;



//bit [number of bits] bit name
bit [2] cr;

reset qr;



//the Z gate 
//U(0,0,pi) qr[0]; 


// CZ ctrl @ Gate controlQubit , targetQubit;
ctrl @ U(0,0,pi) qr[0], qr[1]; 

h qr[0];



cx qr[0] , qr[1];


cr = measure qr; 

'''

# T , T† , y


# circuits to openQasm
#qasm_str = qiskit.qasm3.dumps(qc)

# tern gate to U 
#qc.decomposw()

qc = qiskit.qasm3.loads(OQ)

qc.draw('mpl')

backend = execute(qc, Aer.get_backend('qasm_simulator')).result()
count = backend.get_counts()

print(count)