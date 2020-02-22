import argparse


class Command:
    """Base class for command-line programs."""
    
    def __init__(self):
        self.description = self.__class__.__doc__

    def __call__(self):
        args = self.parse_args()

    def get_argument_parser(self):
        """Define command-line arguments."""
        parser = argparse.ArgumentParser(
            description=self.description
        )

        return parser

    def parse_args(self):
        """Parse command-line arguments."""
        parser = self.get_argument_parser()

        return parser.parse_args()
