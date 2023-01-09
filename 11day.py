from typing import List

rdata = '''Monkey 0:
  Starting items: 63, 57
  Operation: new = old * 11
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 2

Monkey 1:
  Starting items: 82, 66, 87, 78, 77, 92, 83
  Operation: new = old + 1
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 0

Monkey 2:
  Starting items: 97, 53, 53, 85, 58, 54
  Operation: new = old * 7
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 3:
  Starting items: 50
  Operation: new = old + 3
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 4:
  Starting items: 64, 69, 52, 65, 73
  Operation: new = old + 6
  Test: divisible by 17
    If true: throw to monkey 3
    If false: throw to monkey 7

Monkey 5:
  Starting items: 57, 91, 65
  Operation: new = old + 5
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 6:
  Starting items: 67, 91, 84, 78, 60, 69, 99, 83
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 7:
  Starting items: 58, 78, 69, 65
  Operation: new = old + 7
  Test: divisible by 19
    If true: throw to monkey 5
    If false: throw to monkey 1
'''.split('\n')

data = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''.split('\n')

from dataclasses import dataclass
import re
import math

@dataclass
class Monkey:
    name: str
    items: List[int]
    division: int
    true_monkey: str
    false_monkey: str
    operation_list: List[str]
    thrown: int = 0

    def throw(self, monkey_list, lcm):
        while self.items:
            item = self.items.pop(0)
            item = self.operation(item)
            item = self.divide(item,lcm)

            if item % self.division == 0:
                for monkey in monkey_list:
                    if monkey.name == self.true_monkey:
                        monkey.items.append(item)
                        break
            else:
                for monkey in monkey_list:
                    if monkey.name == self.false_monkey:
                        monkey.items.append(item)
                        break
            self.thrown += 1

    def operation(self, item):
        if self.operation_list[1] == "old":
            var = item
        else:
            var = self.operation_list[1]
        var = int(var)

        if self.operation_list[0] == '+':
            item += var
        elif self.operation_list[0] == '*':
            item *= var
        return item

    def divide(self, item, lcm):
        return item %lcm


monkey_list = []
lcm = []
while rdata:
    line = rdata.pop(0)
    name = line.split(':')[0].lower()

    start_items_line = rdata.pop(0)
    items = [int(i) for i in re.findall(r"[0-9]+", start_items_line)]

    operation_line = rdata.pop(0)
    operation = operation_line.split(" ")[-2:]

    division_line = rdata.pop(0)
    division = int(re.findall(r"[0-9]+", division_line)[0])
    lcm.append(division)

    true_line = rdata.pop(0)
    true_monkey = " ".join(true_line.split(' ')[-2:])

    false_line = rdata.pop(0)
    false_monkey = " ".join(false_line.split(' ')[-2:])

    monkey_list.append(
        Monkey(name=name, items=items, operation_list=operation, thrown=0, division=division, true_monkey=true_monkey,
               false_monkey=false_monkey))

    rdata.pop(0)  # get rid of new line

print(monkey_list)
lcm = math.lcm(*list(set(lcm)))

rounds = 10_000
for _ in range(rounds):
    for monkey in monkey_list:
        monkey.throw(monkey_list, lcm)

print(monkey_list)
lst = sorted([ monkey.thrown for monkey in monkey_list],reverse=True)
print(lst[0]*lst[1])