"""{{ cookiecutter.plugin_description }}"""

from plugin import InvenTreePlugin
{% if cookiecutter.plugin_mixins.mixin_list %}
from plugin.mixins import {{ cookiecutter.plugin_mixins.mixin_list | map('trim') | join(', ') }}
{% endif %}
from . import PLUGIN_VERSION
{% if cookiecutter.plugin_mixins.mixin_list %}
class {{ cookiecutter.plugin_name }}({{ cookiecutter.plugin_mixins.mixin_list | map('trim') | join(', ') }}, InvenTreePlugin):
{% else %}
class {{ cookiecutter.plugin_name }}(InvenTreePlugin):
    {% endif -%}
    """{{ cookiecutter.plugin_description }}"""

    # Plugin metadata
    TITLE = "{{ cookiecutter.plugin_title }}"
    NAME = "{{ cookiecutter.plugin_name }}"
    SLUG = "{{ cookiecutter.plugin_slug }}"

    AUTHOR = "{{ cookiecutter.author_name }}"
    DESCRIPTION = "{{ cookiecutter.plugin_description }}"
    VERSION = PLUGIN_VERSION

    {%- if cookiecutter.plugin_mixins.mixin_list %}

    {%- if "SettingsMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Plugin settings
    SETTINGS = {
        # Define your plugin settings here...
    }
    {% endif -%}

    {% endif -%}