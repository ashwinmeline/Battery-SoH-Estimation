Li-ion Battery State-of-Health (SoH) Estimation

Independant Academic Project | FAU Erlangen-Nürnberg | Electromobility-ACES

Overview

This project implements a data-driven pipeline to estimate the State-of-Health (SoH) of Lithium-ion cells using the NASA PCoE dataset. 
The focus is on robust Signal Processing and Feature Engineering to predict capacity fade.

Key Technical Achievements

Methodology & Physics Data Source: NASA Ames Prognostics Center of Excellence (PCoE) Battery Aging Dataset (B0005).

Physics-Based Feature: The Time-to-3.5V feature was selected because it represents the "Discharge Voltage Plateau." 
As the internal resistance of a Li-ion cell increases (Aging), the voltage drops faster under load, making the discharge duration to a fixed threshold a highly linear proxy for capacity loss.

Preprocessing: Implemented MATLAB-to-Python flattening, handling inconsistent indexing across different NASA battery IDs (B0005, B0006).

ML Performance: Achieved an R^2 score of 0.9968 and a Mean Absolute Error (MAE) of 0.0086 Ah using a Linear Regression baseline.

Feature Engineering: Extracted "Time-to-3.5V" from raw discharge telemetry as a primary health indicator.

Modular Data Pipeline: Authored a standalone data_loader.py to handle nested MATLAB structures and inconsistent field naming.

Project Structure

data/: Contains data_loader.py for automated ETL (Extract, Transform, Load) tasks.

notebooks/: Exploratory Data Analysis (EDA) and Model Training.

results/: Visualizations of Capacity Fade and Residual Analysis.
