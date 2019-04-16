from django.shortcuts import render
from .models import Post


def post_list(request):
	#posts = Post.objects.all()
	posts = Post.objects.filter(title__contains='The', text__contains='task')
	return render(request, 'blog/post_list.html', {'posts': posts})

# startwith
# contains
# icontains
# gt >
# gte >=
# lt <
# lte <=
# exact =