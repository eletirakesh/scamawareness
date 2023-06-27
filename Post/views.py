from django.http import HttpResponse
from .models import Post,Comment
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm,LikeForm




# Create your views here.
class Homepageview(ListView):
    model=Post
    template_name='home.html'

class Variousscamspageview(TemplateView):
     template_name='typesofscams.html'


class Aboutpageview(TemplateView):
    template_name='about.html'


class PostListView(ListView):
    model=Post
    template_name='home.html'
    
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['words']  =  ['Stay scam smart', ' Stay vigilant, stay safe', 'Awareness beats scams','Guard your personal info']   
        return context





class PostUpdateView(UpdateView):
    model=Post
    fields=('image','title','description',)
    template_name='post_edit.html'
    success_url=reverse_lazy('home')
    


class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scam = self.get_object()
        current_user = self.request.user

       
        if current_user == scam.author:
            context['can_edit'] = True  
        else:
            context['can_edit'] = False

        return context


class PostDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')



class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='post_create.html'
    fields=('image','title','description',)
    success_url=reverse_lazy('home')
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class CommentView(LoginRequiredMixin,CreateView):
    form=CommentForm
    model=Comment
    fields=['comment']
    template_name='comment.html'
    
    def form_valid(self, form) -> HttpResponse:
        form.instance.author=self.request.user 
        form.instance.scam_id = self.kwargs['pk']
        return super().form_valid(form)
    


    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})




