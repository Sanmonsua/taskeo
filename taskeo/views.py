from django.shortcuts import render, redirect
from home.models import UserProfile

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        try:
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user = UserProfile(user=request.user)
            user.save()
        return render(request, 'taskeo/index.html', context={"user":user})
    return redirect('/signin')
