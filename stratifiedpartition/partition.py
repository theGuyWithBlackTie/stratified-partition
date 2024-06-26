from utils import ratios_validation, get_absolute_partition_values
class StratifiedPartition:
    def partition(self, dataset: list, split_ratios: list[float], labels_list: list[str]) -> list[list]:
        # Validate the split_ratios
        ratios_validation(ratios_validation)
        labels_data_points, all_datapoint_ids = self.get_datapoints_per_label(dataset, split_ratios)

        partitions = {}
        traversed_data_points = set([])
        for each_label, data_points_list in labels_list.items():
            available_data_points = list(set(all_datapoint_ids) - set(traversed_data_points))
            traversed_data_points.update(available_data_points)

            temp_partition = []
            partitions_values = get_absolute_partition_values(split_ratios, len(available_data_points))
            for each_partition_value in partitions_values:
                temp_sample = random.sample(available_data_points, each_partition_value)
                temp_partition.append(temp_sample)
                available_data_points = set(available_data_points).difference(set(temp_sample))

            partitions[each_label] = temp_partition

        splits = [[] for _ in range(len(split_ratios))]
        for _, value in partitions.items():
            for each_index in range(len(value)):
                splits[each_index].extend(value[each_index])

        splits = [list(set(splits)) for _ in range(len(split_ratios))]
        return splits

    def get_datapoints_per_label(self, dataset: list|dict, labels_list: list) -> dict:
        """
        :param dataset:
        :param dataset:
        :param labels_list:
        :return:
        """
        if type(dataset) is dict:
            data_ids = list(dataset.keys())
        else:
            data_ids = list(range(len(dataset)))

        labels_data_points = defaultdict(list)

        for each_datapoint_id in data_ids:
            for each_label, value in dataset[each_datapoint_id].items():
                if each_label in labels_list and (value == 1 or value == True):
                    labels_data_points[each_label].append(each_datapoint_id)

        return labels_data_points, data_ids