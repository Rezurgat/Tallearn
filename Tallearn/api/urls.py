from django.urls import path
from api.blog_n_events_api.views_bne_api import (
    PostListApiView,
    PostDetailApiView,
    CategoryPostListApiView,
    EventListApiView,
    EventDetailApiView,
)
from api.about_api.views_about_api import (
    AboutApiView,
    ContactApiView,
    FeedbackCreateApiView,
)
from api.courses_api.views_courses_api import (
    CategoryCourseListApiView,
    CourseListApiView,
    CourseDetailApiView,
    CommentCreateApiView,
)


urlpatterns = [
    path('api/v1/categorypostlist', CategoryPostListApiView.as_view()),
    path('api/v1/postlist/<int:category>', PostListApiView.as_view()),
    path('api/v1/postdetail/<int:pk>', PostDetailApiView.as_view()),
    path('api/v1/eventlist', EventListApiView.as_view()),
    path('api/v1/eventdetail/<int:pk>', EventDetailApiView.as_view()),

    path('api/v1/aboutlist', AboutApiView.as_view()),
    path('api/v1/contactlist', ContactApiView.as_view()),
    path('api/v1/feedback', FeedbackCreateApiView.as_view()),

    path('api/v1/categorycourselist', CategoryCourseListApiView.as_view()),
    path('api/v1/courselist/<int:category>', CourseListApiView.as_view()),
    path('api/v1/coursedetail/<int:pk>', CourseDetailApiView.as_view()),
    path('api/v1/comment', CommentCreateApiView.as_view())
]