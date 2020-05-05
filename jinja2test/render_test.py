"""
version jinja2 2.11.1

"""



from jinja2 import Environment, FileSystemLoader, Template

import os

env = Environment(
    autoescape=True,
    # trim_blocks=True,
    # lstrip_blocks=True,
    keep_trailing_newline=False,
    loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
)

def test1():
    temp = env.get_template('show.html')
    print(temp.render(name='jack', string='<>').replace(' ', '》'))
    print('++++++')
    temp = env.from_string('<b>{% if a %} \nb\n{% endif %}</b>\n ')
    print(temp.render(a=1).replace(' ', '》'))
    print('++++++')

def test2():
    temp = env.from_string(
"""
<ul class="sitemap">
  {% for item in sitemap recursive %}
  <li>{{ item.name }}
    {% if item.children %}
        <ul class="submenu">
        {{ loop(item.children) }}
        </ul>
    {% endif %}
  </li>
  {% endfor %}
</ul>
""" )
    print(temp.render(sitemap=[{'href': 'root', 'name': 'good', 'children': [{'href': 'pa', 'name': 'a'}, {'href': 'pb', 'name': 'b'}]}]))


def call_test():
    temp = env.from_string(
"""
{% macro render_dialog(title, class='dialog') -%}
    <div class="{{ class }}">
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}

{% call render_dialog('Hello World') %}
    This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}
"""
    )
    print(temp.render())


def join_test():
    temp = env.from_string(
"""
{% set pipe = joiner("|") %}
{% if categories %} {{ pipe() }}
    Categories: {{ categories|join(", ") }}
{% endif %}
{% if author %} {{ pipe() }}
    Author: {{ author() }}
{% endif %}
{% if can_edit %} {{ pipe() }}
    <a href="?action=edit">Edit</a>
{% endif %}
"""
    )
    print(temp.render(categories=['A', 'B'], author=lambda : 'jack', can_edit=1))

# test1()
# test2()
# call_test()
join_test()