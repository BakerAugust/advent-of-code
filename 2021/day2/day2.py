# Day 2 prompt: https://adventofcode.com/2021/day/2

from typing import List


def load_input():
    with open("2021/day2/input.txt", "r") as f:
        input = f.readlines()
    return [(x.strip("\n")) for x in input]

def parse_course(input: List[str]):
    depth = []
    forward = []
    for instruction in input:
        direction, distance = instruction.split(' ')
        match direction:
            case 'forward':
                forward.append(int(distance))
            case 'down':
                depth.append(int(distance))
            case 'up':
                depth.append(-int(distance))
    return depth, forward

def parse_course_with_aim(input: List[str]):
    depth = []
    forward = []
    aim = []
    for instruction in input:
        direction, distance = instruction.split(' ')
        match direction:
            case 'forward':
                forward.append(int(distance))
                depth.append(sum(aim)*int(distance))
            case 'down':
                aim.append(int(distance))
            case 'up':
                aim.append(-int(distance))
    return depth, forward, aim

if __name__ == '__main__':
    input = load_input()
    depth, forward = parse_course(input)
    print(f'Part one solution: {sum(depth)*sum(forward)}')

    depth, forward, aim = parse_course_with_aim(input)
    print(f'Part two solution: {sum(depth)*sum(forward)}')

