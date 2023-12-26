from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Cakes API",
        default_version='v1',
        description="This is an API for cakes. ",
        contact=openapi.Contact(email="lokez21@gmail.com"),
        license=openapi.License(name="Lokesh's License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_all_cakes/', views.cakes_list, name='list_all'),
    path('select_cake/<int:id>', views.select_cake, name='select_cake'),
    path('add_cake/', views.AddCake.as_view(), name='add_cake'),
    path('delete_cake/<int:id>', views.delete_cake, name='delete_cake'),
    path('update_cake/<int:id>', views.update_cake, name='update_cake'),
    path('<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]