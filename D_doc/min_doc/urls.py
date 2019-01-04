from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.Signup.as_view(), name="signup"),
	path('login/', views.Login.as_view(), name="login"),
	path('book-list/(?P<uuid>[a-z\d+]{32})/$', views.BookList.as_view(), name="book_list"),
	path('book-view/(?P<book_uuid>[a-z\d+]{32})/$', views.BookOverView.as_view(), name="book_view"),
	path('book-editor/(?P<book_uuid>[a-z\d+]{32})/$', views.BookEditor.as_view(), name="book_editor"),
]
