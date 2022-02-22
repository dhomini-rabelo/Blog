from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.django.forms.summer_form import SummerFieldForm




class CreatePostsAccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.user
        self.tc['summer_field'] = SummerFieldForm()
        return render(request, 'accounts/account_group/post/create.html', self.tc)




class ListPostsAccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/post/list_posts.html', self.tc)
        



class ListDraftsAccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/post/list_drafts.html', self.tc)
        
        
        
        
        
class EditPostsAccountView(BaseView):

    def get(self, request, code):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/post/edit.html', self.tc)





class PostPreviewAccountView(BaseView):

    def get(self, request, code):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/post/preview.html', self.tc)