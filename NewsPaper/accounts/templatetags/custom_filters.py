from django import template

register = template.Library()

BAD_WORD = ['блин']

@register.filter(name = 'censor')
def censor(text):
    for word in BAD_WORD:
        if word in text:
            text = text.replace(word[1:len(word)], f'{len(word) * "*"}')
            return text
        else:
            return text

