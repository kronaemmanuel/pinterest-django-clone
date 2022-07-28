from django import template

register = template.Library()


@register.filter(name='add_classes')
def add_classes(value, classes):
    """
    Add provided classes to form field
    :param value: form field
    :param classes: string of classes separated by ' '
    :return: edited field
    """
    css_classes = value.field.widget.attrs.get('class', '')

    # get previous classes
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []

    # add new classes to the list
    classes = classes.split(' ')
    for css_class in classes:
        if css_class not in css_classes:
            css_classes.append(css_class)

    # return with all the classes
    return value.as_widget(attrs={'class': ' '.join(css_classes)})
