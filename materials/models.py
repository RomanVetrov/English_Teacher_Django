from django.db import models


class Material(models.Model):
    LEVEL_A1 = "A1"
    LEVEL_A2 = "A2"
    LEVEL_B1 = "B1"
    LEVEL_B2 = "B2"
    LEVEL_C1 = "C1"
    LEVEL_C2 = "C2"
    LEVEL_CHOICES = [
        (LEVEL_A1, "A1"),
        (LEVEL_A2, "A2"),
        (LEVEL_B1, "B1"),
        (LEVEL_B2, "B2"),
        (LEVEL_C1, "C1"),
        (LEVEL_C2, "C2"),
    ]

    TYPE_VIDEO = "video"
    TYPE_PDF = "pdf"
    TYPE_AUDIO = "audio"
    TYPE_OTHER = "other"
    FILE_TYPE_CHOICES = [
        (TYPE_VIDEO, "Видео"),
        (TYPE_PDF, "PDF"),
        (TYPE_AUDIO, "Аудио"),
        (TYPE_OTHER, "Другое"),
    ]

    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True)
    level = models.CharField("Уровень", max_length=2, choices=LEVEL_CHOICES)
    file_type = models.CharField("Тип файла", max_length=10, choices=FILE_TYPE_CHOICES, default=TYPE_OTHER)
    file = models.FileField("Файл", upload_to="materials/")
    is_published = models.BooleanField("Опубликовано", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "материал"
        verbose_name_plural = "материалы"

    def __str__(self):
        return self.title

# Create your models here.
