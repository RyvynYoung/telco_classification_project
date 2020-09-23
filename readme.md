# Telco Churn Classification Project
Ryvyn Young 09/23/2020

# Instructions for Replication

# Key Findings
Exploritory analysis has not yet revealed any clear drivers or answers at this time.
However, a random forest model using all available variables does produce a predictive model that is more effective than the baseline accuracy and does not appear to be overfit to the data.
While the logistic regression model was the poorest performing model, dropping the least impactful coefficients may provide further improvement.
###### Next Steps    
Continue exploration, in particular a deeper dive into Fiber Optic as well as partners and dependents   
Test a models with reduced features, particularly eliminating total charges and years tenure  

# Data Dictionary
| Field Name |	Data in field |	Data Type |
------------------------------------------
payment_type_id	| numeric, method of payment, 1=Electronic Check, 2=Mailed Check, 3=Bank Transfer, 4=Credit Card |	category

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
DELIVERABLES: .py file for data acquisition and notes for replicating results (note access to Codeup SQL data files is required)

## Preparation Stage
DELIVERABLES: .py file for data preparation and notes for replication

## Exploration and Pre-Processing Stage
DELIVERABLES: You are required to run at least 2 statistical tests in your data exploration. Document your hypotheses and set your alpha before running the tests and document your findings well. Summarize your conclusions, provide clear answers to the specific questions, and summarize any takeaways/action plan.

## Modeling Stage
DELIVERABLES: You are required to establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.

## Delivery Stage
DELIVERABLES: Summarize your findings. Key takeaways and next steps should be documented here.
Nice to have - impact of recommended next steps

Refine:
Remove unnecessary columns, charts, etc.

Present:




# Key Findings and Takeaways