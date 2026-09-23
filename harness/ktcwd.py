"""Make a harness entry point independent of the caller's working directory."""
import os


HERE = os.path.dirname(os.path.abspath(__file__))


def enter():
    """Run relative-path legacy code from the harness directory."""
    os.chdir(HERE)
