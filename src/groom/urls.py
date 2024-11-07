from django.urls import path
from .views import (
    groomHome,
    guests,
    seeGuests,
    answerInvite,
    reserveGift,
    addEscort
)

urlpatterns = [
    path("", groomHome, name="home"),
    path('guests/list/', guests, name='guests'),
    path('guests/see/', seeGuests, name='see_guests'),
    path('guests/answer_invite/', answerInvite, name='answer_invite'),
    path('guests/reserve/<uid>', reserveGift, name='reserve_gift'),
    path('guests/add_escort/', addEscort, name='add_escort'),
]
