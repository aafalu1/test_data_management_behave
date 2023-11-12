Feature: Read data from website and store each data into a CSV file

  @input
  Scenario Outline: User retrieves <data >from website for a unique ID <unique_id> and saves it in file <csv_file_path>
    Given the user navigates to the website and retrieves data
    And the user reads and stores test data <data> for <unique_key>
    Then the user stores date with unique key <unique_key> in file <csv_file_path>

    Examples: 
      | unique_key | data      | csv_file_path |
      | A001-2056  |   6542347 | data.csv      |
      | A002-2066  |   6542617 | data.csv      |
      | A001-2098  |   6542332 | data.csv      |
      | A001-2045  |  65890332 | data.csv      |
      | A004-2088  | 654772132 | data.csv      |

  @validation
  Scenario Outline: User validates that the saved data for unique ID <unique_id> in file <csv_file_path> is correct
    Given the user checks previously stored data for unique key <unique_key> in the file <csv_file_path>

    Examples: 
      | unique_key | csv_file_path |
      | A001-2056  | data.csv      |
