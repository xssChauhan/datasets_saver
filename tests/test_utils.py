from unittest.mock import patch
import pytest
from datasets_saver.utils import transform


@pytest.fixture
@patch("datasets.DatasetDict")
@patch("datasets.Dataset")
def test_dataset(dataset_dict, dataset):
    ds = dataset_dict()
    split = dataset()
    ds.items.return_value = [("train", split)]
    return ds, split


def test_transform_csv(test_dataset):
    ds, split = test_dataset
    transform(ds, "imdb", "csv")
    ds.items.assert_called()
    split.to_csv.assert_called_once()


def test_transform_json(test_dataset):
    ds, split = test_dataset
    transform(ds, "imdb", "json")
    ds.items.assert_called()
    split.to_json.assert_called_once()


def test_transform_parquet(test_dataset):
    ds, split = test_dataset
    transform(ds, "imdb", "parquet")
    ds.items.assert_called()
    split.to_parquet.assert_called_once()
