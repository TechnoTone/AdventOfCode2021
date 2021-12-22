from collections import defaultdict
from itertools import permutations
from Extras import Point3D


def part_1(input: list) -> int:
    scanners = parse(input)
    (_, beacons) = align_scanners(scanners)
    return len(beacons)


def part_2(input: list) -> int:
    scanners = parse(input)
    (scanners, _) = align_scanners(scanners)

    return max(
        [
            a.location.manhattan_distance(b.location)
            for a, b in permutations(scanners, 2)
        ]
    )


class Scanner:
    def __init__(self, id: int, beacons: list, location=None):
        self.beacons = beacons
        self.location = location
        self.id = id

    def __str__(self):
        return self.location

    def __repr__(self):
        return self.location

    def rotate_x(self):
        beacons = [b.rotate_x() for b in self.beacons]
        return Scanner(self.id, beacons, self.location)

    def rotate_y(self):
        beacons = [b.rotate_y() for b in self.beacons]
        return Scanner(self.id, beacons, self.location)

    def rotate_z(self):
        beacons = [b.rotate_z() for b in self.beacons]
        return Scanner(self.id, beacons, self.location)


def parse(input: list) -> list:
    scanners = []
    beacons = []

    sid = 0

    for line in input:
        if line == "":
            continue
        elif line.startswith("---"):
            if beacons != []:
                scanners.append(Scanner(sid, beacons))
                sid += 1
                beacons = []
        else:
            x, y, z = map(int, line.split(","))
            beacons.append(Point3D(x, y, z))

    scanners.append(Scanner(sid, beacons))
    scanners[0].location = Point3D(0, 0, 0)

    return scanners


def align_scanners(scanners: list) -> tuple:
    queue = scanners.copy()
    aligned_scanners = []
    beacons = set(
        queue.pop(0).beacons
    )  # take all beacons from first scanner as starting point

    while queue:
        scanner = queue.pop(0)
        aligned_scanner = attempt_alignment(beacons, scanner)
        if aligned_scanner:
            aligned_scanners.append(aligned_scanner)
            beacons |= set(aligned_scanner.beacons)
        else:
            # Return scanner to queue and try again later
            queue.append(scanner)

    return aligned_scanners, beacons


def attempt_alignment(fixed_beacons: set, scanner: Scanner) -> Scanner:
    for rotated_scanner in rotations(scanner):
        deltas = defaultdict(int)

        for b in fixed_beacons:
            for s in rotated_scanner.beacons:
                delta = s - b
                deltas[delta] += 1
                if deltas[delta] >= 12:
                    rotated_scanner.beacons = [
                        b - delta for b in rotated_scanner.beacons
                    ]
                    rotated_scanner.location = delta
                    return rotated_scanner

    return None


def rotations(scanner: Scanner) -> list:
    for _ in range(4):  # turn x4
        for _ in range(4):  # roll x4
            yield scanner
            scanner = scanner.rotate_y()
        scanner = scanner.rotate_z()

    scanner = scanner.rotate_x()  # pitch up
    for _ in range(4):  # roll x4
        yield scanner
        scanner = scanner.rotate_y()

    scanner = scanner.rotate_x()  # pitch down
    scanner = scanner.rotate_x()
    for _ in range(4):  # roll x4
        yield scanner
        scanner = scanner.rotate_y()
