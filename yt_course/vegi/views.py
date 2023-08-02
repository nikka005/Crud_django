from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import *
# Create your views here.

def recipe(request):
    if request.method == "POST":
        
        data = request.POST
        recipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get('recipe_name')
        recipe_des = data.get('recipe_des')
        
        Recipe.objects.create(
            recipe_name =recipe_name,
            recipe_des=recipe_des,
            recipe_img=recipe_img
        )
        return redirect('/reci/')
    recipes  =Recipe.objects.all()

    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains =request.GET.get('search'))




    context={'recipess': recipes}
    return render( request ,"add_receipe.html", context)

def del_recipe(request , id):
    recipes = Recipe.objects.get(id = id)


    recipes.delete()
    return redirect('/reci/')

def up_recipe(request,id):
    update_recipes = Recipe.objects.get(id=id)
    if request.method == "POST":

        data = request.POST
        recipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get('recipe_name')
        recipe_des = data.get('recipe_des')

        update_recipes.recipe_name = recipe_name
        update_recipes.recipe_des = recipe_des

        if recipe_img:
            update_recipes.recipe_img = recipe_img

        update_recipes.save()
        messages.success(request,"Recipt Updated Successfully")
        return redirect('/reci/')







    context={'reci': update_recipes}


    return render( request ,"update.html", context)


