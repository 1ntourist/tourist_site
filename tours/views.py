from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from .forms import *


# class TestTemplateView(TemplateView):
#     template_name = 'test_index.html'


class ArticleListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = 'tour_list.html'
    login_url = 'login'
    paginate_by = 5
    context_object_name = 'tours'


# class TourDetailView(DetailView):
#     model = Tour
#     template_name = 'tour_detail.html'
#     context_object_name = 'tour'


'''------------------------------  LIST OF CATEGORY  ---------------------'''


def list_category(requests):
    category = Category.objects.all()
    return render(requests, 'list_categories.html', {'categories': category})


'''------------------------------ TOURS OF CATEGORY  --------------------'''


def list_of_tours(requests, category__id):
    tour = Tour.objects.all()
    tour = tour.filter(category__id=category__id)
    return render(requests, 'list_tours.html', {'tours': tour})


'''--------------------------------  DETAIL OF TOUR  ----------------------'''


# def detail_of_tour(request, category, id):
#     tour = Tour.objects.all()
#     tour = tour.filter(category_id=category, id=id)
#     return render(request, 'tour_detail.html', {'tours': tour})


'''---------------------  TEST DETAIL ---------------------------------'''


def detail_of_tour(request, category, id):
    tour = Tour.objects.all()
    tour = tour.filter(category_id=category, id=id)
    template_name = 'tour_detail.html'


    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.tour = tour
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'tours': tour,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})