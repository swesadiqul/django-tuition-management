from django.urls import path
from .views import (search, filter, likepost,
addcomment,addphoto, commentdelete,
contact, postview, postcreate, subview, postviewapi,
ContactView, PostDetailView, PostCreateView,
PostListView, PostEditView, PostDeleteView)
from .forms import ContactFormTwo
from .pdf import contact_pdf
app_name = 'tuition'



# create urls
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', search, name='search'),
    path('filter/', filter, name='filter'),
    path('pdf/', contact_pdf, name='pdf'),
    path('likepost/<int:id>/', likepost, name='likepost'),
    path('addphoto/<int:id>/', addphoto, name='addphoto'),
    path('commentdelete/<int:id>/', commentdelete, name='commentdelete'),
    path('postviewapi/', postviewapi, name='postviewapi'),
    path('addcomment/', addcomment, name='addcomment'),
    # path('contacts/', ContactView.as_view(form_class=ContactFormTwo, template_name='contact2.html'), name='contacts'),
    # path('contact/', contact, name='contact'),
    # path('postview/', postview, name='postview'),
    path('postview/', postview, name='postview'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('create/', postcreate, name='create'),
    # path('create/', PostCreateView.as_view(), name='create'),
]
