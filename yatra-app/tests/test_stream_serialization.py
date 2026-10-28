import sys
import unittest
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"
sys.path.insert(0, str(APP_DIR))

from model import WeatherResponseModel
from routes import stream as stream_module


class StreamSerializationTests(unittest.TestCase):
    def test_format_sse_serializes_pydantic_models(self):
        weather = WeatherResponseModel(
            date="2026-06-30",
            condition="Sunny",
            temperature_high=32.0,
            temperature_low=24.0,
            humidity=50.0,
            rain_chance=10.0,
        )

        payload = stream_module.format_sse({"weather_data": [weather]})

        self.assertIn('"weather_data"', payload)
        self.assertIn('"date": "2026-06-30"', payload)
        self.assertIn('"condition": "Sunny"', payload)


if __name__ == "__main__":
    unittest.main()
