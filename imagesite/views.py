from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import Category, Image
from django.db.models.query_utils import Q


def show_about(request):
    name = 'Nitesh here.'
    link = 'www.linkedin.com/in/codenitesh'

    data = {
        'name': name,
        'link': link,
    }
    return render(request, "about.html", data)


def show_home(request):
    images = Image.objects.all()  # It will load all images available (like MODEL)
    categories = Category.objects.all()
    data = {'images': images,
            'categories': categories,
            }  # Work as key -- addAllAttributes("images", image)

    return render(request, "home.html", data)


def show_home_with_category(request, cid):
    print(cid)
    all_categories = Category.objects.all()  # We will get all categories here!

    selected_category = Category.objects.get(pk=cid)
    print(selected_category.title)

    images = Image.objects.filter(
        cat=selected_category)  # cat is in model.images

    data = {
        'categories': all_categories,
        'images': images,
    }
    return render(request, "home.html", data)

# def home(request):
#     return redirect("/home")

def search(request):
    try:
        search_query = request.GET['query']
        selected_images = Image.objects.filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))

        all_categories = Category.objects.all()

        data = {
            'categories': all_categories,
            'images': selected_images
        }
        return render(request, "home.html", data)
    
    except:
        return redirect("/home")
