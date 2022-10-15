"""
provide some functions to practice pytest, covrage and pylint
"""


def mult_two(number1: int, number2: int) -> int:
    """A function calcular multiplication of 2 numbers

    Parameters
    ----------
    number1 : int
        the first number
    number2 : int
        the second number

    Returns
    -------
    int
        the result of multiplication of number1 and number2
    """
    return number1*number2


def checkio(data: list) -> list:
    """ A function remove the non-repeated elemnts in the list

    Parameters
    ----------
    data : list
        a list

    Returns
    -------
    list
        list with only repeated element
    """
    res = []
    for element in data:
        if data.count(element)>1:
            res.append(element)
    return res


def flat_list(array:list) -> list:
    """ A function flat a list of list

    Parameters
    ----------
    data : list
        a list of list

    Returns
    -------
    list
        list flated
    """
    res = []
    for i in array:
        if isinstance(i, list):
            res.extend(flat_list(i))
        else:
            res.append(i)
    return res
