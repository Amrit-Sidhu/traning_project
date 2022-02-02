from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="home1"),
    path('goto_login', views.goto_login, name="goto_login"),
    path('goto_cattle', views.goto_cattle, name="goto_cattle"),
    path('goto_feed', views.goto_feed, name="goto_feed"),
    path('goto_milking_methods', views.goto_milking_methods, name="goto_milking_methods"),
    path('goto_economic', views.goto_economic, name="goto_economic"),
    path('goto_housing', views.goto_housing, name="goto_housing"),
    path('goto_milk_divided', views.goto_milk_divided, name="goto_milk_divided"),
    path('goto_milk_divided_40', views.goto_milk_divided_40, name="goto_milk_divided_40"),
    path('goto_milk_divided_20', views.goto_milk_divided_20, name="goto_milk_divided_20"),
    path('goto_one_animal_milk/', views.goto_one_animal_milk, name="goto_one_animal_milk"),

    path('goto_registration', views.goto_regitration, name="goto_registration"),
    path('goto_home', views.goto_home, name="goto_home"),
    path('goto_animal_record', views.goto_animal_record, name="goto_animal_record"),
    path('goto_animal_detail', views.goto_animal_detail, name="goto_animal_detail"),
    path('goto_animal_added', views.goto_animal_added, name="goto_animal_added"),
    path('goto_more_detail/', views.goto_more_detail, name="goto_more_detail"),
    path('goto_milk_record/', views.goto_milk_record, name="milk"),
    path('goto_ask/', views.goto_ask, name="ask"),
    path('goto_que_added/', views.goto_que_added, name="ask"),
    path('goto_ans_added/', views.goto_ans_added, name="ask"),
    path('goto_update/', views.goto_update, name="goto_update"),

    path('update_animal_data_in_database/', views.update_animal_data_in_database, name="update_animal_data_in_database"),
    path('goto_deworming_added/', views.goto_deworming_added, name="goto_deworming_added"),
    path('show_answer/', views.show_answer, name="show_answer"),
    path('add_vaccination_in_database/', views.add_vaccination_in_database, name="add_vaccination_in_database"),
    path('add_deworming_in_database/', views.add_deworming_in_database, name="add_deworming_in_database"),

    path('showuser/', views.show_username, name="goto_registration"),
    path('add_farmer_data_in_database/', views.add_farmer_data_in_database, name="add_farmer_data_in_database"),
    path('add_animal_data_in_database/', views.add_animal_data_in_database, name="add_animal_data_in_database"),
    path('add_milk_data_in_database/', views.add_milk_data_in_database, name="add_milk_data_in_database"),
    path('add_que_in_database/', views.add_que_in_database, name="add_que_in_database"),
    path('add_ans_in_database/', views.add_ans_in_database, name="add_que_in_database"),
    path('re/', views.goto_re, name="add_que_in_database"),

]

