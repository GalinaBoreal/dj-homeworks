from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calculate_dish(request, dish_name):
    if dish_name in DATA:
        data = DATA[dish_name]
        servings = request.GET.get('servings', None)

        if servings:
            result = dict()
            for key, value in data.items():
                new_value = value * int(servings)
                result[key] = round(new_value, 1)
            context = {
                'dish_name': dish_name,
                'recipe': result
            }
        else:
            context = {
                'dish_name': dish_name,
                'recipe': data
            }

    else:
        context = None

    return render(request, template_name='calculator/index.html', context=context)


def home(request):
    cook_book = list(DATA.keys())
    context = {'cook_book': cook_book}

    return render(request, template_name='calculator/home.html', context=context)
