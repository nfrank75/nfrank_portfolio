from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    pays = models.CharField(max_length=250, default='', blank=True)
    message = models.TextField()
    sujet = models.CharField(max_length=250, default='', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField('Name', max_length=250)
    title = models.CharField('Title', max_length=250)
    description = models.TextField('Description')
    created_at = models.DateTimeField(auto_now_add=True)
    project_date = models.DateTimeField()
    project_completed = models.BooleanField(default=True)
    language_of_prog = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="project/", blank=False, null=False)
    demo = models.URLField()
    github = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Project, self).save(*args, **kwargs)

    def slug_generate(self):
        pass


class Service(models.Model):
    name = models.CharField('Name', max_length=250)
    title = models.CharField('Title', max_length=250, blank=False, null=False)
    description = models.TextField('Description')
    created_at = models.DateTimeField(auto_now_add=True)
    language_of_prog = models.CharField(max_length=250)
    language_of_prog = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to="service/", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    name = models.CharField('Name', max_length=250)
    title = models.CharField('Title', max_length=250)
    description = models.TextField('Description')
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    company_name = models.CharField(max_length=250)
    country= models.CharField(max_length=250)
    number_of_experiences =  models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

class Education(models.Model):

    TYPE_OF_EDUCATION = (
        ('general', 'GENERAL'),
        ('technique', 'TECHNIQUE')
    )

    name = models.CharField('Name', max_length=250)
    title = models.CharField('Title', max_length=250)
    type_of_education = models.CharField( 'Type of Education', max_length=250,  choices=TYPE_OF_EDUCATION, default='general')
    description = models.TextField('Description')
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    school_name = models.CharField(max_length=250)
    country= models.CharField(max_length=250)
    rank =  models.CharField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
class Competence(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.FileField(upload_to='competence/', blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CV(models.Model):
    cv = models.FilePathField( blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
