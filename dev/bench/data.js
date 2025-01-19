window.BENCHMARK_DATA = {
  "lastUpdate": 1737308759107,
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
      },
      {
        "commit": {
          "author": {
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "bdc238397b779d0df55cab720f510c435148da38",
          "message": "Update pre-commit hook astral-sh/ruff-pre-commit to v0.9.2 (#712)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-17T04:57:42Z",
          "tree_id": "b41fb65eaab775e15dbb1db725459cb74d764208",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/bdc238397b779d0df55cab720f510c435148da38"
        },
        "date": 1737089895295,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1336.4182253773392,
            "unit": "iter/sec",
            "range": "stddev: 0.00006117236059217923",
            "extra": "mean: 748.2687537560698 usec\nrounds: 1198"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1355.973143054336,
            "unit": "iter/sec",
            "range": "stddev: 0.00000829250962839518",
            "extra": "mean: 737.4777333329001 usec\nrounds: 1290"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1360.299462461443,
            "unit": "iter/sec",
            "range": "stddev: 0.000026556789345895987",
            "extra": "mean: 735.1322466822959 usec\nrounds: 1281"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3532.0036420243036,
            "unit": "iter/sec",
            "range": "stddev: 0.000012148871409481653",
            "extra": "mean: 283.12541586929626 usec\nrounds: 2823"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ab0948d6032950fc8e8553b7a394cc0be5cfba97",
          "message": "Update pre-commit hook rhysd/actionlint to v1.7.7 (#713)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-19T17:45:14Z",
          "tree_id": "4bcbd88015168d335ffa1b489f1a8646b22efa71",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/ab0948d6032950fc8e8553b7a394cc0be5cfba97"
        },
        "date": 1737308757770,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1373.4200872080658,
            "unit": "iter/sec",
            "range": "stddev: 0.000028067617478252077",
            "extra": "mean: 728.1093449221595 usec\nrounds: 1093"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1412.7117538218436,
            "unit": "iter/sec",
            "range": "stddev: 0.000009507624953994873",
            "extra": "mean: 707.8584837244227 usec\nrounds: 1321"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1372.4645504597147,
            "unit": "iter/sec",
            "range": "stddev: 0.000026678000552199946",
            "extra": "mean: 728.6162689339003 usec\nrounds: 1294"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3575.9726501465952,
            "unit": "iter/sec",
            "range": "stddev: 0.00001530026565430981",
            "extra": "mean: 279.6441969317091 usec\nrounds: 2803"
          }
        ]
      }
    ]
  }
}