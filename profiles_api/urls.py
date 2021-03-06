from django.contrib import admin
from django.urls import path,include
from profiles_api import views


urlpatterns=[
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('auth/trial/',views.trial),
    path('list-add-farmer/',views.feedFarmerInfo),
    path('list-all-farmer/',views.listAllFarmer),
    path('list-id-farmer/<str:pk>/',views.listIdFarmer),
    path('list-one-farmer/<str:pk>/',views.listOneFarmer),
    path('list-add-field/',views.listAddField),
    path('list-field-farmer/<str:pk>/',views.listFieldFarmer),
    path('list-fields-farmer/',views.listFieldsFarmer),
    path('list-id-field-farmer/<str:pk>/',views.listIdFieldFarmer),
    path('list-add-product/',views.listAddProduct),
    path('list-all-product/',views.listAllProduct),
    path('list-one-product/<str:pk>/',views.listProductFarmer),
    path('list-crop-name/<str:pk>/',views.listCrop),
    path('list-add-crop-name/',views.listCropName),
    path('list-all-crop-name/',views.listAllCropName),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('list-all-questions/',views.listquestionsheet),
    path('list-add-question/',views.listaddquestion),
    path('list-some-questions/',views.listquestionsheetwise),
    path('list-past-condition/',views.listpastcondition),
    path('list-add-phase/',views.listaddphase),
    path('list-all-phase/',views.listallphase),
    path('list-some-phase/<str:pk>/',views.listsomephase),
    path('list-date/',views.getcurrentdate),
    path('list-all-linker/',views.listphasequestionlinker),
    path('list-add-linker/',views.listaddlinker),
    path('list-some-linker/<str:pk>/',views.listsomelinker),
    path('list-add-alert/',views.listaddalert),
    path('list-all-alert/',views.listallalert),
    path('list-day-alert/<str:pk>/',views.listdayalert),



 ]
