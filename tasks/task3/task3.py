import json
import sys


def fill_values(test, values_map):
    test_id = test.get("id")

    if test_id in values_map:
        test["value"] = values_map[test_id]

    if "values" in test:
        for nested_test in test["values"]:
            fill_values(nested_test, values_map)


values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file, "r", encoding="utf-8") as f:
    values_data = json.load(f)

with open(tests_file, "r", encoding="utf-8") as f:
    tests_data = json.load(f)

values_map = {
    item["id"]: item["value"]
    for item in values_data["values"]
}

for test in tests_data["tests"]:
    fill_values(test, values_map)

with open(report_file, "w", encoding="utf-8") as f:
    json.dump(tests_data, f, ensure_ascii=False, indent=2)