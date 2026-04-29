from django.contrib import admin
from django.urls import path
from planner import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main),              # 메인 페이지
    path('fukuoka/', views.fukuoka),       # 후쿠오카 페이지
    path('italy/',views.italy),     # 이탈리아 페이지
    path('api/trip/', views.get_trip),
    path('api/trip/update/', views.update_trip),
]
