from django.db import models

class All_col(models.Model):
    all_name=models.CharField(max_length=255)

    def __str__(self) :
        return self.all_name

class Pro_Gallery(models.Model):
    image = models.ImageField(upload_to='portfolio/', default='./portfolio-1.jpg')
    image_name=models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self) :
        return self.image_name
    class Meta:
        verbose_name_plural='pictures'


class Project(models.Model):
    pro_name=models.CharField(max_length=255)
    description = models.TextField()
    size=models.CharField(max_length=300)
    main_image=models.ImageField(upload_to='portfolio/', default='./portfolio-1.jpg')
    gallery = models.ManyToManyField(Pro_Gallery)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    collection_name=models.ForeignKey(All_col,on_delete=models.DO_NOTHING,null=True, blank=True)

    def __str__(self) :
        return self.pro_name


class Collection(models.Model):
    col_name=models.ForeignKey(All_col,on_delete=models.DO_NOTHING,null=True, blank=True)
    col_main_name=models.CharField(max_length=255,null=True, blank=True)
    col_desc = models.TextField()
    material=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    main_image=models.ImageField(upload_to='portfolio/', default='./portfolio-1.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # projects=models.ManyToManyField(Project)

    def __str__(self) :
        return self.col_main_name


# Create your models here.
