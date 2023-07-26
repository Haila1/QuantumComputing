#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:25:06 2023

@author: ha
"""


from qiskit import *
from qiskit import Aer, qiskit, qasm3, execute

#we can name it any thing 
# in this code we named it openQasm
openQasm = '''

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


# use what we defind using openQasm in qiskit

qc = qiskit.qasm3.loads(openQasm)
qc.draw('mpl')

backend = execute(qc, Aer.get_backend('qasm_simulator')).result()
count = backend.get_counts()

print(count)




























