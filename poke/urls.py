from django.urls import path
from poke import views

urlpatterns = [
		path('', views.index),
        path('reg_validate', views.reg_validate),
		path('login_validate', views.login_validate),
		path('logout', views.logout),
		path('pokes', views.pokes),
        path('allpokes', views.allpokes)
]