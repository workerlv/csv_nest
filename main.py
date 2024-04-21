import data_obj, utils
import streamlit as st


st.set_page_config(layout="wide")
st.set_option("deprecation.showPyplotGlobalUse", False)


def sidebar_options_one_file():
    options = ["Display raw file", "Find duplicates in column"]
    option = st.sidebar.radio("Choose CSV operation", options)

    return option


def sidebar_options_two_files():
    pass


def run_process_with_one_excel(df):
    csv_obj = data_obj.DataObj(df=df, file_count=1)

    column_name_list = csv_obj.get_df_column_name_list()
    chosen_column = st.sidebar.selectbox("Choose column", column_name_list)
    option = sidebar_options_one_file()

    filters = {
        "Display raw file": df,
        "Find duplicates in column": csv_obj.get_duplicate_values(chosen_column),
    }

    df_result = filters[option]

    st.divider()
    st.write(option)
    st.dataframe(df_result)


def run_process_with_two_excels(df1, df2):
    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(df1)

    with col2:
        st.dataframe(df2)


def main():

    st.header("CSV processing tool")

    with st.expander("Instructions"):
        st.write("* You can upload your CSV file and start exploring")
        st.write("* CSV file needs to have first row as header row!")
        st.write(
            "* On sidebar you will see 'Choose column' option - for specific tasks like 'finding duplicates' script will use this column name and search in that column "
        )

    st.sidebar.write("Choose 1 or 2 CSV files")
    two_files = st.sidebar.toggle("1 or 2 files", False)
    st.sidebar.divider()

    if not two_files:
        raw_file = st.file_uploader("Upload CSV file", type=["csv"])

        if raw_file:
            file_df = utils.read_file(raw_file)
            run_process_with_one_excel(file_df)

    else:
        st.error("Not implemented yet")
        # raw_file_1 = st.file_uploader("Upload first CSV file", type=["csv"])
        # raw_file_2 = st.file_uploader("Upload second CSV file", type=["csv"])

        # if raw_file_1 and raw_file_2:
        #     file_1_df = utils.read_file(raw_file_1)
        #     file_2_df = utils.read_file(raw_file_2)
        #     run_process_with_two_excels(file_1_df, file_2_df)


if __name__ == "__main__":
    main()
