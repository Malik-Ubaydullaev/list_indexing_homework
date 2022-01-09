def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    
    idx = 0
    if list1[idx] == 1:
        list1[idx] = True
    else:
        list1[idx] = False
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    else:
        list1[idx] = False
        
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    else:
        list1[idx] = False  
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    else:
        list1[idx] = False 
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    else:
        list1[idx] = False 
    
    return list1