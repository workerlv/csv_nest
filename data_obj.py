from dataclasses import dataclass
import pandas as pd


@dataclass
class DataObj:
    df: pd.DataFrame
    file_count: int

    def get_df(self):
        return self.df

    def get_file_count(self):
        return self.file_count

    def get_duplicate_values(self, column_name):
        return self.df[self.df.duplicated(subset=[column_name], keep=False)]

    def get_df_column_name_list(self):
        return self.df.columns.tolist()
