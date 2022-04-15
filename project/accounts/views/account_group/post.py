from django.http import Http404, HttpResponseForbidden
from Support.Code.actions.Support.django.messages.main import load_message, load_messages, save_message
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import get_object_or_404, render, redirect
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.utils.main import if_none
from Support.Code.actions._accounts.account_group.posts.create import create_draft_post, get_data_for_post_form
from Support.Code.actions._accounts.account_group.posts.edit import update_post
from Support.Code.actions.objects._accounts.account_group.posts.create import create_post_form_1, create_post_form_2, load_data, validate_create_post_form
from Support.Code.actions.objects._accounts.account_group.posts.edit import load_edit_post_1_data, load_edit_post_2_data, edit_post_form_1, edit_post_form_2, validate_edit_post_form
from Support.Code.actions.shortcuts.BlockForm.main import get_block_form, save_block_form, delete_used_block_form,delete_base_block_form
from Support.Code.django.forms.summer_form import SummerFieldForm
from django.utils.html import format_html
from posts.models import Post



class CreatePostsAccountView(BaseView):

    def get(self, request):
        self.tc['summer_field'] = SummerFieldForm({'text': if_none(request.session.get('session_text_create'), '')})
        self.tc['form1'] = get_block_form(request, 'ag_create_post_1', create_post_form_1, False)
        form2 = create_post_form_2.copy()
        load_data(*get_data_for_post_form(form2))
        self.tc['form2'] = get_block_form(request, 'ag_create_post_2', form2, False)
        return render(request, 'accounts/account_group/post/create.html', self.tc)

    def post(self, request):
        validation = validate_form(request.POST, validate_create_post_form)

        if validation['status'] == 'valid':
            request.session['session_text_create'] = None
            creation = create_draft_post(request, validation['fields'])
            save_message(request, {'title': 'success_new_draft_post_created', 'message': 'Rascunho criado', 'type': 'success'})
            delete_used_block_form(request, 'ag_create_post_1')
            delete_used_block_form(request, 'ag_create_post_2')
            return redirect(creation['new_draft_post_url'])

        save_block_form(request, 'ag_create_post_1', request.POST, validation['errors'])
        save_block_form(request, 'ag_create_post_2', {**validation['fields'], 'subcategory': request.POST.getlist('subcategory')}, validation['errors'])
        request.session['session_text_create'] = request.POST.get('text')
        return redirect(request.get_full_path())




class ListPostsAccountView(BaseView):

    def get(self, request):
        self.tc['list'] = format_html(request.session['user_save']['posts']['posts_list'])
        self.tc['none_list'] = format_html('<div style="margin-top: 2rem;"><span>Nenhum post</span></div>') if len(self.tc['list']) == 0 else ''
        return render(request, 'accounts/account_group/post/list_posts.html', self.tc)
        



class ListDraftsAccountView(BaseView):

    def get(self, request):
        self.tc['list'] = format_html(request.session['user_save']['posts']['drafts_list'])
        self.tc['none_list'] = format_html('<div style="margin-top: 2rem;"><span>Nenhum post</span></div>') if len(self.tc['list']) == 0 else ''
        return render(request, 'accounts/account_group/post/list_drafts.html', self.tc)
        
        
        
        
        
class EditPostsAccountView(BaseView):

    def get(self, request, code):
        post = get_object_or_404(Post, code=code)
        if post.author != request.user: return HttpResponseForbidden()
        

        form1 = edit_post_form_1.copy()
        form2 = edit_post_form_2.copy()

        if request.session.get('post_save_error') is not True:
            delete_base_block_form(request, 'ag_edit_post_1')
            delete_base_block_form(request, 'ag_edit_post_2')
            load_edit_post_1_data(form1, post)
            load_edit_post_2_data(*get_data_for_post_form(form2), post)
            self.tc['summer_field'] = SummerFieldForm({'text': post.text})
        else:
            self.tc['summer_field'] = SummerFieldForm({'text': if_none(request.session.get('session_text_edit'), '')})
            request.session['post_save_error'] = False

        self.tc['form1'] = get_block_form(request, 'ag_edit_post_1', form1, True)
        self.tc['form2'] = get_block_form(request, 'ag_edit_post_2', form2, True)


        self.tc['messages'] = load_messages(request, 'success_post_save', 'error_post_save', 'success_new_draft_post_created')
        self.tc['published'] = post.published
        self.tc['code'] = code
        return render(request, 'accounts/account_group/post/edit.html', self.tc)

    def post(self, request, code):
        validation = validate_form(request.POST, validate_edit_post_form)

        if validation['status'] == 'valid':
            update_post(request, code, {**validation['fields'], 'subcategory': request.POST.getlist('subcategory')}, request.POST['action'])
            save_message(request, {'title': 'success_post_save', 'message': 'Alterações salvas', 'type': 'success'})
            request.session['post_save_error'] = False
            request.session['session_text_edit'] = None
            delete_used_block_form(request, 'ag_edit_post_1')
            delete_base_block_form(request, 'ag_edit_post_1')
            delete_used_block_form(request, 'ag_edit_post_2')
            delete_base_block_form(request, 'ag_edit_post_2')
        else:
            save_message(request, {'title': 'error_post_save', 'message': 'Corrija os errors para salvar', 'type': 'error'})
            save_block_form(request, 'ag_edit_post_1', {**validation['fields'], 'subcategory': request.POST.getlist('subcategory')}, validation['errors'])
            save_block_form(request, 'ag_edit_post_2', {**validation['fields'], 'subcategory': request.POST.getlist('subcategory')}, validation['errors'])
            request.session['post_save_error'] = True
            request.session['session_text_edit'] = request.POST.get('text')
        
        return redirect(request.get_full_path())
