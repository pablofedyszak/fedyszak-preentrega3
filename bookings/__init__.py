{% extends "base.html" %}
{% block content %}
  <h2>Crear evento</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
  </form>
{% endblock %}
