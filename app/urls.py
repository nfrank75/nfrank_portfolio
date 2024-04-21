from django.urls import path
from .views import (home, about, blog, contact, service,
                    project, job, education, cv)


urlpatterns = [
    path('', home, name='home'),
    path('nfrank-portfolio-about', about, name='nfrank-portfolio-about'),
    path('nfrank-portfolio-blog', blog, name='nfrank-portfolio-blog'),
    path('nfrank-portfolio-contact', contact, name='nfrank-portfolio-contact'),
    path('nfrank-portfolio-service', service, name='nfrank-portfolio-service'),
    path('nfrank-portfolio-project', project, name='nfrank-portfolio-project'),
    path('nfrank-portfolio-job', job, name='nfrank-portfolio-job'),
    path('nfrank-portfolio-education', education, name='nfrank-portfolio-education'),
    path('nfrank-portfolio-cv', cv, name='nfrank-portfolio-cv'),
] 