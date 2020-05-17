from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductForm, RawProductForm, ProductNiceForm


# Create your views here.

def product_delete_view(request, URLid):
    obj = get_object_or_404(Product, id=URLid)
    # obj.delete()
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, URLid):  # URLid comes from urls.py
    # obj = Product.objects.get(id=URLid)
    # obj = get_object_or_404(Product, id=URLid)
    try:
        obj = Product.objects.get(id=URLid)
    except Product.DoesNotExist:
        raise Http404

    context = {
        "object": obj
    }
    return render(request, "products/product_details.html", context)


# Change a product, with initial data
def render_initial_data(request):
    initial_data = {
        'title': "A initial title!"
    }

    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# Model form
def product_create_view(request):
    form = ProductForm(request.POST or None)  # if POST comes true it renders it
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_nice_create_view(request):
    form = ProductNiceForm(request.POST or None)  # if POST comes true it renders it
    if form.is_valid():
        form.save()
        form = ProductNiceForm()

    context = {
        'form': form
    }
    return render(request, "products/product_nice_create.html", context)


# Raw form
# def product_create_view(request):
#     rawForm = RawProductForm()  # Rendering the form (aka instancing from Python)
#     if request.method == "POST":
#         rawForm = RawProductForm(request.POST)  # Rendering the post of the form
#         if rawForm.is_valid():
#             print(rawForm.cleaned_data)
#         else:
#             print(rawForm.errors)
#
#     context = {
#         "form": rawForm
#     }
#     return render(request, "products/product_create.html", context)


# Processing the requests directly w/o form
# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         titleGot = request.POST.get('title')
#         print(titleGot)
#         # Product.objects.create(title=titleGot)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_detal_view(request):
    obj = Product.objects.get(id=1)
    context = {
        # 'title': obj.title,
        # 'description': obj.description,
        'object': obj
    }
    return render(request, "products/product_details.html", context)
