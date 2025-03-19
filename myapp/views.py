from django.shortcuts import render, redirect
from django.views.generic import View
from myapp.models import *
from myapp.forms import *
from django.contrib.auth import authenticate, login, logout 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg,Q
from django.contrib import messages


# Create your views here.
def is_super_user(fn):
    def wrapper(request, **kwargs):
        if request.user.is_superuser:
            return fn(request, **kwargs)
        else:
            return redirect('login')
    return wrapper

def is_user(fn):
    def wrapper(request, **kwargs):
        id = kwargs.get('pk')
        data = Review.objects.get(id=id)
        if request.user == data.user:
            return fn(request, **kwargs)
        return redirect('login')
    return wrapper

class Homepage(View):
    def get(self,request):
        return render(request,"index.html")

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login")
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('movielist')
                return redirect('movielist')
        return render(request, "login.html", {"form": form})

@method_decorator(decorator=is_super_user, name="dispatch")
class MovieAddView(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'movieadd.html', {'form': form})
    
    def post(self, request):
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_superuser:
                Movie.objects.create(**form.cleaned_data)
            return redirect('movielist')
        return redirect('login')

# @method_decorator(decorator=is_super_user, name="dispatch")
class MovieListView(View):
    def get(self, request):
        # Annotate the Movie queryset with the average rating
        data = Movie.objects.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')

        return render(request, 'movielist.html', {'data': data})

@method_decorator(decorator=is_super_user, name="dispatch")
class MovieDeleteView(View):
    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        Movie.objects.get(id=id).delete()
        return redirect('movielist')

@method_decorator(decorator=is_super_user, name="dispatch")
class MovieUpdateView(View):
    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        data = Movie.objects.get(id=id)
        form = MovieForm(instance=data)
        return render(request, 'movieupdate.html', {'form': form})
    
    def post(self, request, **kwargs):
        id = kwargs.get('pk')
        data = Movie.objects.get(id=id)
        form = MovieForm(request.POST, request.FILES, instance=data)
        print("hi")
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('movielist')
        return render(request, 'movieupdate.html', {'form': form})

class MovieDetailView(View):
    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        data = Movie.objects.get(id=id)
        return render(request, 'moviedetails.html', {'data': data})

@method_decorator(login_required, name="dispatch")

class ReviewAddView(View):
    def get(self, request, **kwargs):
        if not request.user.is_superuser:
            id = kwargs.get('pk')
            data = Movie.objects.get(id=id)
            form = ReviewForm()
            return render(request, "reviewadd.html", {"form": form , "data":data})
        
        return redirect('login')
    
    def post(self, request, **kwargs):
        id = kwargs.get('pk')
        data = Movie.objects.get(id=id)
        form = ReviewForm(request.POST)
        if form.is_valid():

            reviewdata=Review.objects.filter(user=request.user,movie=data)
            if not reviewdata:
                 Review.objects.create(user=request.user, movie=data, **form.cleaned_data)

            else:
                messages.error(request, "Already added review for this movie! You can update it!")
        return redirect("movielist")

@method_decorator(is_user, name="dispatch")
class ReviewUpdateView(View):
    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        data = Review.objects.get(id=id)
        form = ReviewForm(instance=data)
        return render(request, "reviewadd.html", {"form": form,"data":data.movie})
    
    def post(self, request, **kwargs):
        id = kwargs.get('pk')
        data = Review.objects.get(id=id)
        form = ReviewForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("movielist")
        return render(request, "reviewadd.html", {"form": form})


class ReviewListView(View):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        moviedata = Movie.objects.get(id=id)
        data = Review.objects.filter(movie=moviedata)
        average = data.aggregate(average=Avg("rating"))  # Correctly calculate the average rating

        return render(request, "reviewlist.html", {"data": data, "id": id, "average": average ,"moviedata":moviedata})


class ReviewUserlistView(View):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        data=Review.objects.filter(user=request.user)
        return render(request,'reviewuserlist.html',{"data":data})


class ReviewDeleteView(View):
    def get(self, request, **kwargs):
        
        id = kwargs.get('pk')
        data=Review.objects.get(id=id)
        if request.user.is_superuser or request.user==data.user:
            no=data.movie.id
            data.delete()
            return redirect("reviewlist",pk=no)
        else:
            return redirect("login")

class Genrelist(View):
    def get(self,request,**kwargs):
        id = kwargs.get('pk')
        data=Movie.objects.filter(genre=id).annotate(average_rating=Avg('review__rating')).order_by('-average_rating')
        return render(request, 'movielist.html', {'data': data})
        
    

class SearchView(View):
    def post(self, request):
        query = request.POST.get('search')
        if query:
            
            data = Movie.objects.filter(
                Q(name__icontains=query) | Q(year__icontains=query)| Q(language__icontains=query)| Q(genre__icontains=query)
            ).annotate(average_rating=Avg('review__rating')).order_by('-average_rating')
        else:
            data = Movie.objects.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')

        return render(request, 'movielist.html', {'data': data})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')

