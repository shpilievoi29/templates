import products as products

from contacts.views import home, contact_list, contact_detail
from second.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact_list, name="contact_list"),
    path("contacts/<slug:contact_slug>", contact_detail, name="contact_detail"),
]
