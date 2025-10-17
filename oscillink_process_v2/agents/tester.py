import os
import importlib.util
from types import ModuleType
from ..core.types import BuildArtifact, TestResults

def _load_module_from_path(name: str, path: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module

def run_tests(artifact: BuildArtifact):
    # Import predict() from main.py in the artifact location using importlib
    main_path = os.path.join(artifact.location, "main.py")
    module = _load_module_from_path("built_main", main_path)
    predict = getattr(module, "predict", None)
    if predict is None:
        raise AttributeError("Built artifact main.py does not define predict(x)")
    xs = [float(x) for x in range(-3, 4)]
    ys = [2.0*x + 1.0 for x in xs]
    preds = [predict(x) for x in xs]
    mse = sum((p-y)**2 for p,y in zip(preds, ys))/len(xs)
    mae = sum(abs(p - y) for p, y in zip(preds, ys)) / len(xs)
    outputs = {"mse": mse, "mae": mae}
    # TestResults 'passed' here is trivial; real pass/fail is at benchmark
    return TestResults(passed=True, outputs=outputs)
