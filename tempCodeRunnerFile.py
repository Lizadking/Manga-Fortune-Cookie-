def get_max_row_count(dataframe):
    """
    MAKE HEADER HERE 
    return: row count 
    """
    try:
        cols = list(dataframe.columns.values)
    except Exception:
        print("Error: could not get max_row_count, perhaps the dataframe does not exist")
        return 0
    else:
        max_row = dataframe[dataframe.columns[0]].count()-1
        return max_row