def ft_water_remainder() -> None:
    days: int = int(input("Days since last watering:"))
    if days <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
