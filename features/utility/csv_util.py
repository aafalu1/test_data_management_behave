import pandas as pd
import os


class CsvUtil:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.data_dict = {}

        # Load CSV data into the data_dict
        if os.path.isfile(csv_file_path):
            with open(csv_file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    unique_id, data = line.strip().split(',')
                    self.data_dict[unique_id] = data

    def add_data(self, unique_id, data):
        self.data_dict[unique_id] = data

        # Write the updated data to the CSV file
        with open(self.csv_file_path, 'w') as f:
            for unique_id, data in self.data_dict.items():
                f.write(f"{unique_id},{data}\n")

    def get_data(self, unique_id):
        return self.data_dict.get(unique_id, None)

    def clear_data(self):
        self.data_dict = {}

        # Clear the CSV file
        if os.path.isfile(self.csv_file_path):
            os.remove(self.csv_file_path)
