test_input_1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

test_input_1_possibilities = {
    "???.### 1,1,3": (1, 1),
    ".??..??...?##. 1,1,3": (4, 16384),
    "?#?#?#?#?#?#?#? 1,3,1,6": (1, 1),
    "????.#...#... 4,1,1": (1, 16),
    "????.######..#####. 1,6,5": (4, 2500),
    "?###???????? 3,2,1": (10, 606250),
}

puzzle_input = """????#??##.????? 1,5,2
..#???.??.. 4,1
??.??????? 1,4,1
#??.????#??. 2,1,2,1
?#????##..#????? 8,1,1,1
.????.?.??. 2,1,1
??#???#?????.? 5,1,1
??#????.?#..??# 4,1,1,3
???????.#??? 4,1,1,1
???.??#????#????? 3,1
..??#..??? 1,1
???????#??#.??????? 3,2,2,1,2
?????.#???#??? 5,3,1,1
??????#??#?.?### 2,1,2,1,4
???.?#.???##.????#.? 3,1,5,1,2,1
.??#.?.??..?? 1,1,2,1
??????#?##? 4,4
?????.???????## 3,1,6
???.???????#??. 2,2
?#?.?????????#?#?#?. 1,15
.?.?????????#?? 1,4,4
??????###?#?. 1,1,1,6
????##??#??#?? 6,4,1
?????.??#?#??#?###? 1,13
#?#??#????##..??.. 8,2,1
#??#???#????##??#? 4,4,5,1
.????.?.???##?????? 3,10
#?#??????????##??? 1,2,1,2,4,1
..?.?.??.. 1,1
.#??.?.???? 2,1,1
.???##..??? 5,2
.##?????.?.??#?##?# 7,1,1,1,4
????????????.??#??# 1,7,1,1,1,1
.???#???#??? 3,1
..##?.#???..?? 2,4,1
..??.#?#???????#???? 1,1,2,9
.?#??.???????# 1,1,3,1
???..#??.##. 3,2,2
?#?#???##..#??.?#??? 3,2,2,3
.????#?#??#???#?##.. 9,4
???#???#???????#? 2,2,1,3
????#?##.#? 5,1
??#?????#??# 3,6
?#?#?..?#?..??? 4,1,2
???#????????#.? 3,7
#..##?..???.?? 1,3,1,1
????????????#?.. 1,6,3
???????????#??.#. 8,2,1,1
????#?????#...?#?# 1,1,2,4,4
#??#?#??..? 7,1
????..##?.?# 4,3,2
?##?????.???#?###.? 6,8
????..??#? 1,2,4
#??#??.?#?..?.?? 1,3,3,1,1
??????..?##? 4,3
?#??#?.??##???.#?#? 1,3,3,1,1,1
??##??????.???.#?? 1,4,2,3,1,1
.????????# 2,5
??.?????##?.?? 2,8,1
?.?????#????????#??? 1,9,1,3,1
.#?.?#.?..??? 2,1,1,1
#?????#?#.? 3,3
??.??#?????### 1,11
.##???????.???# 2,1,1,1,1
?##??.?.##?????#?.#? 5,8,2
#?.??.??.?#?####.??? 1,2,2,7,3
..???.??.??#? 1,2,4
?#??.?#????.??. 3,5
????????#..?.?? 4,2,1
?.??????#. 1,7
?#???..#?? 4,1
??#?#.???????. 3,3
??????.??##??. 3,4
.##?.???????????.??? 3,4,1,1,1,1
???.????#?#?.??? 4,1
.??#?.?????#?????? 3,1,2,1,1
??##???.?? 5,1,1
??#?#????????#?? 1,6,5
?#??#?#???.???..## 1,3,1,3,2
???###.?.???.?###? 5,1,1,4
????.???#??????.?? 2,8,1,1
????.#?##??? 2,4
.#.#??#?#?.?? 1,1,4,1
##???#?.??# 3,2,2
??#?.?.???#??? 2,7
????#??.#??#?? 5,1,3
?.????..???? 1,1,3
###??#.?#?#??? 3,2,5
?.#??#?#?.#?..? 1,1,4,1,1
????#??#??? 1,2,4
????.???.??#??. 1,1,1,1,1
.??????##????? 1,6
.?????..???##?..?. 3,4
.???????##.?? 7,1
?..#???????#????? 1,1,1,1,7
.###???.???? 5,1
???.????.#?##. 1,1,3,4
??#???.???#??#?#??. 3,8,1
???#?#.?#?# 4,4
???.#???#??.?#???? 1,1,4,3
?.??#???.?????#??. 5,5
????#????.?????????? 1,4,2,1,7
?#????.??.##?##??. 4,7
.??#?#??????. 3,6
.?#???###???##.. 2,8
??.????.#?????? 1,6
??#?????..?##. 3,1,3
??..????#??#? 1,3,1,2
??.#??.???#? 2,3,1,1
??.?#.??.?. 2,1,1
?.#?????.? 4,1,1
???#??#????????? 1,5,5
?.?.???#?????#?#? 1,1,3,5
.??#????...??.?. 6,1
..##?.?.??#????? 3,6
??##?#????#?#?#?.? 13,1
?????##..???#? 1,2,4
????##??.?..?.?#?... 3,2
?.???#?###???.???#?? 1,7,5
?????#??.#? 6,1
..#???#????????.#.? 6,1,2,1,1,1
???????#???#????# 11,1,1
##???..#?????#??.? 2,3,5
#?#?#?#??.#?????#?? 9,2,1,3
????..#.?.??? 2,1,1,1
??????#???.##??????. 4,3,7
?.##?.?#?#???. 2,6
???.#????#????? 3,3,4
?.?#.##?#??##??#? 2,2,9
#?##????..?..?#? 4,1,1,3
??####?????##?.?.?#? 13,2
??#?#??.?????????.? 6,7
?#??..#.?#??#???#? 1,1,9
?.#??????.?????.?#?? 7,1,1,1,1
??#?????#?. 1,2,4
#?#?#????#?.?? 1,5,2,1
.??#?#.?.?.##???? 5,1,1,3,1
?????????..#????? 3,5
???##??#??..?#???? 4,3,6
?##?.???#?#??####??? 2,12
????#.?##???? 1,1,7
.?.?????#??#####? 1,13
????.????##..#...??? 3,6,1,2
..###???????????#?. 6,4,1
.???#??####..????? 7,3
?.???##?#????#??. 6,5
???##..?##?#????.??? 2,2,1,1,1
??.#.??.?#?? 1,1,1,1
.???.????????#.? 3,7
.?.#?#.??.#??#? 1,1,1,1,2
???????#?#??.? 1,3
#????.?#?#.?.#.?#? 5,3,1,1,3
#?###???????#?? 5,1,2
#?.??.???#?? 1,1,1,1
.????#.?##?#..#? 1,1,2,1,2
#?.#??#?##??#??# 1,10,1
?#...???##??#??? 1,9
??#??.#?##??? 2,5
???.??????#.?? 2,6,1
?????#???#?#?#.?.?.? 12,1,1
..????#.#??#????# 1,3,2,4,1
#..#??????#?.#?.?# 1,1,1,2,1,1
??...#.?????????#?? 1,5
??#?##?.?? 6,1
???#??.?.????#???# 6,1,5,2
.???????#? 3,3
?????.#??#????.??# 4,2,3,1,1,1
?..??.????#???? 1,1,6
????#????????.?#.? 4,1,2,1,1,1
?.???????#? 1,1,6
?.??#????##?..? 1,1,1,3
?.?.?#????#??? 1,4,2,1
##.??????#?#????? 2,1,2,8
#??.????##??##?#?.?? 3,10,2,1
??.?.???.??##?#????? 2,7
?#?????#?#. 5,3
#.?.??#??#.? 1,1,4
#??#..#?##?.?? 1,1,4,1
???????.#? 7,1
??#???.#????###?. 1,8
?##???#?????.?????? 8,2,3,1
#????.??#.?.?????? 1,1,1,1,5
..?.????????#?#?#?#? 6,2,6
?#?????#?? 4,1,1
?.???.??#?. 1,1,2
??...#..?. 1,1,1
?#?????###??? 1,9
#?#.????#????##. 1,1,5,1,3
#?..##??.#??????.??? 1,3,1,3,1,1
?????#.#??????.??? 4,1,5,1
.?????????. 2,3
#???#??#?##??#.??# 5,8,1
##???#.?.? 3,2,1
#.??.?.?????.. 1,1,1,3
#.#??.??????##???? 1,3,1,5,1
..?.????#??????#?? 1,1,2,6
???#?#?#????.??#. 1,5,2,2
?????.???? 1,1,1
?#?##?????.?##??# 4,1,6
??#?#..??? 5,1
??????###??? 2,5,1
?#?????.?#? 3,2
.#.????????#?????? 1,1,2,2,1,1
.???.??????? 2,5,1
??#??.?.?????#?# 4,1,5
#?#.#.??#??#???.?? 3,1,3,1,1,1
.??#???#...?#?#. 3,2,4
?????.???????.???# 4,3,1,1,2,1
.?#?.???#?#??#?? 2,7
?#??.#????#???????? 4,1,4,4,1
????#?..????? 1,1,1,3
??..#??#.??? 1,1
.???#?????????###? 1,2,1,1,6
#.##??##..???.? 1,6,1,1,1
?#??????????????#?# 2,1,6,4
.#?.#??.?# 1,1,2
???.?#???????.? 1,1,2,1,1
#?#??#???????????#?? 1,1,7,1,1,1
???#???.?#??? 3,1,2,1
???#????###?? 2,4
???#?#??#?.? 1,3,1,1
?????????#?#?? 2,2,4
.#?###??????? 6,1
???????.?#???.?## 1,3,4,2
.?#.??????##?#??.?? 1,11,1
???????##?#?#???? 2,1,7,1
?#??.??##.???. 2,4,1
..???.???#??. 1,1
????#??.?##????? 5,1,7
..???#?????????????# 4,8,1
?#?.????#??# 1,1,1,1
#?#..?????. 3,3,1
.????.??????? 1,1,5,1
?#?#..?#?? 1,1,1
?????????#?#?#?? 1,4,6,1
?.?#?#?.???## 1,1,1,3
????#?????.. 1,7
?####.???. 4,2
#??##?##?.????#?. 8,2,3
.#???##????????? 8,2
?.??##?#??#?????#? 1,6,8
?##?..?#??##??# 4,2,5
#??.#?...???.##?#?. 3,1,1,1,2,1
????#????#?????? 3,4,1
?????.??#????????.?? 2,1,9,2
??????.????. 1,2
??#?###??????##?#?? 16,1
?.???#?#??#??????#?. 6,2
??.???????.?#?????? 2,2,1,2,1,1
??#?#??##??..?.?? 5,2,1
?#.?###???. 1,7
.?#?....???.? 2,3
##?????????? 2,1,1,4
?????#..???#??? 2,2,3
??.#????????#.#. 1,1,6,1,1
?.??.??.??#?.?#? 2,1,1,1,2
.??#.?..??? 2,1,1
?.????#?..??#? 5,1,2
.#??#?#?????.. 1,6,1
#???#???#??#???????. 5,2,6
????????????#???#? 1,1,2,1,1,3
.?#.#???#?.? 1,5
#.????.?#??..???? 1,1,4,4
#??.##??#????# 2,10
?.?#?#.#??????#?#?? 3,1,8
?#?#??.???? 1,3,1
???##???#.?.??.?# 5,1,1,2
????#?#.#?#?#..?# 1,1,1,5,1
#???##?#.#..#.# 6,1,1,1,1
#.#??##?#?.?# 1,1,5,1
#??##????.???.???? 1,3,1,1,1,2
??.??.?##??#???? 1,9
??????##??.#?? 4,2,1,1
????.????.? 2,1,1
.??????.#?###??????? 3,1,11
?.?#?#???..?? 5,2
.?????????????? 1,1,4,1
##?.????#..? 3,3,1,1
.?##????####??#?? 5,5,1
??.?????#??? 1,7
??.?#??.?.?#??. 4,3
??.#????.???#.#???? 1,3,1,2,4
?.?..?#???...#??#? 3,4
???#????????.#? 3,1,2,1
?#???????. 3,3
#?.?#???#??.?? 2,5,1
??#???#.????#??? 5,3
.#??????#???.? 1,1,5
?????.???#? 1,1,4
?#?##?#???#???#.. 4,3,1,1
?.#..????? 1,1,1
??.??#?##?.?.?.. 6,1
????###????????#? 2,4,1,1,3
.??..???#? 1,2,1
?.#..???##?.? 1,1,3,1
.?.??.??#?? 1,1,1
?.?#.?.#?????.??? 1,1,2,1,2
.#?..??#.?.??.?#?#? 1,1,1,1,1,5
?#.?.?.???? 2,1,4
?#???#???????#?#??.? 6,2,6
?.##??#???.? 2,3
????.?????#? 3,4
?.?#?.??##???#? 2,8
?.???.#??????###?? 2,3,6
???????.??. 5,1,1
?.#?????##. 2,5
#?#??##?#??#????? 1,1,9,1
.??.??##??#??#?. 1,10
??.#.#??#??.?##? 1,1,2,3,2
.?..?.???#?##? 1,7
.?.????.??????? 1,3
?#..???#??#????#???? 1,11
..?????#?.??? 4,2,1,1
?.?##??#?#??#??#? 3,11
???#??#?#????###???? 9,5
.?????????.???#??#. 1,1,6
???.??????? 2,2,2
#????.??.?? 1,1,2
##????.?.? 6,1
?????#????##???#?? 1,1,1,8
.?????????#.?##??.?? 9,4
????#???#?????????? 9,1,1,4
..#??#.???. 4,1,1
?.??.??.??. 1,2
??#?##??#?.???? 2,5,1
??#???.??? 3,1,1
?#?#??????.????????. 4,1,2,1,4
.??????#?#?. 2,2,1
?#.??##?#?? 1,6
.####?#??##?.. 7,3
??#???#??.?#??##??. 6,7
????##?#?.??????#??. 7,7
?????#??.????..? 5,3
#.???##????#. 1,5,1,1
???.#???.??#? 1,1,1,2
.???.??????.??????# 2,3,1,1,2
???##???????? 6,1,2
?##??.??.?##???. 3,1,4,1
???.??#?#.??? 2,5,2
.#????#??.?? 2,2,1,1
??????#???...?..? 4,1,1,1,1
.????.?#??#?.?. 1,3,1,1
#??.??????.? 2,1,1,1
.?#???????.? 8,1
?????#????#.#?##?#? 5,2,7
??????.???#????.?#?. 6,1,3,1,2
?####????##?.??#? 10,1,2
.??.?#?##????.?. 1,9
.#?..??#??#???##. 1,8,2
?.???#???#?..? 1,3
?????#?#???##?.?#??. 2,8,2,1
?##?#.??.?#..?? 3,1,1,1,1
?##??#????. 2,1,2
???#??..#?#??#. 5,6
?????????##?#?#?.? 1,9,1,1
?????.#.#.? 5,1,1
#???.?#.?????.? 1,1,2,1,1
.????##??#####?.#??. 9,1
##?.?#?#??.. 2,6
.?#?.??.????#??#. 2,8
?#?#?#????#??? 8,1,1
??####.???##. 5,2
???????###?#??##??.? 3,13
####??#???????? 4,1,2,1
?????#?#?#???#???? 1,1,1,9
???.??.#???#?#?? 2,1,1,6
?##???.?.?.??? 6,2
??.???#?#??...???? 4,1
.#????#?#?#???? 3,3,1,1
?##???##?#?##?.??? 13,3
?.?#???.??. 3,2
??#?#???.#??????. 1,3,5
.??????##??????.# 13,1
#??##????###?#?#???? 1,10,4,1
?##?#?###????? 8,1
??.???...???#.?##?. 2,2,4,3
???##???.??#? 6,1,1,1
?????#??????. 1,3,3
.?.??????#??#??? 1,8,1,1
.???#??????.??????.? 9,4
????.???#??? 1,1,1,4
.#?#?#???#??### 3,3,6
.#?#?..#.?????.?#### 1,1,1,5,4
.?.??#.#??#??.? 1,1,4,1
????#??#???.#???#??? 1,1,1,1,1,8
???.??#?#??????.???. 2,1,1,7,2
?#?..?????? 1,1,2
#??#??..#?? 5,1
?.????#???#?#?? 1,9,1
?.?????.????? 1,3,1,1
#?#..?????#.??? 3,1,2,1,3
???????#??????? 2,6
#?#?..?#??? 4,3,1
?.##????.??#???..?## 1,2,1,4,3
????.??.??#??# 2,2,5
?.???#???#??#?? 1,8,3
#??#???..???##?# 1,2,1,7
???#?#?.??.#???? 4,1,2,1,1
.??????.?..????. 2,1,2
?#?...#?.??. 3,1
?#?#??????.??#?##??? 5,3,1,4,1
#??#?#..????.??#? 4,1,2,4
?????#?#.?#???.#???. 7,3,4
?##???#.??.?#??#?? 6,4
??#?.??#?????#?? 1,8
.?##?#???? 6,1
????#?##??.???#??#. 8,1,1,2
?????????.?#? 3,2,1
.#?.????.. 1,4
???????????. 6,1
#??..?.??? 3,1
?#???#????.????#. 7,1,1
?.????.???#? 3,2,2
???#...??##.??. 4,4
.??###?.?.?????## 5,1,2,3
??????.???????? 1,1,1,6,1
.??????????#?????? 1,11
???#?.???? 4,1
#?.???.?????##?????? 1,1,2,5,1,1
?..#???#??. 1,3
.?#??.???# 3,4
.???????.#? 3,1
.?????..#? 1,1,1
????????.???#?????. 1,4,4,3
??..#?.??#??#.?# 1,1,3,1,2
?#.?????..? 1,5,1
?????#??#???? 2,9
????#??.??????##. 4,6
?????.??#?#??#... 3,6
???.#??#???????? 1,1,3,2,2
???#?????#####??#. 2,10
.....?.?#?? 1,3
..???..#??????????? 1,2,3
?..?#?.?????? 3,1,1
???#?#?##?????#.? 1,8,1,1,1
?.????????#.????#. 1,9,1,1
?#???###???.????..?. 7,1,1,1,1
???##?#???#?## 3,2,5
?..???##??.????? 1,3,1
.???#?#..?????#??. 6,8
?????????#????#? 3,4,2
?#???.????#?. 3,4
?##??#??#?#???????#? 10,6
?.??????.??# 1,1,1,1
#??????#??#????#?.?? 2,2,11,1
??#???????????#?.#? 3,10,2
???.???##??.?.#? 1,1,4,1,2
???.?.????#?#.. 1,7
.??.?##?.?????#?#? 4,7
???.???##?? 1,4
???#???#.?.???? 5,1,2
????#?#?#????# 9,1,1
???.#?#???###??#? 1,13
???.#????#?.??? 1,1,1,2
..???????#???? 1,6,2
?#??#?.?.??.?.. 6,1,1,1
.?.?#??????#??#.? 1,4,4,1
?.#????..??????#??? 4,1,4
.?#.?.??#???#???#?.. 1,12
????#???????.#???. 2,7,2
??#.???.?.??#?????? 2,1,1,7,1
??.#.????#??? 1,1
???.#?????????#??. 6,3
????#??#?###???.. 11,1
???#????##?#????. 7,5
?#?##?#????????#? 1,8,4
.#?????##???????# 1,1,7,1,1
??###??.?#????##??? 5,9
?.??#.???#????????? 1,1,1,5,1,1
??#??#?????.??.?. 1,1,2,4,1
??#?#??.???#??????? 7,1,7
.#???????????#? 1,1,1,1,3
???#?..?#????.?.??? 1,3,2,3,1
.?##?.?#??????.????? 4,7,3
????..???????###?#? 3,12
????.??..??##?.? 1,2
#????????#.???? 6,1,1
??.#??#????.??? 1,1,4,1,3
#??#???...?. 1,4
??#??#..?#?#??.? 5,5
????#??.??.??? 6,1,1
????.#?##?????#. 1,5,1,1
??????.???##??. 2,4
??.????????????? 1,2
?#.?????????.? 1,1,3,1
#?#.???##.. 3,4
#?##???#??? 8,1
.??.#?#?#??#?. 1,8
.?#?#?.### 3,3
.?#????#???##?.?#? 7,4,1
#?.????????#.? 2,8
??????.#???#????# 1,1,10
???#??.#.??.. 4,1,1
#.??#?#??. 1,2,2
.###???.?????#. 5,3
??#??????#?#.?.?## 11,1,3
???#?#?#????? 8,1
.????????##?...#??? 11,1
?##.???##?? 3,1,2
.#??.???#??#?. 3,1,4
?????#???#?????#??.? 1,1,1,11,1
.?.???????#?##??#?? 1,4,7
???##???.??? 7,3
??.???#???? 2,1,2
?#????#??????##??#?? 4,2,1,1,2,3
.?#.?.????????# 1,1,1,2,1
??####.#???#????.? 5,5,1,1,1
???#.#?.#?#???#?..? 4,1,7,1
????#?.?.#???#? 1,1,2,3
#?#?????#????? 6,3,1
?????#.?#?. 4,1,2
.????.?#?.?## 2,1,2,2
??#?.?#??? 4,2,1
????#???#???.?? 11,1
#?#..##?.???#? 3,3,5
.???.?#???? 1,3
.#.?..???#???#??? 1,8
.?.?#?#????? 4,2
?#?#??#??????.#??#? 1,6,1,1,2
.????.????? 1,2,1
????????.?.##?? 7,4
.??????#..?????? 2,1,1
?##?##..?#? 5,2
?????????.?#?#??? 2,3,4,1
??????.???# 1,1,2
.???.???#?.? 3,1,1
.?????#??. 2,2
??.##??##?#???.??.? 1,11,2
???????#?#? 3,3
#..?.#?#??.?.#? 1,1,5,1,2
.?####?????.?? 7,1,2
#???##?????.???..?? 1,7,1,1,1
#?????.##.#?##???# 1,1,1,2,1,6
?##?.????.????? 3,3
#?##?#?.??.?#?.?.? 6,1,1,1
#?????#?.?? 1,4
??.???????#?.##??.? 1,7,4
?.???.#?.#?#??....# 1,1,2,3,1,1
.?##?#????#.? 5,2
?#???.??.#?#??# 1,1,6
?????#??#????? 4,5,1
??????##????# 1,1,4,2
????#?#?#?.???#?## 2,1,1,2,1,5
?.?.???#??? 1,1
#??#?#??.#.?.?.#? 8,1,1,1,1
??????#????.??##?? 6,1,3
??#??#?#????##??.#? 15,1
??#.????#? 1,1,1
.??#?..???.??????. 4,1,6
#??#?#.?#.??#?????#? 4,1,1,9
.#?????#???#??? 4,6
?.????????.??#?# 1,5,1,5
.?.?????#.#?#?? 1,2,1,1,1
????#??#?.??.?##??? 1,1,1,2,1,6
?#?????#??..???? 9,1
??#?#??.????#?????? 3,9
.#???????.?#..?? 7,2,2
#?###?#.?#?? 5,1,1
????#??????#???.???? 3,1,5,1,1
???.??.??#?#????? 3,6,1
.??.??????. 2,1,1
.?#???#???????? 2,3,1,1
???.???#??#???#. 1,1,1,5
#??????#.#????#?? 1,5,1,3
.???????????#???? 3,4
#??.#?????????? 2,1,3,2
##.###????????#.#?. 2,9,1,1
#???##.???.#??? 6,3,1
????.??###??..? 1,7
?##?????.?.# 5,1,1,1
.??##?.???##? 3,1,3
?.?#?.????????.#.? 1,3,2,4,1
#??#?..??#.#.???? 1,2,3,1,2
??.???.????????.# 1,1,3,2,1
.???##??#?.#??.?? 6,1,1,1,1
?#?????#???#??.??? 2,7,3,1
??#??#?#??##??#?.??? 4,5,2,2
???##?.?.????? 6,2
?.??????##?.?#???#?? 1,1,5,4,1,1
??#??????####??#. 1,1,9
?????#.#???? 4,2,2
????#??.#??.?? 5,1,2,1
#????????#???????. 8,3,4
??????????????#. 1,2,4,1
??#?????###????##??. 3,14
????..##????#?##???? 1,1,10,1,1
??#???#??.?.? 3,2,1
?#???#???.?? 1,4,1,1
.?.?.??##?##?#???#? 1,13
???.??#????#?? 1,3,2
???#??#???#.?. 4,1,3,1
??#????#?????? 1,3,2
?..?????#???.. 1,1,2
.???#?#..???? 1,1,1,3
..?#?#??????. 2,7
##????????#???#?. 5,10
#.????#?.#?.#?#??# 1,5,2,1,4
???.##?????? 1,3,2,1
?????????? 2,1
????.???##? 2,5
?#???????### 1,1,1,4
???????#?#??# 3,6
.#??#???????#???? 12,1
???##.????.? 3,2
???????.?????????.?? 6,2,1,1,1
??????#??.?#???# 2,4,4,1
???#?.?..????##?##? 4,8
...??#????? 5,1
#.?#.????????.??# 1,2,6,2
??????.??????..??. 5,1,3,2
??.#??????????#? 1,4,2,2
.?????.##?###.? 2,1,6,1
.?#???#?????.?? 2,6,1
???#?????? 5,1,1
#????#???##?#?????? 1,3,8,1
?#?#.?????###? 4,6
???????????? 8,1
????##.??.?.??? 2,2
?####??#????????? 7,2
??????..?.??# 1,2,1,1
?#?..?##?#? 1,3,2
??.?????#???.##? 1,1,2
?.?????#????.??. 1,4,1,1,1
?????????.??#?? 2,3
???#??????. 1,2,2
??##???????.#?# 10,1,1
??.??#??#?. 2,5
.??#?#?#????#.? 10,1
?#?.??????.## 1,1,1,2
??.???##.?? 1,4,1
???????#??????? 1,7,1
?###?.???????.?????# 5,6,6
?##??.?##??#?.##? 3,1,3,2,2
????????.?.? 2,2,1
?????????#?###?# 1,2,2,1,5
??#?#????# 5,1,1
?.#?.#?..#? 1,2,2
???.?.???.?#??.??.?. 1,2
??????.#?. 1,2,2
??#??#????##.?. 6,1,2,1
##????.?#???#. 4,1,3,2
??.????#.??? 1,1,1,1
????????#?? 5,3
??#???###.? 2,4
???.?#???? 2,4
?????#?????#???.?#? 14,1
.?????????#??###..? 2,9
#??#.???#?.???#? 1,1,1,1,4
????.?#?.???? 1,3,1,1
..?????.?.#. 2,1
?????.#???..?#? 2,1,1,1,1
##??#???.??###?? 2,2,2,1,3
#.?.#?#????? 1,1,5
.???????#?? 3,1,1
?.?????????..? 7,1
????.?.???#?#?.#? 3,1,4,2
..?.?????.??#?#?? 1,4,1,3,1
??#??????#????#? 1,11
?#???????. 3,3,1
?.#?..?.?.#. 1,2,1,1
#?#?..??#??? 4,4
.???.?#????.? 2,3
.????????????.? 8,3,1
.?##??#?????# 7,1,2
??####???#??#?.?.#? 14,2
?##?????????# 3,6,1
??.#???.???????.##?? 1,1,1,4,4
?????#?.?#?? 1,3,1
?...?##???#? 1,4,1
?#???.#????? 2,3,1
??.?#????.#?.#?? 1,4,2,1,1
??.#.?.????# 1,1,1,5
?????.???? 1,3
??????.?..##?##?. 3,5
?????.#???#?.???? 3,5,2
.???#?.#?? 5,2
#.??.??###?##?#.? 1,1,8,1,1
???.#???????#??? 3,5
?.#?????####.??. 4,4,2
????#??#?????????? 1,13,1
?.???.#??.#?# 2,2,3
.?#?#?.?????#????. 5,8
##?#???.?. 4,1
????.?????#?#? 1,1,1,3
????????#??? 3,1,1,2
.?????.???#?##?? 1,1,6
??????????#?#?#? 1,10
.#?#?????#?#?##??#?? 5,11
..?#????.??? 5,1
?.#?.?????? 2,2,3
?.?.???#??#????. 1,7
.#??#?#??.???? 1,5,1,2
????#.??##? 1,1,3
??#????.??.?#? 2,2,1,1
????##??.??#??? 1,5,4,1
.?.??#????#? 3,2
?#???????#???#?? 1,1,7,1
?#?.??.#.??#.? 1,2,1,2
.?.???##??##?#?..? 1,10,1
.??#???..??.? 1,1,1,1
???##????#.??#?#??#? 9,7
?..?.???#.???#??. 1,1,2,1,4
???#??????#?. 3,6
#.#?#?#.?? 1,5,1
??????.?#?#?#?? 1,7
??.?#??#????####? 1,2,1,8
.?????#####?????.??? 7,1
???#?.??#???#? 1,2,2,2
???#??.?#.????#.?? 1,1,2,1,3,1
.???#..???? 3,1
#.??#??##?#.?. 1,7,1,1
?.??#?#?#???? 6,1
???.?????? 1,1,1
??#????###????????. 9,1,1,1
.??.??..###? 1,1,3
?#.#??#????? 2,2,3,1
?.??????????.??.? 1,4,2,2
.?.?#????.??.. 1,3,1,1
.?.#??#??.?.?????.?. 6,2
#????#?#?##????????# 1,5,2,1,3,1
???#??..????#????..? 4,1,6
??..?????#?? 1,5
??.???.#?? 1,1,2
?#.???##??#???#?? 1,1,4,7
?#????#?..#. 1,2,1
????..#.?.##???# 1,1,2,3
?.???.?.?..#??? 2,1,4
???...?#??? 1,3
?????????.??.?# 3,2,2,1
???????#???? 1,1,3,1
?????#.???.?#??#???? 1,1,1,2,5,2
.?###?##???.????. 9,4
#?????#??? 4,4
?#?.#?##?#??????. 3,11
#????????.? 1,6
.??????#?#?#???#??? 3,4,3,4
.??#??????##???# 8,2,2
#?#?..?#???#? 3,2,2
???##???#.???#?#??#. 7,1,1,1,4
#?#??..?.??????? 5,1,5,1
##?.?.?##. 2,2
#?.???#..?? 2,3,1
???.#??#??###? 1,1,2,3
????????.??. 1,2,1,1
??????..?#?#?.#. 5,1,1,1
.???#.#?#?#??? 3,1,6
?#?.??#?#?????? 2,1,1,4,1
#?#??????.?##??#?#?? 6,7
?.???#?#????? 1,3
????????##?????#.#.? 9,4,1
.??#????.? 1,2,2
..??????..?#..? 5,1
#??????#??.?#?#?? 4,2,4
.?...????#?#?##?#. 1,12
?#??#.?##?.??# 4,3,1,1
??.??.##?.?? 1,3
??..??.?.?.???# 1,2,1,4
?????.?????##?? 1,1,1,4,3
??#??????. 2,1,1
#???.#??.#?###?#??? 2,1,1,1,7,1
??????#.??#???? 4,1,1,3,1
..#???????#????#?# 1,2,2,6
#.####???##????#?.?. 1,15,1
?????##????..?? 7,1
??#?#????????... 7,1,1
?#.?#?###?#?..#? 1,7,1
???#?.?.#????. 4,2
?#..?????? 2,4
??..??#?????????.#?? 1,1,6,1,2
????.??#?.#? 1,1,1,1
.??#?.???? 3,1,2
???.?.?????.#?? 1,1,2,1,1
#???.##???##??#???? 2,1,2,10
.##?##?????????. 5,1,3
???????#?#??#??##?## 1,1,6,1,6
???#??#??#?.?.##? 4,3,1,1,3
#.??##.??#???????.? 1,3,1,1,2,1
?#.??#??#?#? 2,3,4
.???.#?.??#???#?#? 1,2,3,1,1,2
??????##?? 3,4
???????.?##????#???? 6,3,6
..??#???.?? 3,1,1
##???..??#????..#? 4,4,1,1
??.#???#???#?.?. 1,2,6,1
?.#?????#?.?.?#??#? 7,5
?#.#?????.#.???#??? 1,2,3,1,4,2
??#??##?????. 2,7
??.?????##? 2,6
????.??????? 3,1,3
?##.#????###??.?.? 2,1,2,3,1,1
?#??.?#??#????.? 3,5,2
.?#?.??#?? 1,5
????.#??????? 1,2,4,1
.??.?#??.??????.? 1,3,6
...?#???.?#?? 2,1,3
?.#?????#???????. 1,7,2,1,1
.????..??. 2,1
.???..???#? 2,1,1
#??????#.????????#? 1,1,3,1,1,2
????????#.?## 4,1,2
?##?#????????.? 10,1
??.????.#?? 1,2,1
??.?#.??????..???? 2,1,1,4,1
.?????#??? 1,3
??#????.???#????? 5,5,1
?##??????#??#? 9,2
?#???.?#?????.#? 1,1,7,2
#.???????####?##??? 1,1,3,5,2,1
????????.??? 2,1,2,2
????##?.?.???????. 3,2,1,5,1
????????#? 2,3,1
?##?..???. 4,3
????#?????? 1,8
??#?#?.?.# 5,1,1
?#?.???###?#???? 1,7,2
?.#?#???.??#???? 5,2
???.???#?? 1,3
?????.???#?#?#??#??? 1,2,1,9
?????###??#?? 9,1
?#?#????#?????. 4,4,4
????#???..?.??.???? 2,2,1,1,4
?????#?##??#???. 1,7,2
????.#????# 1,1,2
.#??..#?#????#??? 3,6,2
?#####??#?.#.??.#??? 8,1,1,1,1
?#.#??.???????? 1,2,1,3
#?##???????????#??? 1,4,1,2,2,3
#?#??#?#.#?#????? 1,1,1,1,8
??????#.?.?##??# 2,1,2,1,5
????????#????##?.? 1,5,2
?#?#???#???????.???? 5,1,5,3
?##??#????.?.? 9,1,1
.#...???## 1,1,3
?#?#?.?##? 4,3
??###?#????##??????? 12,3
????#?#.????#???# 3,3,6,1
.?#.?.????#?? 1,1,1,2
?#???#????.????.#??. 2,1,3,2,3
?.##??.#??? 4,1,1
?.??#??.??.??#?#?#? 1,3,1,1,3,3
?.#??#?..?#. 2,2,2
?????#?#?.? 2,1,2
.?#?????##.?????#?.? 8,4,2
??..??????#??##? 2,7
.?.?????.. 1,1,1
?#.??.?..???#??? 1,1,7
?????..???. 2,1
.?.????#?.?# 1,3,1,2
???????.?? 2,1,2
???#?#??##????.?? 1,11,2
##?.?.??##??????#.?? 3,9
##?#????#.??#?#??? 5,1,3,1
???#??????#??? 7,3
?.???#?..?##?.??#??? 3,3,3
#????#??##??????#??? 1,2,1,3,2,4
..?...?#???#??#?# 1,1,4,1
?#?#.?#.?? 4,2,1
?#?#???????#?. 3,1,5
???#?#???????? 1,3,1,1
???##?#?.#?????##? 1,2,2,9
.????#??????? 1,7
??.##?.#?#?.?? 2,3,4,1
?.?#?????????... 2,3
??.?#??????? 1,2,2,1
???#?????##?##? 1,4,6
?????###?##?##???? 12,1
???#?.?#??#??. 2,2,3
???.#??##. 3,2,2
??.#?#?.??#??###?# 1,1,1,8,1
??.??.??#????#? 1,1,4,1,2
.#???.??.?#?##? 1,1,1,5
.?#.???.#????#???#? 2,10
????#?#?#???###?#?.? 13,1
?#???????.????? 9,1,2
????????????.#? 5,1,1,1
?#.?#?#.??????..#?#. 1,2,1,4,1,1
?.??#?.???????#?##. 2,9
?.????????????#????? 5,3
??#.?????? 3,1
????#??#?#??.?. 2,4
?#?##?###???.???##? 10,5
???#?##?????? 8,1
.??#?.?.??. 3,1
???#??#??.??.????. 7,2,2
.#?.#??..?????#?##. 2,3,9
?????##.???? 5,2
???????...? 2,2
#.?#.?#?#????.?? 1,2,5,2,1
?.???...?? 1,1,1
?#?##???##??#..?? 9,1,1
.?.?##.??? 1,2,2
??????#??#??? 1,1,1,4
??..#????.???????? 1,1,1,1,1,5
.?##??.???#??? 2,2
??.????..?.??#?????? 1,3,1,6
.?#???#???..??# 9,1
.???#.#.#?#??.? 1,1,1,4,1
??#?#??.?.? 5,1
???..?..#???????# 3,1,4,1
?.?#.????#.?.?## 1,2,2,3
??#????.#? 1,3,1
.?#???.?#?#.???? 3,4,2
??#?###????# 7,3
???#?..?.#?????????? 4,1,1,3,3
??.?#.#??.. 1,2,3
.#?#.?#????#?# 3,1,4
????#?#?#?.?.?# 1,5,2
?..??.#??.#? 1,1,2,2
.????.???.?? 2,1,2
?##????????????#???# 4,3,1,5,1
#??.????#?????????? 1,1,1,5,1,4
?##??#?##.#. 3,2,2,1
?#??.#??.????? 3,1,1,5
#?##??????#???.?? 13,1
#.#?.????##????? 1,1,10
#.?.????#??????.?? 1,1,1,9,1
???###.?#?.?. 1,3,1,1
???..??#??? 2,4
??????#?.?.??? 7,1,2
#.????????? 1,2
?##???#.????? 4,1,1,2
???#.?#?#?.???? 4,4,2,1
????#?#????#?.?#. 10,1
#.?.????.?????..?? 1,1,2,2,1,1
??#???#####?#???.?. 1,10
??..?????# 1,2,1
#??????????? 3,5
###??##???#?#????? 13,1,1
?.?#??##???. 1,2,6
??????..??#??#??. 1,7
???##?#??#???.#????? 7,3,1,2,1
??#???.??.#? 5,1,2
?...?????????.?##?? 7,3
.????#?#..?#?#?.?? 3,3,3,2
??#???.?.#?#.?.?.. 4,1,1,1,1,1
.??#??##?.? 1,6,1
????..??#????# 3,3,4
??#??#???#??.?.##?# 5,1,1,2,1
#????...#.?????.?? 5,1,1,1,1
???#.??????#??# 1,1,8,1
??????????#? 1,1,1,2
???????#??.?????? 2,2,4,1,1
?.#???.?????.#?###?# 1,1,1,1,7
###?.?.#?? 3,2
????#?.??.#?#. 3,3
.???.?#???.? 1,3
#?.??####?. 1,4
??????????#?. 7,2
??????.??#??????.? 2,7
????#???.?##? 6,2
.#?#?#??????#.????. 1,8,1,2,1
??#?????##????? 1,5
?#??#..??? 1,2,2
?.???.?#???? 1,2,1,1
??.???????#.????? 1,6,1,3,1
?#?#?#.???? 1,3,1
??#??##?#??#.#?.? 5,2,1,1,1
????#?#???#?? 8,2
.?#?#?#?.#?#?? 6,4
##?#???????#?# 8,3
..??#??.#?.?#?? 5,1,4
.?#???????#???.#?? 1,8,1
?..?#?##.#????.? 4,4
.??.??#.#?? 1,1,2
???????.#?#??????## 2,4,1,1,4
?.?.??.#??#? 1,1,4
??.#?##??.??##?##.. 5,5
????..#..#?. 1,1,1,1
??.?.????#? 1,2,1
??#????#?.?. 4,4,1
#?#?#?##?##?#???#??? 1,1,4,4,3
???????##?.#?????? 1,6,3,2
.??.??#???.???#? 2,5,2
??????.#?? 1,2
#.???????.???.????? 1,1,4,3,5
?.#??..???#?.?? 2,5
?????#????? 1,2
?????.??##? 1,1,2
????????#?#? 2,1,1,3
?????.?#.?#. 1,1,1,1
?.????.?#???#? 2,6
??#???##?????## 2,7,2
?..?#??###??? 1,9
?????.??????#??##?## 2,1,1,5
?#?#?.???? 2,1,4
??#?#?????.??? 7,1,1
.???#???.??# 7,1
??##???????##??##?. 5,10
?????#???#???#? 1,7,1
???..?#????##? 3,1,1,2
?????####??...#?#??. 2,7,1,3
??#????????#. 5,2,1
.?.?????????##.??#? 1,1,1,5,2
???.#?????#???? 2,1,5,1
.?#??.??????###??# 2,1,1,1,3,2
.?.#?#????????? 1,1,2,1,4
?##?#?.????? 5,4
????.#???? 2,1,1
?????????#?? 2,1,1,1
?????.?##?? 1,1,4"""
