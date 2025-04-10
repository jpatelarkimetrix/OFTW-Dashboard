import polars as pl

from utils.data_loader import data_loader

class DataPreparer:
    def __init__(self):
        pass

    def get_col_unique_values(self, dataset_name, col_name, sort_desc = False):
        """
        Retrieves the unique list of column from the dataset.
        """
        lf = data_loader.get_data(dataset_name)
        return lf.filter(pl.col(col_name).is_not_null()).select(col_name).unique().sort(by = col_name, descending = sort_desc).collect().to_series().to_list()
    
    def get_unique_col_count(self, dataset_name, col_name):
        """
        Retrieves the count of unique values in the column.
        """
        lf = data_loader.get_data(dataset_name)
        return lf.select(pl.col(col_name).n_unique()).collect().item()
    
    def filter_data(self, dataset_name, filters = None, columns = None, logic = "AND"):
        """
        Generic method to filter and select columns from a dataset.

        Parameters:
        - dataset_name (str): Dataset to query.
        - filters (list of tuples): [(canonical_name, operator, value)], e.g., [("center_id", "==", 123)].
        - columns (list of str): Canonical column names to return.
        - logic (str): "AND" (default) or "OR" for combining filters.

        Returns:
        - LazyFrame: Filtered and projected dataset.
        """
        lf = data_loader.get_data(dataset_name)

        # Apply filters if provided
        if filters:
            expressions = [self._build_filter_expr(dataset_name, f) for f in filters]
            # print(expressions)
            # combined_filter = pl.all(expressions) if logic == "AND" else pl.any(expressions)
            # print(combined_filter)
            lf = lf.filter(expressions)

        # Select required columns
        if columns:
            lf = lf.select(columns)

        return lf

    def _build_filter_expr(self, dataset_name, filter_tuple):
        """
        Helper to convert (canonical_name, operator, value) to a Polars expression.
        """
        col_name, operator, value = filter_tuple

        # Handle None values
        if operator in ["not_null", "null"]:
            if operator == "not_null":
                return pl.col(col_name).is_not_null()
            elif operator == "null":
                return pl.col(col_name).is_null()
        
        ops = {
            "==": pl.col(col_name) == value,
            "!=": pl.col(col_name) != value,
            ">": pl.col(col_name) > value,
            ">=": pl.col(col_name) >= value,
            "<": pl.col(col_name) < value,
            "<=": pl.col(col_name) <= value,
            "in": pl.col(col_name).is_in(value) if isinstance(value, list) else pl.col(col_name) == value,
            "not_in": ~pl.col(col_name).is_in(value) if isinstance(value, list) else pl.col(col_name) != value,
        }

        if operator not in ops:
            raise ValueError(f"Unsupported operator: {operator}")

        return ops[operator]