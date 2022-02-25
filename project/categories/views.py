from django.shortcuts import render
from django.views.generic import View




class CategoriesList(View):
    def get(self, request):
        return render(request, 'categories/list_categories.html')





class SubCategoriesList(View):
    def get(self, request, category):
        return render(request, 'categories/list_subcategories.html')



