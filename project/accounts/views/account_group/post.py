from django.http import Http404, HttpResponseForbidden
from Support.Code.actions.Support.django.messages.main import load_message, save_message
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import get_object_or_404, render, redirect
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.utils.main import if_none
from Support.Code.actions._accounts.account_group.posts.create import create_draft_post, get_data_for_post_form
from Support.Code.actions._accounts.account_group.posts.edit import update_post
from Support.Code.actions.objects._accounts.account_group.posts.create import create_post_form_1, create_post_form_2, load_data, validate_create_post_form
from Support.Code.actions.objects._accounts.account_group.posts.edit import load_edit_post_1_data, load_edit_post_2_data, edit_post_form_1, edit_post_form_2
from Support.Code.actions.shortcuts.BlockForm.main import get_block_form, save_block_form
from Support.Code.django.forms.summer_form import SummerFieldForm
from django.utils.html import format_html
from posts.models import Post



class CreatePostsAccountView(BaseView):

    def get(self, request):
        self.tc['summer_field'] = SummerFieldForm({'text': if_none(request.session.get('session_text'), '')})
        self.tc['form1'] = get_block_form(request, 'ag_create_post_1', create_post_form_1, False)
        form2 = create_post_form_2.copy()
        load_data(*get_data_for_post_form(form2))
        self.tc['form2'] = get_block_form(request, 'ag_create_post_2', form2, False)
        return render(request, 'accounts/account_group/post/create.html', self.tc)

    def post(self, request):
        validation = validate_form(request.POST, validate_create_post_form)

        if validation['status'] == 'valid':
            request.session['session_text'] = None
            creation = create_draft_post(request, validation['fields'])
            save_message(request, {'title': 'success_new_draft_post_created', 'message': 'Rascunho criado', 'type': 'success'})
            return redirect(creation['new_draft_post_url'])

        save_block_form(request, 'ag_create_post_1', request.POST, validation['errors'])
        save_block_form(request, 'ag_create_post_2', {**validation['fields'], 'subcategory': request.POST.getlist('subcategory')}, validation['errors'])
        request.session['session_text'] = request.POST.get('text')
        return redirect(request.get_full_path())




class ListPostsAccountView(BaseView):

    def get(self, request):
        self.tc['list'] = request.session['user_save']['posts']['posts_list']
        return render(request, 'accounts/account_group/post/list_posts.html', self.tc)
        



class ListDraftsAccountView(BaseView):

    def get(self, request):
        self.tc['list'] = format_html(request.session['user_save']['posts']['drafts_list'])
        return render(request, 'accounts/account_group/post/list_drafts.html', self.tc)
        
        
        
        
        
class EditPostsAccountView(BaseView):

    def get(self, request, code):
        post = get_object_or_404(Post, code=code)
        if post.author != request.user: return HttpResponseForbidden()
        self.tc['summer_field'] = SummerFieldForm({'text': post.text})
        self.tc['message'] = load_message(request, 'success_new_draft_post_created')
        form1 = edit_post_form_1.copy()
        load_edit_post_1_data(form1, post)
        self.tc['form1'] = get_block_form(request, 'ag_edit_post_1', form1)
        form2 = edit_post_form_2.copy()
        load_edit_post_2_data(*get_data_for_post_form(form2), post)
        self.tc['form2'] = get_block_form(request, 'ag_edit_post_2', form2)
        self.tc['published'] = post.published
        return render(request, 'accounts/account_group/post/edit.html', self.tc)

    def post(self, request, code):
        # testar injeção de subcategory com lista
        validation = validate_form(request.POST, validate_create_post_form)
        if validation['status'] == 'valid':
            update_post(request, code, {**validation['fields'], 'subcategory': request.POST.getlist('subcategory')}, request.POST['action'])
        return redirect(request.get_full_path())
