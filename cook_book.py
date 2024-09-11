from pprint import pprint


with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        name_dish = line.strip()
        number_ingredients = int(f.readline())
        products = []
        for i in range(number_ingredients):
            product = f.readline().strip()
            ingredient_name, quantity, measure = product.split(' | ')
            products.append({'ingredient_name': ingredient_name,
                             'quantity': int(quantity),
                             'measure': measure})
        f.readline()
        cook_book[name_dish] = products
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                m_q_list = {}
                if ingredient['ingredient_name'] not in shop_list:
                    m_q_list['measure'] = ingredient['measure']
                    m_q_list['quantity'] = ingredient['quantity'] * person_count
                    shop_list[ingredient['ingredient_name']] = m_q_list
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] = (
                            shop_list)[ingredient['ingredient_name']]['quantity'] + \
                            ingredient['quantity'] * person_count
        else:
            print (f'Такого блюда нет в списке!')
    return shop_list
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))