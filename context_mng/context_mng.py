import pathlib
import logging
import os
from decimal import Decimal, localcontext


# 1. Working with files
"""
file_path = pathlib.Path("assessments\General Insurance_____321Z28W_02HBPXPSN007LXB_Assessment Report_page1.tif")

try:
    with file_path.open(mode='rb', encoding='latin1') as file:
        for line in file:
            print(line)

except Exception as e:
    logging.error(f"Reading file failed: {e}")
"""

# 2. Traversing Directories
"""
with os.scandir('./assessments') as entries:
    for entry in entries:
        print(f"{entry.name} -> {entry.stat().st_size}bytes")
"""

# 3. Performing high precision calculations
"""
with localcontext() as ctx:
    ctx.prec = 42
    print(Decimal('22')/Decimal('7'))
"""

# 4. Async with
"""
import asyncio
import aiohttp


async def check_site(site_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(site_url) as response:
            print(f"{site_url} status code is: {response.status}")
            html = await response.text()
            print(html)
            # print(f"{site_url} type is: {html[:17].strip()}")

async def main():
    await asyncio.gather(
    check_site('https://vk-kpower.herokuapp.com/')
    )

asyncio.run(main())
"""

# 5. Class-Based Context Managers
"""
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from pprint import pprint
import sys

class GetCurrentRegions:

    def __enter__(self):
        print("Entering the context")
        try:
            # the url is purposely incorrect. check for correct one
            client = MongoClient(
                'mongodb+srv://kp_root:KPUser22@kp-work.fzwv.mongodb.net/kplc_region_demo?retryWrites=true&w=majority'
            )
            db = client['kplc_region_demo']
            cll = db['regions_v2']
            item = list(cll.find().sort("_id", -1))[0]
            return item
        except ConfigurationError as ce:
            print(ce)


    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context")
        # should close connection here
        if isinstance(exc_value, ConfigurationError):
            print(exc_type, exc_value, exc_tb, sep="\n")
            return True
        else:
            # this else part was not tested. it is supposed to close connection to db
            client.close()




with GetCurrentRegions() as regions:
    pprint(regions)
"""

# 6. Opening Files for reading using pathlib

"""
class ReadableFile:
    def __init__(self, path_to_file):
        self.file_r = pathlib.Path(path_to_file)

    def __enter__(self):
        self.file_obj = open(self.file_r, mode='rb')
        return self.file_obj

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file_obj:
            self.file_obj.close()


# 7. Measuring the execution time of a block of code:

from time import perf_counter

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end = perf_counter()

with Timer() as tm:
    with ReadableFile('test.txt') as rf:
        print(rf.read())

print(tm())
"""

# 8. Implementing context managers in functions
"""
from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode='w')
    try:
        yield file
    finally:
        file.close()

with writable_file('test.txt') as target:
    target.write("Changed contents of this file")
"""

# 9. An indentation API (Domain SPecific Language)
"""
class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self,et,ev,etb):
        self.level -= 1
        # print('Out of context')

    def print(self, txt):
        print("  "*self.level + txt)

with Indenter() as indent:
    indent.print('sample')
    with indent:
        indent.print('another')
"""
