# abYaml
Simplified version of the YAML context manager allowing single line read/write operations.

## read
Return a dictionary object from the given .yml file path.
## read_docs
Return a generator object that yields dictionary objects for each document in the given .yml file path.

## write
Write or overwrite a .yml file path with the contents of the given dictionary.
## write_docs
Write or overwrite a .yml file path with multiple documents in the given list.