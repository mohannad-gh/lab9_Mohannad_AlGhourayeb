
import time
import unittest
import memory_profiler

from profiler import (
    slow_function,
    fast_function,
    memory_intensive_function
)


class TestProfiler(unittest.TestCase):

    def time_function(self, func):
        """Measure the execution time of a function."""
        start_time = time.time()
        result = func()
        end_time = time.time()
        return end_time - start_time, result

    def test_slow_function(self):
        duration, result = self.time_function(slow_function)

        print(f"slow_function executed in {duration:.2f} seconds.")

        self.assertGreaterEqual(duration, 2)
        self.assertEqual(result, sum(i ** 2 for i in range(10000)))

    def test_fast_function(self):
        duration, result = self.time_function(fast_function)

        print(f"fast_function executed in {duration:.2f} seconds.")

        self.assertLess(duration, 1)
        self.assertEqual(result, sum(i ** 2 for i in range(100)))

    def test_memory_intensive_function(self):
        mem_usage_before = memory_profiler.memory_usage()[0]

        duration, result = self.time_function(
            memory_intensive_function
        )

        mem_usage_after = memory_profiler.memory_usage()[0]

        print(
            f"memory_intensive_function executed in "
            f"{duration:.2f} seconds."
        )

        print(
            f"Memory usage before: {mem_usage_before:.2f} MiB, "
            f"after: {mem_usage_after:.2f} MiB."
        )

        self.assertEqual(
            result,
            sum(i ** 2 for i in range(10000000))
        )


if __name__ == "__main__":
    unittest.main()
