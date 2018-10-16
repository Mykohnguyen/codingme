from django.conf.urls import url
 
from django.conf import settings

from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^logging_in$',views.logging_in),
    url(r'^invalid$',views.invalid),
    url(r'^user$',views.user_page),
    url(r'^user/info$',views.user_info),
    url(r'^user/edit$',views.user_edit),
    url(r'^registering$',views.registering),
    url(r'^user/user_info_edit$',views.user_info_edit),
    url(r'^ranking_page$',views.ranking_page),
    url(r'user/classroom$',views.classroom),
    url(r'^mall$',views.mall),
    url(r'^mall/(?P<category>\w+)$',views.mall_weapon),
    url(r'^adding$',views.adding),
    url(r'^addingq$',views.addingq),
    url(r'^addinga$',views.addinga),
    url(r'^classroom/(?P<language>\w+)/(?P<difficulty>\w+)/(?P<number>\d+)$',views.classroom_questions),
    url(r'^check_answers$',views.check_answers),
    url(r'^classroom/end_of_quiz$',views.end_of_quiz),
    url(r'^ending$',views.ending),
    url(r'^buy/(?P<category>\w+)/(?P<id>\d+)$',views.buy_item),
    url(r'^charge$',views.charge),
    url(r'^favorite/(?P<category>\w+)$',views.favorite_item),
    url(r'^user/(?P<userid>\d+)$',views.view_user),
    url(r'^logout$',views.logout)
]
