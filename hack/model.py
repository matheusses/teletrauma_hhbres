from sklearn.externals import joblib


def predict(df):
    loaded_model = joblib.load('./teletrauma-lr-v1.pkcls')
    x_test_final = df.iloc[:,0:13].values
    y_test_final = df.iloc[:,14].values

    result = loaded_model.predict(x_test_final)
    return result
