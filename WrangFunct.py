def meanMonths(df, metric):
    import pandas as pd
    cols = df.columns
    years = ['2010', '2011', '2012', '2013', '2014', 
             '2015', '2016', '2017', '2018', '2019']
    meanPerYear = {}
    
    for year in years:
        colName = (f"{metric}{year}")
        
        condYr = df.columns.str.contains(year)
        regionMeans = df[cols[condYear]].mean(axis=1)
        meanPerYear.update({colName: regionMeans})
    
    return pd.DataFrame(meanPerYear)

def getSevTN(df):
    import pandas as pd
    condition = df['RegionName'] == ('Sevierville, TN')
    return df[condition]