import pandas as pd

def read_csv_and_append_row(csv_file : str, new_row : list) -> pd.DataFrame:
    data = pd.read_csv(csv_file, names=["Date", "Price"]).values.tolist()
    data.append(new_row)
    dataframe = pd.DataFrame(data, columns=['Date', 'Price'])
    return dataframe

def model(price : str, date : str) -> pd.DataFrame:
    print('modeller')
    dataframe = read_csv_and_append_row(csv_file="data.csv", new_row=[date, price])
    print(dataframe.describe())
    dataframe.to_csv(path_or_buf="data.csv", header=False, index=False)
    return dataframe
