def get_result(result_arr, categories_arr):
    index_of_result = result_arr.index(1)
    if index_of_result < len(categories_arr):
        return categories_arr[index_of_result]
    else:
        raise Exception('Index of result was higher can size of categories')


categories = {
    1: 'One',
    2: 'Two',
    3: 'Three',
}

result = [[0, 0, 0, 0, 1]]

print(get_result(result[0], categories))
