import numpy as np
from typing import List, Tuple, Union

class LinearScaleEngine:
    """
    Replaces multi-case legacy routines with dynamic equation-of-line math schemas
    and scale-factor adjustments for hydrometric/environmental sensor data.
    """

    def __init__(self, calibration_points: List[Tuple[float, float]], scale_factor: float = 1.0):
        """
        :param calibration_points: List of (x, y) tuples defining the line schema / rating curve.
        :param scale_factor: Dynamic multiplier for sensor scaling or unit offset.
        """
        if len(calibration_points) < 2:
            raise ValueError("At least two calibration points are required to establish an equation of line.")
        
        # Sort points by X ascending
        sorted_points = sorted(calibration_points, key=lambda p: p[0])
        self.x_coords = np.array([p[0] for p in sorted_points], dtype=np.float64)
        self.y_coords = np.array([p[1] for p in sorted_points], dtype=np.float64)
        self.scale_factor = float(scale_factor)

    def calculate_single(self, raw_value: float) -> float:
        """Calculates interpolated y for a single input value."""
        result = np.interp(raw_value, self.x_coords, self.y_coords)
        return float(result * self.scale_factor)

    def calculate_batch(self, raw_values: Union[List[float], np.ndarray]) -> np.ndarray:
        """
        Vectorized evaluation across dataset arrays.
        Replaces 500+ line legacy loops with efficient matrix math.
        """
        inputs = np.asarray(raw_values, dtype=np.float64)
        interpolated = np.interp(inputs, self.x_coords, self.y_coords)
        return interpolated * self.scale_factor

    def compute_slope_intercept(self, segment_idx: int = 0) -> Tuple[float, float]:
        """
        Extracts the explicit slope (m) and intercept (b) for a specific line segment: y = mx + b
        """
        if segment_idx < 0 or segment_idx >= len(self.x_coords) - 1:
            raise IndexingError("Invalid segment index.")

        x1, x2 = self.x_coords[segment_idx], self.x_coords[segment_idx + 1]
        y1, y2 = self.y_coords[segment_idx], self.y_coords[segment_idx + 1]

        m = (y2 - y1) / (x2 - x1)
        b = y1 - (m * x1)
        return float(m * self.scale_factor), float(b * self.scale_factor)
