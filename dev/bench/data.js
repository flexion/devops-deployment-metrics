window.BENCHMARK_DATA = {
  "lastUpdate": 1739370186269,
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
          "id": "f48065aa8942eaacc4522684b65fb6658b89d2a4",
          "message": "Update step-security/harden-runner action to v2.10.4 (#714)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-20T05:22:26Z",
          "tree_id": "f2cf828f98a9bf1ea5c314529bd9fa8197a23442",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/f48065aa8942eaacc4522684b65fb6658b89d2a4"
        },
        "date": 1737350581084,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1344.2608709185174,
            "unit": "iter/sec",
            "range": "stddev: 0.000010814363037945167",
            "extra": "mean: 743.9032271442312 usec\nrounds: 1061"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1334.0476260120042,
            "unit": "iter/sec",
            "range": "stddev: 0.000019971588169537985",
            "extra": "mean: 749.5984254995418 usec\nrounds: 1302"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1326.247726659677,
            "unit": "iter/sec",
            "range": "stddev: 0.00006116888481370792",
            "extra": "mean: 754.0069474943621 usec\nrounds: 1257"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3590.434575842534,
            "unit": "iter/sec",
            "range": "stddev: 0.00001274208308367596",
            "extra": "mean: 278.5178169596195 usec\nrounds: 2901"
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
          "id": "13002397e36bd0a883fa29ad6d8d421cac632431",
          "message": "Update github/codeql-action action to v3.28.2 (#715)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-22T05:04:52Z",
          "tree_id": "103ddab84413d45430b505d9e10566ef10a341fe",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/13002397e36bd0a883fa29ad6d8d421cac632431"
        },
        "date": 1737522326400,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1367.008244215472,
            "unit": "iter/sec",
            "range": "stddev: 0.000008912559439485141",
            "extra": "mean: 731.5244836536458 usec\nrounds: 1040"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1353.953586651619,
            "unit": "iter/sec",
            "range": "stddev: 0.000009292653613129371",
            "extra": "mean: 738.5777547020942 usec\nrounds: 1276"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1355.8822875947217,
            "unit": "iter/sec",
            "range": "stddev: 0.000009502242330770884",
            "extra": "mean: 737.5271505124225 usec\nrounds: 1269"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3547.8816649742494,
            "unit": "iter/sec",
            "range": "stddev: 0.00003364781166066712",
            "extra": "mean: 281.858329682272 usec\nrounds: 2830"
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
          "id": "00ae450f6da7e5540c7d0bd345f7b10962edfa4c",
          "message": "Update github/codeql-action action to v3.28.3 (#716)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-23T05:01:23Z",
          "tree_id": "5bf38846defbf7629943b0ff760ec3b65acdeba8",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/00ae450f6da7e5540c7d0bd345f7b10962edfa4c"
        },
        "date": 1737608518679,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1372.8956855487372,
            "unit": "iter/sec",
            "range": "stddev: 0.00003800100220680696",
            "extra": "mean: 728.387459095486 usec\nrounds: 1039"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1357.9341808224244,
            "unit": "iter/sec",
            "range": "stddev: 0.000057091868334939264",
            "extra": "mean: 736.4127172896967 usec\nrounds: 1284"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1377.6118959361556,
            "unit": "iter/sec",
            "range": "stddev: 0.00003652538381888066",
            "extra": "mean: 725.8938478608668 usec\nrounds: 1262"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3555.598695594974,
            "unit": "iter/sec",
            "range": "stddev: 0.00001455011864113918",
            "extra": "mean: 281.24658759687884 usec\nrounds: 2580"
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
          "id": "84771418340d79f45d46f168f891a08132aed6e1",
          "message": "Update patch dependencies (#718)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-24T05:33:03Z",
          "tree_id": "1c42d3e12e36f676de06dc47a127aabb974104df",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/84771418340d79f45d46f168f891a08132aed6e1"
        },
        "date": 1737696823558,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1369.8304874682274,
            "unit": "iter/sec",
            "range": "stddev: 0.00007962592235382431",
            "extra": "mean: 730.0173336397542 usec\nrounds: 1088"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1379.9176802402023,
            "unit": "iter/sec",
            "range": "stddev: 0.00006371632057029642",
            "extra": "mean: 724.6809098249469 usec\nrounds: 743"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1355.8127641191218,
            "unit": "iter/sec",
            "range": "stddev: 0.00014465396862443973",
            "extra": "mean: 737.5649694887665 usec\nrounds: 1311"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3552.8049636540045,
            "unit": "iter/sec",
            "range": "stddev: 0.000013966199162448982",
            "extra": "mean: 281.46774456527316 usec\nrounds: 2944"
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
          "id": "eb1410483d25d39a8f152d5b09f8bdd0575967cc",
          "message": "Update github/codeql-action action to v3.28.5 (#719)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-25T04:55:45Z",
          "tree_id": "ded0c9455f52f8b17a765af8f770f21cf4b98e5f",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/eb1410483d25d39a8f152d5b09f8bdd0575967cc"
        },
        "date": 1737780980627,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1324.045064250017,
            "unit": "iter/sec",
            "range": "stddev: 0.000009796537215100629",
            "extra": "mean: 755.26130265546 usec\nrounds: 1130"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1349.055260278927,
            "unit": "iter/sec",
            "range": "stddev: 0.00001655099800122346",
            "extra": "mean: 741.2594794621257 usec\nrounds: 1266"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1334.4602399612907,
            "unit": "iter/sec",
            "range": "stddev: 0.000009283473250817941",
            "extra": "mean: 749.3666503162412 usec\nrounds: 1264"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3596.6860687886497,
            "unit": "iter/sec",
            "range": "stddev: 0.00001816662461322714",
            "extra": "mean: 278.03371794881065 usec\nrounds: 2886"
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
          "id": "e60c38b6a3b557100653b1f6acc6577c8a27ba3c",
          "message": "Update actions/setup-python digest to 4237552 (#722)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-28T12:28:17Z",
          "tree_id": "82fd26760c7ca94f7bc4adc0d1e8ff0d351e1e66",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/e60c38b6a3b557100653b1f6acc6577c8a27ba3c"
        },
        "date": 1738067331941,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1329.2076754979828,
            "unit": "iter/sec",
            "range": "stddev: 0.000051223418823964646",
            "extra": "mean: 752.3278855769123 usec\nrounds: 1040"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1328.6114777812297,
            "unit": "iter/sec",
            "range": "stddev: 0.000059051404353284004",
            "extra": "mean: 752.6654832682854 usec\nrounds: 1285"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1345.4915965577416,
            "unit": "iter/sec",
            "range": "stddev: 0.0000119478509234443",
            "extra": "mean: 743.2227763877269 usec\nrounds: 1279"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3583.253099692056,
            "unit": "iter/sec",
            "range": "stddev: 0.000013791569170254892",
            "extra": "mean: 279.07601617254994 usec\nrounds: 2968"
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
          "id": "caba0a76f8699b29fff4bdbf284ece9a7295b91e",
          "message": "Update github/codeql-action action to v3.28.6 (#723)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-28T16:42:05Z",
          "tree_id": "350fda1d8a0b0463c73c6319456473409386a3b6",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/caba0a76f8699b29fff4bdbf284ece9a7295b91e"
        },
        "date": 1738082566912,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1335.9696799518597,
            "unit": "iter/sec",
            "range": "stddev: 0.000009992437886760508",
            "extra": "mean: 748.5199814085855 usec\nrounds: 1022"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1358.3117771021916,
            "unit": "iter/sec",
            "range": "stddev: 0.000010451870501611206",
            "extra": "mean: 736.2080023581846 usec\nrounds: 1272"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1323.595437933436,
            "unit": "iter/sec",
            "range": "stddev: 0.00009998808513583834",
            "extra": "mean: 755.5178654599521 usec\nrounds: 1271"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3494.9274793756517,
            "unit": "iter/sec",
            "range": "stddev: 0.00001912970213734885",
            "extra": "mean: 286.12897002905595 usec\nrounds: 2736"
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
          "id": "5001761661138638ec08947217a1166ea717d852",
          "message": "Update github/codeql-action action to v3.28.7 (#724)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-29T16:33:34Z",
          "tree_id": "de711200bbdc88121bc55b0465ea53157a93d0a2",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/5001761661138638ec08947217a1166ea717d852"
        },
        "date": 1738168454286,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1332.482574203216,
            "unit": "iter/sec",
            "range": "stddev: 0.000008391337146707623",
            "extra": "mean: 750.4788575550186 usec\nrounds: 1039"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1328.1379323140618,
            "unit": "iter/sec",
            "range": "stddev: 0.000009801621315691895",
            "extra": "mean: 752.9338449491195 usec\nrounds: 1277"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1343.9401837596617,
            "unit": "iter/sec",
            "range": "stddev: 0.0000091148705499748",
            "extra": "mean: 744.0807352024464 usec\nrounds: 1284"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3535.8846672204404,
            "unit": "iter/sec",
            "range": "stddev: 0.000011384590107001443",
            "extra": "mean: 282.8146543552565 usec\nrounds: 2870"
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
          "id": "4f6807024911fecba843bb24f725da3a7cb7759c",
          "message": "Merge pull request #706 from flexion/chore/695/fix-sca-workflow\n\nRestore SCA dependency scanning",
          "timestamp": "2025-01-29T13:45:43-06:00",
          "tree_id": "6f36489293fa12b8fe717a18eacdd58950dfcdbc",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/4f6807024911fecba843bb24f725da3a7cb7759c"
        },
        "date": 1738179992218,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1302.5507910180177,
            "unit": "iter/sec",
            "range": "stddev: 0.000009932333841813745",
            "extra": "mean: 767.72438118781 usec\nrounds: 1010"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1268.5788921082724,
            "unit": "iter/sec",
            "range": "stddev: 0.00017313531559484612",
            "extra": "mean: 788.2836504855313 usec\nrounds: 1236"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1325.3900008743155,
            "unit": "iter/sec",
            "range": "stddev: 0.00004755557480997062",
            "extra": "mean: 754.4949028892125 usec\nrounds: 1246"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3519.521509855603,
            "unit": "iter/sec",
            "range": "stddev: 0.0000272125924914726",
            "extra": "mean: 284.12953215365553 usec\nrounds: 2939"
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
          "id": "0dce736605c6649e9bfc4a2f221b5310a9bb591c",
          "message": "Update github/codeql-action action to v3.28.8 (#725)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-30T05:45:38Z",
          "tree_id": "bc763f3ec8340b75ff065f028ea9d9c896a8a070",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/0dce736605c6649e9bfc4a2f221b5310a9bb591c"
        },
        "date": 1738215970827,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1374.8530346927,
            "unit": "iter/sec",
            "range": "stddev: 0.000008430059999250145",
            "extra": "mean: 727.3504692983529 usec\nrounds: 1140"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1380.0379907544584,
            "unit": "iter/sec",
            "range": "stddev: 0.000008771886508731883",
            "extra": "mean: 724.6177327722015 usec\nrounds: 1306"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1373.4828505601986,
            "unit": "iter/sec",
            "range": "stddev: 0.000012098991105622953",
            "extra": "mean: 728.0760728771626 usec\nrounds: 1331"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3577.0556750214396,
            "unit": "iter/sec",
            "range": "stddev: 0.000013871479564737842",
            "extra": "mean: 279.559529079459 usec\nrounds: 3009"
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
          "id": "85165f3ab14b85f2a3a1a2c5ead48860312a2ee5",
          "message": "Update pre-commit hook astral-sh/ruff-pre-commit to v0.9.4 (#726)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-01-31T05:39:33Z",
          "tree_id": "7a1bc60b6d00c061de70061de5faf3a1fe519348",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/85165f3ab14b85f2a3a1a2c5ead48860312a2ee5"
        },
        "date": 1738302005452,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1327.4258511105916,
            "unit": "iter/sec",
            "range": "stddev: 0.000009036970109872096",
            "extra": "mean: 753.3377470111415 usec\nrounds: 1004"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1335.6563531122586,
            "unit": "iter/sec",
            "range": "stddev: 0.000024010956064392055",
            "extra": "mean: 748.6955740298512 usec\nrounds: 1263"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1338.0389859474126,
            "unit": "iter/sec",
            "range": "stddev: 0.000029452874272621355",
            "extra": "mean: 747.3623791999898 usec\nrounds: 1250"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3542.0685146045857,
            "unit": "iter/sec",
            "range": "stddev: 0.00001049743254892444",
            "extra": "mean: 282.3209082141749 usec\nrounds: 3007"
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
          "id": "c52572211f04c7d6b4d20662f6b0f58902944452",
          "message": "Merge pull request #721 from flexion/dependabot/github_actions/codecov/codecov-action-5.3.1\n\nBump codecov/codecov-action from 5.1.2 to 5.3.1",
          "timestamp": "2025-02-05T21:16:55-06:00",
          "tree_id": "74be8a7c2942dc15dd86ae7964d9498171c07e5f",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/c52572211f04c7d6b4d20662f6b0f58902944452"
        },
        "date": 1738811849434,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1303.7498995288513,
            "unit": "iter/sec",
            "range": "stddev: 0.00004131011541560029",
            "extra": "mean: 767.0182757915301 usec\nrounds: 979"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1306.1816156312304,
            "unit": "iter/sec",
            "range": "stddev: 0.00007143434972665709",
            "extra": "mean: 765.5903191660955 usec\nrounds: 1247"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1314.2738576326603,
            "unit": "iter/sec",
            "range": "stddev: 0.000017847856138547436",
            "extra": "mean: 760.8764293624869 usec\nrounds: 722"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3501.095102241928,
            "unit": "iter/sec",
            "range": "stddev: 0.000015761261943583385",
            "extra": "mean: 285.6249175749752 usec\nrounds: 2936"
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
          "id": "f011fcdd68475a201c174e974d8ba567a201959c",
          "message": "Merge pull request #720 from flexion/dependabot/github_actions/dependabot/fetch-metadata-2.3.0\n\nBump dependabot/fetch-metadata from 2.2.0 to 2.3.0",
          "timestamp": "2025-02-05T23:55:12-06:00",
          "tree_id": "978e2e379aef1c40c3fcfabdf153bee2a59b7323",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/f011fcdd68475a201c174e974d8ba567a201959c"
        },
        "date": 1738821345540,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1326.6751281916634,
            "unit": "iter/sec",
            "range": "stddev: 0.00003862052871134763",
            "extra": "mean: 753.7640366885141 usec\nrounds: 1063"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1321.158215036381,
            "unit": "iter/sec",
            "range": "stddev: 0.000009128202840268709",
            "extra": "mean: 756.9116163520678 usec\nrounds: 1272"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1320.8055234159397,
            "unit": "iter/sec",
            "range": "stddev: 0.000007628214138906142",
            "extra": "mean: 757.1137326968055 usec\nrounds: 1257"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3576.2695174388696,
            "unit": "iter/sec",
            "range": "stddev: 0.000009311127556156602",
            "extra": "mean: 279.62098357624507 usec\nrounds: 2679"
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
          "id": "a5797597f2c9aa33faaef1ac43209b36aa23fe1e",
          "message": "Update pre-commit hook astral-sh/ruff-pre-commit to v0.9.5 (#727)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-02-07T04:40:15Z",
          "tree_id": "8f42843f073ae554147604aafed45b3749610b98",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/a5797597f2c9aa33faaef1ac43209b36aa23fe1e"
        },
        "date": 1738903254930,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1321.9299485135919,
            "unit": "iter/sec",
            "range": "stddev: 0.000017847819701327414",
            "extra": "mean: 756.4697366334901 usec\nrounds: 1010"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1306.8084891964547,
            "unit": "iter/sec",
            "range": "stddev: 0.000052037961810467435",
            "extra": "mean: 765.2230669353022 usec\nrounds: 1240"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1316.7069311365797,
            "unit": "iter/sec",
            "range": "stddev: 0.00011946964247086834",
            "extra": "mean: 759.4704458165199 usec\nrounds: 729"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3551.5336713494053,
            "unit": "iter/sec",
            "range": "stddev: 0.000014373596295115039",
            "extra": "mean: 281.5684975950263 usec\nrounds: 2703"
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
          "id": "9649018025200bb7256a1820c432239a676cc2fb",
          "message": "Update github/codeql-action action to v3.28.9 (#728)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2025-02-07T18:14:27Z",
          "tree_id": "0668f8fca49080b5e649694dd2ef3ce7916cf6f7",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/9649018025200bb7256a1820c432239a676cc2fb"
        },
        "date": 1738952107369,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1302.9249272098111,
            "unit": "iter/sec",
            "range": "stddev: 0.000012986281202724567",
            "extra": "mean: 767.5039283663725 usec\nrounds: 1047"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1307.4940551777217,
            "unit": "iter/sec",
            "range": "stddev: 0.000011567922684635218",
            "extra": "mean: 764.8218330629998 usec\nrounds: 1234"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1305.7327028134728,
            "unit": "iter/sec",
            "range": "stddev: 0.000015335332707237125",
            "extra": "mean: 765.8535302403716 usec\nrounds: 1207"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3543.5826382840933,
            "unit": "iter/sec",
            "range": "stddev: 0.0000264035520660333",
            "extra": "mean: 282.20027640846257 usec\nrounds: 2840"
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
          "id": "28ec5adbf448a18bf6700f76574d8273eef982ca",
          "message": "Merge pull request #705 from flexion/chore/692/migrate-to-uv\n\nContinue  migration to uv",
          "timestamp": "2025-02-09T17:08:59-06:00",
          "tree_id": "011d85590ad18a47ba2bc420205e9bf75d0682ac",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/28ec5adbf448a18bf6700f76574d8273eef982ca"
        },
        "date": 1739142572035,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1318.5563138608572,
            "unit": "iter/sec",
            "range": "stddev: 0.000010518384671075917",
            "extra": "mean: 758.4052266011345 usec\nrounds: 1015"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1325.4761494671488,
            "unit": "iter/sec",
            "range": "stddev: 0.00002130220614228147",
            "extra": "mean: 754.44586490825 usec\nrounds: 1251"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1306.2979138772885,
            "unit": "iter/sec",
            "range": "stddev: 0.000029758549671564703",
            "extra": "mean: 765.522159514019 usec\nrounds: 1235"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3531.552554730666,
            "unit": "iter/sec",
            "range": "stddev: 0.000016252495883629535",
            "extra": "mean: 283.1615796458861 usec\nrounds: 2938"
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
          "id": "82216747b5992d4b71e461bad0686c8855f8e050",
          "message": "Merge pull request #730 from flexion/bug/729/zricethezavgitleaks-at-v8212\n\nConfigure renovate not to update zricethezav/gitleaks for now",
          "timestamp": "2025-02-10T20:55:09-06:00",
          "tree_id": "d99479f0e0ce017ab5ee0ab9fe34115fed15f3c0",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/82216747b5992d4b71e461bad0686c8855f8e050"
        },
        "date": 1739242542306,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1370.9322643209987,
            "unit": "iter/sec",
            "range": "stddev: 0.00004872169813461446",
            "extra": "mean: 729.430640758378 usec\nrounds: 1055"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1360.2125017187627,
            "unit": "iter/sec",
            "range": "stddev: 0.00005179540386391407",
            "extra": "mean: 735.179244960917 usec\nrounds: 1290"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1371.0306252094035,
            "unit": "iter/sec",
            "range": "stddev: 0.000014432720205979608",
            "extra": "mean: 729.3783097275931 usec\nrounds: 1285"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3504.5567045760986,
            "unit": "iter/sec",
            "range": "stddev: 0.000009329859294772847",
            "extra": "mean: 285.3427934820524 usec\nrounds: 2915"
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
          "id": "0dfab7cf5bf15bd510bcd489d5753dae34e05285",
          "message": "Merge pull request #717 from flexion/renovate/all-minor\n\nUpdate minor dependencies",
          "timestamp": "2025-02-10T20:58:06-06:00",
          "tree_id": "3d04a4a91fd10a0b184dad240c13d742ee86a85a",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/0dfab7cf5bf15bd510bcd489d5753dae34e05285"
        },
        "date": 1739242719229,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1307.656014451968,
            "unit": "iter/sec",
            "range": "stddev: 0.000020883699751000453",
            "extra": "mean: 764.7271063247432 usec\nrounds: 1091"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1297.2740022946653,
            "unit": "iter/sec",
            "range": "stddev: 0.000041092884431219334",
            "extra": "mean: 770.8471751003749 usec\nrounds: 1245"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1301.1840893794595,
            "unit": "iter/sec",
            "range": "stddev: 0.000024958150515241842",
            "extra": "mean: 768.530762220513 usec\nrounds: 1207"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3428.587406436768,
            "unit": "iter/sec",
            "range": "stddev: 0.000025202223046773004",
            "extra": "mean: 291.66530744487306 usec\nrounds: 2807"
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
          "id": "9611dc7b1edb1a797cff04dcac959d085e38e5d8",
          "message": "Merge pull request #733 from flexion/renovate/all-patch\n\nUpdate pre-commit hook astral-sh/ruff-pre-commit to v0.9.6",
          "timestamp": "2025-02-10T21:05:40-06:00",
          "tree_id": "a72970b5de8c0cf1c64e061836c7155f43be2c66",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/9611dc7b1edb1a797cff04dcac959d085e38e5d8"
        },
        "date": 1739243173024,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1374.900889227855,
            "unit": "iter/sec",
            "range": "stddev: 0.000010257680644432657",
            "extra": "mean: 727.3251532782122 usec\nrounds: 1083"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1377.390846490565,
            "unit": "iter/sec",
            "range": "stddev: 0.000009650228690211319",
            "extra": "mean: 726.0103423424702 usec\nrounds: 1221"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1350.4408893992675,
            "unit": "iter/sec",
            "range": "stddev: 0.00002184499635985261",
            "extra": "mean: 740.4989050982023 usec\nrounds: 1275"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3612.0866696982803,
            "unit": "iter/sec",
            "range": "stddev: 0.000009815707318198566",
            "extra": "mean: 276.8482850616457 usec\nrounds: 2845"
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
          "id": "0ae570a2e0c4149aabf05964af9c53a5cc49b924",
          "message": "Merge pull request #734 from flexion/renovate/all-patch\n\nUpdate dependency myst_parser to v4.0.1",
          "timestamp": "2025-02-12T08:22:27-06:00",
          "tree_id": "027d7e733529e61ba07a42b33a99a486221aaf95",
          "url": "https://github.com/flexion/devops-deployment-metrics/commit/0ae570a2e0c4149aabf05964af9c53a5cc49b924"
        },
        "date": 1739370185662,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_metrics.py::test_deployment_frequency_metric",
            "value": 1310.0941523194285,
            "unit": "iter/sec",
            "range": "stddev: 0.00002068900492510828",
            "extra": "mean: 763.3039184470606 usec\nrounds: 1030"
          },
          {
            "name": "tests/test_metrics.py::test_change_fail_rate_metric",
            "value": 1303.7016379926451,
            "unit": "iter/sec",
            "range": "stddev: 0.000010994341591283934",
            "extra": "mean: 767.0466699265139 usec\nrounds: 1227"
          },
          {
            "name": "tests/test_metrics.py::test_mean_time_to_recovery_metric",
            "value": 1294.5682493672264,
            "unit": "iter/sec",
            "range": "stddev: 0.00002178319366140268",
            "extra": "mean: 772.4583083887553 usec\nrounds: 1216"
          },
          {
            "name": "tests/test_config.py::test_config",
            "value": 3599.8848712225636,
            "unit": "iter/sec",
            "range": "stddev: 0.00001716976932933047",
            "extra": "mean: 277.78666145520043 usec\nrounds: 1855"
          }
        ]
      }
    ]
  }
}