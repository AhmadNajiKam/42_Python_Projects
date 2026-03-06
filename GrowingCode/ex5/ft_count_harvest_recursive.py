def ft_count_harvest_recursive(day: int = 1, total_days: int | None = None):
    if total_days is None:
        total_days: int = int(input("Days until harvest: "))
    if day > total_days:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(day + 1, total_days)
