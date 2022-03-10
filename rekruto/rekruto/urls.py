from django.urls import path, include

import greeting


urlpatterns = [
    path("", include('greeting.urls'))
]
