
from django.db import models
from ckeditor.fields import RichTextField 

#Modelo de la tabla
class TaskModel(models.Model):
    
    class Meta:
        verbose_name_plural = 'Tasks_lists'
        verbose_name = 'Task_list'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=254, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    estado = models.CharField(max_length=50, default="Incompleto")
    cuerpo = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    



    