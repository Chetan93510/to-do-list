from .models import To_do

def todo(request):
    return {
        'alltodo': To_do.objects.all()
    }


# def system(request):
#     return {
#         'name': 'Juneco'
#         'phone'
#     }