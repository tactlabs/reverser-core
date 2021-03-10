import argparse
import json
import pprint
from xml.dom import minidom

from reverser import RevClient


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Python3 Reverser')
    
    # Parse command line arguments
    r_client = RevClient()
    r_client.rev_me("Hello World!")