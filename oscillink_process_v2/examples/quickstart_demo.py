"""Oscillink Process™ v2 quick demonstration

Phases: Idea -> Plan -> Scaffold -> Build -> Test -> Benchmark -> Publish -> Maintain
This is dependency-light and vendor-neutral. It illustrates the **process**, not a specific stack.
"""
import os
from ..core.policy import should_publish, load_acceptance
from ..core.logging_util import init_logging
from ..runner.sandbox import ensure_workspace

from ..agents.ideator import capture_idea
from ..agents.planner import make_plan
from ..agents.scaffolder import generate_scaffold
from ..agents.builder import complete_build
from ..agents.tester import run_tests
from ..agents.benchmarker import compare_against_thresholds
from ..agents.publisher import publish
from ..agents.maintainer import maintain

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKSPACE = os.path.join(ROOT, "workspace", "project")
PUBLISHED = os.path.join(ROOT, "published")
MAINT_DIR = os.path.join(ROOT, "maintenance")
POLICY_FILE = os.path.join(ROOT, "policies", "default.json")
LOGS_DIR = os.path.join(ROOT, "workspace", "logs")

def main():
    logger = init_logging(LOGS_DIR)
    logger.info("=== Oscillink Process v2 Demo ===")
    # Idea
    idea = capture_idea("Implement a linear mapping y = 2x + 1 with low error",
                        constraints=["Local execution", "No network"])
    logger.info("[Idea] %s", idea.statement)

    # Plan (load acceptance thresholds from policy file if present)
    acceptance = load_acceptance(POLICY_FILE)
    plan = make_plan(idea, acceptance_override=acceptance if acceptance else None)
    logger.info("[Plan] steps=%s", plan.steps)
    logger.info("[Plan] acceptance=%s", plan.acceptance)

    # Scaffold
    ensure_workspace(os.path.dirname(WORKSPACE))
    scaffold = generate_scaffold(plan, WORKSPACE)
    logger.info("[Scaffold] files=%s", list(scaffold.structure.keys()))

    # Build
    artifact = complete_build(scaffold, plan, WORKSPACE)
    logger.info("[Build] artifact=%s at %s", artifact.id, artifact.location)

    # Test
    test_results = run_tests(artifact)
    logger.info("[Test] results=%s", test_results.outputs)

    # Benchmark
    bench = compare_against_thresholds(test_results, plan)
    logger.info("[Benchmark] metrics=%s threshold=%s passed=%s", bench.metrics, bench.threshold, bench.passed)

    # Publish (gate)
    if should_publish(bench):
        release_dir = publish(artifact, PUBLISHED)
        logger.info("[Publish] released to: %s", release_dir)
        # Maintain
        log_path = maintain(artifact, MAINT_DIR)
        logger.info("[Maintain] log appended at: %s", log_path)
        logger.info("Demo complete: artifact published and maintenance run executed.")
    else:
        logger.info("Demo stopped: benchmark did not pass; revise and rebuild.")

if __name__ == "__main__":
    main()
