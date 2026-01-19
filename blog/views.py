from django.shortcuts import render

# Статические данные для демонстрации
POSTS = [
    {
        'id': 1,
        'title': 'Первый пост',
        'content': 'Это содержимое первого поста в нашем блоге. Здесь может быть любой текст.',
        'author': 'Админ',
        'date': '18 января 2026'
    },
    {
        'id': 2,
        'title': 'Второй пост',
        'content': 'Это содержимое второго поста. Django - отличный фреймворк для веб-разработки.',
        'author': 'Админ',
        'date': '17 января 2026'
    },
    {
        'id': 3,
        'title': 'Третий пост',
        'content': 'Ещё один пост для нашего блога. Практикуемся в создании веб-приложений.',
        'author': 'Админ',
        'date': '16 января 2026'
    },
]


def index(request):
    """Главная страница блога"""
    context = {
        'posts': POSTS,
        'title': 'Главная'
    }
    return render(request, 'blog/index.html', context)


def about(request):
    """Страница о блоге"""
    context = {
        'title': 'О блоге'
    }
    return render(request, 'blog/about.html', context)


def post_detail(request, post_id):
    """Страница отдельного поста"""
    post = None
    for p in POSTS:
        if p['id'] == post_id:
            post = p
            break

    context = {
        'post': post,
        'title': post['title'] if post else 'Пост не найден'
    }
    return render(request, 'blog/post_detail.html', context)
