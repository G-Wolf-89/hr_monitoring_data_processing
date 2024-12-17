def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    #Create new list which we will be storing our filtered data
    new_list = [] 

    for fil in data:
    # in this loop remove any spaces, if value in list isdigit, append it to new_list converted to integers
        x = fil.strip() 
        if x.isdigit(): 
            new_list.append(int(x))
    #Skip non-digit numbers 
        else:
            continue 
    
    return new_list

def filter_outliers(data: list) -> list:
    """
    Filter out all heart rate samples that are less than 30 and greater than 250.

    Args:
        data (list[str]): list of strings representing heart rate samples.
            
    Returns:
        list[int]: list of integers, with numbers greater than 30 and less than 250 removed.
    """
    #Create new list for our filtered outlier data 
    outlier_list = [] 
    
    # In a loop for the items greater than 30 and less than 250 we will append them to a new list converted to integers
    for item in data:
        if item >30  and item < 250:
             outlier_list.append(int(item)) 
    #Skip numbers do that not meet the criteria in loop 
        else:
            continue 
    
    
    return outlier_list 
 