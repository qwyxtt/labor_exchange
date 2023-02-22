from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class ProfilePage(DetailView):
    model = Employer
    template_name = 'authentications/user_page.html'

    def page_of_user(self, *args, **kwargs):
        user = Employer.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        page_user = self.model.objects.get_object_or_404(Employer, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class ProfilePage(DetailView):
    model = Employee
    template_name = 'authentications/users_page.html'

    def page_of_user(self, *args, **kwargs):
        user = Employee.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        page_user = self.model.objects.get_object_or_404(Employee, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class Created_profile(CreateView):
    model = Employer

    template_name = 'authentications/create_profile.html'
    fields = ['profile_pic', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
