import re
from day12_utils import memoize
from typing import List


def generate_all_possibilities(length: int) -> List[str]:
    components = [".", "#"]
    possibilities: [str] = components[:]
    for i in range(length - 1):
        possibilities = [x + y for x in possibilities for y in components]
    return possibilities


def yield_all_possibilities_recursive(length: int) -> List[str]:
    if length == 1:
        yield "."
        yield "#"
    else:
        for i in yield_all_possibilities_recursive(length - 1):
            yield i + "."
            yield i + "#"


def apply_possibity_to_spring_statuses(
    possibility: str, spring_states: str, question_positions: List[str]
) -> str:
    result = list(spring_states)
    for i in range(len(question_positions)):
        result[question_positions[i]] = possibility[i]
    return "".join(result)


def is_row_correct(spring_statuses: str, damage_records: List[int]) -> bool:
    damaged_springs = re.split(r"\.+", spring_statuses)
    damages_springs_counts = [l for x in damaged_springs if (l := len(x)) and l > 0]
    return damages_springs_counts == damage_records


def get_correct_possibilities_of_row(row: str) -> int:
    return get_correct_possibilities(row.split(" "))


def get_correct_possibilities_of_expanded_row(row: str) -> (List[str], List[str]):
    [springs_statuses, damage_records_string] = row.split(" ")
    correct_possibilities_right = get_correct_possibilities(
        (f"{springs_statuses}?", damage_records_string)
    )
    # correct_possibilities_right = [
    #     x for x in correct_possibilities_right if x[0] == "." or x[-1] == "."
    # ]
    correct_possibilities_left = get_correct_possibilities(
        (f"?{springs_statuses}", damage_records_string)
    )
    correct_possibilities_left = [
        x for x in correct_possibilities_left if x[0] == "." or x[-1] == "."
    ]

    correct_possibilities = get_correct_possibilities(
        [springs_statuses, damage_records_string]
    )

    return (
        correct_possibilities_left
        if len(correct_possibilities_left) > len(correct_possibilities_right)
        else correct_possibilities_right,
        correct_possibilities,
    )


def get_correct_possibilities(status_damage_pair: List[str]) -> List[str]:
    [springs_statuses, damage_records_string] = status_damage_pair
    damage_records = [int(x) for x in damage_records_string.split(",")]
    question_positions = [
        x for x in range(len(springs_statuses)) if springs_statuses[x] == "?"
    ]
    generate_func = yield_all_possibilities_recursive
    possiblities = generate_func(len(question_positions))
    correct_possibilities = [
        p
        for x in possiblities
        if (
            p := apply_possibity_to_spring_statuses(
                x, springs_statuses, question_positions
            )
        )
        and is_row_correct(p, damage_records)
    ]
    return correct_possibilities


def run_step_1(input: str) -> int:
    lines = input.split("\n")
    counts = [len(get_correct_possibilities_of_row(x)) for x in lines]
    return sum(counts)


def expand(input: str) -> List[str]:
    lines = input.split("\n")
    splitted_lines = [line.split(" ") for line in lines]
    expanded_lines = [
        f"{'?'.join([l[0]] * 5)} {','.join([l[1]] * 5)}" for l in splitted_lines
    ]
    return expanded_lines


def run_step_2(input: str) -> int:
    lines = input.split("\n")
    counts = [
        (len(p[0]) ** 4) * len(p[1])
        for x in lines
        if (p := get_correct_possibilities_of_expanded_row(x))
    ]
    return sum(counts)
