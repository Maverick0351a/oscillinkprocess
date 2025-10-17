from typing import Dict, Optional, Any
from ..core.types import IdeaSpec, PlanSpec

def make_plan(idea: IdeaSpec, acceptance_override: Optional[Dict[str, Any]] = None) -> PlanSpec:
    steps = [
        "Generate scaffold",
        "Implement core logic",
        "Add tests",
        "Run tests",
        "Benchmark against thresholds",
        "If pass, publish; else revise and rebuild"
    ]
    components = ["main module", "tests", "config"]
    acceptance = acceptance_override or {"max_mse": 0.01}
    return PlanSpec(steps=steps, components=components, acceptance=acceptance, iterations=3)
