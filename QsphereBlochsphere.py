#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:41:02 2023

@author: ha
"""

from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_state_qsphere, plot_bloch_multivector

qc = QuantumCircuit(1,1)
qc.h(0)
#qc.measure(0, 0)
job = execute(qc, Aer.get_backend('statevector_simulator'))
output = job.result().get_statevector()
#print(Aer.backends())

plot_state_qsphere(output)
plot_bloch_multivector(output)


qc = QuantumCircuit(3,1)
qc.h(0)
#qc.measure(0, 0)
job = execute(qc, Aer.get_backend('statevector_simulator'))
output = job.result().get_statevector()
#print(Aer.backends())

plot_state_qsphere(output)
plot_bloch_multivector(output)


