Feature: Read data from website and store each data into a CSV file

  @input
  Scenario Outline: User retrieves <data >from website for a unique ID <unique_id> and saves it in file <csv_file_path>
    Given the user navigates to the website and retrieves data
    And the user reads and stores test data <data> for <unique_key>
    Then the user stores date with unique key <unique_key> in file <csv_file_path>

    Examples: 
      | unique_key | data     | csv_file_path |
      | A001-2056  | Al23lu   | data.csv      |
      | A002-2045  | Bl23ol   | data.csv      |
      | A0034-2098 | Cl23alu  | data.csv      |
      | A056-2045  | Dl23alle | data.csv      |
      | A078-2088  | El23liza | data.csv      |

  @validation @csv_data
  Scenario Outline: User validates that the saved data for unique ID <unique_id> in file <csv_file_path> is correct
    Given the user checks previously stored data for unique key <unique_id> in the file <csv_file_path>

    Examples: 
      | unique_id  | csv_file_path |
      | A001-2056  | data.csv      |
      | A002-2045  | data.csv      |
      | A0034-2098 | data.csv      |
      | A056-2045  | data.csv      |
      | A078-2088  | data.csv      |
      | A078-2099  | data.csv      |
