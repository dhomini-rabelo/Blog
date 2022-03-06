from Support.Code.Fast.models.cards import get_suggestion_html

def add_suggestion_in_session(request, suggestion, type_):
    request.session['user_save']['suggestions'][type_] += get_suggestion_html(suggestion, 'loading')
    request.session.save()