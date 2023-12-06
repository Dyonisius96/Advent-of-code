import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def create_a_map(seed_to_soil_mapping):
    full_map = {}

    source_range_start = 0
    destination_range_start = 0
    range = 0

    for line in seed_to_soil_mapping:
        counter = 0
        destination_range_start = int(line[0])
        source_range_start = int(line[1])
        range = int(line[2])

        while counter < range:
            full_map[source_range_start] = destination_range_start
            destination_range_start += 1
            source_range_start += 1
            counter += 1
    return full_map

def find_in_map(value, mapping):
    source_range_start = 0
    destination_range_start = 0
    range = 0
    ret_value = value

    for line in mapping:
        destination_range_start = int(line[0])
        source_range_start = int(line[1])
        range = int(line[2])
        if source_range_start <= value <= source_range_start+range:
            ret_value = (value - source_range_start) + destination_range_start
            break
    return ret_value

def find_range_in_map(value, seed_range, mapping):
    source_range_start = 0
    destination_range_start = 0
    range = 0
    ret_value = value
    ret_range = seed_range
    ret_value_range_pairs = []
    second_value_range_pair_results = []
    nothing_found = True

    for line in mapping:
        destination_range_start = int(line[0])
        source_range_start = int(line[1])
        range = int(line[2])
        if source_range_start <= value <= source_range_start+range:
            if value + seed_range <= source_range_start + range:
                # contains the range fully
                # update the starting position of the seed for now, range stays the same
                ret_value = (value - source_range_start) + destination_range_start
                ret_value_range_pairs.append([ret_value, seed_range])
                nothing_found = False
                # stop the execution of the loop
                break
            elif value + seed_range > source_range_start + range:
                # goes outside of the original range
                ret_value = (value - source_range_start) + destination_range_start
                # set new range to be what was left that is not contained inside the map range
                ret_range = (destination_range_start + range) - ret_value
                ret_value_range_pairs.append([ret_value, ret_range])
                old_value = value
                value = source_range_start + range + 1 # all of the range found, moving to one outside
                seed_range = seed_range - (value - old_value)
                nothing_found = False
        elif value < source_range_start:
            if source_range_start <= value+seed_range <= source_range_start + range:
                # first part not contained in the range, but it enters the range
                ret_range = (value + seed_range) - source_range_start
                ret_value = destination_range_start
                # update the seed range to be what is left of in the end
                seed_range = source_range_start - value
                ret_value_range_pairs.append([ret_value, ret_range])
                nothing_found = False
            elif value+seed_range < source_range_start:
                # does not contain the seed range
                continue
            elif value+seed_range > source_range_start + range:
                # Starts before the range, but goes through the whole range and goes beyond
                ret_value = destination_range_start
                ret_range = range
                ret_value_range_pairs.append([ret_value, ret_range])
                # now we are left with two ranges to deal with
                old_seed_range = seed_range
                seed_range = source_range_start - value
                new_seed_value = source_range_start + range + 1
                new_seed_range = (value + old_seed_range) - (source_range_start + range)
                second_value_range_pair_results = find_range_in_map(new_seed_value, new_seed_range, mapping)
                for pair in second_value_range_pair_results:
                    if pair:
                        ret_value_range_pairs.append(pair)
                nothing_found = False
        elif value > source_range_start + range:
            # does not contain the seed range at all
            continue
    if nothing_found == True:
        ret_value_range_pairs.append([ret_value, ret_range])
    return ret_value_range_pairs

def find_ranges_in_map(input_pairs, mapping):
    value = -1
    seed_range = -1
    ret_value_range_pairs = []
    temp_pairs = []

    for input_pair in input_pairs:
        value = input_pair[0]
        seed_range = input_pair[1]
        temp_pairs = find_range_in_map(value, seed_range, mapping)
        for pair in temp_pairs:
            ret_value_range_pairs.append(pair)

    return ret_value_range_pairs


