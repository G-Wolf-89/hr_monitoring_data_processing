def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    
    new_list = []

    for fil in data:
        x=fil.strip()
    
        if x.isdigit():
            new_list.append(int(x))

        else:
            continue
    return new_list

def filter_outliers(data: list) -> list:
    
    outlier_list = []

    for item in data:
        if item >30  and item < 250:
             outlier_list.append(int(item))
        else:
            continue
    return outlier_list
