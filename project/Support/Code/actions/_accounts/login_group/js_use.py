def save_javascript_use(request):
    request.session['js_use'] = 'checked' if request.POST.get('javascript') == 'on' else ''
