with open("pails.in", "r") as file:
    x, y, m = map(int, file.readline().split())

print("Pail sizes: X =", x, "Y =", y, "Max size M =", m)


max_y_fill_count = m // y


possible_milk_amounts = []

for num_y_pours in range(max_y_fill_count + 1):
    remaining_capacity = m - (num_y_pours * y)
    
    max_x_fill_count = remaining_capacity // x
    
    total_milk = (num_y_pours * y) + (max_x_fill_count * x)
    possible_milk_amounts.append(total_milk)

max_x_fill_count_only = m // x
total_milk_using_only_x = max_x_fill_count_only * x
possible_milk_amounts.append(total_milk_using_only_x)

max_milk_amount = max(possible_milk_amounts)

with open("pails.out", "w") as file:
    file.write(str(max_milk_amount) + "\n")

print("Maximum milk amount:", max_milk_amount)
