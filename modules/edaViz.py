from collections import Counter

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
        print("{} Count : ".format(i), '\n', var[i].value_counts(), "\n\n")

def mode(x):
    cnt = Counter(x)
    return cnt.most_common(1)[0][0]

def mergeGroupby(origin, grouped, foo, by='card_id'):
    '''merge by "card_id or etc" groupby Series to DF
    origin : train or test or sth sp
    grouped : grouped pd.Series
    foo : agg func
    by : merge base'''
    prepared = grouped.aggregate(foo)
    def keyErrorHandler(x):
        try:
            return prepared[x]
        except KeyError:
            return None
    ret = origin[by].apply(lambda row : keyErrorHandler(row))
    return ret

def compressYear(df):
    def byRow(row):
        if row == 2018 : return 2017
        if row==2011 or row==2012 or row==2013 : return 2014
        return row
    return df['first_active_year'].apply(lambda row : byRow(row))
