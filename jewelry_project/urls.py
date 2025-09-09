from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.models import User

# --- Only enable this in DEBUG (development) ---
def create_admin_now(request):
    if not settings.DEBUG:
        return HttpResponse("❌ This endpoint is disabled in production.", status=403)

    try:
        user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "3638siddhisvjc@gmail.com",
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )

        # Always reset password
        user.set_password("siddhi123")
        user.save()

        if created:
            return HttpResponse("✅ Admin user created!<br>Username: admin<br>Password: siddhi123")
        else:
            return HttpResponse("✅ Admin user password updated!<br>Username: admin<br>Password: siddhi123")

    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
]

# Only add the admin creation route in DEBUG mode
if settings.DEBUG:
    urlpatterns.append(path("create-admin-now/", create_admin_now))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
