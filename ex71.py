names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
# ['Elie Schoppik', 'Colt Steele']


def extract_full_name(inp_list):
    # names_tup = [(person["first"], person["last"]) for person in inp_list]
    # return [" ".join(person) for person in names_tup]

    # return [person["first"] + " " + person["last"] for person in inp_list]

    # return [f"{person["first"]} {person["last"]}" for person in inp_list]

    return list(map(lambda person: f"{person["first"]} {person["last"]}", inp_list))


print(extract_full_name(names))
