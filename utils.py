import pandas as pd


def read_file(file):
    if file.type == "text/csv":
        df = pd.read_csv(file)
    else:
        # TODO: check if this function return None, if yes display message
        # st.error("Invalid file format. Please upload a CSV or Excel file.")
        return None
    return df
