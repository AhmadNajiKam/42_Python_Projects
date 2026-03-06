def ft_plant_age() -> None:
    days: int = int(input("Enter plant age in days: "))
    if days <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
