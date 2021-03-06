"""recomendador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from companies.views_api import CompanyViewSet, BranchCompanyViewSet, BranchServicesViewSet, QualificationViewSet
from persons import views
from persons.views import HomeView
from services.views_api import CategoryViewSet, ServiceViewSet
from persons.views_api import UserViewSet, CityViewSet, ClientViewSet, SupervisorViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register("cities", CityViewSet)
router.register("clients", ClientViewSet)
router.register("categories", CategoryViewSet)
router.register("services", ServiceViewSet)
router.register("supervisors", SupervisorViewSet)
router.register("companies", CompanyViewSet)
router.register("branchcompanies", BranchCompanyViewSet)
router.register("branchservices", BranchServicesViewSet)
router.register("qualifications", QualificationViewSet)


urlpatterns = [

    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    #path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
