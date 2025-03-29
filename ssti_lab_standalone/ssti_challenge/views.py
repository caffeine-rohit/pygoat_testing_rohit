# ---------------------------------------
# Server-side Template Injection (SSTI)
# ---------------------------------------

import os
import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Blogs

def ssti(request):
    if request.user.is_authenticated:
        return render(request, "Lab_2021/A3_Injection/ssti.html")
    else:
        return redirect('/')

def ssti_challenge(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            users_blogs = Blogs.objects.filter(author=request.user)
            return render(request, "Lab_2021/A3_Injection/ssti_challenge.html", {"blogs": users_blogs})
        elif request.method == "POST":
            blog = request.POST["blog"]
            id = str(uuid.uuid4()).split('-')[-1]

            blog = filter_blog(blog)
            prepend_code = "{% extends 'introduction/base.html' %}\
                {% block content %}{% block title %}\
                <title>SSTI-Blogs</title>\
                {% endblock %}"

            blog = prepend_code + blog + "{% endblock %}"
            new_blog = Blogs.objects.create(author=request.user, blog_id=id)
            new_blog.save()
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, f"templates/Lab_2021/A3_Injection/Blogs/{id}.html")
            with open(filename, "w+") as file:
                file.write(blog)
            return redirect(f'blog/{id}')
    else:
        return redirect('/')

def ssti_view_blog(request, blog_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, f"Lab_2021/A3_Injection/Blogs/{blog_id}.html")
        elif request.method == "POST":
            return HttpResponseBadRequest()