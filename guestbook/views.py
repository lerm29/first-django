from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def guestbook(request):
    """Страница книги отзывов с формой добавления"""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш отзыв успешно отправлен! Он появится после проверки администратором.')
            return redirect('guestbook:guestbook')
    else:
        form = ReviewForm()

    # Показываем только проверенные отзывы
    reviews = Review.objects.filter(is_verified=True)

    context = {
        'form': form,
        'reviews': reviews,
        'title': 'Книга отзывов'
    }
    return render(request, 'guestbook/guestbook.html', context)
