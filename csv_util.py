import pandas as pd
import re

class CSVUtility:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)
        self.columns = self.df.columns.tolist()
        self.numeric_columns = self.df.select_dtypes(include='number').columns.tolist()

    def read_and_display(self, n=3):
        print(self.df.head(n))

    def filter_rows(self, column, operator, value):
        try:
            if pd.api.types.is_datetime64_any_dtype(self.df[column]):
                value_parsed = self.pd.to_datetime(value)
            elif pd.api.types.is_numeric_dtype(self.df[column]):
                value_parsed = float(value)
            else:
                value_parsed = value

            if operator == '>':
                return self.df[self.df[column] > value_parsed]
            elif operator == '<':
                return self.df[self.df[column] < value_parsed]
            elif operator == '==':
                return self.df[self.df[column] == value_parsed]
            elif operator == 'contains':
                return self.df[self.df[column].astype(str).str.contains(value_parsed)]
            else:
                raise ValueError("Invalid operator")
        except Exception as e:
            raise ValueError("Unable to Parse the Column")

    def sort_rows(self, column, ascending=True):
        return self.df.sort_values(by=column, ascending=ascending)

    def aggregate_column(self, column, operation):
        if operation == 'sum':
            return self.df[column].sum()
        elif operation == 'avg':
            return self.df[column].mean()
        elif operation == 'min':
            return self.df[column].min()
        elif operation == 'max':
            return self.df[column].max()
        else:
            raise ValueError("Invalid aggregation")

    def write_to_csv(self, df, output_file):
        df.to_csv(output_file, index=False)
        print(f"Data written to {output_file}")

    def count_palindromes(self, column):
        pattern = re.compile(r'^[ADBVN]+$', re.IGNORECASE)
        count = 0
        
        for val in self.df[column].dropna():
            val_str = str(val).strip().upper()
            
            if pattern.fullmatch(val_str) and val_str == val_str[::-1]:
                count += 1
        
        return count