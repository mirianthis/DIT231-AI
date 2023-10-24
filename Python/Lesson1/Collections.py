a_tuple = (1, 2, 4)
a_tuple[0] = 3

a_set = {5, 3, 2, 5}
for i in a_set:
    print(i)

a_set.add(6)
a_set.remove(6)
a_set

a_dict = {}
a_dict[5] = 12
a_dict["key_2"] = 27
a_dict["key_3"] = [13, "value"]
a_dict[5] = "new value"
a_dict["key_2"] = 28
a_dict

a_dict_copy = {5: 'new value', 'key_2': 28, 'key_3': [13, 'value']}