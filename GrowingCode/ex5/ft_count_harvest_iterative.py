def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    i: int = 1
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
