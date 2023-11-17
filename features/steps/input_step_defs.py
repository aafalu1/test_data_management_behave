from behave import *

from features.utility.csv_util import CsvUtil, KeyNotFoundError


@given(u'the user navigates to the website and retrieves data')
def step_impl(context):
    print("Navigating to the website")


@given(u'the user reads and stores test data {data} for {unique_key}')
def step_impl(context, data, unique_key):
    context.dynamic_data = data
    context.data_storage.add_data(unique_key, context.dynamic_data)
    context.my_custom_dict = dict(
        context.data_storage.data_dict)


@then(u'the user stores date with unique key {unique_key} in file {file_name}')
def step_save_data(context, unique_key, file_name):
    pass

@given(u'the user checks previously stored data for unique key {unique_key} in the file {file_name}')
def step_impl(context, unique_key, file_name):
     filtered_data = [
        item for item in context.excel_data if item.get('Unique ID') == unique_key
    ]
     if not filtered_data:
      raise KeyNotFoundError(f"Key '{key}' not found in the Excel data.")
     return filtered_data
    p
