from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.models import User

# Add this function for admin creation
def create_admin_now(request):
    try:
        # Create or update admin user
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': '3638siddhisvjc@gmail.com',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True
            }
        )
        
        # Always set the password
        user.set_password('siddhi123')
        user.save()
        
        if created:
            return HttpResponse('✅ Admin user created successfully!<br>Username: admin<br>Password: siddhi123')
        else:
            return HttpResponse('✅ Admin user password updated!<br>Username: admin<br>Password: siddhi123')
            
    except Exception as e:
        return HttpResponse(f'❌ Error: {e}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('create-admin-now/', create_admin_now),  # Add this line for admin creation
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)