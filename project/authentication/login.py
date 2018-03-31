'''
# url(r'^login/$', login,  name='auth.login'),


from django.shortcuts import HttpResponseRedirect,render
from user.models import MyUser as User
from django.contrib.auth import login as auth_login

def login(request):
    if request.method=="POST":
        user = User.objects.get(pk=2)
        print(user.email)
        auth_login(request, user)

        return HttpResponseRedirect('/xxx')
    return render(request,'admin/login.html',{})




'''
from django.contrib.auth.views import deprecate_current_app,REDIRECT_FIELD_NAME,\
    AuthenticationForm,warnings,RemovedInDjango21Warning,LoginView as OriginLoginView

from django.contrib.auth import login as auth_login
from django.shortcuts import HttpResponseRedirect


class LoginView(OriginLoginView):
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user=form.get_user()
        auth_login(self.request, user )


        return HttpResponseRedirect(self.get_success_url())

@deprecate_current_app
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=False):
    warnings.warn(
        'The login() view is superseded by the class-based LoginView().',
        RemovedInDjango21Warning, stacklevel=2
    )
    return LoginView.as_view(
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        form_class=authentication_form,
        extra_context=extra_context,
        redirect_authenticated_user=redirect_authenticated_user,
    )(request)
