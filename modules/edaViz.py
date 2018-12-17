from collections import Counter
import pandas as pd
import numpy as np
import seaborn as sns
import lightgbm as lgb
import matplotlib.pyplot as plt

def preFirstActiveMonth(df):
    '''split first active month to year and month
    x : pd.Series of which column name is 'first_active_month'
    '''
    year = df['first_active_month'].apply(lambda row : str(row)[:4])
    month = df['first_active_month'].apply(lambda row : str(row)[5:7])
    return year, month

def printInfo(name, var):
    '''print pandas df.info() with additional words
    name : DF name
    var : pandas dataframe'''
    print("{} information : ".format(name), '\n')
    var.info()
    print("\n")

def printDescribe(name, var):
    '''print pandas df.describe() with additional words
    name : DF name
    var : pandas dataframe'''
    print("{} Describe : ".format(name), '\n', var.describe(), "\n\n")

def printUniqCount(var):
    '''print pandas df.describe() with additional words
    var : pandas dataframe'''
    for i in var:
        print("{} Unique : ".format(i), '\n', var[i].unique(), "\n")
        print("{} Count : ".format(i), '\n', var[i].value_counts(dropna=False), "\n\n")

def mode(x):
    cnt = Counter(x)
    return cnt.most_common(1)[0][0]

def mergeGroupby(left, right, col, foo, rename=None, by='card_id'):
    '''merge by "card_id or etc" groupby Series to DF
    origin : train or test or sth sp
    grouped : grouped pd.Series
    foo : agg func
    by : merge base'''
    grouped = right[[by, col]].groupby([by]).aggregate(foo)
    if rename : grouped = grouped.rename(columns = {col : rename})
    ret = left.merge(right=grouped, how='left', on=by)
    return ret

def compressYear(df):
    def byRow(row):
        if row == 2018 : return 2017
        if row==2011 or row==2012 or row==2013 : return 2014
        return row
    return df['first_active_year'].apply(lambda row : byRow(row))

def compareTrainTest(col, train, test, hist=True, bins=None, figsize=(15,15)):
    fig, (axTrain, axTest) = plt.subplots(2, 1, figsize=figsize)
    axTrain = sns.distplot(train[col], color = 'blue', ax=axTrain, hist=hist, bins=bins)
    axTest = sns.distplot(test[col], color = 'red', ax=axTest, hist=hist, bins=bins)
    plt.show()

def compareMeanStd(train, test, col, form = '0.2f'):
    trainMean = train[col].mean()
    testMean = test[col].mean()
    meanDiff = (abs(trainMean-testMean)*2)/(trainMean+testMean)
    trainStd = train[col].std()
    testStd = test[col].std()
    stdDiff = (abs(trainStd-testStd)*2)/(trainStd+testStd)
    print('''{} : Train - Test Difference
    Mean : {:{form}}%
    Std : {:{form}}%'''.format(col, meanDiff, stdDiff, form=form))

def briefLgb(cols, train):
    lgbTrain = lgb.Dataset(train[cols], label=train['target'], categorical_feature = cols)
    param = {'metric':'l2_root', 'objective':'regression', 'num_thresds' : 2, 'reg_sqrt':True}
    cvResult = lgb.cv(param, lgbTrain, 5, nfold=5, stratified=False)
    return cvResult
