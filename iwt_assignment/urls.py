
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('check',views.check,name="check"),
    path('add',views.add,name="add"),
    path('addbooks',views.addbooks,name="addbooks"),
    path('display',views.display,name="display"),
    path('status_student',views.status_student,name="status_student"),
    path('requested_books',views.requested_books,name="requested_books"),
    path('requesting_book',views.requesting_book,name="requesting_book"),
    path('update/<int:id>',views.update,name="update"),
    path('decline/<int:id>',views.decline,name="decline"),
    path('admin/', admin.site.urls),
]
