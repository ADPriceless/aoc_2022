import aoc_utils


class Sensor:
    def __init__(self, x, y, beacon_x, beacon_y) -> None:
        self.x = x
        self.y = y
        self._beacon_x = beacon_x
        self._beacon_y = beacon_y
        self.range = 0
        self._get_range()

    def _get_range(self):
        self.range = abs(self.x - self._beacon_x) + abs(self.y - self._beacon_y)

    def get_line_coverage(self, line_y) -> tuple[int, int]:
        distance_to_line = abs(line_y - self.y)
        if distance_to_line > self.range:
            return 0, 0
        else:
            deviation = abs(self.range - distance_to_line)
            return self.x - deviation, self.x + deviation


class Environment:
    def __init__(self, aoc_input: list[str], line_y) -> None:
        self.aoc_input = aoc_input
        self.line_y = line_y
        self.covered = set()
        self.beacons_on_y = set()
        self.sensors = []
        self._setup_sensors()

    def _setup_sensors(self) -> list[Sensor]:
        for line in self.aoc_input:
            parts = line.split()
            sensor_x = int(parts[2][2:-1])
            sensor_y = int(parts[3][2:-1])
            beacon_x = int(parts[8][2:-1])
            beacon_y = int(parts[9][2:])
            self.sensors.append(
                Sensor(
                    sensor_x, sensor_y,
                    beacon_x, beacon_y
                )
            )
            # also track x-values of beacons
            if beacon_y == self.line_y:
                self.beacons_on_y.add(beacon_x)

    def find_beacon_exclusion(self) -> int:
        for sensor in self.sensors:
            lower, upper = sensor.get_line_coverage(self.line_y)
            if (lower, upper) == (0, 0):
                continue
            for x in range(lower, upper + 1):
                if x not in self.covered and x not in self.beacons_on_y:
                    self.covered.add(x)
        return len(self.covered)

    def find_frequency_of_distress_beacon(self, size: int = 4_000_000) -> int:
        for y in range(size + 1): # F U range
            if y % 100_000 == 0:
                print(y)
            covered = []
            for sensor in self.sensors:
                lower, upper = sensor.get_line_coverage(y)
                if len(covered) == 0:
                    covered.append([lower, upper])
                else:
                    for i in range(len(covered) - 1, -1, -1): # WHAT?! *goat scream (AAHHHH)*
                        covered_lower, covered_upper = covered[i]
                        # TODO: rewrite to remove absorbed ranges in list
                        if covered_lower <= lower and upper <= covered_upper: # current range within covered
                            break
                        elif lower <= covered_lower and covered_upper <= upper: # current range consumes covered
                            covered[i] = [lower, upper]
                            break
                        elif lower <= covered_lower and covered_lower <= upper: # overlap left
                            covered[i] = [lower, covered_upper]
                            break
                        elif lower <= covered_upper and covered_upper <= upper: #overlap right
                            covered[i] = [covered_lower, upper]
                            break
                    else: # range not covered at all (no overlap)
                        covered.append([lower, upper])
            if len(covered) > 1:
                print(covered)
                break

    def _calculate_frequency(self, x: int, y: int) -> int:
        return 4_000_000 * x + y


def main():
    # aoc_input = aoc_utils.readlines('input\\example15.txt')
    # env = Environment(aoc_input, line_y=10)
    aoc_input = aoc_utils.readlines('input\\day15.txt')
    env = Environment(aoc_input, line_y=2_000_000)
    answer = env.find_beacon_exclusion()
    print(f'Part 1: {answer}')
    
    answer = env.find_frequency_of_distress_beacon()
    print(f'Part 2: {answer}')


if __name__ == '__main__':
    main()
