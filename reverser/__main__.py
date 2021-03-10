import argparse
import json
import pprint
from xml.dom import minidom

from reverser.rclient import RevClient


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Python3 Reverser Client')
    
    # Parse command line arguments
    r_client = RevClient()
    r_client.rev_me("Hello World!")