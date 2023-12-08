from pathlib import Path

from datasets import Dataset, load_dataset

transform_types = ["csv", "json", "parquet"]


def get_default_output_dir(name) -> Path:
    """Get the path of default output directory.

    :param name: _description_
    :type name: _type_
    :return: _description_
    :rtype: Path
    """
    output_dir = Path.home() / "saved_datasets" / name
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir


def load(dataset_name: str):
    dataset = load_dataset(dataset_name)

    return dataset


def transform(dataset: Dataset, name: str, transform_type: str) -> None:
    """Transform the dataset and persist on disk.

    :param dataset: dataset object
    :type dataset: Dataset
    :param name: name of the dataset
    :type name: str
    :param transform_type: the output format
    :type transform_type: str
    """
    assert (
        transform_type in transform_types
    ), f"The output type should be one of {','.join(transform_types)}"
    output_dir = get_default_output_dir(name)
    for split_name, split in dataset.items():
        if transform_type == "csv":
            split.to_csv(output_dir / (split_name + ".csv"))
        if transform_type == "json":
            split.to_json(output_dir / (split_name + ".json"))
        if transform_type == "parquet":
            split.to_parquet(output_dir / (split_name + ".parquet"))
