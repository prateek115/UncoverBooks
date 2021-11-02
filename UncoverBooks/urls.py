from django.contrib import admin
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.index, name ="Home Page"),
    path('about', views.about, name="aboutUs"),
    path('Contact', views.contact_us, name="ContactUs"),
    path('search', views.search, name="search"),
    path('product/<int:myid>', views.productView, name="productview"),
    path('<int:myid>', views.productView, name="productview"),
    path('tracker', views.tracker, name="tracker"),
    path('checkout', views.checkout, name="checkout"),
    path('cart', views.cart, name="cart"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    # path('novel', views.novel, name="novel"),
    # path('textbook', views.textbook, name="textbook"),
    # path('narrative', views.narrative, name="narrative"),
    # path('nonfiction', views.nonfiction, name="nonfiction"),
    # path('mystery', views.mystery, name="mystery"),
    # path('poetry', views.poetry, name="poetry"),
    # path('horror', views.horror, name="horror"),
    # path('romance', views.romance, name="romance"),
    # path('humor', views.humor, name="humor"),
    # path('fantasy', views.fantasy, name="fantasy"),
    # path('crime', views.crime, name="crime"),
    # path('fiction', views.fiction, name="fiction"),
    path('handelSignUp', views.handelSignUp, name="handelSignUp"),
    path('handelLogin', views.handelLogin, name="handelLogin"),
    path('handelLogout', views.handelLogout, name="handelLogout"),
    path('postcomment', views.postcomment, name="postcomment"),
    path('tocsv', views.exportcsv, name="tocsv"),
    #path('view/<str:gen>', views.genre_display, name="genre_display"),
    path('<str:gen>', views.genre_display, name="genre_display"),
]
