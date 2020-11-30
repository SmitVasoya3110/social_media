from django.shortcuts import render, redirect
from .models import Post, Like
from user_profile.models import Profile

from .forms import PostModelForm


# Create your views here.
def post_comment_create_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    #POST FORM, COMMENT FORM
    post_form = PostModelForm(request.POST or None, request.FILES or None)
    if post_form.is_valid():
        print(True)
        instance = post_form.save(commit=False)
        instance.author = profile
        instance.save()
        post_form = PostModelForm()

    context = {
        'qs': qs,
        'profile':profile,
        'post_form':post_form
    }
    return render(request, 'post/main.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        else:
            like.value = 'Like'
            post_obj.save()
            like.save()

        return redirect('post:main-post-view')
