import matplotlib.pyplot as plt
import numpy as np

activities = ['Сон', 'Работа', 'Учеба', 'Спорт', 'Отдых', 'Еда']
time_spent = [8, 8, 4, 1, 2, 1]

fig, ax = plt.subplots(figsize=(15, 6))

bar_width = 0.35
index = np.arange(len(activities))

for i, (activity, time) in enumerate(zip(activities, time_spent)):
    bar1 = ax.bar(index[i] - bar_width/2, time, bar_width, color='skyblue', label=activity)
    ax.text(bar1[0].get_x() + bar1[0].get_width() / 2., bar1[0].get_height(), '%d' % int(bar1[0].get_height()),
            ha='center', va='bottom', color='red')
    
    if i < len(activities) - 1:
        bar2 = ax.bar(index[i] + bar_width/2, time_spent[i+1], bar_width, color='lightgreen', label=activities[i+1])
        ax.text(bar2[0].get_x() + bar2[0].get_width() / 2., bar2[0].get_height(), '%d' % int(bar2[0].get_height()),
                ha='center', va='bottom', color='red')

ax.set_xlabel('Деятельность')
ax.set_ylabel('Время, часы')
ax.set_title('Выделение времени на различные занятия в течение дня')

ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
