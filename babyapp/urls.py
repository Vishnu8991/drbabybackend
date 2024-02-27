from django.urls import path
from .views import *

urlpatterns=[
    path('authtoken/',Registeruser.as_view()),
    path('authlogin/',LoginView.as_view(),name='logins'),
    path('logoutt/',logoutview.as_view),
#create child
    path('childcreate/', ChildListCreateView.as_view(), name='child-list'),
#modify child
    path('children/<int:pk>/', ChildDetailView.as_view(), name='child-detail'),

    

    path('vax-names/', VaxNameListCreateView.as_view(), name='vax-name-list'),
    path('vax-names/<int:pk>/', VaxNameDetailView.as_view(), name='vax-name-detail'),

    # path('vax-programscreate/', VaxProgramView.as_view(), name='vax-program-list'),
    # path('vax-programs-modify/<int:pk>/', VaxProgramDelete_Update.as_view(), name='vax-program-detail'),

    path('vax-cycles/', VaxCycleAPIView.as_view(), name='vax-cycle-list'),
    path('vax-cycles/<int:pk>/', VaxCycleDelete_Update.as_view(), name='vax-cycle-detail'),

    path('vaxes/', VaxAPIView.as_view(), name='vax-list'),
    path('vaxes/<int:pk>/', VaxDelete_Update.as_view(), name='vax-detail'),
    
    path('hospitalupdate/<pk>',HospitalDetailAPIView.as_view()),


     path('childcreate/<int:child_id>/vaccination-dates/',vaccination_dates_view, name='vaccination_dates'),
    #  path('vaccination/<int:child_id>/', VaccinationProgramView.as_view(), name='vaccination_programs'),
    
    # path('vaccination-dates/<int:child_id>/', VaccinationDatesAPIView.as_view(), name='vaccination-dates'),
   
   

    
    path('send_mail_date/',send_mail_to_parent),
    #  path('send-mail/', SendMailToParentView.as_view(), name='send-mail'),
    

    #chat
    # path('chat/', ChatbotAPI.as_view(), name='chat'),
    path('chatbot/', ChatbotAPI.as_view(), name='chatbot_api'),

#add vaccine names

    path('vaccinenames/',VaccineListView.as_view(),name='vaccines'),


#set vaccine programs

    path('vaccine_programs/', VaccineProgramsListCreateView.as_view(), name='vaccine-programs-list-create'),
    path('vaccine_programs_update/<int:pk>/', VaccineProgramsDetailView.as_view(), name='vaccine-programs-detail'),
    #hospital add
    path('hospitals/', HospitalsAPIView.as_view(), name='hospitals-list'),
    # new vaccine book
    path('vaccinebook/',VaccineBookingList.as_view(),name='book'),
    #see all vaccine program with status
    path('vaccinestatus/', VaccineProgramsAPI.as_view(), name='vaccine-programs'),
    #set vaccine status to programs
    path('setvaccinestatus/<int:pk>/', VaccineProgramsAPI.as_view(), name='vaccine-program-detail'),
    path('child_vaccine_status/<str:child_name>/', ChildVaccineStatusAPI.as_view(), name='child_vaccine_status'),
     


]



