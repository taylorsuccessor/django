from django import template

register = template.Library()


@register.inclusion_tag("admin/partial/header.html", takes_context=True)
def admin_header(context):

    return {
            'username':context['request'].user,
            'languageList':{'en':'English','ar':'Arabic'},
            'notificationList':notificationList()
            }




def notificationList():
    carNotificationList=[
        {
            'title':'My Title',
            'link':'mylink',
            'img':'myImg',
            'date':'2018-02-20',
            'description':'my description here',

        },
        {
            'title':'second',
            'link':'mylink',
            'img':'myImg',
            'date':'2018-02-20',
            'description':'my description here',

        },
    ]


    return {'carNotificationList':carNotificationList}

