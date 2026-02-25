from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HabitLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('done', models.BooleanField(default=False)),
                ('minutes', models.IntegerField(default=0)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='tracker.habit')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('habit', 'date')},
            },
        ),
    ]
