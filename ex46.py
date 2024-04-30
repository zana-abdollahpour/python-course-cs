'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(num1, num2):
    if num1 == num2:
        return "Nums are equal"
    return "First is greater" if num1 > num2 else "Second is greater"
