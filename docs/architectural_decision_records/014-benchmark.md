# 14. Use pytest-benchmark to Benchmark the Python Project

## Date

2024-05-28

## Status

Approved

## Context

We need to implement a reliable and consistent way to benchmark our Python project to ensure performance improvements and regressions are easily identifiable. Benchmarking will help us maintain high performance standards and make informed decisions regarding code changes and optimizations.

## Decision

We will use `pytest-benchmark` as the benchmarking tool for our Python project.

## Considered Options

- `pytest-benchmark`
- `timeit` module
- custom benchmarking scripts

## Decision Outcome

Chosen Option: `pytest-benchmark`

We chose pytest-benchmark for the following reasons:

- Ease of Integration: It integrates seamlessly with pytest, which is already used for testing in our project.
- Consistency: Provides a consistent way to write and run benchmarks alongside our existing tests.
- Reporting: Offers detailed and customizable benchmark reports that are easy to analyze.
- Comparison: Facilitates comparison between different benchmark runs, allowing us to track performance changes over time.
- Community and Support: Well-documented with a strong community, ensuring long-term support and ease of finding solutions to potential issues.

## Other Options Considered

### `timeit` module

#### Pros

- Built-in Python module, no additional dependencies.
- Simple and easy to use for small scripts.

#### Cons

- Lacks integration with pytest.
- Less powerful and flexible compared to pytest-benchmark.
- Limited reporting and comparison capabilities.

### Custom Benchmarking Scripts

#### For

- Fully customizable to our specific needs.

#### Against

- Requires significant development effort.
- Higher maintenance burden.
- Reinventing the wheel when established solutions are available.

## Consequences

### Positive

- Efficiency: Streamlines the process of benchmarking, allowing developers to focus on performance improvements rather than tooling.
- Reliability: Ensures consistent and reliable benchmarks.
- Visibility: Provides clear visibility into performance metrics, helping identify bottlenecks early.

### Negative

- Learning Curve: Team members will need to familiarize themselves with pytest-benchmark, though this is mitigated by its extensive documentation.
- Dependency: Introduces an additional dependency to the project.

## Implementation

Install pytest-benchmark: Add pytest-benchmark to the project's dependencies.

```bash
Copy code
pip install pytest-benchmark
```

Write Benchmarks: Create benchmark tests using pytest-benchmark's API.

```python
def test_my_function(benchmark):
    result = benchmark(my_function, *args)
    assert result == expected_result
```

Run Benchmarks: Execute the benchmarks using pytest.

```bash
pytest --benchmark-only
```

or

```bash
nox -s benchmark
```

Analyze Results: Review the generated benchmark reports to make informed decisions about performance optimizations.
