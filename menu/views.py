from django.shortcuts import render
from .models import Category


def menu_view(request):
    categories = Category.objects.prefetch_related('dishes').filter(dishes__is_active=True).distinct()
    return render(request, 'menu/menu.html', {'categories': categories})