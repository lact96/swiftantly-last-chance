from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, WorkspaceCreationForm
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from rest_framework import viewsets

User = get_user_model()
class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('workspace:dashboard')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Generate token
            token = default_token_generator.make_token(user)

            # Email sending logic
            mail_subject = 'Activate your Swiftantly account'
            current_site = get_current_site(request)
            message = render_to_string('account/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            })
            send_mail(mail_subject, message, 'noreply@swiftantly.com', [user.email])

            return redirect('account_activation_sent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        # Create a workspace for the user
        workspace = Workspace(owner=user, name=f"{user.first_name}'s Workspace")
        workspace.save()

        # Log the user in (optional)
        return redirect('workspace_created')  # Redirect to a view that confirms the workspace creation
    else:
        return render(request, 'account/activation_invalid.html')
    
def dashboard(request):
    return render(request, 'dashboards/index.html')



