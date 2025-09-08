# Add to jewelry_project/urls.py
from django.http import HttpResponse
from django.contrib.auth.models import User

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

# Add to your urlpatterns:
urlpatterns = [
    # ... your existing patterns ...
    path('create-admin-now/', create_admin_now),
]