from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

from blog.models import Post

def index(request):
    queryset = Post.objects.order_by('-timestamp').filter(is_published=True)[:3]

    context = {
        'posts_list': queryset
    }
    return render(request, 'pages/index.html', context)

def contact(request):
    if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      message = request.POST['message']

      contact = Contact(name=name, email=email, message=message)

      contact.save()
    # Send mail
      send_mail(
          'JohnDev Inquery',
          'There has been an inquery from ' + name + '. Message:' + message +'.Log into the admin panel for more info',
          'muyambojohn1@gmail.com',
          ['webmaster@studio22.co.za'],
          fail_silently=False
      )

      return HttpResponse('')
