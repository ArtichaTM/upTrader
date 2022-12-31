from django.db import models
from django.template.loader import render_to_string


class Menu(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    submenus = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='parent_to')

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    def as_list(self) -> str:
        return render_to_string('menus/element.html', context={'menu': self})


class Relationship(models.Model):
    parent = models.ForeignKey(Menu, related_name='parent', on_delete=models.CASCADE)
    subordinate = models.ForeignKey(Menu, related_name='subordinate', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.parent.name} -> {self.subordinate.name}"

    def __repr__(self) -> str:
        return str(self)
