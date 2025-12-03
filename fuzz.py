import random
import string
import os
import time
from datetime import datetime
from pathlib import Path
import traceback

# Import your mining functions
from mining.mining import (
    giveTimeStamp,
    makeChunks,
    dumpContentIntoFile,
    days_between,
    getPythonFileCount,
)

# LOGFILE setup – always created, always contains something
LOGFILE = Path("fuzz_results.log")
LOGFILE.touch(exist_ok=True)

# Ensure artifact always has content
with open(LOGFILE, "w") as f:
    f.write("Fuzzing started.\n")


def log_failure(func, inputs, exc):
    with open(LOGFILE, "a") as f:
        f.write("\n" + "=" * 70 + "\n")
        f.write(f"Function: {func}\n")
        f.write(f"Inputs: {inputs}\n")
        f.write(f"Exception: {repr(exc)}\n")
        f.write("Traceback:\n")
        traceback.print_exc(file=f)


def fuzz_giveTimeStamp():
    for _ in range(200):
        try:
            giveTimeStamp()
        except Exception as e:
            log_failure("giveTimeStamp", None, e)


def fuzz_makeChunks():
    for _ in range(200):
        lst = [random.randint(0, 100) for _ in range(random.randint(0, 20))]
        size = random.randint(-5, 20)
        try:
            list(makeChunks(lst, size))
        except Exception as e:
            log_failure("makeChunks", (lst, size), e)


def fuzz_dumpContentIntoFile():
    for _ in range(200):
        content = "".join(random.choice(string.ascii_letters) for _ in range(20))
        file = f"tmp_fuzz_{random.randint(0, 9999)}.txt"
        try:
            dumpContentIntoFile(content, file)
        except Exception as e:
            log_failure("dumpContentIntoFile", (content, file), e)
        finally:
            if os.path.exists(file):
                os.remove(file)


def fuzz_days_between():
    for _ in range(200):
        try:
            d1 = datetime.fromtimestamp(random.randint(0, int(time.time())))
            d2 = datetime.fromtimestamp(random.randint(0, int(time.time())))
            days_between(d1, d2)
        except Exception as e:
            log_failure("days_between", (d1, d2), e)


def fuzz_getPythonFileCount():
    for _ in range(200):
        # random directories
        path = random.choice([".", "./mining", "./empirical", "./does_not_exist"])
        try:
            getPythonFileCount(path)
        except Exception as e:
            log_failure("getPythonFileCount", path, e)


def main():
    print("Running fuzzing...")

    fuzz_giveTimeStamp()
    fuzz_makeChunks()
    fuzz_dumpContentIntoFile()
    fuzz_days_between()
    fuzz_getPythonFileCount()

    print("Fuzzing complete.")
    print("Check fuzz_results.log for failures.")


if __name__ == "__main__":
    main()
