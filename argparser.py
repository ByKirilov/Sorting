import argparse


def parse_args():
    """Command-line arguments parser"""
    parser = argparse.ArgumentParser(description="EXTERNAL SORTING: "
                                                 "Sorts large files that do not fit into memory")
    parser.add_argument('file_path', type=str, nargs='?', default=None, help="path to the file you want to sort")
    parser.add_argument('buffer_size', type=int, nargs='?', default=None, help="size of memory in bytes")
    parser.add_argument('comparator', type=str, nargs='?', default=None, help="sorting comparator"
                        "available comparators:"
                        "'lex' - lexicographical order"
                        "'length' - length order"
                        "'random' - random order")
    parser.add_argument('-r', action="store_true", help="reverse order")
    return parser.parse_args()
