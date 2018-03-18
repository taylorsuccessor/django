# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.http.response import HttpResponseRedirect

from django.utils.html import format_html
from models import MyCar, Shop
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from  django.shortcuts import render

from rest_framework.response import Response

# Register your models here.


class TextWidget(forms.TextInput):
     class Media:
        js = ('js/jquery.js','js/custom/text_filter_pattern.js',)




class MyCarForm(forms.ModelForm):
    name=forms.CharField(widget=TextWidget)

    fields={'name'}
    class Meta:
        model = MyCar
        exclude = []
        widgets = {
            'age': forms.Textarea(attrs={'cols': 80, 'rows': 1,'class':'form-control'}),
        }
        labels = {
            'owner': _('Override owner'),
        }
        help_texts = {
            'name': _('My Override Owner Some useful help text.'),
        }
        error_messages = {
            'number_of_door': {
                'min_value': _("min_value Override message or customize "),
            },
        }



from django.contrib.admin import SimpleListFilter
from django.utils.encoding import force_text


class SimpleTemplateFilter(SimpleListFilter):


    def choices(self, changelist):

        for lookup, title in self.lookup_choices:
            if lookup == '':
                yield {
                    'selected': self.value() is None,
                    'query_string': changelist.get_query_string({}, [self.parameter_name]),
                    'display': title,
                }
            else:
                yield {
                    'selected': self.value() == force_text(lookup),
                    'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                    'display': title,
                }












class NumberOfRowInPageFilter(SimpleTemplateFilter):
    title = 'Number Of Rows in list'
    parameter_name = 'per_page'
    template = 'admin/filter.html'

    def lookups(self, request, model_admin):

        return  [ ('10', '10 Rows'),('25', '25 Rows'),('50', '50 Rows'),('100', '100 Rows')]

    def queryset(self, request, queryset):
         return queryset





class TextAreaWidget(forms.Select):
    template_name = 'custom_admin/templates/admin/form/textarea.html'

class ActionTemplateForm(forms.Form):
    action = forms.ChoiceField(label=_('Action:'),widget=TextAreaWidget)

    select_across = forms.BooleanField(
        label='',
        required=False,
        initial=0,
        widget=forms.HiddenInput({'class': 'select-across'}),
    )

from django.template.loader import render_to_string
def renderCustomFieldsetList(request,object,form):

    return {'Notes':render_to_string('custom_field.html',{'field_name':'age','object':object,'form':form})}

class MyCarAdmin(admin.ModelAdmin):


    list_display = ('__str__','name','status',  'age','module_link')
    list_display_links = ()
    list_filter = ('status','shop',NumberOfRowInPageFilter,)
    list_select_related = False
    list_per_page = 20

    list_max_show_all = 200
    list_editable = (('name','status'))
    search_fields = ['owner__email', 'owner__first_name', 'owner__last_name', 'name','description']
    date_hierarchy = 'created_at'
    save_as = True
    save_as_continue = True
    save_on_top = False
    # paginator = Paginator
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = 'admin/change_form.html'
    change_form_template =  'admin/change_form.html'
    change_list_template =  'admin/change_list.html'
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = ['custom_action_selected']
    action_form = ActionTemplateForm
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True

    # checks_class = ModelAdminChecks
    form = MyCarForm
    # fieldsets = (
    #         (None, {
    #             'fields': list(MyCarForm.fields)
    #         }),
    #         ('Notes', {
    #             'fields': ['age']
    #         }),
    # )





    def lookup_allowed(self, lookup, value):
        return True

    def custom_action_selected(self, request, queryset):

        queryset.update(status='xx')
        return HttpResponseRedirect('/admin/my_car/shop')

    custom_action_selected.short_description = "Publish the selected posts"
    def get_actions(self, request):
        # Disable delete
        actions = super(MyCarAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


    def get_search_results(self, request, queryset, search_term):
        queryset=queryset
        use_distinct=False

        if True :
           queryset, use_distinct=super(MyCarAdmin,self).get_search_results( request, queryset, search_term)


        return queryset, use_distinct


    def module_link(self, obj):
        return format_html('<a href="#">link</a>')

    def get_queryset(self, request):

        return self.model.objects.filter()


    def changelist_view(self, request, extra_context=None):

        # import pdb;pdb.set_trace()


        request.GET._mutable = True

        if request.GET.get('per_page',False) :
          self.list_per_page=int(request.GET.get('per_page',10))
          # request.GET.pop('per_page')

        extra_context = extra_context or {}
        extra_context['filter_container_class'] = 'col-xs-4'
        extra_context['date_hierarchy_container_class']='col-xs-12'



        extra_context['title']='title'
        extra_context['bannerTitle']='bannerTitle'
        extra_context['bannerDescription']='bannerDescription'
        extra_context['modelTableHead']='modelTableHead'
        extra_context['modelTableDescription']='modelTableDescription'



        return super(MyCarAdmin, self).changelist_view(request, extra_context=extra_context)

    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #
    #     return super(MyCarAdmin, self)\
    #         .changelist_view(self, request, object_id, form_url, extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['customFieldsetList'] = renderCustomFieldsetList(request,object,self.form)
        return super(MyCarAdmin, self).add_view(request, form_url,
                                                  extra_context=extra_context)

    def change_view(self, request, form_url='', extra_context=None):

        extra_context = extra_context or {}

        if request.method=='POST':
            myForm=self.form(request.POST)


        object=MyCar.objects.get(pk=int(form_url))
        extra_context['customFieldsetList'] = renderCustomFieldsetList(request,object,myForm)


        return super(MyCarAdmin, self).change_view(request, form_url,
                                                  extra_context=extra_context)



    # def response_change(self, request, obj):
    #     return Response({'form':'dddddddddd'})

    # def save_form(self, request, form, change):
    #     # custom stuff here
    #     obj.save()

admin.site.register(MyCar,MyCarAdmin)
admin.site.site_header = 'My Administration'



from models import Shop
admin.site.register(Shop)
