from django.shortcuts import render

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
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
    }
}


def calculate_recipe_view(request, dish):

    if dish in DATA:
        data = DATA[dish]
        servings = request.GET.get('servings', None)

        if servings:
            result = dict()
            for key, value in data.items():
                serv = value * int(servings)
                result[key] = serv
            context = {
                'recipe_name': dish,
                'recipe': result
            }
        else:
            context = {
                'recipe_name': dish,
                'recipe': data
            }

    else:
        context = None

    return render(request, template_name='calculator/index.html', context=context)


def home_view(request):

    context = {'all_recipes': list(DATA.keys())}

    return render(request, template_name='home/home.html', context=context)