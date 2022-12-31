from django import template
from django.template.loader import render_to_string
from ..models import Menu

register = template.Library()


def render_menu(menu: Menu) -> str:
    """Renders menu in html format"""
    return render_to_string('menus/main.html', {'menus': menu.submenus.all()})


@register.simple_tag
def draw_menu(menu_name: str, doesnotexist_ok: bool = False) -> str:
    """Tag, that renders menu in html page with given page name. If nothing found, raises exception
    :param menu_name: name of menu to display
    :param doesnotexist_ok: when menu with given name doesn't exist:
        True: returns empty string
        False: raises exception
    :return: string with HTML code inside
    """

    # Searching for menu
    try:
        menu = Menu.objects.get(name=menu_name)

    # No menu found?
    except Menu.DoesNotExist:

        # Empty tag allowed?
        if doesnotexist_ok:

            # Return empty string
            return ''

        # Raise exception
        raise Menu.DoesNotExist("Template trying to get menu, that doesn't exist")

    # Menu found. Render html list
    return render_menu(menu)
