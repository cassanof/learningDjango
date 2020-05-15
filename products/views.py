from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.

# Raw form
def product_create_view(request):
    rawForm = RawProductForm()  # Rendering the form (aka instancing from Python)
    if request.method == "POST":
        rawForm = RawProductForm(request.POST)  # Rendering the post of the form
        if rawForm.is_valid():
            print(rawForm.cleaned_data)
        else:
            print(rawForm.errors)

    context = {
        "form": rawForm
    }
    return render(request, "products/product_create.html", context)


# Processing the requests directly
# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         titleGot = request.POST.get('title')
#         print(titleGot)
#         # Product.objects.create(title=titleGot)
#     context = {}
#     return render(request, "products/product_create.html", context)

# Model form
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


def product_detal_view(request):
    obj = Product.objects.get(id=1)
    context = {
        # 'title': obj.title,
        # 'description': obj.description,
        'object': obj
    }
    return render(request, "products/product_details.html", context)
