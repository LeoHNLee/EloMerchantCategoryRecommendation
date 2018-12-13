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
