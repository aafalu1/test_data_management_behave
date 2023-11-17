import pandas as pd
import os
from typing import Mapping, Any

from file_handler import File_Handler


class KeyNotFoundError(Exception):
    pass


class CsvUtil:

    def __init__(self, csv_file_name):
        self.file_name = self._set_file_name(csv_file_name)

    def write_to_csv(self, data_dict: Mapping[str, Any], append=False):
        new_df = pd.DataFrame(list(data_dict.items()),
                              columns=['Unique ID', 'Data'])

        if os.path.exists(self.file_name) and not append:
            # If file exists and append is False, overwrite the file with new data
            df = new_df
        else:
            df = pd.read_csv(self.file_name) if os.path.exists(
                self.csv_file_path) else pd.DataFrame(columns=['Unique ID', 'Data'])
            df = pd.concat([df, new_df], ignore_index=True, sort=False)

        df.to_csv(self.file_name, index=False,
                  mode='w' if not append else 'a', header=True)

    def read_csv_to_dataframe(self):
        try:
            df = pd.read_csv(self.file_name)
            return df
        except pd.errors.EmptyDataError:
            # Handle the case where the file is empty
            return pd.DataFrame(columns=['Unique ID', 'Data'])

    def get_data_by_key(self, key: str):
        df = self.read_csv_to_dataframe()
        filtered_data = df[df['Unique ID'] == key].to_dict(orient='records')
        if not filtered_data:
            raise KeyNotFoundError(f"Key '{key}' not found in the {
                                   self.file_name} file.")
        return filtered_data

    def _set_file_name(self, csv_file_name):
        csv_dir = File_Handler().create_directory_on_project_root("test_data")
        file_path = os.path.join(csv_dir, csv_file_name)
        if not os.path.isfile(file_path):
            raise ValueError(f"{file_path} is not a valid file path.")
        return file_path
