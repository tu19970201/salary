workTime = int(input('請輸入本月工作時數：'))
salary = 0
wage = 160
wage1 = wage * 1.25
wage2 = wage * 1.5
if workTime <= 60:
    salary = workTime * wage
    print('本月的薪資為：', salary)
elif workTime <= 80:
    salary = 60 * wage + ( workTime - 60) * wage1
    print('本月的薪資為：', int(salary))
else:
    salary = 60 * wage + 20 * wage1 + ( workTime - 80) * wage2
    print('本月的薪資為：', int(salary))