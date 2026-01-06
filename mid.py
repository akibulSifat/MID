# ---------- Objective Function ----------
def f(x):
    return -(x - 50) ** 2 + 2500


# ---------- Hill Climbing ----------
def hill_climbing(start, step):
    curr = start
    current_value = f(curr)

    best = curr
    best_value = current_value

    while True:

        right_value = curr + step
        right_value = f(right_value)

        left_x = curr - step
        left_value = f(left_x)

        if right_value > left_value:
            best_neighbor_x = right_value
            best_neighbor_value = right_value
        else:
            best_neighbor_x = left_x
            best_neighbor_value = left_value

        if best_neighbor_value <= current_value:
            break

        curr = best_neighbor_x
        current_value = best_neighbor_value

        if current_value > best_value:
            best = curr
            best_value = current_value

    return best, best_value


with open("/student\Desktop\MID\mid.py") as file_handle:
    start = int(file_handle.readline().strip())
    step = int(file_handle.readline().strip())

solution, value = hill_climbing(start, step)

print("Optimal CPU Load:", solution)
print("Maximum Efficiency:", value)
