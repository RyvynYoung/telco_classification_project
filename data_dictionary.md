| Field Name               | Data in field                                                                                                         | Data Type |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|
| payment_type_id          | numeric, method of payment, 1=Electronic Check, 2=Mailed Check, 3=Bank Transfer, 4=Credit Card                        | category  |
| internet_service_type_id | numeric, type of internet service, 1=DSL, 2=Fiber Optic, 3=None                                                       | category  |
| contract_type_id         | numeric ID for type of contract,1 = month-to-month, 2 = annual, 3 = two-year                                          | category  |
| customer_id              | Unique identifier retained for use in churn predictiions file (pred_churn.csv)                                        | object    |
| senior_citizen           | encoded as 1=Senior, 0=non-senior                                                                                     | int64     |
| months_tenure            | Number of months customer has been active; remains static once customer has churned                                   | int64     |
| monthly_charges          | Current monthly charges for customer                                                                                  | float64   |
| total_charges            | Total charges for customer                                                                                            | float64   |
| churn                    | encoded as 1=has churned, 0=stayed                                                                                    | unit8     |
| mult_lines               | encoded as 1=has mulitple lines, 0=does not have multiple lines, additional service                                   | unit8     |
| online_sec               | encoded as 1=has online security, 0=does not have online security, additional service                                 | unit8     |
| online_backup            | encoded as 1=has online backup, 0=does not have online backup, additional service                                     | unit8     |
| device_protection        | encoded as 1=has device protection, 0=does not have device protection, additional service                             | unit8     |
| paperless                | encoded as 1=received paperless billing, 0=does receive paperless billing, additional service                         | unit8     |
| stream_movies            | encoded as 1=is registered for streaming movies, 0=is not registered for streaming movies, additional service         | unit8     |
| stream_tv                | encoded as 1=is registered for streaming television, 0=is not registered for streaming television, additional service | unit8     |
| tech                     | encoded as 1=is registered for tech support, 0=is not registered for tech support, additional service                 | unit8     |
| phone                    | encoded as 1=has phone service, 0=does not have phone service                                                         | unit8     |
| dependents               | encoded as 1=has dependents, 0=does not have dependents                                                               | unit8     |
| partner                  | encoded as 1=has partner, 0=does not have partner                                                                     | unit8     |
| Male                     | encoded as 1 if Male or 0 if female                                                                                   | unit8     |
| extra_serv               | numeric, sum of additional services customer has                                                                      | unit8     |