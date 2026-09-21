# Kipsang's Solution

def oddities(the_list):
    list_with_nones = [
        val if idx % 2 == 0 else None for idx, val in enumerate(the_list)
    ]

    final_list = []
    for item in list_with_nones:
        if item is not None:
            final_list.append(item)

    return final_list


# These examples should all print True
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities([1, 2, 3, 4]) == [1, 3])
print(oddities(["abc", "def"]) == ['abc'])
print(oddities([123]) == [123])
print(oddities([]) == [])