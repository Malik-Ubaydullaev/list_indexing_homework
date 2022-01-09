def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    idx = 0
    if list1[idx] == 0:
        list1[idx] = False
    
    idx += 1
    if list1[idx] == 0:
        list1[idx] = False
    
    idx += 1
    if list1[idx] == 0:
        list1[idx] = False
    
    idx += 1
    if list1[idx] == 0:
        list1[idx] = False
    
    idx += 1
    if list1[idx] == 0:
        list1[idx] = False
    
    return list1