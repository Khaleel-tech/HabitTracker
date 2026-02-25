import json
from datetime import timedelta

from django.db.models import Avg, Sum
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import HabitForm, HabitLogForm
from .models import Habit, HabitLog


def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HabitForm()

    return render(request, 'tracker/add_habit.html', {'form': form})


def log_habit(request):
    if request.method == 'POST':
        form = HabitLogForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            HabitLog.objects.update_or_create(
                habit=cleaned['habit'],
                date=cleaned['date'],
                defaults={
                    'minutes': cleaned['minutes'],
                    'done': cleaned['done'],
                },
            )
            return redirect('dashboard')
    else:
        form = HabitLogForm(initial={'date': timezone.localdate()})

    return render(request, 'tracker/log_habit.html', {'form': form})


def _streak_for_habit(habit: Habit, today):
    logs_by_date = {
        log.date: log.done
        for log in HabitLog.objects.filter(habit=habit, done=True)
    }

    streak = 0
    day_cursor = today
    while logs_by_date.get(day_cursor, False):
        streak += 1
        day_cursor -= timedelta(days=1)

    return streak


def dashboard(request):
    today = timezone.localdate()
    start_date = today - timedelta(days=6)

    habits = Habit.objects.all()
    date_labels = [start_date + timedelta(days=i) for i in range(7)]

    habit_summaries = []
    chart_data = []

    for habit in habits:
        last_week_logs = HabitLog.objects.filter(habit=habit, date__gte=start_date, date__lte=today)

        totals = last_week_logs.aggregate(
            total_minutes=Sum('minutes'),
            avg_minutes=Avg('minutes'),
            done_days=Sum('done'),
        )

        streak = _streak_for_habit(habit, today)

        minutes_by_date = {
            label: 0 for label in date_labels
        }
        for log in last_week_logs:
            minutes_by_date[log.date] = log.minutes

        habit_summaries.append(
            {
                'habit': habit,
                'total_minutes': totals['total_minutes'] or 0,
                'average_minutes': round(totals['avg_minutes'] or 0, 2),
                'done_days': totals['done_days'] or 0,
                'streak': streak,
            }
        )

        chart_data.append(
            {
                'label': habit.name,
                'data': [minutes_by_date[day] for day in date_labels],
            }
        )

    context = {
        'habit_summaries': habit_summaries,
        'chart_labels_json': json.dumps([day.strftime('%Y-%m-%d') for day in date_labels]),
        'chart_data_json': json.dumps(chart_data),
    }
    return render(request, 'tracker/dashboard.html', context)
