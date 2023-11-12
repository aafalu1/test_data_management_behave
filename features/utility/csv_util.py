import pandas as pd
import os
from typing import Mapping, Any

from file_handler import File_Handler


class KeyNotFoundError(Exception):
    pass


class CsvUtil:

    @staticmethod
    def write_to_csv(data_dict: Mapping[str, Any], csv_file_path: str, append=False):
        csv_dir = File_Handler().create_directory_on_project_root("test_data")
        file_path = os.path.join(csv_dir, csv_file_path)
        if not os.path.isfile(file_path):
            raise ValueError(f"{file_path} is not a valid file path.")
        new_df = pd.DataFrame(list(data_dict.items()),
                              columns=['Unique ID', 'Data'])

        if os.path.exists(file_path) and not append:
            # If file exists and append is False, overwrite the file with new data
            df = new_df
        else:
            df = pd.read_csv(file_path) if os.path.exists(
                csv_file_path) else pd.DataFrame(columns=['Unique ID', 'Data'])
            df = pd.concat([df, new_df], ignore_index=True, sort=False)

        df.to_csv(file_path, index=False,
                  mode='w' if not append else 'a', header=True)

    @staticmethod
    def read_from_csv(csv_file_path: str, key: str):
        file_path = File_Handler().generate_file_path(
            "test_data", file_name=csv_file_path)
        try:
            df = pd.read_csv(file_path)
            filtered_data = df[df['Unique ID']
                               == key].to_dict(orient='records')
            if not filtered_data:
                raise KeyNotFoundError(
                    f"Key '{key}' not found in the CSV file.")
            return filtered_data
        except pd.errors.EmptyDataError:
            # Handle the case where the file is empty
            return []
