from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'inventory_app' 

urlpatterns = [
   path('', views.Home.as_view(), name="home"),
   path('accounts/profile/', views.Home.as_view(), name="home"),
   path('logout/', views.log_out, name="logout"),   
   path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
   path('ingredient/', views.IngredientView.as_view(), name="ingredient"),
   path('ingredient/create', views.IngredientCreate.as_view(), name="add_ingredient"),
   path('ingredient/update/<int:pk>', views.IngredientUpdate.as_view(), name="update_ingredient"),
   path('ingredient/delete/<int:pk>', views.IngredientDelete.as_view(), name="delete_ingredient"),
   path('menu/', views.MenuItemView.as_view(), name="menu"),
   path('menu/create', views.MenuItemCreate.as_view(), name="add_menu"),
   path('menu/update/<int:pk>', views.MenuItemUpdate.as_view(), name="update_menu"),
   path('menu/delete/<int:pk>', views.MenuItemDelete.as_view(), name="delete_menu"),
   path('require/create', views.RecipeRequirement.as_view(), name="add_requirement"),
   path('purchases/', views.PurchasesView.as_view(), name="purchases"),
   path('purchases/create', views.PurchasesCreate.as_view(), name="add_purchase"),
   path('sales/', views.SalesView.as_view(), name="sales"),
]