from .models import Item,MEAL_TYPE
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Item

class MenuList(generic.ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'meals'
    paginate_by=6

    def get_queryset(self):
        queryset = super().get_queryset()
        item_name = self.request.GET.get('item_meal')

        if item_name:
            queryset = queryset.filter(Q(name__icontains=item_name))

        return queryset



class MenuItemDetail(generic.DetailView):
    model=Item
    template_name='menu_item_detail.html'