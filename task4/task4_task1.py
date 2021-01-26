import sys
hours, salary, bonus = map(sys.argv, float)
print(f"Зарабатная плата: {hours*salary + bonus}")


