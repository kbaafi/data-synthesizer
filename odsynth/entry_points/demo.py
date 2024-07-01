import typer
from typing_extensions import Annotated

from odsynth.data_generator import DataGenerator
from odsynth.transformers import JsonTransformer, PandasDataframeTransformer
from odsynth.utils import load_yaml

app = typer.Typer()


@app.command()
def main(
    schema_spec: Annotated[
        str, typer.Option(help="Location of schema definition for data generation")
    ],
    num_samples: Annotated[int, typer.Option(help="Number of samples to be generated")],
    plugins_dir: Annotated[
        str, typer.Option(help="Location for user added data generation providers.")
    ] = None,
):
    schema = load_yaml(schema_spec)
    generator = DataGenerator(
        schema=schema,
        plugins_dir=plugins_dir,
        num_examples=num_samples,
        transformer=PandasDataframeTransformer(),
    )
    for data in generator.yield_data():
        print(data, "\n")
    print(generator.get_data())


if __name__ == "__main__":
    app()
