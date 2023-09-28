# Pharmaceutical Animal Study Analysis with Matplotlib

----

## Table of Contents (Pymaceuticals.ipynb)

----

# <br>  <br> **Section 1: Data Preparation**

> ## <br> **Section 1.1: Data Retrievel**

>> ### **Read CSV Files into DataFrames**

>> ###  **Merge DataFrames**

>> ### **Display Merged DataFrame**

> ## <br>  **Section 1.2: Mouse IDs with Duplicate Timepoints**

>> ### **Display the Number of Unique Mouse IDs**

>> ### **Check for Any Mouse IDs with Duplicate Timepoints**

>> ### **Display Mouse IDs with Duplicate Timepoints**

>> ### **Display All Mouse IDs with Duplicate Timepoints Records**

>> ### **Clean Medical Study DataFrame without Mouse IDs with Duplicate Timepoints Records**

>> ### **Display the Updated Number of Unique Mouse IDs**

# <br> <br> **Section 2: Tumor Volume Summary Statistics**

> ## <br> **Section 2.1: Statistical Calculations**

>> ### **New Medical Study DataFrame Grouped by Drug Regimen**

>> ### **Tumor Volume (Mean)**

>> ### **Tumor Volume (Median)**

>> ### **Tumor Volume (Variance)**

>> ### **Tumor Volume (Standard Deviation)**

>> ### **Tumor Volume (Standard Errror of the Mean)**

>> ### **Tumor Volume Summary Statistics DataFrame**

> ## **Section 2.2: Display Summary Statistics (Tumor Volume)**

>> ### **Display Summary Statistics**

# <br> **Section 3: Tumor Volume Over Time Per Drug Regimen**

> ## **Section 3.1: Medical Study DataFrame by Drug Regimen**

>> ### **Medical Study DataFrame (Capomulin)**

>> ### **Medical Study DataFrame (Ceftamin)**

>> ### **Medical Study DataFrame (Infubinol)**

>> ### **Medical Study DataFrame (Ketapril)**

>> ### **Medical Study DataFrame (Naftisol)**

>> ### **Medical Study DataFrame (Placebo)**

>> ### **Medical Study DataFrame (Propriva)**

>> ### **Medical Study DataFrame (Ramicane)**

>> ### **Medical Study DataFrame (Stelasyn)**

>> ### **Medical Study DataFrame (Zoniferol)**

> ## **Section 3.2: Random Mouse ID by Drug Regimen**

>> ### **Random Mouse ID Selection (Capomulin)**

>> ### **Random Mouse ID Selection (Ceftamin)**

>> ### **Random Mouse ID Selection (Infubinol)**

>> ### **Random Mouse ID Selection (Ketapril)**

>> ### **Random Mouse ID Selection (Naftisol)**

>> ### **Random Mouse ID Selection (Placebo)**

>> ### **Random Mouse ID Selection (Propriva)**

>> ### **Random Mouse ID Selection (Ramicane)**

>> ### **Random Mouse ID Selection (Stelasyn)**

>> ### **Random Mouse ID Selection (Zoniferol)**

> ## **Section 3.3: Mouse Record Retrievel by Drug Regimen**

>> ### **Mouse Data Retrieval (Capomulin)**

>> ### **Mouse Data Retrieval (Ceftamin)**

>> ### **Mouse Data Retrieval (Infubinol)**

>> ### **Mouse Data Retrieval (Ketapril)**

>> ### **Mouse Data Retrieval (Naftisol)**

>> ### **Mouse Data Retrieval (Placebo)**

>> ### **Mouse Data Retrieval (Propriva)**

>> ### **Mouse Data Retrieval (Ramicane)**

>> ### **Mouse Data Retrieval (Stelasyn)**

>> ### **Mouse Data Retrieval (Zoniferol)**

> ## **Section 3.4: Line Calculations by Drug Regimen**

>> ### **Line Calculations (Capomulin)**

>> ### **Line Calculations (Ceftamin)**

>> ### **Line Calculations (Infubinol)**

>> ### **Line Calculations (Ketapril)**

>> ### **Line Calculations (Naftisol)**

>> ### **Line Calculations (Placebo)**

>> ### **Line Calculations (Propriva)**

>> ### **Line Calculations (Ramicane)**

>> ### **Line Calculations (Stelasyn)**

>> ### **Line Calculations (Zoniferol)**

> ## **Section 3.5: Display Drug Regimen Treatment of Random Mouse**

>>  ### **Display Line Plot (Capomulin)**

>> ### **Display Line Plot (Ceftamin)**

>> ### **Display Line Plot (Infubinol)**

>> ### **Display Line Plot (Ketapril)**

>> ### **Display Line Plot (Naftisol)**

>> ### **Display Line Plot (Placebo)**

>> ### **Display Line Plot (Propriva)**

>> ### **Display Line Plot (Ramicane)**

>> ### **Display Line Plot (Stelasyn)**

>> ### **Display Line Plot (Zoniferol)**

# <br> **Section 4: Last Tumor Volume by Drug Regimen Statistics**

> ## **Section 4.1: Calculations**

>> ### **Most Promising Drug Treatment Regimens**

>> ### **The Last (Greatest) Timepoint for Each Mouse (All)**

>> ### **New Merged DataFrame with Last Timepoints (All)**

>> ### **Drug Regimen List (All)**

>> ### **Populate Tumor Volume List (All)**

> ## **Section 4.2: Display Tumor Volume Statistics**

>> ### **Display Tumor Volume Statistics (All)**

# <br> **Section 5: Last (Greatest) Timepoint  Statistics**

> ## **Section 5.1: Populate Last Timepoint List**

