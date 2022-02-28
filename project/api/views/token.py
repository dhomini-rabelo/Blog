from django.shortcuts import redirect
from Support.Code.actions._accounts.login_group.login import get_token_for_user
from django.contrib.auth.decorators import login_required
from django.http import Http404



@login_required
def get_cookie(request):
    if request.method == 'GET':
        response = redirect(request.GET.get('latest_url'))
        token = get_token_for_user(request)
        response.set_cookie('access_token', token['access'], max_age=60*60*24*3)
        response.set_cookie('refresh_token', token['refresh'], max_age=60*60*24*365)
        response.set_cookie('email', request.session['user_save']['email'], max_age=60*60*24*365)
        return response
    raise Http404