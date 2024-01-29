#!/usr/bin/env python3
"""Hypermedia pagination"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass


def index_range(page, page_size):
    """
    Takes two integer arguments page and page_size
    Returns a tuple
    """
    return 0


def get_page(page=1, page_size=10):
    """Get Page"""
    return 0



def get_hyper(page=1, page_size=10):
    """Hyper pagination"""
    return 0
