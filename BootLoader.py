'''
Author: Toby Sherwood
Date: 11/6/18

AIMS: Bootloader for calibration process
--------------------------------------------------------------------------
Set up


Log Data
    Check the system is working
    Test DAC offset by running Testfile.py on @pi
    Configure DAC by running characterise_DAC.py on @pi
    ready to recive connection by running consolidator.py on PC
    run characterise_DAC on mode 3 to play each DAC value for 10 minutes
    observe process to ensure values are not too wrong

Calculate Coeffs
    pull data from phone
    pull data from calibration
    collate data
    use logged data in calc_calibration_params.py

Anylyse results
    Check results
    analyse data to confirm calibration successful


Upload results
----------------------------------------------------------------------------
'''

import numpy as np
import pandas as pd

