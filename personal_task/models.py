from django.db.models import Case, When, Value ,Count
from django.db import models
from accounts.models import CustomUser
# from datetime import date , timedelta


class MyTaskModel(models.Model):
    PRIORITY_CHOICE = (
        ('high','HIGH'),
        ('medium', 'MEDIUM'),
        ('low' , 'LOW'),
    )
    title = models.CharField( max_length=150)
    body = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_in = models.DateTimeField( auto_now_add=True)
    priority = models.CharField( max_length=50, choices=PRIORITY_CHOICE, default='medium')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta :
        ordering = [
            Case(When(priority='high', then=Value(0)), When(priority='medium', then=Value(1)), default=Value(2)),
        ]

    @property
    def priority_display(self):
        return dict(self.PRIORITY_CHOICE)[self.priority]
    
    def get_total_tasks_by_priority(self):
        """
        Calculates and returns the dictionary of total tasks by priority.
        Caches the result for efficiency if accessed multiple times.
        """

        total_tasks_by_priority = {}
        if not hasattr(self, '_total_tasks_by_priority'):
            queryset = MyTaskModel.objects.values('priority').annotate(count=Count('id'))
            for item in queryset:
                total_tasks_by_priority[item['priority']] = item['count']
            self._total_tasks_by_priority = total_tasks_by_priority

        return self._total_tasks_by_priority

       
    