window.BENCHMARK_DATA = {
  "lastUpdate": 1736955156035,
  "repoUrl": "https://github.com/flexion/devops-deployment-metrics",
  "entries": {
    "Pytest-Benchmark Benchmark": [
      {
        "commit": {
          "author": {
            "name": "Tom Willis",
            "username": "tomwillis608",
            "email": "tomwillis608@gmail.com"
          },
          "committer": {
            "name": "Tom Willis",
            "username": "tomwillis608",
            "email": "tomwillis608@gmail.com"
          },
          "id": "ff02938a8aac2947bb48c567b6dbe25efbde0468",
          "message": "Use regular GITHUB_TOKEN, not personal token, to try to  resolve the issue.",
          "timestamp": "2025-01-12T02:51:40Z",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/ff02938a8aac2947bb48c567b6dbe25efbde0468"
        },
        "date": 1736651780963,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1366.9432285813139,
            "unit": "iter/sec",
            "range": "stddev: 0.000033076067005098715",
            "extra": "mean: 731.5592769992744 usec\nrounds: 1213"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1374.510690454399,
            "unit": "iter/sec",
            "range": "stddev: 0.000008549736407514484",
            "extra": "mean: 727.5316277601379 usec\nrounds: 1268"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1360.8732375239836,
            "unit": "iter/sec",
            "range": "stddev: 0.000014727956308040917",
            "extra": "mean: 734.8222982321499 usec\nrounds: 1301"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3647.979247667821,
            "unit": "iter/sec",
            "range": "stddev: 0.000019138168954094742",
            "extra": "mean: 274.12436642541405 usec\nrounds: 2901"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "twillis@flexion.us",
            "name": "Tom Willis",
            "username": "tomwillis608"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "6dfc90f269a404dc3095de98e0aca81c275ea9fe",
          "message": "Merge pull request #709 from flexion/bug/708/fix-benchmark-ci\n\nUse regular GITHUB_TOKEN, not personal token, to try to  resolve the …",
          "timestamp": "2025-01-13T15:43:24-06:00",
          "tree_id": "e05b1bfe985451d6b69384e659f8f1a09114d130",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/6dfc90f269a404dc3095de98e0aca81c275ea9fe"
        },
        "date": 1736804641162,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1383.4975767307787,
            "unit": "iter/sec",
            "range": "stddev: 0.00004379517005995061",
            "extra": "mean: 722.805747418085 usec\nrounds: 1065"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1394.574096125044,
            "unit": "iter/sec",
            "range": "stddev: 0.000056753815618169415",
            "extra": "mean: 717.0648033536509 usec\nrounds: 1312"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1401.619238348266,
            "unit": "iter/sec",
            "range": "stddev: 0.00004695330603451043",
            "extra": "mean: 713.4605266823015 usec\nrounds: 1293"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3543.1872126247063,
            "unit": "iter/sec",
            "range": "stddev: 0.000014758885409692436",
            "extra": "mean: 282.2317704345136 usec\nrounds: 2875"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "twillis@flexion.us",
            "name": "Tom Willis",
            "username": "tomwillis608"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "16edbab5371a2420b6813b8d97e1ccceddc469fe",
          "message": "Merge pull request #707 from flexion/chore/502/block-runners-with-step-security\n\nApply StepSecurity recommendations to block egress",
          "timestamp": "2025-01-15T09:31:58-06:00",
          "tree_id": "df6cef33b7d5e3846051566abfaa96ff374a74ef",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/16edbab5371a2420b6813b8d97e1ccceddc469fe"
        },
        "date": 1736955155091,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1344.5517451317394,
            "unit": "iter/sec",
            "range": "stddev: 0.000063756313112411",
            "extra": "mean: 743.7422945012949 usec\nrounds: 1073"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1371.4542354794564,
            "unit": "iter/sec",
            "range": "stddev: 0.00001142008305728316",
            "extra": "mean: 729.1530217560653 usec\nrounds: 1287"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1382.2357222713572,
            "unit": "iter/sec",
            "range": "stddev: 0.000010705245110869518",
            "extra": "mean: 723.4656027821009 usec\nrounds: 1294"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3616.30060253087,
            "unit": "iter/sec",
            "range": "stddev: 0.000011581935196249207",
            "extra": "mean: 276.5256846458365 usec\nrounds: 2781"
          }
        ]
      }
    ]
  }
}