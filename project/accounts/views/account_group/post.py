from Support.Code.actions.Support.django.messages.main import load_messages, save_message
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions._accounts.account_group.posts.create import create_draft_post
from Support.Code.actions.shortcuts.form.main import get_block_form, save_block_form
from Support.Code.django.forms.summer_form import SummerFieldForm




class CreatePostsAccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.user
        self.tc['summer_field'] = SummerFieldForm()
        self.tc['form'] = get_block_form()
        return render(request, 'accounts/account_group/post/create.html', self.tc)

    def post(self, request):
        validation = validate_form()

        if validation['status'] == 'valid':
            creation = create_draft_post(validation['fields'])
            save_message(request, {'title': 'success_new_draft_post_created', 'message': 'Rascunho criado', 'type': 'success'})
            return redirect(creation['new_draft_post_url'])

        save_block_form()
        return redirect('account_group_post_create')




class ListPostsAccountView(BaseView):

    def get(self, request):
        self.tc['posts_list'] = request.session['user_save']['posts']['posts_list']
        return render(request, 'accounts/account_group/post/list_posts.html', self.tc)
        



class ListDraftsAccountView(BaseView):

    def get(self, request):
        self.tc['posts_list'] = request.session['user_save']['posts']['drafts_list']
        return render(request, 'accounts/account_group/post/list_drafts.html', self.tc)
        
        
        
        
        
class EditPostsAccountView(BaseView):

    def get(self, request, code):
        self.tc['message'] = load_messages(request, 'success_new_draft_post_created')
        return render(request, 'accounts/account_group/post/edit.html', self.tc)





class PostPreviewAccountView(BaseView):

    def get(self, request, code):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/post/preview.html', self.tc)