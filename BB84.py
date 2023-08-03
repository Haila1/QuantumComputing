import numpy as np
from numpy.random import randint
from qiskit import qiskit
from qiskit import *
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.providers.aer import QasmSimulator
from math import *
from qiskit.quantum_info import *

from qiskit.quantum_info import random_statevector #to omport 
import random


np.random.seed(seed=0)

n = int(input('input massage length '))
m_filter =  randint(2, size=n)
bob_filter = randint(2, size=n)
m_to_qc = []
bob_measure = []
#step2: massage
m = randint(2, size=n)

def alice():
    #m = input(' input massage ')
    #m_list = m.split() 

    for i in range(n):
        qc = QuantumCircuit(1,1)
        
        # Z-axis
        if m_filter[i] == 0: 
            if m[i] == 1:
                qc.x(0)
        else: #X-axis
            if m[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        m_to_qc.append(qc)
        
        m_to_qc[i].draw('mpl')
        

def bob():
    for i in range(n):
        # measuring in Z-axis
        if bob_filter[i] == 0:
            m_to_qc[i].measure(0,0)
            
        # measuring in X-axis
        if bob_filter[i] == 1: 
            m_to_qc[i].h(0)
            m_to_qc[i].measure(0,0)

        job = execute(m_to_qc[i], Aer.get_backend('qasm_simulator'))
        output= job.result().get_counts()
        out = list(output.keys())[0]
        bob_measure.append(int(out))
        
        m_to_qc[i].draw('mpl')
    



alice()
bob()

#comparing 
alice_key = []
for i in range(n):
    if m_filter[i] == bob_filter[i]:
         alice_key.append(m[i])
print( f' alice_key=  {alice_key}' )
Bob_key = []
for i in range(n):
    if m_filter[i] == bob_filter[i]:
         Bob_key.append(bob_measure[i])
print(f' bob key =  {Bob_key}')
if Bob_key == alice_key:
    print('shared key')

        

 
   
    
   
    
   