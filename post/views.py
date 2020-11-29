from django.shortcuts import render
from .models import Post


# Create your views here.
def post_comment_create_list_view(request):
    qs = Post.objects.all()

    context = {
        'qs': qs
    }
    return render(request, 'post/main.html', context)
