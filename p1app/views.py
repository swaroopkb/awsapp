from django.shortcuts import render
from p1app.models import User
# Create your views here.


def index(request):
    return render(request,'p1app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'p1app/users.html',context=user_dict)
