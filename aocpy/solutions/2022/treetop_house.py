from aocpy.base import BaseSolution


class TreetopTreeHouse(BaseSolution[list[int]], year=2022, day=8):
    def prepare(self, line: str) -> list[int]:
        return list([int(i) for i in line.strip()])

    def part1(self, inputs: list[list[int]]):
        visible_trees = 0
        for i in range(len(inputs)):
            for j in range(len(inputs[i])):
                tree_height = inputs[i][j]
                visible_from_left = all(map(lambda x: x < tree_height, inputs[i][:j]))
                visible_from_right = all(
                    map(lambda x: x < tree_height, inputs[i][j + 1 :])
                )

                y_line = []
                for k in range(len(inputs)):
                    y_line.append(inputs[k][j])

                visible_from_top = all(map(lambda x: x < tree_height, y_line[:i]))
                visible_from_bottom = all(
                    map(lambda x: x < tree_height, y_line[i + 1 :])
                )

                if (
                    visible_from_left
                    or visible_from_right
                    or visible_from_top
                    or visible_from_bottom
                ):
                    visible_trees += 1
        return visible_trees

    def part2(self, inputs: list[list[int]]):
        highest_scenic_score = 0

        for i in range(1, len(inputs) - 1):
            for j in range(1, len(inputs[i]) - 1):
                tree_height = inputs[i][j]
                transposed = []
                for k in range(len(inputs)):
                    transposed.append(inputs[k][j])

                left_score = 0
                for k_tree in reversed(inputs[i][:j]):
                    left_score += 1
                    if k_tree < tree_height:
                        continue
                    else:
                        break

                right_score = 0
                for k_tree in inputs[i][j + 1 :]:
                    right_score += 1
                    if k_tree < tree_height:
                        continue
                    else:
                        break

                top_score = 0
                for k_tree in reversed(transposed[:i]):
                    top_score += 1
                    if k_tree < tree_height:
                        continue
                    else:
                        break

                bot_score = 0
                for k_tree in transposed[i + 1 :]:
                    bot_score += 1
                    if k_tree < tree_height:
                        continue
                    else:
                        break

                scenic_score = left_score * right_score * top_score * bot_score
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score

        return highest_scenic_score
