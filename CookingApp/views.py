from django.shortcuts import render, get_object_or_404
from .models import Review, Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, ReviewForm


def index(request):
    return render(request, 'CookingApp/index.html')

def getRecipes(request):
    recipeData = Recipe.objects.all()

    return render(request, 'CookingApp/recipes.html', {'recipeData' : recipeData})

def recipeDetails(request, id):

    recipeDetail = Recipe.objects.get(pk=id)

    recipeReview = recipeDetail.reviews.all()


    context = {
        'recipeDetail' : recipeDetail,
        'recipeReview' : recipeReview,
    }


    return render(request, 'CookingApp/recipedetails.html', context=context)


@login_required
def newReview(request):
     form = ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()

     return render(request, 'CookingApp/newreview.html', {'form': form})


@login_required
def newRecipe(request):
     form = RecipeForm
     if request.method=='POST':
          form=RecipeForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=RecipeForm()
     else:
          form=RecipeForm()

     return render(request, 'CookingApp/newrecipe.html', {'form': form})




def loginmessage(request):
    return render(request, 'CookingApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'CookingApp/logoutmessage.html')

    


