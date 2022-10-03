from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin# This is needed for object oriented programming. A class should only inherit one class. A Mixin is another class that can be inherited from allwoing for a class to inherit more classes essentially.
from django.urls import reverse_lazy
from .models import Post, Status
# more info:
# https://docs.djangoproject.com/en/4.1/ref/urlresolvers/
# This looks up a url pattern via its name tag, but waits until the underlying database transaction is complete

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
class DraftPostListView(ListView):
    template_name = "posts/list.html"
    model = Post 
    # Refer to class video for more information: FSDI 112-2 C30 @ 02hr:29min
    def get_context_data(self, **kwargs): #Keyword arguments. All list views have this get_context_data() method. 
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="draft") # The get method returns records that matched the name = "draft". you can also use it like this, .get(name="draft")
        context["post_list"] = Post.objects.filter(author=self.request.user # Ensuring that the data is returned based on the author logged in.
                                          ).filter(status=pending_status
                                          ).order_by("created_on"
                                          ).reverse()
        return context
class ArchivedPostListView(ListView):
    template_name = "posts/list.html"
    model = Post 
    # Refer to class video for more information: FSDI 112-2 C30 @ 02hr:29min
    def get_context_data(self, **kwargs): #Keyword arguments. All list views have this get_context_data() method. 
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="archived") # The get method returns records that matched the name = "archived". you can also use it like this, .get(name="archived")
        context["post_list"] = Post.objects.filter(author=self.request.user # Ensuring that the data is returned based on the author logged in.
                                          ).filter(status=pending_status
                                          ).order_by("created_on"
                                          ).reverse()
        return context
class PublishedPostListView(ListView):
    template_name = "posts/list.html"
    model = Post 
    # Refer to class video for more information: FSDI 112-2 C30 @ 02hr:29min
    def get_context_data(self, **kwargs): #Keyword arguments. All list views have this get_context_data() method. 
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="published") # The get method returns records that matched the name = "published". you can also use it like this, .get(name="published")
        context["post_list"] = Post.objects.filter(author=self.request.user # Ensuring that the data is returned based on the author logged in.
                                          ).filter(status=pending_status
                                          ).order_by("created_on"
                                          ).reverse()
        return context
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html" 
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form): # This overrides the default form_valid() method of Django 
        form.instance.author = self.request.user # Allows the Author to request the user model.
        return super().form_valid(form) # Super() calls the form method


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # REMEMBER, Mixin order matters for validations.
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"] # Fields will be showed on the page
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user

# delete view for details

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # REMEMBER, Mixin order matters for validations.
    model = Post
    # success_url ="/posts" # You can specify success urlurl to redirect after successfully
    template_name = "posts/confirm_delete.html" # deleting object
    success_url = reverse_lazy("list") # From Django's urls module. Redirects after successfully deleting object
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user
