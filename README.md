----

# Pymaceuticals Animal Study Analysis

----

Over the course of 45 days, this study analyzes the effects of a placebo and nine drug treatment regimens on the tumor development of 248 mice suffering from a commonly occurring form of skin cancer, squamous cell carcinoma (SCC).  From the initial results, the most promising treatments include Ceftamin, Infubinol, Ramicane, and this company’s drug of interest, Capomulin.  The study’s ultimate purpose is to compare the performance of Capomulin against the other drug candidates.

A superficial review yields some interesting observations concerning the efficacy of the top four drugs.  Except for Ramicane with its symmetrical tumor volume distribution, all the treatment regimens have skewed distributions towards the low end indicated by a difference between the median and mean below.  Moreover, Ramicane and Capomulin have the narrowest distributions while Ceftamin’s is the widest, about as wide as the placebo’s, followed by Infubinol.  Generally, the narrower distributions with their lower variances infer consistency in outcomes.  On top of that, Ramicane and Capomulin have the lowest median tumor volumes; Ceftamin and Infubinol have the same median, which is noticeably higher and comparable to the placebo’s value.  What’s more, Capomulin’s mouse weight and tumor volume metrics have a very strong relationship evidenced by a 0.842 linear correlation.

Unfortunately, upon closer examination, there are serious anomalies in data collection and quality control.  For instance, Infubinol’s distribution has a single low outlier: inexplicably, one of only two data points from a single mouse in a study where each mouse should have ten.  From this discovery, further investigation reveals that Ramicane and Capomulin have 22-29% more data points than the other treatment regimens except for Propriva where the deviation grows to 55%.  The origin of this discrepancy is data points per mouse: each candidate has about 25 mice for its trial, however, unlike the others who have fewer – in some cases, appreciably fewer – Ramicane’s and Capomulin’s mice overwhelmingly have the maximum number of data points, ten.  If we assume that each trial has 25 mice with ten data points, then the total should be 2,500 not 1,880: hence, the study is missing 620 data points or 24.8% of its expected total.  In addition, the original number of mice was 249, but one mouse had duplicate timepoints with incredulously different tumor volumes.

![PymaceuticalsFigure731NumberofMiceVsDrugTreatmentRegimen](https://github.com/njgeorge000158/pandas-challenges/assets/137228821/c696c1db-0cd8-430a-a5da-62b192f4b02f)

Is this situation a product of poor administration or a deliberate attempt to manipulate results in favor of certain unmerited treatments?  Ostensibly, Ramicane is the most promising drug with Capomulin a close second, and neither Ceftamin nor Infubinol have any discernable effect on decreasing tumor volume.  In truth, this study should be invalidated due to asymmetrical data collection, suspicious inconsistencies, and insufficient sample spaces.  Therefore, I recommend another study of these treatments where each mouse uniformly provides the same quantity of data points for analysis, the number of mice per trial increases, at least, by an order of magnitude, the weight of each mouse in the study is approximately the same, and clinical trial managers review data closely immediately after collection.  Once information based on a valid and accurate study is forthcoming and available to management, the company can then use drug cost to determine each treatment’s level of effectiveness per dollar spent and examine the impact of varying the dosage of Capomulin, or any other treatment for SCC, based on a subject’s weight.

----

## Copyright

N. James George © 2023. All Rights Reserved.
