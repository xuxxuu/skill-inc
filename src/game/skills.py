from typing import Protocol


class Skill(Protocol):
    name: str
    level: int
    experience: int

    def execute(self) -> None: ...
    def gain_exp(self) -> None: ...


class WoodcuttingService:
    def __init__(self) -> None:
        self.name = "woodcutting"
        self.level = 1
        self.experience = 0

    def execute(self) -> None:
        print("You struck the tree!")

    def gain_exp(self) -> None: ...


class FishingService:
    def __init__(self) -> None:
        self.name = "fishing"
        self.level = 1
        self.experience = 0

    def execute(self) -> None:
        print("You cast out your line!")

    def gain_exp(self) -> None: ...


class SkillHandler:
    def __init__(self) -> None:
        self.services = {
            "woodcutting": WoodcuttingService(),
            "fishing": FishingService(),
        }

    def execute_skill(self, tag: str):
        skill: Skill = self.services[tag]
        skill.execute()
