# Grade Analyzer

A simple command-line tool to calculate university grade averages and estimate the score needed on an upcoming exam to reach a target weighted average.

## Features

- Calculate the **arithmetic average** of all exams
- Calculate the **weighted average** (weighted by CFU/credits)
- **Estimate the grade** needed on a future exam to reach a target weighted average
- Input validation (invalid CFU, out-of-range averages, missing CSV file)

## Requirements

- Python 3.10+
- [pytest](https://pytest.org/) (only needed to run the test suite)

No external dependencies are required to run the tool itself — only the Python standard library (`csv`, `pathlib`).

## Project structure

grade-analyzer/
├── data/
│ └── voti.csv # your exam data
├── src/
│ ├── esame.py # Esame class (single exam: name, CFU, grade)
│ ├── analyzer.py # Analyzer class (reads CSV, computes statistics)
│ └── main.py # CLI entry point
└── tests/
├── conftest.py # makes src/ importable from tests/
└── test_analyzer.py # unit tests for Analyzer



## CSV format

`data/voti.csv` must have this exact header, one row per exam:

```csv
esame,cfu,voto
Analisi Matematica 1,9,28
Fondamenti di Programmazione,9,30
Fisica 1,6,25
```

| Column  | Meaning         |
|---------|-----------------|
| `esame` | Exam name       |
| `cfu`   | Credits (CFU)   |
| `voto`  | Grade (18–30)   |

## Usage

From the `src/` folder, run:

```bash
cd src
python main.py
```

**Example — weighted average:**

2
Your current weighted average is: 27.60


**Example — grade estimation:**

3
How many CFU is the exam worth: 6
Target average: 25
18.5


## Running the tests

From the project root:

```bash
pytest
```

## Design notes

- The weighted average is computed as `sum(voto × cfu) / sum(cfu)`, not divided by the number of exams — this correctly reflects that heavier exams (more CFU) count more toward the final average.
- The grade estimation solves a linear equation for the unknown grade, given the current weighted total and the CFU of the upcoming exam. If the required grade exceeds 30, the target is reported as unreachable.

## Author

Federico ([@fefedip](https://github.com/fefedip))