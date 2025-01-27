date_create = input("Введите дату создания заметки в формате ДД ММ ГГГГ:")
if int(date_create[0:2:1]) > 31 : print("День не может быть больше 31")
if int(date_create[3:5:1]) > 12 : print("Месяц не может быть больше 12")
date_issue = input("Введите дату окончания срока исполнения в формате ДД ММ ГГГГ:")
date_create_output = date_create[0:2:1] + "." + date_create[3:5:1]
date_issue_output = date_issue[0:2:1] + "." + date_issue[3:5:1]
if int(date_create[0:2:1]) > 31 : print("День не может быть больше 31")
print("Дата создания:", date_create_output)
print(f"Дата окончания срока исполнения: {date_issue_output}")

# Я тут попытался использовать оператор if. Но пока не понимаю как заставить пользователя
# вводить данные заново в случае ошибки