#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PymaceuticalsSubRoutines.py
 #
 #  File Description:
 #      This Python script, PymaceuticalsSubRoutines.py, contains generic 
 #      Python subroutines for completing common tasks in the Pymaceuticals
 #      Challenge.  Here is the list:
 #
 #      DisplayTumorVolumeStatistics
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyLogFunctions as log_function
import PyLogSubRoutines as log_subroutine
import PyFunctions as function


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PymaceuticalsSubRoutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  SubRoutine Name:  DisplayTumorVolumeStatistics
 #
 #  Function Description:
 #      This subroutine calculates summary statistics about each drug 
 #      and displays the results.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          dataSeriesParameter
 #                          The parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/19/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayTumorVolumeStatistics \
        (regimenListParameter,
         tumorVolumeSeriesListParameter,
         sectionNameStringParameter,
         typeStringParameter):
    
    try:
    
        for index, regimen in enumerate(regimenListParameter):
            
            summaryStatisticsDataFrame \
                = function \
                    .ReturnSummaryStatisticsAsDataFrame \
                        (tumorVolumeSeriesListParameter[ index ])
            
            captionStringVariable \
                = 'Table ' \
                  + sectionNameStringParameter \
                  + f'.{index+1}: ' \
                  + typeStringParameter \
                  + f' Statistics for {regimen}'
            
            currentStylerObject \
                = function \
                    .ReturnStylerObjectStandardFormat \
                        (summaryStatisticsDataFrame, 
                         captionStringVariable)
            
            log_function \
                .ReturnStylerObjectSavePNGImage \
                    (currentStylerObject,
                     captionStringVariable)
            
            display \
                (currentStylerObject)

    except:
    
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayTumorVolumeSeriesList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to display tumor volume statistics.')


# In[ ]:




