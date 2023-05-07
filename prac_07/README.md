# Practical 07 - Classes 2
## 1. Programming Languages
- Add another language to the file
- Add another field to `ProgrammingLanguage` class
- Update codes

## 2.More Guitars
- Define Guitar class
- Redefining comparison operators
- Ask the user to enter their new guitars
- Read and write csv
- Test Guitar class

## 3.Project Management Program
- Load projects \
> read file\
> Initialize object and add to list
- Save projects \
> write object list to file
- Display projects \
> show two groups, sorted by priority\
> \__lt__(self, other)
- Filter projects by date
> list.sort()
- Add new project
> get user input and convert to a project object
- Update project
> modify certain project

```python
import datetime

date_string = input("Date (d/m/yyyy): ") # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))
```

**Initialized Data**
```
Name	Start Date	Priority	Cost Estimate	Completion Percentage
Build Car Park	12/09/2021	2	600000.0	95
Mow Lawn	31/10/2022	3	3.0	0
Organise Pantry	20/07/2022	1	25.0	55
Record Music Video	01/12/2022	9	250000.0	0
Read 7 Habits Book	13/12/2021	6	99.0	100
```