from django.db import models


class Habit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    done = models.BooleanField(default=False)
    minutes = models.IntegerField(default=0)

    class Meta:
        unique_together = ('habit', 'date')
        ordering = ['-date']

    def __str__(self) -> str:
        return f'{self.habit.name} - {self.date}'
