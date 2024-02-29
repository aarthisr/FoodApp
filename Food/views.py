from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from django.template import loader
from .forms import Item_Form
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required


# Create your views here.
# def index(request):
    # items=Item.objects.all()
    # template=loader.get_template('Food/index.html')
    # context={
        # 'item_list': items,
    # }
    # return render(request, 'Food/index.html', context)


class IndexItemList(ListView):
    model=Item;
    template_name="Food/index.html"
    context_object_name="item_list"


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


# def detail(request, item_id):
#     item=Item.objects.get(id=item_id)
#     context={
#         'item': item,
#     }
#     return render(request, 'Food/detail.html', context)


class FoodDetail(DetailView):
    model=Item;
    template_name="Food/detail.html"


# def create_item(request):
#     form = Item_Form(request.POST or None)
#     context={
#         'form': form,
#     }
#     if form.is_valid():
#         form.save()
#         return redirect("Food:index")
#     return render(request, 'Food/item-form.html', context)


class FoodCreate(CreateView):
    model=Item;
    fields=['item_name', 'item_desc', 'item_price', 'item_image']
    template_name="Food/item-form.html"
    def form_valid(self, form):
        form.instance.usr_name=self.request.user
        return super().form_valid(form)


def update_item(request, item_id):
    item=Item.objects.get(id=item_id)
    form = Item_Form(request.POST or None, instance=item)
    context={
        'form': form,
        'item': item
    }
    if form.is_valid():
        form.save()
        return redirect("Food:index")
    return render(request, 'Food/item-form.html', context)


def delete_item(request, item_id):
    item=Item.objects.get(id=item_id)
    context={
        'item': item
    }
    if request.method=='POST':
        if 'Confirm' in request.POST:
            item.delete()
        return redirect("Food:index")
    return render(request, 'Food/item-delete.html', context)
