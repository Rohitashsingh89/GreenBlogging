from .models import Images, Owner

def images(request):
    try:
        images_obj = Images.objects.first()
        return {'images': images_obj}
    except Images.DoesNotExist:
        return {}

def owner(request):
    try:
        owner_obj = Owner.objects.first()
        return { 'owner' : owner_obj }
    except Owner.DoesNotExist:
        return {}