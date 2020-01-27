
idSevierville = 395086

def MetricMeans(df, metric):
    import pandas as pd
    import numpy as np
    cols = df.columns
    years = ['1996', '1997', '1998', '1999', '2000',
             '2001', '2002', '2003', '2004', '2005',
             '2006', '2007', '2008', '2009',
             '2010', '2011', '2012', '2013', '2014', 
             '2015', '2016', '2017', '2018', '2019']
    meanPerYear = {}
    
    for year in years:
        
        dfLen = len(df['RegionName'])
        colName = (f"{metric}_{year[2:4]}")
        condYr = df.columns.str.contains(year)
        
        if condYr.sum() == 0:
            continue
            #nanCol = [np.nan] * dfLen
            #meanPerYear.update({colName: nanCol})
        if condYr.sum() > 0:
            regionMeans = df[cols[condYr]].mean(axis=1)
            meanPerYear.update({colName: regionMeans})
    
    metric_per_year = pd.DataFrame(meanPerYear)
    
    #startingCols = df['RegionName', 'SizeRank']
    #MetricDF = pd.concat(startingCols, metric_perYear)
    #return MetricDF
    
    
    return metric_per_year
        
    
def getSevTN(df):
    import pandas as pd
    condition = df['RegionName'] == ('Sevierville, TN')
    return df[condition]
