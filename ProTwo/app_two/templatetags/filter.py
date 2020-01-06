from django import template

register = template.Library()


@register.filter
def cut(value, args):
    args = args.lower()
    return value.lower().replace(args, 'vishnu')
