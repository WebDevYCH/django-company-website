from django.urls import path
from . import views
app_name = "blogs"
urlpatterns = [
    path('blogs/', views.IndexView.as_view(), name='blogs'),

    path('archives/', views.ArchivesView.as_view(), name='archives'),
    path('blog/<int:pk>/<slug:slug>/', views.article, name='post'),

    path('categories/', views.Categories.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),

    path('tags/', views.TagsView.as_view(), name='tags'),
    path('tag/<int:pk>/', views.TagListView.as_view(), name='tag_list'),

    path('download/', views.file_test, name='download'),
    # path('courses/', views.CoursesView.as_view(), name='courses'),
    # path('course/<int:pk>', views.course, name='course'),
    # path('course/article/<int:pk>', views.course_article, name='course_article'),
]