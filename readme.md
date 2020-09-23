# Telco Churn Classification Project
Ryvyn Young 09/23/2020

# Instructions for Replication
Files are located in Git Repo [here](https://github.com/RyvynYoung/telco_classification_project)
User will need env.py file with access to Codeup database
acquire.py and prepare.py files need to be run in order they occur in notebook 

# Key Findings
Exploritory analysis has not yet revealed any clear drivers or answers at this time.
However, a random forest model using all available variables does produce a predictive model that is more effective than the baseline accuracy and does not appear to be overfit to the data.
While the logistic regression model was the poorest performing model, dropping the least impactful coefficients may provide further improvement.
###### Next Steps    
Continue exploration, in particular a deeper dive into Fiber Optic as well as partners and dependents   
Test a models with reduced features, particularly eliminating total charges and years tenure  

# Data Dictionary
https://github.com/RyvynYoung/telco_classification_project/blob/master/data_dictionary.md

## Planning Stage
Project Description: Why are our customers churning?

GOALS:
Find drivers for customer churn.
Construct a ML classification model that accurately predicts customer churn.
Create modules that make your process repeateable.
Document your process well enough to be presented or read like a report.

MVP Questions to answer
Are there clear groupings where a customer is more likely to churn?
Are there features that indicate a higher propensity to churn?
Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point?

Audience: Codeup Data Science Team
Setting: Virtual 5 minute walk through of Documented Jupyter Notebook
Brainstorm: key highlights, key visualizations, prototype

## Acquire Stage
DELIVERABLES: acquire.py file for data acquisition and notes for replicating results (note access to Codeup SQL data files is required)

## Preparation Stage
DELIVERABLES: prepare.py file for data preparation and notes for replication

## Exploration and Pre-Processing Stage
DELIVERABLES: You are required to run at least 2 statistical tests in your data exploration. 

## Modeling Stage
DELIVERABLES: You are required to establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models.

## Delivery Stage
DELIVERABLES: Summarize your findings. Key takeaways and next steps should be documented here.
