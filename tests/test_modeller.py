import os
from rcci_playground.modeller.modeller import read_csv_and_append_row

def test_read_csv_and_append_row():
    # Create a temporary CSV file for testing
    csv_file = 'test.csv'
    with open(csv_file, 'w') as file:
        file.write('2022-01-01,100\n2022-01-02,200\n')

    # Define the new row to append
    new_row = ['2022-01-03', 300]

    # Call the function
    dataframe = read_csv_and_append_row(csv_file, new_row)

    # Assert that the new row is appended correctly
    expected_data = [
        ['2022-01-01', 100],
        ['2022-01-02', 200],
        ['2022-01-03', 300]
    ]
    assert dataframe.values.tolist() == expected_data

    # Clean up the temporary CSV file
    os.remove(csv_file)