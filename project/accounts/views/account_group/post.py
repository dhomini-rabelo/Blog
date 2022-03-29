from Support.Code.actions.Support.django.messages.main import load_messages, save_message
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions._accounts.account_group.posts.create import create_draft_post, get_data_for_post_form
from Support.Code.actions.objects._accounts.account_group.posts.create import create_post_form_1, create_post_form_2, load_data
from Support.Code.actions.shortcuts.BlockForm.main import get_block_form, save_block_form
from Support.Code.django.forms.summer_form import SummerFieldForm





class CreatePostsAccountView(BaseView):

    def get(self, request):
        self.tc['summer_field'] = SummerFieldForm()
        self.tc['form1'] = get_block_form(request, 'ag_post_1', create_post_form_1, False)
        form2 = create_post_form_2.copy()
        load_data(*get_data_for_post_form(form2))
        self.tc['form2'] = get_block_form(request, 'ag_post_2', form2, True)
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
        return render(request, 'accounts/account_group/post/preview.html', self.tc)