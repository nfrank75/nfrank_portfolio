from django.contrib import admin
from .models import Contact, Project, Service, Education, Job, Competence, CV

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'pays', 'sujet')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')
    list_editable = ('email','phone', 'pays', 'sujet')

    
    ordering = ('-updated_at',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'created_at', 'project_date', 'project_completed', 'language_of_prog', 'image', 'demo', 'github')
    search_fields = ('name', 'title')
    list_filter = ('name', 'title')
    list_editable = ('title', 'description', 'language_of_prog')

    ordering = ('-updated_at',)



class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'created_at', 'language_of_prog', 'image')
    search_fields = ('name', 'title', 'description', 'created_at', 'language_of_prog')
    list_filter = ('name', 'title')
    list_editable = ('title', 'description', 'language_of_prog')
    
    ordering = ('-updated_at',)



class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'started_at', 'ended_at', 'company_name', 'country', 'number_of_experiences')
    search_fields = ('name', 'title', 'description', 'started_at', 'ended_at', 'company_name', 'country', 'number_of_experiences')
    list_filter = ('name', 'title')
    list_editable = ('title', 'description')
    
    ordering = ('-updated_at',)


class Educationdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'type_of_education', 'description', 'started_at', 'ended_at', 'school_name', 'country', 'rank')
    search_fields = ('name', 'title', 'type_of_education',)
    list_filter = ('name', 'title')
    list_editable = ('title', 'type_of_education')
    
    ordering = ('-updated_at',)

class Competenceadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('ttle',)
    list_editable = ('description',)
    
    ordering = ('-updated_at',)

class CVadmin(admin.ModelAdmin):
    list_display = ('cv',)




admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Education, Educationdmin)
admin.site.register(Competence, Competenceadmin)
admin.site.register(CV, CVadmin)