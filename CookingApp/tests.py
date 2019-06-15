from django.test import TestCase
from .models import Recipe, Review
from django.contrib.auth.models import User
# Create your tests here.


# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')

# class GetProductsTest(TestCase):
#     def setUp(self):
#         self.u = User(username='myUser')
#                     #you can write it like this (just the name of the class)
#         self.type = TechType(techtypename = 'laptop')
#                     #or like this, (with .object.create)
#         self.prod = Product.objects.create(productname = 'product1', techtype=self.type, user=self.u, productprice=500.00, productentrydate='2019-04-02', productdescription='lalalalala lalalaal')

#     def test_product_detail_success(self):
#         response=self.client.get(reverse('product', args=(self.prod.id,)))
#         self.assertEqual(response.status_code, 200)


class RecipeTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(username='myUser')
        self.testrecipe = Recipe.objects.create(recipeTitle="Pasta", shortDescription="A very good easy pasta recipe", ingredients="pasta, water", description="Bla bla bla bla", date="2019-04-04", user=self.u)

    def test_recipe_Title(self):
        self.assertEqual(str(self.testrecipe.recipeTitle), self.testrecipe.recipeTitle)

    def test_recipe_shortDescription(self):
        self.assertEqual(str(self.testrecipe.shortDescription), "A very good easy pasta recipe")

    def test_recipe_description(self):
        self.assertEqual(str(self.testrecipe.description), "Bla bla bla bla")

    def test_recipe_date(self):
        self.assertEqual(str(self.testrecipe.date), "2019-04-04")

class ReviewTest(TestCase):
    def setUp(self):
        self.u2 = User.objects.create(username='myUser2')
        self.u3 = User.objects.create(username='myUser3')
        self.recipetest = Recipe.objects.create(recipeTitle="Pasta", shortDescription="A very good easy pasta recipe", ingredients="pasta, water", description="Bla bla bla bla", date="2019-04-04", user=self.u2)
        self.reviewtest = Review.objects.create(recipe=self.recipetest, title="I love it", description="Easy to make", rating="5", date="2019-04-04",user=self.u3 )
  
    def test_title(self):
        self.assertEqual(str(self.reviewtest.title), "I love it")
    
    def test_description(self):
        self.assertEqual(str(self.reviewtest.title), "Easy to make")

# class Recipe(models.Model):
#     recipeTitle = models.CharField(max_length = 100)
#     shortDescription = models.CharField(max_length = 255, default='SOME STRING')
#     ingredients = models.TextField()
#     description = models.TextField()
#     date = models.DateField()
#     user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

# class Review(models.Model):
#     recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete = models.DO_NOTHING)
#     title = models.CharField(max_length = 100)
#     description = models.CharField(max_length = 255)
#     rating = models.SmallIntegerField()
#     date = models.DateField()
#     user = models.ForeignKey(User, on_delete = models.DO_NOTHING)



