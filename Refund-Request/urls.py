from django.contrib import admin
from django.urls import path
from . import views
from customer.views import customer_about, login_view, get_login_status, logout_view
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='customer/homepage.html'), name='customer-homepage'),
    path('about/', customer_about, name='customer_about'),
    path('signup/', views.customer_signup, name='customer_signup'),
    path('login/', login_view, name='login'),
    path('get-login-status/', get_login_status, name='get_login_status'),
    path('logout/', logout_view, name='logout'),
    path('services/', views.services, name='services'),
    path('destinations/', views.destinations, name='destinations'),
    path('explore-cruises/', views.explore_cruises, name='explore_cruises-customer'),
    path('book-now/', views.book_now, name='book_now'),

    # Profile urls
     
    path('profile/', views.profile, name='profile'),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('loyalty/details/', views.loyalty_program_details, name='loyalty_program'),
    path('loyalty/purchase/', views.purchase_membership, name='purchase_loyalty'),
    path('feedback/', views.feedback_view, name='feedback_reviews'),
    path('itinerary/', views.itinerary, name='itinerary'),
    path('special-request/', views.special_request_view, name='special-request'),

    # Booking urls

    path('start/', views.start_booking, name='start_booking'), 
    path('select-cruise/', views.select_cruise, name='select-cruise'),
    path('select-cruise/<int:booking_id>/', views.select_cruise, name='select-cruise'),
    path('add-passenger/<int:booking_id>/', views.add_passenger, name='add_passenger'),
    path('resume-booking/<int:booking_id>/', views.resume_booking, name='resume-booking'),
    path('select-services/<int:booking_id>/', views.select_services, name='select-services'),
    path('other-details/<int:booking_id>/', views.save_other_details, name='save-other-details'),
    path('booking-summary/<int:booking_id>/', views.booking_summary, name='booking_summary'),
    path('payments/<int:booking_id>/', views.payment_page, name='payment_page'),
    path('payment/success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('ticket/', views.ticket_info, name='ticket'),
    path('download_ticket/', views.download_ticket_pdf, name='download_ticket'),
    path('generate-invoice/<int:booking_id>/', views.generate_invoice, name='generate_invoice'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('notifications/', views.notifications, name='customer-notifications'),
    path('mark-all-notifications-read/', views.mark_all_notifications_read, name='mark-all-notifications-read'),
    path('refund-request/', views.refund_request, name='refund_request'),
]

