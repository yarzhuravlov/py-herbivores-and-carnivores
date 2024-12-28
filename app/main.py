from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def decrease_health(self, decrease_on: int) -> None:
        self.health -= decrease_on
        self.check_is_alive()

    def check_is_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                + f"Health: {self.health}, "
                + f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    DEFAULT_HEALTH_DECREASE = 50

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            return

        if animal.hidden:
            return

        animal.decrease_health(self.DEFAULT_HEALTH_DECREASE)
