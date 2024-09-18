from .models import Menu
def get_custom_context(request):
    menu = []
    for i in Menu.objects.all():
        menu.append({'name':i.name , 'url_name': i.url_name})
    
    return {'menu':menu}

