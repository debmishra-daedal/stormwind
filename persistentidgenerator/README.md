# Sequential ID Generator

This Python program provides a robust solution for generating sequential IDs for various entities. It supports up to a billion IDs per entity with the option to expand further. Additionally, it allows for the deletion and reuse of IDs.

## Features

1. **ID Allocation**: Allocate up to a billion IDs per entity with the option to expand.
2. **Entity Selection**: Choose from the following entities for ID generation:
   - `fx`: 1 (fx)
   - `prices`: 2 (hp)
   - `static`: 3 (sec)
   - `index`: 4 (idx)
   - `benchmarks`: 5 (bmrk)
   - `holdings`: 6 (hld)
   - `portfolio`: 7 (por)
   - `entity`: 8 (ent)
   - `other`:0 (oth)
3. **ID Deletion and Reuse**: Option to delete an ID and have it reused.

## Installation

List of dependant modules are mentioned below.

- `DateTime` = "^5.5"

  Ensure that you have SLITE_DB_PATH environment variable set. If not it'll store in profile and wont be persistent
  if you have concurrent users.

## Usage

It has a class and multiple methods

1.  **Classes**

    - `guidgen` : All methods of the program are written here

2.  **Methods**

    - `create_database()` : Creates the sqlite database for persistent storage
    - `table_exists()` : Checks if the table exists
    - `create_table()` : Creates new table, if table doesn't exist in database

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact infra@daedal.codes.