def find_lowest_location(seeds,
                        seed_to_soil_map:list,
                        soil_to_fertilizer_map:list,
                        fertilizer_to_water_map:list,
                        water_to_light_map:list,
                        light_to_temperature_map:list,
                        temperature_to_humidity_map:list,
                        humidity_to_location_map:list):
    location = []
    location_ranges = []
    unsorted_list = humidity_to_location_map
    humidity_to_location_map.sort()

    for seed in seeds:
        seed_value = int(seed[0])
        range = int(seed[1])

        temp_list = find_range_in_map(seed_value, range, seed_to_soil_map)
        temp_list = find_ranges_in_map(temp_list, soil_to_fertilizer_map)
        temp_list = find_ranges_in_map(temp_list, soil_to_fertilizer_map)
        temp_list = find_ranges_in_map(temp_list, fertilizer_to_water_map)
        temp_list = find_ranges_in_map(temp_list, water_to_light_map)
        temp_list = find_ranges_in_map(temp_list, light_to_temperature_map)
        temp_list = find_ranges_in_map(temp_list, temperature_to_humidity_map)
        location_ranges = find_ranges_in_map(temp_list, humidity_to_location_map)
        for location_range in location_ranges:
            location.append(location_range)


    location.sort()
    return location[0]

def main():
    data = []
    seeds = []
    seed_to_soil_mapping = []
    soil_to_fertilizer_mapping = []
    fertilizer_to_water_mapping = []
    water_to_light_mapping = []
    light_to_temperature_mapping = []
    temperature_to_humidity_mapping = []
    humidity_to_location_mapping = []
    # seed_to_soil_map = {}
    # soil_to_fertilizer_map = {}
    # fertilizer_to_water_map = {}
    # water_to_light_map = {}
    # light_to_temperature_map = {}
    # temperature_to_humidity_map = {}
    # humidity_to_location_map = {}

    with open('input_test.txt', 'r') as iFile:
        data = iFile.readlines()

    seeds = data[0].split(":")[1].split()
    seeds_with_ranges = []
    for id in range(0, len(seeds), 2):
        seeds_with_ranges.append([seeds[id],seeds[id+1]])

    index = data.index("seed-to-soil map:\n")
    for line in data[index+1:]:
        if line != "\n":
            seed_to_soil_mapping.append(line.splitlines()[0].split())
        else:
            break

    index = data.index("soil-to-fertilizer map:\n")
    for line in data[index+1:]:
        if line != "\n":
            soil_to_fertilizer_mapping.append(line.splitlines()[0].split())
        else:
            break

    index = data.index("fertilizer-to-water map:\n")
    for line in data[index+1:]:
        if line != "\n":
            fertilizer_to_water_mapping.append(line.splitlines()[0].split())
        else:
            break

    index = data.index("water-to-light map:\n")
    for line in data[index+1:]:
        if line != "\n":
            water_to_light_mapping.append(line.splitlines()[0].split())
        else:
            break

    index = data.index("light-to-temperature map:\n")
    for line in data[index+1:]:
        if line != "\n":
            light_to_temperature_mapping.append(line.splitlines()[0].split())
        else:
            break

    index = data.index("temperature-to-humidity map:\n")
    for line in data[index+1:]:
        if line != "\n":
            temperature_to_humidity_mapping.append(line.splitlines()[0].split())
        else:
            data.remove(line)
            break

    index = data.index("humidity-to-location map:\n")
    for line in data[index+1:]:
        if line != "\n":
            humidity_to_location_mapping.append(line.splitlines()[0].split())
        else:
            break

    # seed_to_soil_map = create_a_map(seed_to_soil_mapping)
    # soil_to_fertilizer_map = create_a_map(soil_to_fertilizer_mapping)
    # fertilizer_to_water_map = create_a_map(fertilizer_to_water_mapping)
    # water_to_light_map = create_a_map(water_to_light_mapping)
    # light_to_temperature_map = create_a_map(light_to_temperature_mapping)
    # temperature_to_humidity_map = create_a_map(temperature_to_humidity_mapping)
    # humidity_to_location_map = create_a_map(humidity_to_location_mapping)

    lowest_location = find_lowest_location(seeds_with_ranges,
                                            seed_to_soil_mapping,
                                            soil_to_fertilizer_mapping,
                                            fertilizer_to_water_mapping,
                                            water_to_light_mapping,
                                            light_to_temperature_mapping,
                                            temperature_to_humidity_mapping,
                                            humidity_to_location_mapping)
    print("Lowest location is: ", lowest_location)


if __name__ == "__main__":
    main()