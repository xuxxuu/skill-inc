from typing import Protocol
from hpbars import TreeHPBar


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

        self.axe_types = ["bronze", "iron", "steel"]
        self.current_axe = self.axe_types[0]
        self.axe_efficiencies = {"bronze": 1, "iron": 2, "steel": 3}

        self.tree_types = ["oak", "willow", "maple"]
        self.trees = {
            "oak": {"hp": 10, "exp": 5},
            "willow": {"hp": 20, "exp": 10},
            "maple": {"hp": 30, "exp": 15},
        }

        self.current_tree = list(self.trees.keys())[0]
        self.tree_hp = self.trees[self.current_tree]["hp"]  # current HP of the tree
        self.axe_efficiency = self.axe_efficiencies[self.current_axe]  # current efficiency of the axe

    def execute(self, tree_bar: TreeHPBar) -> None:
        self.tree_hp -= self.axe_efficiency
        print("You swing your axe at the tree!")

        if self.tree_hp <= 0:
            print(f"You have successfully chopped down the {self.current_tree} tree!")
            self.gain_exp(self.current_tree)
            print(f"Gained experience! {self.current_tree} gave {self.trees[self.current_tree]['exp']} EXP.")
            self.tree_hp = self.trees[self.current_tree]["hp"]
            print("New tree has grown!")

        print(f"Current tree HP: {self.tree_hp}")

    def gain_exp(self, tree_type: str) -> None:
        self.experience += self.trees[tree_type]["exp"]


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
