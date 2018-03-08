from django.contrib.admin.sites import site
from django.apps import apps


from django import template

register = template.Library()




@register.inclusion_tag("admin/partial/menu.html", takes_context=True)
def admin_menu(context):
    adminSite=site


    app_list=adminSite.get_app_list(context['request'])


    # import pdb ; pdb.set_trace()
    admin_list={}
    if app_list :
        for one_app in app_list:
                one_admin_list={'label':one_app['app_label'],'url':one_app['app_url'],'name':one_app['name'],'icon':'fa fa-cogs','sub':{}}



                for model in one_app['models']:
                    one_admin_list['sub'][model['object_name']]={ 'name':model['name'],
                             'admin_url': model['admin_url'] if model['admin_url'] else '',
                             'add_url':model['add_url'] if model['add_url'] else '',
                         }



                admin_list[one_admin_list['name']]=one_admin_list

    #____my_car
    from my_car.models import admin_menu as my_car_admin_menu
    admin_list['My_Car']=my_car_admin_menu()


    return {'app_list':admin_list}
