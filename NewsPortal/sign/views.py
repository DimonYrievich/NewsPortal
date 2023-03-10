
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):    #ПРЕДСТАВЛЕНИЕ для отображения информации авторизованным пользователям и определения, состоят они в группе authors или нет
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required                                     # Пишем функцию-представление для добавления пользователя в группу authors
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

#class MyView(PermissionRequiredMixin, CreateView):
#    permission_required = ('<app>.<action>_<model>',
#                           '<app>.<action>_<model>')
#ЭТОТ КУСОК ДОЛЖЕН БЫТЬ ЛИБО ЗДЕСЬ, ЛИБО в news\views.py НЕ ПОНЯТНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class EditPost(PermissionRequiredMixin, CreateView):    # ПРЕДСТАВЛЕНИЕ: Ограничения и права доступа пользователя
    permission_required = ('news.add_post',
                           'news.delete_post',
                           'news.view_post',
                           'news.change_post',)
