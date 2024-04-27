#!/usr/bin/env python3
import click
import json
import yaml
import pathlib


import click

@click.command()
@click.argument('fname', type=click.Path(exists=True))

def main(fname):
    with open(fname,"r") as f:
        python_dict=json.load(f)
        
    pth = pathlib.Path(fname)
        
    try:
        yaml_string=yaml.dump(python_dict)
        with open( pth.stem +".yaml", "w") as y:
            y.write(yaml_string)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    main()
