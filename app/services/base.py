import pandas as pd


class BaseService:
    def file_extension(self, extension: str):
        if extension != "csv":
            raise ValueError("Invalid file extension. Only CSV files are allowed.")

    def validate_data(self, reader: pd.io.parsers.readers.TextFileReader, n_cols: int):
        """Validate if the data has the correct number of columns.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be validated.

        Raises:
            ValueError: If the number of columns is different from n_cols.
        """
        try:
            # Get a sample chunk to check the number of columns
            sample_chunk = next(reader)
            if len_columns := len(sample_chunk.columns) != n_cols:
                raise ValueError(
                    f"Invalid number of columns. Expected {n_cols} columns, got {len_columns}."
                )
        except StopIteration:
            # If the reader is empty, raise an error
            raise ValueError("The input file is empty.")
