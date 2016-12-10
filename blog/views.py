from django.shortcuts import render
from blog.models import Post

# Create your views here.

def inicio(request):
	query = Post.objects.all()
	print(query)

	return render(request,'blog/inicio.html',{ 'query' : query})
