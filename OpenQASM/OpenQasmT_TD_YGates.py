#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:21:32 2023

@author: ha
"""



from qiskit import *
from qiskit import Aer, qiskit, qasm3, execute

T='''


OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [2]   qr;



//bit [number of bits] bit name
bit [2] cr;

reset qr;


//U(pi/4);

// ct ctrl @ Gate controlQubit , targetQubit;

//CT
ctrl @ U(0,0,pi/4) qr[0], qr[1];

cr = measure qr; 


'''


TD='''

OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [2]   qr;



//bit [number of bits] bit name
bit [2] cr;

reset qr;

//CT†
ctrl @ U(0,0,-pi/4) qr[0], qr[1];

cr = measure qr; 

'''



Y='''


OPENQASM 3;

//we need to include library
include "stdgates.inc";

// circuit [Qubit number]  qubit name
qubit [2]   qr;



//bit [number of bits] bit name
bit [2] cr;

reset qr;

//CY
ctrl @ U(pi,pi/2,pi/2) qr[0], qr[1];


cr = measure qr; 

'''

# T , T† , y
# circuits to openQasm
#qasm_str = qiskit.qasm3.dumps(qc)

# tern gate to U 
#qc.decompose()

OQ = input('what Truth Table do you want (T , TD , Y )  :')
O = globals()[OQ.upper()]

qc = qiskit.qasm3.loads(O)

qc.draw('mpl')

backend = execute(qc, Aer.get_backend('qasm_simulator')).result()
count = backend.get_counts()

print(count)

