#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:58:30 2023

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
     

def bellStates():
    qc1 = QuantumCircuit(2)      
    qc1.h(0)
    qc1.cx(0,1)
    qc1.draw('mpl')
    qctitle = qc1.draw('mpl')
    qctitle.axes[0].set_title("case1 |00> + |11>")
    job = execute(qc1, Aer.get_backend('statevector_simulator'))
    output = job.result().get_statevector()
    plot_state_qsphere(output)

    
    qc2 = QuantumCircuit(2)       
    qc2.h(0)
    qc2.cx(0,1)
    qc2.z(1)
    qctitle = qc2.draw('mpl')
    qctitle.axes[0].set_title("case2  |00> - |11>")
    job = execute(qc2, Aer.get_backend('statevector_simulator'))
    output = job.result().get_statevector()
    plot_state_qsphere(output)
    
    qc3 = QuantumCircuit(2)
    qc3.h(0)
    qc3.cx(0,1)
    qc3.x(0)
    qctitle = qc3.draw('mpl')
    qctitle.axes[0].set_title("case3 |01> + |10>")
    job = execute(qc3, Aer.get_backend('statevector_simulator'))
    output = job.result().get_statevector()
    plot_state_qsphere(output)
    
    
    qc4 = QuantumCircuit(2)
    qc4.h(0)
    qc4.cx(0,1)
    qc4.x(0)
    qc4.z(1)
    qctitle = qc4.draw('mpl')
    qctitle.axes[0].set_title("case4 |01> - |10>")
    job = execute(qc4, Aer.get_backend('statevector_simulator'))
    output = job.result().get_statevector()
    plot_state_qsphere(output)
    
    
    


bellStates()