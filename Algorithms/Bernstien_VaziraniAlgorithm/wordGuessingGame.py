#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:43:05 2023
@author: ha
"""


from qiskit import QuantumCircuit, transpile, Aer, IBMQ, BasicAer, qiskit, execute
from qiskit.visualization import plot_histogram
import random


# binary and ASCII 
import binascii

# user password 
word = input("Enter word and numbers for the quantum computer to Guess, And please keep it short: ")
#NOTE: long strings work too but for some reason my name Restarts the kernel

# string to a binary: 
# word.encode('utf-8') string as UTF-8 to obtain bytes
# binascii.hexlify() bytes to a hexadecimal 
# int(hex_string, 16) hexadecimal to an integer, base = 16
# bin(int()) converts  integer to a binary  
# [2:] remove the leading '0b'.
key = bin(int(binascii.hexlify(word.encode('utf-8')), 16))[2:]
# binary string lingth 
n = len(key)


# Quantum part
# qquantum cerciut qc
qc = QuantumCircuit(n+1,n)

#BV oracle
def oracle(oq):
    for i in range(n):
        if key[i] == '0':
            oq.i(i)
        else:
            oq.cx(i,n)  
    return oq
 
#BV Algorithm
# returns the binary string optaind by the BV Algorithm
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
    print(f'oracle output:  {s}')
    return s 

#binary string optaind by the BV Algorithm
skey = BV_Algo(qc)    

#binary to string:
#int(skey, 2) binary to integer, base = 2
# '%x' % int(skey, 2) integer to a hexadecimal
# binascii.unhexlify() converts hexadecimal to binary 
# .decode('utf-8') decodes binary into a UTF-8 encoded string
p = binascii.unhexlify('%x' % int(skey, 2)).decode('utf-8')
print("the word is :", p)








