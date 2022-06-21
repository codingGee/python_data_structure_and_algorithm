def oddNumbers(l, r):
    if l % 2 == 1: 
        return list(range(l,     r + 1, 2))
    else: 
        return list(range(l + 1, r + 1, 2))
    
    
    # or 
def oddNumbers(l, r):
    return list(range(l if l % 2 else l + 1, r + 1, 2))   
