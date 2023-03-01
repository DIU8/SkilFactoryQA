num_tickets = int(input("Введите количество билетов: "))
total_cost = 0

for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i+1}: "))
    if age < 18:
        ticket_cost = 0
    elif age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390
    total_cost += ticket_cost

if num_tickets > 3:
    total_cost *= 0.9

print(f"Общая стоимость билетов: {total_cost} руб.")


num_tickets = int(input("Введите количество билетов: "))
total_cost = 0

for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i+1}: "))
    if age < 18:
        ticket_cost = 0
    elif age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390
    total_cost += ticket_cost

if num_tickets > 3:
    total_cost *= 0.9

print(f"Общая стоимость билетов: {total_cost} руб.")
