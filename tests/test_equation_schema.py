import unittest
import numpy as np
from src.equation_schema import LinearScaleEngine

class TestLinearScaleEngine(unittest.TestCase):

    def setUp(self):
        # Sample calibration points (e.g., stage vs discharge or raw voltage vs telemetry reading)
        self.points = [(0.0, 0.0), (10.0, 50.0), (20.0, 200.0)]
        self.engine = LinearScaleEngine(calibration_points=self.points, scale_factor=1.1)

    def test_single_interpolation(self):
        # Midpoint of (0,0) and (10,50) is (5, 25). With 1.1 scale factor: 25 * 1.1 = 27.5
        val = self.engine.calculate_single(5.0)
        self.assertAlmostEqual(val, 27.5, places=4)

    def test_batch_vectorization(self):
        inputs = [0.0, 5.0, 10.0]
        results = self.engine.calculate_batch(inputs)
        expected = np.array([0.0, 27.5, 55.0])
        np.testing.assert_array_almost_equal(results, expected)

    def test_out_of_bounds_extrapolation(self):
        # np.interp clamps values outside bounds by default
        val_low = self.engine.calculate_single(-5.0)
        self.assertAlmostEqual(val_low, 0.0, places=4)

if __name__ == "__main__":
    unittest.main()
