import typer

from datasets_saver.utils import load, transform

from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def download(
    dataset_name: Annotated[
        str, typer.Argument(help="Name of the dataset to download")
    ],
    format: Annotated[
        str,
        typer.Option(
            help="The format of persisting the dataset. Choose from csv, json, parquet",
        ),
    ] = "csv",
):
    """Download a huggingface dataset."""
    typer.echo(f"Downloading {dataset_name}")
    dataset = load(dataset_name)
    transform(dataset, dataset_name, format)


@app.callback()
def callback():
    pass
