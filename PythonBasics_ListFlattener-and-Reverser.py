
#This code defines two functions: flatten, which recursively flattens a nested list into a single list, and reverse_lists, which recursively reverses the elements of a nested list, including the nested ones.

def flatten(input_list):
    flattened= []

    for item in input_list:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)

    return flattened

input_data = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(f'Flattened: ', flatten(input_data))


def reverse_lists(input_list):
    reversed_list = []

    for item in input_list:
        if isinstance(item, list):
            reversed_list.append(reverse_lists(item))
        else:
            reversed_list.append(item)

    return reversed_list[::-1]

input_data = [[1, 2], [3, 4], [5, 6, 7]]
print(f'Reversed: ', reverse_lists(input_data))

