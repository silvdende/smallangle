import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

#creates command for sin function
@cmd_group.command()
#creates option to determine amount of steps
@click.option(
    "-n",
    "--number",
    default = 10,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
@click.option("-n", "--number", default = 10)
def sin(number):
    """gives the sin of NUMBER numbers between 0 and 2pi.
    
    NUMBER is the amount of numbers between 0 and 2pi."""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

#creates command for tan function
@cmd_group.command()
#creates option to determine amount of steps
@click.option(
    "-n",
    "--number",
    default = 10,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
@click.option("-n", "--number", default = 10)
def tan(number):
    """gives the tan of NUMBER numbers between 0 and 2pi.
    
    NUMBER is the amount of numbers between 0 and 2pi."""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()