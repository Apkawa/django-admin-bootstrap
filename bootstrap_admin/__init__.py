__version__ = '0.3.6'

from django.contrib import admin


def monkey_patch():
    old_each_context = admin.AdminSite.each_context

    def each_context(self, request):
        context = old_each_context(self, request)
        context['ADMIN_SITE'] = self
        return context

    admin.AdminSite.each_context = each_context


monkey_patch()
