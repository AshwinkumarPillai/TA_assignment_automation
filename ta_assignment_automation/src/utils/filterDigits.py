def filter_digits(input_array: list) -> list:
    
    # TODO - CHANGE DOCUMENTATION
    
    """
    This function 

    Arguments
    ----------
    input_array: list
        the 
        
    Returned Values
    ----------
    None

    """
    filtered_array = []

    for string in input_array:
        filtered_string =  int(''.join(char for char in string if char.isdigit()))
        filtered_array.append(filtered_string)

    return filtered_array