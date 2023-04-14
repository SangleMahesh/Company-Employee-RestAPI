# Company-Employee-RestAPI
Company-Employees API Using DRF

This API can perform CRUD operations on company and its employees.
You can fetch companies , add new companies , add employees to the company.
Also there is a custom route created to build relationship between company and employees which gets details of all the employees of a particular company.
Class based views are used.

In urls there is default router which provide browsable API for adding, fetching the data.
The serializers in REST framework work very similarly to Django's Form and ModelForm classes. 

Serializer class gives a powerful, generic way to control the output of your responses,
Even there is an option to restrict the access for unauthenticated users and provide read-only resources.

Add this attribute in settings.py file.

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.

urlpatterns = [

    path('api-auth/', include('rest_framework.urls'))
]
