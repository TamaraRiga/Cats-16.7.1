from cats_16_7_1 import Cat

cats = [
    {
        'name': 'Барон',
        'sex': 'мальчик',
        'age': '2 года'
    },
    {
        'name': 'Сэм',
        'sex': 'мальчик',
        'age': '2 года'
    }
]

for cat in cats:
    cat_object = Cat()
    cat_object.init_from_dict(cat)
    print('имя: ', cat_object.name)
    print('пол: ', cat_object.sex)
    print('возраст: ', cat_object.age)
    print('-------')