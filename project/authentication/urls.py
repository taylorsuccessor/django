from django.conf.urls import url

from django.contrib.auth import views as auth_views
from .login import login
from .password_reset import password_reset,password_reset_done
from .api_token import obtain_jwt_token
from .password_reset_confirm import password_reset_confirm,password_reset_complete

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'admin/login.html'}, name='auth.login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='auth.logout'),




    url(r'^password/reset/$', password_reset,
        {'template_name': 'admin/registration/password_reset_form.html', 'post_reset_redirect': 'auth.password_reset_done',
         'email_template_name': 'admin/registration/password_reset_email.html'}, name='auth.password_reset'),

    url(r'^password/reset/done/$', password_reset_done,{'template_name': 'admin/registration/password_reset_done.html'}, name='auth.password_reset_done'),




    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'admin/registration/password_reset_confirm.html','post_reset_redirect': 'auth.password_reset_complete'}, name='auth.password_reset_confirm'),

    url(r'^password/reset/complete/$', password_reset_complete,{'template_name': 'admin/registration/password_reset_complete.html'}, name='auth.password_reset_complete'),



    url(r'^api-token-auth/', obtain_jwt_token),

]