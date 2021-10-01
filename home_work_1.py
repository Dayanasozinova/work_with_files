from pprint import pprint
def get_data(file_name):
    data = dict()
    with open(file_name) as file:
        for line in file:
            cook_name = line.strip()
            counter = int(file.readline())

            temp_list = []

            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                temp_list.append(
                    {'ingrediate_name': ingredient_name.strip(), 'quantity' : quantity.strip(), 'measure' : measure.strip()}
                )
                data[cook_name] = temp_list

             
            file.readline() 
    return data

# pprint(get_data('cook_book.txt'))
pprint(get_data('cook_book.txt'), sort_dicts=False)