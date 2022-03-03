from django.contrib.auth.decorators import login_required
from Support.Code.actions.Support.django.decorators import no_login_required
from django.urls import path
from .views.login_group import *
from .views.account_group.account_page import *
from .views.account_group.edit import *
from .views.account_group.post import *
from .views.account_group.suggestions import *


# contas/
urlpatterns = [
    path('cadastro/', no_login_required(RegisterView.as_view()), name='register'),
    path('cadastro/confirmacao-de-email', no_login_required(RegisterEmailConfirmationView.as_view()), name='register_email_confirmation'),
    path('cadastro/confirmacao-de-email/reenviar', no_login_required(send_new_email_for_register), name='send_new_email_for_register'),
    path('login/', no_login_required(LoginView.as_view()), name='login'),
    path('nova-senha/informar-email', no_login_required(ForgotPasswordEmailView.as_view()), name='forgot_password_email'),
    path('nova-senha/alterar-senha', no_login_required(ForgotPasswordView.as_view()), name='forgot_password'),
    path('nova-senha/email-confirmado', no_login_required(forgot_valid_email), name='forgot_valid_email'),
    path('logout/', login_required(logout_view), name='logout'),
    path('minha-conta/', AccountView.as_view(), name='account_page'),
    path('minha-conta/post/criar', login_required(CreatePostsAccountView.as_view()), name='account_group_post_create'),
    path('minha-conta/post/editar/meus-posts', login_required(ListPostsAccountView.as_view()), name='account_group_post_list_posts'),
    path('minha-conta/post/editar/meus-rascunhos', login_required(ListDraftsAccountView.as_view()), name='account_group_post_list_drafts'),
    path('minha-conta/post/editar/<int:code>', login_required(EditPostsAccountView.as_view()), name='account_group_post_edit'),
    path('minha-conta/post/rascunhos/preview/<int:code>', login_required(PostPreviewAccountView.as_view()), name='account_group_post_preview'),
    path('minha-conta/sugestao/categorias', login_required(SuggestionCategoriesAccountView.as_view()), name='account_group_suggestions_categories'),
    path('minha-conta/sugestao/sub-categorias', login_required(SuggestionSubCategoriesAccountView.as_view()), name='account_group_suggestions_sub_categories'),
    path('minha-conta/editar/informacoes-basicas', login_required(EditBasicAccountView.as_view()), name='account_group_edit_basic'),
    path('minha-conta/editar/email', login_required(EditEmailAccountView.as_view()), name='account_group_edit_email'),
    path('minha-conta/editar/senha', login_required(EditPasswordAccountView.as_view()), name='account_group_edit_password'),
]
