from code_builder.name_conventions import english_to_snake_case
from data_analytics.exploratory_data_analysis import is_numeric_data_type_column
from pandas import DataFrame
import os
import math


def build_sliders(dataframe: DataFrame) -> str:
    text: str = ""
    columns = dataframe.columns.tolist()

    string_values = ""
    for column_name in columns:
        variable_name: str = english_to_snake_case(column_name)
        string_values += f"{variable_name}, "

        if (is_numeric_data_type_column(dataframe[column_name])):
            max_value = round(dataframe[column_name].max() * 2)
            min_value = 0
            intervals = math.ceil((max_value - min_value) / 20)
            text += f"{variable_name} = streamlit.sidebar.slider('{column_name}', {min_value}, {max_value}, {intervals}){os.linesep}"
        else:
            value_list=""
            unique_values = dataframe[column_name].unique()
            for word in unique_values:
                value_list+=f'"{word}",'

            text += f"{value_list}{os.linesep}"
            text += f"{variable_name} = streamlit.sidebar.selectbox('{column_name}', {value_list}){os.linesep}"

    return text + os.linesep + string_values

