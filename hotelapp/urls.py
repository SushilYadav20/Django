from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name="Home"),
    path('layout/',views.layout,),
    path('register/',views.register, name="Registration"),
    path('login/',views.login, name="Login"),
    path('base/',views.base),
    path('blog/',views.blog , name="Create blog"),
    path('list_blog/',views.list_blog, name="List blog"),
    path('Cards/',views.Cards,name="Cards"),
    path('student/',views.student,name="Student"),
    path('update_blog/<int:id>/',views.update_blog,name="update_blog"),
    path('delete_blog/<int:id>/',views.delete_blog,name="delete_blog"),
    path('todo/',views.todo,name="todo"),
    path('show_todo/',views.show_todo,name="show_todo"),
    path('update_todo/<int:id>/',views.update_todo,name="update_todo"),
    path('delete_todo/<int:id>/',views.delete_todo,name="delete_todo")
]