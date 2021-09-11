from django.db import models
from tinymce import models as tinymce_models

from .logic.post_image_filepath import post_image_path


class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    preview_text = models.TextField()
    main_text = tinymce_models.HTMLField()
    image = models.ImageField(upload_to=post_image_path, blank=True)

    def __str__(self):
        return self.title
