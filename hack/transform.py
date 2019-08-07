import pandas
from sklearn.preprocessing import LabelEncoder

def removeDays(dataframe):
  dataframe = dataframe[dataframe['DIAS'] != 0]
  return dataframe


def encodeLabels(dataframe, columnName):
  label_encoder = LabelEncoder()
  label_encoder.fit(dataframe[columnName])
  dataframe[columnName] = label_encoder.transform(dataframe[columnName])

  
def categorizeByDays(df):
    bins = [0, 4, 8, 999]
    labels = [4, 8, 999]
    df['DIAS_GROUP'] = pandas.cut(df['DIAS'], bins=bins, labels=labels, include_lowest=True)
    return df


def transformIt(df):
    df = removeDays(df)
    
    for colName in df.columns.tolist():
      if colName not in ['DIAS', 'SUBREGIAO', 'SETOR']:
        encodeLabels(df, colName)

    df = categorizeByDays(df)

    return df
