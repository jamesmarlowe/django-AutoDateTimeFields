django-AutoDateTimeFields
=========================

django date time fields that don't break like auto_now and auto_now_add do

Installation
------------
install the python package with pip

```
pip install django-AutoDateTimeFields
```
or install manually

```
python setup.py install
```

add autodatetimefields to installed apps setting:

```python
INSTALLED_APPS = (
    ...
    'autodatetimefields'
)
```

Usage
-----

```python
from autodatetimefields.models import AutoNewDateTimeField, AutoDateTimeField

class ModelName(models.Model):
    date_created = AutoNewDateTimeField(blank=True)
    date_updated = AutoDateTimeField(blank=True)
```

Contributors
------------
James Marlowe https://github.com/jamesmarlowe
