import click
import os
import sys

from schema import GeocoverSchema

DEFAULT_WORKSPACE = r"D:/connections/GCOVERP@osa.sde"

try:
    curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
except NameError:
    curdir = r"H:\code\lg-geology-data-model"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))


@click.command(context_settings={"show_default": True})
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False),
    help="The directory for the output",
    default=DEFAULT_OUTPUT_DIR,
)
@click.option(
    "-w",
    "--workspace",
    type=str,
    help="Workspace (SDE string or GDB)",
    default=DEFAULT_WORKSPACE,
)

def main(output_dir, workspace):

    from encoder import ExtendedEncoder

    so = GeocoverSchema.instance(workspace)

    print(so)
    print(so.tables)
    print(so.domains, type(so.domains[0]))

    encoder = ExtendedEncoder()
    print(encoder.to_json(so.domains, indent=4))

    print(encoder.to_yaml(so.domains))



if __name__ == "__main__":
    main()

