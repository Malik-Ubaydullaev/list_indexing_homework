def is_same(list1):
    if len(list1) == 1 and len(list1) == 0:
        return True
    elif len(list1) == 5 and list1[0] == list1[1] and list1[0] == list1[2] and list1[0] == list1[3] and list1[0] == list1[4]:
        return True
    
    elif len(list1) == 4 and list1[0] == list1[1] and list1[0] == list1[2] and list1[0] == list1[3]:
        return True
    
    elif len(list1) == 3 and list1[0] == list1[1] and list1[0] == list1[2]:
        return True
    
    elif len(list1) == 2 and list1[0] == list1[1]:
        return True
    else:
        return False
    
    
def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    return is_same(list1)