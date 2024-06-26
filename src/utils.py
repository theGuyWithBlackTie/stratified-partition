def ratios_validation(split_ratios: list):
    total_count = 0.0
    for ratio in split_ratios:
        if type(ratio) != float:
            raise TypeError(f"Split ratio must be of type float")
        total_count += ratio

    if total_count > 1:
        raise AssertionError(f"Sum of split ratio must be equal to 1")

    return True


def get_absolute_partition_values(split_ratios: list, length: int) -> list:
    absolute_partition_values = [int(each_split*length) for each_split in split_ratios[:-1]]
    absolute_partition_values.append(total - sum(absolute_partition_values))
    return absolute_partition_values