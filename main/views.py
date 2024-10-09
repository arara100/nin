from django.shortcuts import render, redirect, get_object_or_404


games_list = [
    {
        'id': 1,
        'name': 'Гра 1',
        'price': 1500,
        'description': 'rghjrf jfhjgfhk ghfgifhi',
        'img': 'deps/img/prev_1.jpg'
    },
    {
        'id': 2,
        'name': 'Гра 2',
        'price': 1800,
        'description': 'Велика пригодницька гра з відкритим світом.',
        'img': 'deps/img/prev_2.jpg'
    },
    {
        'id': 3,
        'name': 'Гра 3',
        'price': 2000,
        'description': 'Стратегія в реальному часі з складними механіками.',
        'img': 'deps/img/prev_3.jpg'
    },
    {
        'id': 4,
        'name': 'Гра 4',
        'price': 2500,
        'description': 'Шутер з елементами рольової гри та захоплюючим сюжетом.',
        'img': 'deps/img/prev_4.jpg'
    },
    {
        'id': 5,
        'name': 'Гра 5',
        'price': 1700,
        'description': 'Гра на виживання з акцентом на будівництво та крафт.',
        'img': 'deps/img/prev_5.jpg'
    }
]


def index(request):
    context = {
        'games': games_list
    }
    return render(request, 'templates/index.html', context)


def add_to_cart(request, game_id):
    game = next((game for game in games_list if game['id'] == game_id), None)

    if game is None:
        return redirect('main:index')

    cart = request.session.get('cart', {})

    if str(game['id']) not in cart:
        cart[str(game['id'])] = {
            'name': game['name'],
            'price': game['price'],
            'quantity': 1,
            'img': game['img']
        }
    else:
        cart[str(game['id'])]['quantity'] += 1

    request.session['cart'] = cart
    return redirect('main:index')


def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'templates/cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, game_id):
    cart = request.session.get('cart', {})

    if str(game_id) in cart:
        del cart[str(game_id)]

    request.session['cart'] = cart
    return redirect('main:cart')

