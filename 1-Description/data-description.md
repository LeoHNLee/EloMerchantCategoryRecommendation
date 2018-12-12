## 1. Data

### 1.1 field explanation

- *train.csv*/*test.csv* : ***card id***, ***target***(train only)
- transactions : desinged to be joined with *train.csv*, *test.csv*, and *merchants.csv*
  - *historical transaction.csv* : 3 months' worth of transaction for every card at any of the provided ***marchant id***
  - *new merchant transaction.csv* : (new : ***merchant id*** that this particular ***car id*** has not yet visited) over a 2 months
- *merchants.csv* : aggregate information ***merchant id*** represented in the data set
- *sample submission.csv* : contains all ***card id***s you are expected to predict for

### 1.2 what am I predicting?

- predicting a loyalty score for each ***card id*** in *test.csv* and *sample submission.csv*

## [2. Data Field Descriptions](./Data_Dictionary.xlsx)
