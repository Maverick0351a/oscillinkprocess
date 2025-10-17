import os
from ..core.types import PlanSpec, ScaffoldSpec

def generate_scaffold(plan: PlanSpec, workspace: str) -> ScaffoldSpec:
    os.makedirs(workspace, exist_ok=True)
    structure = {
        "README.txt": "Auto-generated scaffold readme",
        "main.py": "Core module",
        "tests.py": "Simple test harness"
    }
    for fname, desc in structure.items():
        fpath = os.path.join(workspace, fname)
        if not os.path.exists(fpath):
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(f"# {desc}\n")
    return ScaffoldSpec(structure=structure)
