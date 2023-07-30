#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:33:52 2023

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


qc = QuantumCircuit(4)      
qc.h(0)
qc.cx(0,1)
qc.cx(1,2)
qc.cx(2,3)
qc.x(1)

qctitle = qc.draw('mpl')
qctitle.axes[0].set_title("Qiskit Logo Ciruit")
job = execute(qc, Aer.get_backend('statevector_simulator'))
output = job.result().get_statevector()
plot_state_qsphere(output).axes[0].set_title("Qiskit Logo") 