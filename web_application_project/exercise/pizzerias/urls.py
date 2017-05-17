from django.conf.urls import url

from . import views

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),

    # Show all pizzas
    url(r'^pizzas/$', views.pizzas, name='pizzas'),
    # Detailed for single pizza
    url(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza')
]