from collections import Counter
import pandas as pd
import numpy as np
import seaborn as sns
import lightgbm as lgb
import matplotlib.pyplot as plt

def printUniqCount(df):
    '''print pandas df.describe() with additional words
    df : pandas dataframe'''
    for col in df.columns:
        print("{} Unique : ".format(i), '\n', df[col].unique(), "\n")
        print("{} Count : ".format(i), '\n', df[col].value_counts(dropna=False), "\n\n")

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

def compareTrainTest(cols, train, test, bins=100, hist=True, figsize=(20,5)):
    length = len(cols)
    width, height = figsize
    fig = plt.figure(figsize=(width, length*height))
    for idx, col in enumerate(cols):
        locals()[col+'TrainAx'] = fig.add_subplot(length, 2,idx*2+1)
        sns.distplot(train[col], color = 'blue', hist=hist, bins=bins, ax=locals()[col+'TrainAx'])
        locals()[col+'TestAx'] = fig.add_subplot(length, 2,(idx+1)*2)
        sns.distplot(test[col], color = 'red', hist=hist, bins=bins, ax=locals()[col+'TestAx'])
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

def idxKeyErrHandler(x, foo, ext=None):
    try : return foo(x)
    except IndexError : return ext
    except KeyError : return ext
