from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Like
from user_profile.models import Profile

from .forms import PostModelForm, CommentModelForm


# Create your views here.
@login_required
def post_comment_create_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    post_form = PostModelForm()
    comment_form = CommentModelForm()
    post_added = False

    #POST FORM, COMMENT FORM
    if 'post-form' in request.POST:
        post_form = PostModelForm(request.POST, request.FILES)
        if post_form.is_valid():
            print(True)
            instance = post_form.save(commit=False)
            instance.author = profile
            instance.save()
            post_added = True
            post_form = PostModelForm()

    if 'comment-form' in request.POST:
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            print(True)
            instance.save()
            comment_form = CommentModelForm()

    context = {
        'qs': qs,
        'profile':profile,
        'post_form':post_form,
        'comment_form':comment_form,
        'post_added':post_added,

    }
    return render(request, 'post/main.html', context)

@login_required
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

        data = {
            'value': like.value,
            'likes':post_obj.liked.all().count()
        }
        return JsonResponse(data, safe=False)

    return redirect('post:main-post-view')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post/confirm_del.html'
    success_url = reverse_lazy('post:main-post-view')
    # success_url = '/post/'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request, 'You Need To be the Author of the Post in order to Delete the Post')
        return obj


class PostUpdateView(LoginRequiredMixin,UpdateView):
    form_class = PostModelForm
    model = Post
    template_name = 'post/update.html'
    success_url = reverse_lazy('post:main-post-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be an author of the post in order to update" )
            return self.form_invalid(form)