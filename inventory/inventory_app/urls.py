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
   path('inventory_app/ingredient/create', views.IngredientCreate.as_view(), name="add_ingredient"),
   path('inventory_app/ingredient/update/<int:pk>', views.IngredientUpdate.as_view(), name="update_ingredient"),
   path('inventory_app/ingredient/delete/<int:pk>', views.IngredientDelete.as_view(), name="delete_ingredient"),
   path('inventory_app/menu/', views.MenuItemView.as_view(), name="menu"),
   path('inventory_app/menu/create', views.MenuItemCreate.as_view(), name="add_menu"),
   path('inventory_app/menu/update/<int:pk>', views.MenuItemUpdate.as_view(), name="update_menu"),
   path('inventory_app/menu/delete/<int:pk>', views.MenuItemDelete.as_view(), name="delete_menu"),
   path('inventory_app/require/create', views.RecipeRequirement.as_view(), name="add_requirement"),
   path('inventory_app/purchases/', views.PurchasesView.as_view(), name="purchases"),
   path('inventory_app/purchases/create', views.PurchasesCreate.as_view(), name="add_purchase"),
]