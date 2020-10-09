import os
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def screen_cleaner(flag):
    if flag:
        os.system('cls' if os.name == 'nt' else 'clear')


def render_template(context=None, template="default.jinja2", cls=True):
    """Prints rendered template with context data

    Args:
        context (dict, optional): [data for rendering template]. Defaults to None.
        template (str, optional): [template filename]. Defaults to "default.jinja2".
        cls (bool, optional): [Clear screen flas. Shows if screan should be 
        cleaned before showing this view]. Defaults to True.
    """
    if not context:
        context = {}
    screen_cleaner(cls)
    template = env.get_template(template)
    print(template.render(**context))
