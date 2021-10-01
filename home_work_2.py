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
cook_book = get_data('cook_book.txt')
# pprint(get_data('cook_book.txt'))
pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingr_name = ingr['ingrediate_name']
            measure = ingr['measure']
            quantity_ = int(ingr['quantity']) * person_count
            if ingr_name in shop_list:
                shop_list[ingr_name]['quantity'] += quantity_ 
            else:
                shop_list[ingr_name] = {}
                shop_list[ingr_name]['measure'] = measure
                shop_list[ingr_name]['quantity'] = quantity_
                

                

    return shop_list


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))