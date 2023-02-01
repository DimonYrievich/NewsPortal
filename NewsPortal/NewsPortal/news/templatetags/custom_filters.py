                            # СОЗДАЕМ СОБСТВЕННЫЕ ФИЛЬТРЫ #

from django import template

register = template.Library()

CENSOR_WORDS = ['против','сериал','боец']

@register.filter()
def censor(value):
    """
    text: текст к которому нужно применить фильтр
    """
    for word in CENSOR_WORDS:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value






#from django import template
#register = template.Library()
# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
#@register.filter()
#def censor(value):
#   badwords = ('против', 'сериал', 'боец')
#   value = value.split()
#   for index, word in enumerate(value):
#      if any(badword in word for badword in badwords):
#         value[index] = word[0] + "".join('*' if c.isalpha() else c for c in word)
#         value[index] = value[index].replace('*', '', 1)
#   return " ".join(value)