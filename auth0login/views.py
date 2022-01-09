from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
import json

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard) # If the user is already logged in, the "dashboard" view will be shown instead.
    else:
        return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        # 'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 ('l-cafe.us.auth0.com', 'xO7v4R3GmZjBcxGLC4oggwHPqzCHSa0x', return_to)
    return HttpResponseRedirect(logout_url)



