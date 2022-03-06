from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.actions._accounts.account_group.suggestions import add_suggestion_in_session
from accounts.tasks.suggestions import save_suggestion
from django.utils.html import format_html
from Support.Code.actions.Support.django.messages.main import save_message, load_message




class SuggestionPostProcess(BaseView):
        
    def suggestion_post_process(self, request, type_):
        suggestion = request.POST.get('suggestion')
        valid = False

        if not isinstance(suggestion, str):
            error = 'VALOR INVÁLIDO'
        elif (len(suggestion) < 1) or (len(suggestion) > 50):
            error = 'TAMANHO INVÁLIDO'
        else:
            valid = True
            save_suggestion.delay(suggestion, type_, request.session['user_save']['data']['email'])
            add_suggestion_in_session(request, suggestion, type_)
            
        if valid:
            save_message(request, {'title': 'suggestion_feedback', 'message': 'SUGESTÃO ENVIADA', 'type':  'success'})
        else:
            save_message(request, {'title': 'suggestion_feedback', 'message': error, 'type':  'error'})
        
        
        
        
class SuggestionCategoriesAccountView(SuggestionPostProcess):

    def get(self, request):
        self.tc['suggestions'] = format_html(request.session['user_save']['suggestions']['categories'])
        self.tc['message'] = load_message(request, 'suggestion_feedback')
        return render(request, 'accounts/account_group/suggestions/categories.html', self.tc)

    def post(self, request):
        self.suggestion_post_process(request, 'categories')
        return redirect('account_group_suggestions_categories')

        
    
    
class SuggestionSubCategoriesAccountView(SuggestionPostProcess):

    def get(self, request):
        self.tc['suggestions'] = format_html(request.session['user_save']['suggestions']['subcategories'])
        self.tc['message'] = load_message(request, 'suggestion_feedback')
        return render(request, 'accounts/account_group/suggestions/sub_categories.html', self.tc)
    
    def post(self, request):
        self.suggestion_post_process(request, 'subcategories')
        return redirect('account_group_suggestions_sub_categories')
