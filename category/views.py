from django.shortcuts import render,redirect
from .models import  *
from django.http import HttpResponse
from django.contrib import messages

def welcome(request):
    return render(request, 'welcome.html')

def category(request):
    if request.method == 'POST':
        name = request.POST['name']

        if Category.objects.filter(name=name).exists():
            messages.error(request, "Category already exist")

        else:
            Category(name=name)
            #return HttpResponse("Category Added")
            return redirect('showCategory')
    return render(request,'category.html')


def showCategory(request):
    category = Category.objects.all
    return render(request, 'show.html',{'category':category})

def searchCategory(request):
    name = request.POST['name']
    category = Category.objects.filter(name__contains=name)

    return render(request, 'show.html', {'category': category})

def editCategory(request,id):
    category = Category.objects.get(id=id)
    return render(request, 'edit.html', {'category': category})

def updateCategory(request, id):
    if request.method == 'POST':
        name = request.POST['name']

        if Category.objects.filter(name=name).exists():
            messages.error(request, "Category already exist")
            #return HttpResponse("Duplicate Category")
            return redirect('showCategory')

        else:
            Category.objects.filter(id=id).update(name=name)
            # return HttpResponse("Category Added")
            return redirect('showCategory')

def deleteCategory(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/showCategory')


def subcategory(request):
    category = Category.objects.all
    if request.method == 'POST':
        name = request.POST['name']
        cate_id = request.POST['cate_id']

        if Subcategory.objects.filter(name=name).exists():
            messages.error(request, "SubCategory already exist")

        else:
            query = Subcategory(name=name)
            query.category_id = cate_id
            query.save()
            #return HttpResponse("SubCategory Added")
            return redirect('showSubcategory')

    return render(request, 'subcategory.html',{'category':category})

def showSubcategory(request):
    subcate = Subcategory.objects.all
    return render(request, 'showsubcategory.html',{'subcate':subcate})

def editSubcategory(request,id):
    cate = Category.objects.all
    subcate = Subcategory.objects.get(id=id)
    return render(request, 'subedit.html', {'subcate': subcate,'cate':cate})

def updateSubCategory(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        cate_id = request.POST['cate_id']

        if Subcategory.objects.filter(name=name).exists():
            messages.error(request, "subcategory already exist")
            #return HttpResponse("Duplicate Category")
            return redirect('showSubcategory')

        else:
            Subcategory.objects.filter(id=id).update(name=name,category=cate_id)
            return redirect('showSubcategory')

def deleteSubcategory(request, id):
    subcategory = Subcategory.objects.get(id=id)
    subcategory.delete()
    return redirect('/showSubcategory')

def product(request):
    cate = Category.objects.all
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        cate_id = request.POST['cate_id']

        if Subcategory.objects.filter(name=name).exists():
            messages.error(request, "Product already exist")

        else:
            query = Product(name=name,price=price)
            query.cate_id_id = cate_id
            query.save()
            #return HttpResponse("SubCategory Added")
            return redirect('showProduct')

    return render(request, 'product.html',{'cate':cate})

def showProduct(request):
    product = Product.objects.all
    return render(request, 'showproduct.html',{'product':product})

def editProduct(request,id):
    product = Product.objects.get(id=id)
    cate = Category.objects.all
    return render(request, 'productedit.html', {'product': product,'cate':cate})

def updateProduct(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        cate_id = request.POST['cate_id']

        if Product.objects.filter(name=name).exists():
            messages.error(request, "Product already exist")
            #return HttpResponse("Duplicate Category")
            return redirect('showProduct')

        else:
            Product.objects.filter(id=id).update(name=name,price=price,cate_id=cate_id)
            return redirect('showProduct')

def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/showProduct')


def searchProduct(request):
    name = request.POST['name']
    product = Product.objects.filter(name__contains=name)
    return render(request, 'showProduct.html', {'product': product})








