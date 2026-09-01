# industrial-math-linearization-engine
This repository refactors legacy, hardcoded conditional logic (500+ lines of nested if/else statements or static lookup tables) into a vectorized linear interpolation and scale-factor adjustment engine using NumPy
Here is the complete setup for **`dynamic-linear-interpolation-schema`**.

This repository refactors legacy, hardcoded conditional logic (500+ lines of nested `if/else` statements or static lookup tables) into a vectorized linear interpolation and scale-factor adjustment engine using `NumPy`.


# Dynamic Linear Interpolation Schema

A lightweight, high-performance mathematical engine designed to replace 500+ lines of legacy, hardcoded conditional scripts with vectorized linear interpolation (`NumPy`) and dynamic scale-factor adjustment routines.

Originally developed for telemetry and dashboard data processing within **Aquatic Informatics Aquarius WebPortal** environments.

## Features

* **Legacy Code Reduction:** Replaces hundreds of lines of repetitive `if/else` checks and lookup tables with clean, matrix-backed equation-of-line math schemas.
* **Vectorized Processing:** Evaluates large time-series sensor datasets in milliseconds using NumPy's `np.interp`.
* **Dynamic Scale-Factor Adjustments:** Supports real-time unit offsets, gain calibrations, and multi-segment slope (`y = mx + b`) extractions.

---

## Architecture & Layout

```text
dynamic-linear-interpolation-schema/
├── .github/
│   └── workflows/
│       └── run_tests.yml          # CI workflow
├── src/
│   ├── __init__.py
│   └── equation_schema.py         # Linear scale engine
├── tests/
│   └── test_equation_schema.py    # Unit test suite
├── .gitignore
├── README.md
└── requirements.txt

```

---

## Quickstart

### Installation

```bash
git clone [https://github.com/your-username/dynamic-linear-interpolation-schema.git](https://github.com/your-username/dynamic-linear-interpolation-schema.git)
cd dynamic-linear-interpolation-schema
pip install -r requirements.txt

```

### Basic Usage

```python
from src.equation_schema import LinearScaleEngine

# Define calibration points [(x0, y0), (x1, y1), ...]
calibration_curve = [(0.0, 0.0), (10.0, 50.0), (20.0, 200.0)]

# Initialize engine with a 1.05 scale factor multiplier
engine = LinearScaleEngine(calibration_points=calibration_curve, scale_factor=1.05)

# Single Point Evaluation
output_val = engine.calculate_single(5.0)
print(f"Calculated Value: {output_val}")

# Batch Time-Series Evaluation
raw_dataset = [2.0, 4.0, 6.0, 8.0, 12.0]
scaled_dataset = engine.calculate_batch(raw_dataset)
print(f"Scaled Dataset: {scaled_dataset}")

```

---

## Testing

Run unit tests via `unittest` or `pytest`:

```bash
python -m unittest discover -s tests

```

---

## License

MIT License. Free for open reuse and adaptation.

```

```
