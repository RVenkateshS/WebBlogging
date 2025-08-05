from .models import Post
from django.views.generic import ListView , DetailView , CreateView, UpdateView, DeleteView
from .models import Post
from .Forms import PostForm , EditForm
from django.urls import reverse_lazy
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView) :
 model = Post
 template_name = 'home.html'
#  ordering = ['-id']
 ordering = ['-post_date']
    
class ArticalDetailView(DetailView):
    model = Post
    template_name = 'artical_details.html'
    
class  AddPostView(CreateView) :
    model = Post
    form_class = PostForm
    template_name = 'AddPost.html'
    # fields = '__all__'
    #fields = ('title' , 'body')
    
class  UpdatePostView(UpdateView) :
    model = Post
    form_class = EditForm
    #fields = ['title' , 'body', 'title_tag']
    template_name = 'update_post.html'
    

class  DeletePostView(DeleteView) :
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
    
    