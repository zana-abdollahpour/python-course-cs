'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(input_list):
    return [val for val in input_list if val]


print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))
