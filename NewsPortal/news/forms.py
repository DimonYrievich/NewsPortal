
# ВАЛИДАЦИЯ(проверка) ДАННЫХ В ФОРМАХ

from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        # В fields можно указать особенное значение ’__all__’, которое означает, что Django сам должен пойти в модель и взять все поля,
        # кроме первичного ключа (его мы не должны редактировать). Но вместо этого мы сами перечислим все поля.
        fields = [
            'title',
            'text',
            'categories',
            'author',
            'article_or_news',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 3:
            raise ValidationError({
                "text": "Текст публикации не может быть менее 3 символов."
            })

        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Заголовок публикации не может быть идентичен тексту публикации."
            )

        return cleaned_data
        # Мы переопределили метод clean и реализовали в нём проверку.

