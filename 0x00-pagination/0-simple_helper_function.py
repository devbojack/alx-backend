#!/usr/bin/env python3
""" Simple helper function"""
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size
    Returns a tuple
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
