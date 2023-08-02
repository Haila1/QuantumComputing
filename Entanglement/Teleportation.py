#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:25:45 2023

@author: ha
"""

from qiskit import qiskit
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.providers.aer import QasmSimulator
from math import *
from qiskit.quantum_info import *

qc = QuantumRegister(3)
cx = ClassicalRegister(1) 
cz = ClassicalRegister(1) 
teleportation = QuantumCircuit(qc,cx,cz)   

# step 0: psi and bell state 
psi = random_statevector(2) 
teleportation.initialize(psi  , 0) 
plot_bloch_multivector(psi)
teleportation.barrier()

def bellState():
    teleportation.h(1)
    teleportation.cx(1,2)
    teleportation.barrier()
#step 2.1: CNOT then H the psi and Bell state
def sara():
    teleportation.cx(0, 1)
    teleportation.h(0)
    teleportation.barrier()
    # step 2.2: measure 
    teleportation.measure(0, cz)
    teleportation.measure(1, cx)
#step 3: X and Z gates, (X if cx==1) (Z if cz ==1) 
def khalid():
    teleportation.x(2).c_if(cx, 1) 
    teleportation.z(2).c_if(cz, 1)
    
   
bellState()
sara()
khalid()

teleportation.draw('mpl')
job = execute(teleportation, Aer.get_backend('statevector_simulator'))
output = job.result().get_statevector()
plot_bloch_multivector(output)

