"""
Battery Data Loader Logic
Developed by: [Ashwin Meline Antony]
Purpose: Extracts and flattens NASA PCoE Battery Dataset (.mat) for ML training.
"""
import numpy as np
from scipy.io import loadmat

# 'file_path' 
def load_nasa_data(file_path):
    """
    Function based on Section #2 of the analysis notebook.
    Extracts discharge cycles from NASA .mat files.
    """
    # 'file_path' here
    data = loadmat(file_path)
    
    # Automatically finds the battery key (e.g., 'B0005')
    battery_key = [k for k in data.keys() if not k.startswith('__')][0]
    cycles = data[battery_key][0, 0]['cycle'][0]

    discharge_cycles = []

    for i in range(len(cycles)):
        cycle_type = cycles[i]['type'][0]
        
        if cycle_type == 'discharge':
            meas = cycles[i]['data']
            
            # Robust extraction of 'Capacity'
            try:
                capacity_val = cycles[i]['capacity'][0][0]
            except (ValueError, KeyError, IndexError):
                capacity_val = meas['Capacity'][0][0][0]
            
            # Organizes the messy arrays into a clean dictionary
            discharge_cycles.append({
                'voltage': meas['Voltage_measured'][0][0].flatten(),
                'current': meas['Current_measured'][0][0].flatten(),
                'temp': meas['Temperature_measured'][0][0].flatten(),
                'time': meas['Time'][0][0].flatten(),
                'capacity': float(capacity_val.item()) if hasattr(capacity_val, 'item') else float(capacity_val) 
            })

    return discharge_cycles
  
