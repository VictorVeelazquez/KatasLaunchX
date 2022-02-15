class Rocket:

    def __init__(self) -> None:
        self.destination = None
        self.fuel = 0

    def config(self, file):
        try:
            with open(file) as f:
                lines = f.readlines()
                self.destination = lines[0].strip()
                self.fuel = int(lines[1].strip())
        except FileNotFoundError:
            print("El archivo no existe")

    def water_left(self, astronauts, water, days):
        daily_usage = astronauts * 11
        total_usage = daily_usage * days
        total_water = water - total_usage
        if total_water < 0:
            raise RuntimeError(f"No hay suficiente agua para los {astronauts} astronautas en {days} días")
        return f"El agua que queda después de {days} días es de {total_water} litros"

    def __str__(self) -> str:
        if self.destination:
            return "Cohete con destino a {} con {} kg de combustible".format(self.destination, self.fuel)
        else:
            return "Cohete no cofigurado"


def main():
    rocket = Rocket()
    rocket.config("config.txt")
    print(rocket.water_left(5, 100, 2))
    print(rocket)

if __name__ == "__main__":
    main()