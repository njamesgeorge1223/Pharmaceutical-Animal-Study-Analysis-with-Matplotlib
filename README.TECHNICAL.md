# **Pharmaceutical Animal Study Analysis with Matplotlib**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook requires the following to execute: holoviews, hvplot, panel, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install panel

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

----

### **Usage:**

----

The IPython notebook, Pymaceuticals.ipynb, uses the CSV files, MouseMetaData.csv and StudyResults.csv, as input and will not run without them.  The interactive Python notebook must have the following Python scripts in the same folder with it:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PymaceuticalsFunctions.py

PymaceuticalsSubRoutines.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  The Resources folder holds input files from the IPython Notebook; the Logs folder contains debug and log files from testing the IPython Notebook; and the Images folder has the PNG image files of the IPython Notebook's tables and plots.

To place the IPython notebook in log mode, debug mode, or image mode set the parameter for the appropriate subroutine in coding cell #2 to True. In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in log mode for log information sent to a log file. If the program is in log mode but not debug mode, it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes all DataFrames, hvplot maps, and matplotlib plots to png files in the Images folder.

----

### **Resource Summary:**

----


#### Source code

Pymaceuticals.ipynb, PyConstants.py, PyFunctions.py, PyLogConstants.py, PyLogFunctions.py, PyLogSubRoutines.py, PymaceuticalsFunctions.py, PymaceuticalsSubRoutines.py, PySubroutines.py

#### Input files

MouseMetaData.csv, StudyResults.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Python 3.11.4, Pandas, Matplotlib, Numpy

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./ETLMiniProjectConstants.py](./ETLMiniProjectConstants.py)

|&rarr; [./ETLMiniProject_NGeorge_SSmith.ipynb](./ETLMiniProject_NGeorge_SSmith.ipynb)

|&rarr; [./PyConstants.py](./PyConstants.py)  

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/ETLMiniProjectTable111InitialCrowdfundingDataFrame.png](./Images/ETLMiniProjectTable111InitialCrowdfundingDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable113CrowdfundingDataFrameDescription.png](./Images/ETLMiniProjectTable113CrowdfundingDataFrameDescription.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable114CrowdfundingDataFrameMemoryUsage.png](./Images/ETLMiniProjectTable114CrowdfundingDataFrameMemoryUsage.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable121UpdatedCrowdfundingDataFrame.png](./Images/ETLMiniProjectTable121UpdatedCrowdfundingDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable131CategoryDataFrame.png](./Images/ETLMiniProjectTable131CategoryDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable132SubcategoryDataFrame.png](./Images/ETLMiniProjectTable132SubcategoryDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable211InitialCampaignDataFrame.png](./Images/ETLMiniProjectTable211InitialCampaignDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable221CampaignDataFrameWithRenamedColumns.png](./Images/ETLMiniProjectTable221CampaignDataFrameWithRenamedColumns.png)

  &emsp; |&rarr; [./Images/ETLMiniProjectTable222CampaignDataFrameColumnDataTypes.png](./Images/ETLMiniProjectTable222CampaignDataFrameColumnDataTypes.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable223CampaignDataFrameWithDates.png](./Images/ETLMiniProjectTable223CampaignDataFrameWithDates.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable231MergedCampaignDataFrame.png](./Images/ETLMiniProjectTable231MergedCampaignDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable232CleanMergedCampaignDataFrameFinal.png](./Images/ETLMiniProjectTable232CleanMergedCampaignDataFrameFinal.png)

  &emsp; |&rarr; [./Images/ETLMiniProjectTable234CleanMergedCampaignDataFrameDescription.png](./Images/ETLMiniProjectTable234CleanMergedCampaignDataFrameDescription.png)
  
  &emsp; |&rarr; 
[./Images/ETLMiniProjectTable235CleanMergedCampaignDataFrameMemoryUsage.png](./Images/ETLMiniProjectTable235CleanMergedCampaignDataFrameMemoryUsage.png)

  &emsp; |&rarr; [./Images/ETLMiniProjectTable311InitialContactsDataFrame.png](./Images/ETLMiniProjectTable311InitialContactsDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable321UpdatedContactsDataFramewithContactID.png](./Images/ETLMiniProjectTable321UpdatedContactsDataFramewithContactID.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable324UpdatedContactsDataFrameWithName.png](./Images/ETLMiniProjectTable324UpdatedContactsDataFrameWithName.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable325UpdatedContactsDataFrameWithEmail.png](./Images/ETLMiniProjectTable325UpdatedContactsDataFrameWithEmail.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable331TransformedContactsDataFrame.png](./Images/ETLMiniProjectTable331TransformedContactsDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable332TransformedContactsDataFrameWithFirstandLastNames.png](./Images/ETLMiniProjectTable332TransformedContactsDataFrameWithFirstandLastNames.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable341CleanContactsDataFrame.png](./Images/ETLMiniProjectTable341CleanContactsDataFrame.png)
  
  &emsp; |&rarr; [./Images/ETLMiniProjectTable343CleanContactsDataFrameMemoryUsage.png](./Images/ETLMiniProjectTable343CleanContactsDataFrameMemoryUsage.png)
  
  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20230922ETLMiniProjectDebug.txt](./Logs/20230922ETLMiniProjectDebug.txt)

  &emsp; |&rarr; [./Logs/20230922ETLMiniProjectLog.txt](./Logs/20230922ETLMiniProjectLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

  &emsp; |&rarr; [./Resources/campaign.csv](./Resources/campaign.csv)

  &emsp; |&rarr; [./Resources/category.csv](./Resources/category.csv)

  &emsp; |&rarr; [./Resources/contacts.csv](./Resources/contacts.csv)

  &emsp; |&rarr; [./Resources/contacts.xlsx](./Resources/contacts.xlsx)

  &emsp; |&rarr; [./Resources/crowdfunding.xlsx](./Resources/crowdfunding.xlsx)

  &emsp; |&rarr; [./Resources/subcategory.csv](./Resources/subcategory.csv)

|&rarr; [./SQL/](./SQL/)

  &emsp; |&rarr; [./SQL/PostgresDBTable_campaign.png](./SQL/PostgresDBTable_campaign.png)

  &emsp; |&rarr; [./SQL/PostgresDBTable_category.png](./SQL/PostgresDBTable_category.png)
  
  &emsp; |&rarr; [./SQL/PostgresDBTable_contacts.png](./SQL/PostgresDBTable_contacts.png)

  &emsp; |&rarr; [./SQL/PostgresDBTable_subcategory.png](./SQL/PostgresDBTable_subcategory.png)

  &emsp; |&rarr; [./SQL/Project2Group8EntityRelationshipDiagram.png](./SQL/Project2Group8EntityRelationshipDiagram.png)

  &emsp; |&rarr; [./SQL/README.md](./SQL/README.md)

  &emsp; |&rarr; [./SQL/crowdfunding_db_schema.sql](./SQL/crowdfunding_db_schema.sql)

----

### **References:**

----

[ETL (Extract, Transform, Load)](https://www.bmc.com/blogs/what-is-etl-extract-transform-load-etl-explained/) \

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html) \

[PgAdmin Documentation](https://www.postgresql.org/docs/) \

[Postgres Documentation](https://www.pgadmin.org/docs/) \

[PostgresSQL Documentation](https://www.postgresql.org/docs/) \

[The Complete Guide to Regular Expressions](https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/) \

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.


