from .types import BenchmarkResult
from typing import Dict
import json

def should_publish(bench: BenchmarkResult) -> bool:
    return bench.passed

def load_acceptance(policy_file: str) -> Dict[str, float]:
    """Load acceptance thresholds from a JSON policy file.

    Expected format:
    {
      "acceptance": {"max_mse": 0.01, ...}
    }

    Returns an empty dict if file is missing or unreadable.
    """
    try:
        with open(policy_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        acc = data.get("acceptance", {})
        # Ensure values are numeric
        return {k: float(v) for k, v in acc.items()}
    except Exception:
        return {}
