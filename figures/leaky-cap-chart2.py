#!/usr/bin/env python3
"""
Create the RCL chart for a leaky capacitor with the following parameters:

    Rs = 2 Ω
    Rp = 500 kΩ
    C = 1 nF
    L = 10 μH
    fmin = 1 Hz
    fmax = 100 MHz
    zmin = 1 Ω
    zmax = 1 MΩ
    filename = "leaky-cap-chart.svg"
"""

from rlc_chart import RLC_Chart
from inform import fatal, os_error
from numpy import logspace, log10 as log, pi as π
from quantiphy import Quantity

# Add parameters as local variables
params = Quantity.extract(__doc__)
globals().update(params)

f = logspace(log(fmin), log(fmax), 2000, endpoint=True)
z1 = 2 + 1/(2j*π*f*1e-9) + 2j*π*f*10.0e-6
z2 = 5e5
z = z1 * z2 / (z1 + z2)

try:
    with RLC_Chart(filename, fmin, fmax, zmin, zmax) as chart:
        chart.add_trace(f, abs(z.real), stroke='blue')
        chart.add_trace(f, abs(z.imag), stroke='red')
        chart.add_trace(f, abs(z))
except OSError as e:
    fatal(os_error(e))
