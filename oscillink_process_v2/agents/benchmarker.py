from typing import Dict
from ..core.types import TestResults, BenchmarkResult, PlanSpec

def compare_against_thresholds(results: TestResults, plan: PlanSpec) -> BenchmarkResult:
    """
    Supports multiple numeric metrics. Plan.acceptance can be:
      {"max_mse": 0.01}  OR  {"mse": {"lte": 0.01}, "mae": {"lte": 0.02}}
    The TestResults.outputs should at least include "mse"; others optional (e.g., "mae").
    """
    metrics = dict(results.outputs)
    thresholds = plan.acceptance or {}

    # Normalize thresholds: allow {"max_mse": 0.01} or {"mse":{"lte":0.01}}
    norm: Dict[str, Dict[str, float]] = {}
    for k, v in thresholds.items():
        if k.startswith("max_"):
            metric = k.replace("max_", "", 1)
            norm[metric] = {"lte": float(v)}
        elif isinstance(v, dict):
            norm[k] = {kk: float(vv) for kk, vv in v.items()}
        else:
            # treat as lte by default
            norm[k] = {"lte": float(v)}

    def metric_pass(value: float, cond: Dict[str, float]) -> bool:
        ok = True
        if "lte" in cond:
            ok = ok and (value <= cond["lte"])
        if "gte" in cond:
            ok = ok and (value >= cond["gte"])
        return ok

    # Evaluate
    checks = []
    for metric, cond in norm.items():
        val = float(metrics.get(metric, float("inf")))
        checks.append(metric_pass(val, cond))

    passed = all(checks) if checks else False
    return BenchmarkResult(passed=passed, metrics=metrics, threshold=norm)
