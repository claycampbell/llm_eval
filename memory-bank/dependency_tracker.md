# Module Dependency Tracker

## Key Definitions
1A: utils/  # Contains core utility functions
1B: tests/  # Contains test modules
1C: data/   # Contains data storage

## Dependencies
X 1A 1B 1C
1A = onn  # utils/ has no module-level dependencies
1B = <on  # tests/ depends on utils/
1C = nno  # data/ has no module-level dependencies

## Notes
- utils/processing.py depends on utils/config.py (internal module dependency, tracked in mini-tracker)
- tests/utils/test_*.py files depend on corresponding utils/*.py files
- No direct dependencies on data/ module observed