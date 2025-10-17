import argparse
import json
import os

from .agents.ideator import capture_idea
from .agents.planner import make_plan
from .agents.scaffolder import generate_scaffold
from .agents.builder import complete_build
from .agents.tester import run_tests
from .agents.benchmarker import compare_against_thresholds
from .agents.publisher import publish
from .agents.maintainer import maintain

from .core.policy import should_publish, load_acceptance
from .core.logging_util import init_logging
from .runner.sandbox import ensure_workspace


def main():
    parser = argparse.ArgumentParser(description="Run the Oscillink Process v2 pipeline")
    parser.add_argument("--root", default=os.path.abspath(os.path.dirname(__file__)), help="Project root directory")
    parser.add_argument("--workspace", default=os.path.join(os.path.abspath(os.path.dirname(__file__)), "workspace", "project"), help="Workspace directory")
    parser.add_argument("--published", default=os.path.join(os.path.abspath(os.path.dirname(__file__)), "published"), help="Published artifacts directory")
    parser.add_argument("--maintenance", default=os.path.join(os.path.abspath(os.path.dirname(__file__)), "maintenance"), help="Maintenance directory")
    parser.add_argument("--policy", default=os.path.join(os.path.abspath(os.path.dirname(__file__)), "policies", "default.json"), help="Policy JSON file path")
    parser.add_argument("--idea", default="Implement a linear mapping y = 2x + 1 with low error", help="Idea statement")
    parser.add_argument("--max-mse", type=float, default=None, help="Override max MSE threshold")
    parser.add_argument("--thresholds", type=str, default=None, help='JSON map, e.g. {"mse":{"lte":0.01},"mae":{"lte":0.02}}')
    args = parser.parse_args()

    WORKSPACE = args.workspace
    PUBLISHED = args.published
    MAINT_DIR = args.maintenance
    POLICY_FILE = args.policy

    logs_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "workspace", "logs")
    logger = init_logging(logs_dir)
    logger.info("=== Oscillink Process v2 CLI ===")
    idea = capture_idea(args.idea, constraints=["Local execution", "No network"])
    logger.info("[Idea] %s", idea.statement)

    acceptance = load_acceptance(POLICY_FILE)
    if args.thresholds:
        acceptance = json.loads(args.thresholds)
    elif args.max_mse is not None:
        acceptance = {**acceptance, "max_mse": args.max_mse}

    plan = make_plan(idea, acceptance_override=acceptance if acceptance else None)
    logger.info("[Plan] steps=%s", plan.steps)
    logger.info("[Plan] acceptance=%s", plan.acceptance)

    ensure_workspace(os.path.dirname(WORKSPACE))
    scaffold = generate_scaffold(plan, WORKSPACE)
    logger.info("[Scaffold] files=%s", list(scaffold.structure.keys()))

    artifact = complete_build(scaffold, plan, WORKSPACE)
    logger.info("[Build] artifact=%s at %s", artifact.id, artifact.location)

    test_results = run_tests(artifact)
    logger.info("[Test] results=%s", test_results.outputs)

    bench = compare_against_thresholds(test_results, plan)
    logger.info("[Benchmark] metrics=%s threshold=%s passed=%s", bench.metrics, bench.threshold, bench.passed)

    if should_publish(bench):
        release_dir = publish(artifact, PUBLISHED)
        logger.info("[Publish] released to: %s", release_dir)
        log_path = maintain(artifact, MAINT_DIR)
        logger.info("[Maintain] log appended at: %s", log_path)
        logger.info("Pipeline complete: artifact published and maintenance run executed.")
    else:
        logger.info("Pipeline stopped: benchmark did not pass; revise and rebuild.")


if __name__ == "__main__":
    main()
