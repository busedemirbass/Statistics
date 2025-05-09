def shifted(data):
    if not data:
        return false
    length = len(data)
    mean = sum(data) / length
    if length %2 == 0:
        median = data[((length/2))+data((length/2)-1)]/2
    else:
        median = data[((length+1)/2)-1]
    result = abs(int(((mean - median)/mean)*100)) 
    return result
