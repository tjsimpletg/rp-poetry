 
def mult_two(a: int, b: int) -> int:
    
    return a*b 


def checkio(data: list) -> list:
    res = []
    for e in data:
        if data.count(e)>1:
            res.append(e)
    return res


def flat_list(array:list) -> list:
    res = []
    for i in array:
        if isinstance(i, list):
            res.extend(flat_list(i))
        else:
            res.append(i)
    return res