> ## **Section 5.2: Display Last (Greatest) Timepoint  Statistics**

# <br> **Section 6: Data Points Per Mouse Analysis**

> ## **Section 6.1: Mouse Data Points by Drug Regimen**

>> ### **Calculate Number of Observed Observatons**

>> ### **Display Observed Mouse Timepoints by Drug Regimen**

> ## **Section 6.2: Infubinol Statistical Outlier**

>> ### **Display Infubinol Statistical Outlier**

>> ### **Display Statistical Outlier Mouse Records**

> ## **Section 6.3: Range of Data Points per Mouse**

>> ### **Display Range of Data Points per Mouse**

> ## **Section 6.4: Drug Treatment Regimen by Data Points Per Mouse**

>> ### **Mouse ID by Number of Data Points**

>> ### **Display Mouse ID by Number of Data Points**

>> ### **Mouse ID Lists**

>> ### **Medical Study Information Based on Data Point Count per Mouse**

>> ### **Mouse ID/Drug Regimen Information**

>> ### **Number of Mice Vs. Drug Treatment Regimen**

>> ### **Drug Treatment Regimen by Data Points Per Mouse**

>> ### **Display Drug Treatment Regimen by Data Points Per Mouse**

> ## **Section 6.5: Percentage of Missing Data Points**

>> ### **Number of Expected Data Points**

>> ### **Number of Actual Data Points**

>> ### **Display Percentage of Missing Data Points**

# **Section 7: Tumor Volumes vs. Mouse Weights by Drug Regimen**

> ## **Section 7.1: Tumor Volumes (Median) By Drug Regimen**

>> ### **Tumor Volumes (Median) By Drug Regimen (Capomulin)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Ceftamin)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Infubinol)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Ketapril)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Naftisol)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Placebo)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Propriva)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Ramicane)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Stelasyn)**

>> ### **Tumor Volumes (Median) By Drug Regimen (Zoniferol)**

> ## **Section 7.2: Mouse Weights (Median) by Drug Regimen**

>> ### **Mouse Weights (Median) by Drug Regimen (Capomulin)**

>> ### **Mouse Weights (Median) by Drug Regimen (Ceftamin)**

>> ### **Mouse Weights (Median) by Drug Regimen (Infubinol)**

>> ### **Mouse Weights (Median) by Drug Regimen (Ketapril)**

>> ### **Mouse Weights (Median) by Drug Regimen (Naftisol)**

>> ### **Mouse Weights (Median) by Drug Regimen (Placebo)**

>> ### **Mouse Weights (Median) by Drug Regimen (Propriva)**

>> ### **Mouse Weights (Median) by Drug Regimen (Ramicane)**

>> ### **Mouse Weights (Median) by Drug Regimen (Stelasyn)**

>> ### **Mouse Weights (Median) by Drug Regimen (Zoniferol)**

> ## **Section 7.3: Display Tumor Volumes vs. Mouse Weights With Regression**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Capomulin)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Ceftamin)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Infubinol)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Ketapril)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Naftisol)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Placebo)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Propriva)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Ramicane)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Stelasyn)**

>> ### **Display Tumor Volumes vs. Mouse Weights With Regression (Zoniferol)**

>> ### **Display Tumor Volumes vs. Mouse Weights Plots with High Correlation**

> ## **Section 7.4: Mouse Weight Statistics**

>> ### **Median Mouse Weights DataFrame**

>> ### **Display Mouse ID by Drug Regimen and Weight**

>> ### **Populate Median Mouse Weight List**

>> ### **Display Mouse Weight Statistics**

# <br> **Section 8: Male vs. Female Mouse Distribution**

> ## **Section 8.1: Mouse Count by Gender for Each Regimen**

>> ### **Calculate Mouse Count by Gender (Capomulin)**

>> ### **Calculate Mouse Count by Gender (Ceftamin)**

>> ### **Calculate Mouse Count by Gender (Infubinol)**

>> ### **Calculate Mouse Count by Gender (Ketapril)**

>> ### **Calculate Mouse Count by Gender (Naftisol)**

>> ### **Calculate Mouse Count by Gender (Placebo)**

>> ### **Calculate Mouse Count by Gender (Propriva)**

>> ### **Calculate Mouse Count by Gender (Ramicane)**

>> ### **Calculate Mouse Count by Gender (Stelasyn)**

>> ### **Calculate Mouse Count by Gender (Zoniferol)**

>> ### **Calculate Mouse Count by Gender (All)**

>> ### **Gender Count Distribution DataFrame**

>> ### **Display Mouse Gender Count Distribution by Drug Regimen**

>> ### **Gender Percent Distribution DataFrame**

>> ### **Display Mouse Gender Percent Distribution by Drug Regimen**

> ## **Section 8.2: DisplayMale vs. Female Mouse Distribution**

>> ### **Display Female vs. Male Distribution  (All)**

>> ### **Display Female vs. Male Distribution (Capomulin)**

>> ### **Display Female vs. Male Distribution (Ceftamin)**

>> ### **Display Female vs. Male Distribution (Infubinol)**

>> ### **Display Female vs. Male Distribution (Ketapril)**

>> ### **Display Female vs. Male Distribution (Naftisol)**

>> ### **Display Female vs. Male Distribution (Placebo)**

>> ### **Display Female vs. Male Distribution (Propriva)**

>> ### **Display Female vs. Male Distribution (Ramicane)**

>> ### **Display Female vs. Male Distribution (Stelasyn)**

>> ### **Display Female vs. Male Distribution (Zoniferol)**

>> ### **Display Female vs. Male Distribution (All)**

----

## Copyright

N. James George © 2023. All Rights Reserved.
