
from django.contrib import admin
from django.urls import path
from category import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name="welcome"),
    path('category',views.category,name="category"),
    path('showCategory',views.showCategory,name="showCategory"),
    path('searchCategory',views.searchCategory,name="searchCategory"),
    path('editCategory/<int:id>',views.editCategory,name="editCategory"),
    path('updateCategory/<int:id>',views.updateCategory,name="updateCategory"),
    path('deleteCategory/<int:id>',views.deleteCategory,name="deleteCategory"),
    path('subcategory', views.subcategory, name="subcategory"),
    path('showSubcategory', views.showSubcategory, name="showSubcategory"),
    path('editSubcategory/<int:id>',views.editSubcategory,name="editSubcategory"),
    path('updateSubCategory/<int:id>',views.updateSubCategory,name="updateSubCategory"),
    path('deleteSubcategory/<int:id>',views.deleteSubcategory,name="deleteSubcategory"),
    path('product',views.product,name="product"),
    path('showProduct',views.showProduct,name="showProduct"),
    path('editProduct/<int:id>',views.editProduct,name="editProduct"),
    path('updateProduct/<int:id>',views.updateProduct,name="updateProduct"),
    path('deleteProduct/<int:id>',views.deleteProduct,name="deleteProduct"),
    path('searchProduct', views.searchProduct, name="searchProduct"),

]
