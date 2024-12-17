def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window size
    """
    #Create list where we will store our maximums from each window size
    maximums = [] 
    # In this for loop we will pull the maxiums out of the data and append it to our maximums list 
    for i in range(0,len(data),n): 
       maximum = data[i:i + n ]
       maximums.append(max(maximum))
    return maximums

def window_average(data: list, n: int) -> list:
    """
    Calculate the average of every "n"-size window 

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of averages from each window size
    """
    #Create list where we will store our window averages
    result = []
    #In this loop calulate the averages within the data list and window size
    for i in range(0,len(data), n):
        window = data[i:i + n]
        window_average = sum(window) /len(window)
    #once we have the averages appened them to this result list rounded 2 places
        result.append(round(window_average,2)) 
    
    
    return result


def window_stddev(data: list, n: int) -> list:
    """
    Calculate the Standard Deviation value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of standard deviations for each window size  
    """
    #Create list where we will store our standard deviations 
    result = []

    #In the loop calculate the standrd deviations for the data given in list and data size
    for i in range(0,len(data), n): 
        
        window = data[i:i+n] 
    #if the length of the variable window is equal to 1 then skip 
        if len(window) == 1: 
                continue 
    #Calculate the standard deviation
        window_average = sum(window) / len(window) 
    
        variance = sum((i- window_average)** 2 for i in window) / (len(window) -1)
     #get the standard deviation and append results rounded 2 places to the result list 
        std_dev = variance ** 0.5 
        result.append(round(std_dev,2))
   
   
    return result