def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    idx = 0
    if list1[idx] == 1:
        list1[idx] = True
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    
    idx += 1
    if list1[idx] == 1:
        list1[idx] = True
    
    return list1