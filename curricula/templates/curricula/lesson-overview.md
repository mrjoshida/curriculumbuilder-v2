# Overview

{{ lesson.description|safe }}
{% if lesson.vocab.count > 0 %}## Vocabulary

{% for word in lesson.vocab.all %}* **{{ word.word }}** - {{ word.detailDef|safe }}
{% endfor %}{% endif %}
{% if lesson.blocks.count > 0 %}## Introduced Code

{% for block in lesson.blocks.all %}* [{{ block.title }}]({{ block.get_published_url }})
{% endfor %}{% endif %}
{% if lesson.resources.count > 0 %}## Resources

{% for resource in lesson.resources.all %}{% if resource.student %}* {{ resource.formatted_md|safe }}{% endif %}
{% endfor %}{% endif %}