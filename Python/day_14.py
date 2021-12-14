from collections import Counter


def part_1_unoptimised(input: list) -> int:
    template = input[0]
    rules = parse_rules(input[2:])

    template = expand_template(template, rules, 10)

    element_counts = Counter(template).most_common()

    min_value = element_counts[-1][1]
    max_value = element_counts[0][1]

    return max_value - min_value


def part_1(input: list) -> int:
    template = input[0]
    rules = parse_rules(input[2:])

    element_counts = expand_counters(template, rules, 10).most_common()

    min_value = element_counts[-1][1]
    max_value = element_counts[0][1]

    return max_value - min_value


def part_2(input: list) -> int:
    template = input[0]
    rules = parse_rules(input[2:])

    element_counts = expand_counters(template, rules, 40).most_common()

    min_value = element_counts[-1][1]
    max_value = element_counts[0][1]

    return max_value - min_value


def parse_rules(rules: list) -> dict:
    return dict(rule.split(" -> ") for rule in rules)


def expand_template(template: list, rules: dict, iterations: int) -> list:
    # This is a crude brute force solution.
    # It works for part 1 but for part 2 it's too slow.

    elements = list(template)

    for _ in range(iterations):
        for pos in range(len(elements) - 2, -1, -1):
            pair = "".join(elements[pos : pos + 2])
            elements.insert(pos + 1, rules[pair])

    return "".join(elements)


def expand_counters(template: str, rules: dict, iterations: int) -> Counter:
    # A better solution that tracks the counts of each element.
    template_pairs = [a + b for a, b in list(zip(template, template[1:]))]
    pairs = Counter(template_pairs)  # track all the pairs to be expanded
    counts = Counter(template)

    for _ in range(iterations):
        new_pairs = Counter()  # to hold the new pairs for the next iteration
        for pair, quantity in pairs.items():
            e1, e2 = pair
            e_new = rules[pair]
            new_pairs[e1 + e_new] += quantity
            new_pairs[e_new + e2] += quantity
            counts[e_new] += quantity
        pairs = new_pairs

    return counts
