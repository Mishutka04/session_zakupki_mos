from django.urls import path
from session import views

app_name = 'session'

urlpatterns = [
     path('session/', views.QuotationSessionAPIView.as_view(), name='get_session'),
     path('tender/',  views.TenderDataView.as_view(), name='tender_data'),
     path('violations/',  views.ViolationsAPIView.as_view(), name='violations'),
]