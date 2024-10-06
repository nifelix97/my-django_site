from .models import Notification

def unread_notifications_count(request):
    if request.user.is_authenticated and request.user.is_staff:
        return {
            'unread_notifications_count': Notification.objects.filter(is_read=False).count()
        }
    return {}