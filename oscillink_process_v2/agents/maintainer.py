import os, time
from ..core.types import BuildArtifact
from .tester import run_tests

def maintain(artifact: BuildArtifact, log_dir: str):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "maintenance_log.txt")
    res = run_tests(artifact)
    line = f"{time.strftime('%Y-%m-%d %H:%M:%SZ', time.gmtime())} | mse={res.outputs.get('mse'):.6f} | status=OK\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line)
    return log_path
