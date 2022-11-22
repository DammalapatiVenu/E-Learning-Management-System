from django.contrib import admin
from django.urls import path, include
from . import views, user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404',views.PAGE_NOT_FOUND, name='404'),
    path('base', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('courses', views.SIGNLE_COURSE, name='single_course'),
    path('course/<slug:slug>', views.COURSE_DETAILS, name='course_details'),
    path('search', views.SEARCH_COURSE, name='search_course'),
    path('search_my_course', views.SEARCH_MY_COURSE, name="search_my_course"),
    path('contact', views.CONTACT_US, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),
    path('accounts/register', user_login.REGISTER, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('account/profile/update',user_login.PROFILE_UNPDATE, name='profile_update'),
    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('my-course',views.MY_COURSE, name='my_course'),
    path('product/filter-data',views.filter_data,name='filter-data'),
    path('course/watch-course/<slug:slug>', views.WATCH_COURSE, name='watch_course'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
