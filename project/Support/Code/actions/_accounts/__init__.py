def save_javascript_use(request):
    js_use = request.POST.get('javascript')

    request.session['not_use_javascript'] = True if js_use != 'on' else False

    