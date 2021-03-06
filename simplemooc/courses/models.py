from django.db import models

# Create your models here.

# gerenciador
class CourseManager(models.Manager):

    # faz busca no nome e na descrição
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |  
            models.Q(description__icontains=query)
        ) 

class Course(models.Model):
    
    name = models.CharField('Nome', max_length=100)

    slug = models.SlugField('Atalho')

    description = models.TextField('Descrição Simples', blank=True)
    # blank=True, campo não obrigatorio

    about = models.TextField('Sobre o Curso', blank=True)

    start_date = models.DateField(
        'Data de Início', null=True, blank=True
        # null=True, a nivel de banco de dados, pode ser nulo.
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    update_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )
    
    objects = CourseManager()

    # returna o nome dos cursos na pagina admin
    def __str__(self):
        return self.name       

    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug':self.slug})
# return (namespace courses com valor details, \
#         argumentos não nomeáveis, argumentos nomeáveis {dicionario})

    # mudar o nome da class Course para Curso ou Cursos
    # na pagina do admin
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos' 
        ordering = ['name'] # organiza por ordem alfabética
