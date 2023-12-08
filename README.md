![tests](https://github.com/xssChauhan/datasets_saver/actions/workflows/python-app.yml/badge.svg)
# datasets_saver
Export Huggingface datasets in persistable formats uing CLI.

## Installation

1. Clone the repo
2. Install using pip `pip install .`
3. Now it is available as a CLI command.


## CLI Interface

`datasets download --help`
![cli help](images/cli.png)

Example: 
`datasets download imdb` 
This will download the [imdb](https://huggingface.co/datasets/imdb) dataset and persists it in `csv` format.
The default output location is `~/saved_datasets/`.
A dataset can be saved in `csv`, `json` and `parquet` files.
All the splits/files of a dataset are downloaded and stored separately.
The director `~/saved_datasets` is populated as follows:
```shell
$ tree ~/saved_datasets/
.
└── imdb
    ├── test.csv
    ├── train.csv
    └── unsupervised.csv

2 directories, 3 files
```

Similarly, the dataset can be downloaded in `json` and `parquet` files by using the `--format` option:

JSON: `$ datasets download imdb --format json` <br>
Parquet: `$ datasets download imdb --format parquet`
