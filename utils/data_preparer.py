import polars as pl

import openai
import os

from utils.data_loader import data_loader

# Set up OpenAI API (ensure this is your valid API key)
openai.api_key = os.getenv("OPENAI_API_KEY")

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
        return lf.filter(pl.col(col_name).is_not_null()).select(pl.col(col_name).n_unique()).collect().item()
    
    def get_col_unique_values_lf(self, lf, column_name):
        """
        Returns the unique values of a given column in a DataFrame.

        Parameters:
        lf (DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column to get unique values from.

        Returns:
        list: A list of unique values in the specified column.
        """
        return lf.filter(pl.col(column_name).is_not_null()).select(column_name).unique().sort(by = column_name).collect().to_series().to_list()
    
    def get_unique_col_count_lf(self, lf, column_name):
        """
        Returns the count of unique values of a given column in a DataFrame.

        Parameters:
        lf (DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column to get unique values count from.

        Returns:
        list: A total count of unique values in the specified column.
        """
        return lf.filter(pl.col(column_name).is_not_null()).select(pl.col(column_name).n_unique()).collect().item()
    
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
    
    def get_llm_insight(self, plotly_fig_data):
        """
        Placeholder for LLM insight retrieval.
        """

        prompt = """
            You are an AI assistant for the OFTW (One for the World is a movement aimed at revolutionizing charitable giving to 
            eradicate extreme poverty by educating and motivating people to donate effectively.) dashboard.
            Based on the plotly figure data below, provide:  
            1. A short (1 line) summary of what the graph shows. 
            2. 2 key insights from the data. 
            3. 2 actionable suggestions for organization.  
            Plotly Figure Data: {}
            Please provide the insights in a structured format, such as:
            1. Summary: [Your summary here]
            2. Key Insights: [Your insights here]
            3. Action Suggestions: [Your suggestions here]
            Use plain language and keep it concise. 
        """.format(plotly_fig_data)

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in LLM insight retrieval: {e}")
            # Handle error (e.g., log it, raise it, etc.)
            # For now, return a placeholder
            return "LLM could not generate insight."