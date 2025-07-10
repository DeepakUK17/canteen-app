from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RoleBasedLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('customer-signup/', views.customer_signup, name='customer_signup'),
    path('shop-owner-signup/', views.shop_owner_signup, name='shop_owner_signup'),
    path('login/', RoleBasedLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Customer URLs
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('place-order/', views.place_order, name='place_order'),
    path('customer-orders/', views.customer_orders, name='customer_orders'),
    path('receipt/<int:order_id>/', views.generate_receipt, name='generate_receipt'),
    
    # Shop Owner URLs
    path('shop-owner-dashboard/', views.shop_owner_dashboard, name='shop_owner_dashboard'),
    path('manage-orders/', views.manage_orders, name='manage_orders'),
    path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('manage-food-items/', views.manage_food_items, name='manage_food_items'),
    path('add-food-item/', views.add_food_item, name='add_food_item'),
    path('edit-food-item/<int:food_id>/', views.edit_food_item, name='edit_food_item'),
]
