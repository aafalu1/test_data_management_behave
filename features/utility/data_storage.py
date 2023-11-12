# datastorage.py

import pandas as pd
class DataStorage:
    def __init__(self):
        self.data_dict = {}

    def add_data(self, unique_id, data):
        self.data_dict[unique_id] = data

    def create_dataframe(self):
        return pd.DataFrame(list(self.data_dict.items()), columns=['Unique ID', 'Data'])

    def clear_data(self):
        self.data_dict = {}

   
