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



def find_lowest_location(seeds,
                        seed_to_soil_map:dict,
                        soil_to_fertilizer_map:dict,
                        fertilizer_to_water_map:dict,
                        water_to_light_map:dict,
                        light_to_temperature_map:dict,
                        temperature_to_humidity_map:dict,
                        humidity_to_location_map:dict):
    location = []
    for seed in seeds:
        seed_value = int(seed[0])
        range = int(seed[1])
        seed_iter = 0
        while seed_iter < range:
            seed_to_soil = find_in_map(seed_value, seed_to_soil_map)
            soil_to_fert = find_in_map(seed_to_soil, soil_to_fertilizer_map)
            fert_to_wat = find_in_map(soil_to_fert, fertilizer_to_water_map)
            wat_to_light = find_in_map(fert_to_wat, water_to_light_map)
            light_to_temp = find_in_map(wat_to_light, light_to_temperature_map)
            temp_to_hum = find_in_map(light_to_temp, temperature_to_humidity_map)
            location.append(find_in_map(temp_to_hum, humidity_to_location_map))
            seed_iter += 1
            seed_value += 1

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

    with open('input.txt', 'r') as iFile:
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