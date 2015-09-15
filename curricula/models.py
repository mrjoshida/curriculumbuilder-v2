from django.db import models
from mezzanine.pages.models import Page, RichText, Orderable
from mezzanine.core.fields import RichTextField
from standards.models import Standard, GradeBand
from lessons.models import Lesson

"""
Curriculum

"""
class Curriculum(Page, RichText):
  gradeband = models.ForeignKey(GradeBand)

  class Meta:
      verbose_name_plural = "curricula"

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return '/curriculum/' + self.slug + '/'

  @property
  def units(self):
    return Unit.objects.filter(parent=self)

"""
Curricular Unit

"""
class Unit(Page, RichText):
  curriculum = models.ForeignKey(Curriculum, blank=True, null=True)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return self.curriculum.get_absolute_url() + self.slug + '/'

  @property
  def number(self):
    return self._order + 1

  @property
  def lessons(self):
    return Lesson.objects.filter(parent=self)

  def save(self, *args, **kwargs):
    try:
      self.curriculum = self.parent.curriculum
    except:
      return
    super(Unit, self).save(*args, **kwargs)

"""
Intermediary Model for lessons
Deprecated

class UnitLesson(Orderable):
  unit = models.ForeignKey(Unit)
  lesson = models.ForeignKey(Lesson)

  def __unicode__(self):
    return self.lesson.title

  def url(self):
    return self.lesson.get_absolute_url()
"""