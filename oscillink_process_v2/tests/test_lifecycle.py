import os
import shutil
import tempfile
import unittest

from oscillink_process_v2.agents.ideator import capture_idea
from oscillink_process_v2.agents.planner import make_plan
from oscillink_process_v2.agents.scaffolder import generate_scaffold
from oscillink_process_v2.agents.builder import complete_build
from oscillink_process_v2.agents.tester import run_tests
from oscillink_process_v2.agents.benchmarker import compare_against_thresholds
from oscillink_process_v2.core.policy import should_publish


class TestOscillinkLifecycle(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_end_to_end_passes_default_threshold(self):
        idea = capture_idea("Linear mapping y=2x+1")
        plan = make_plan(idea)
        workspace = os.path.join(self.tmp, "project")
        scaffold = generate_scaffold(plan, workspace)
        artifact = complete_build(scaffold, plan, workspace)
        results = run_tests(artifact)
        bench = compare_against_thresholds(results, plan)
        self.assertTrue(should_publish(bench))
        self.assertLessEqual(results.outputs["mse"], plan.acceptance.get("max_mse", 0.01))

    def test_multi_metric_thresholds(self):
        idea = capture_idea("Linear mapping y=2x+1")
        # multi-metric acceptance
        plan = make_plan(idea, acceptance_override={"mse": {"lte": 0.01}, "mae": {"lte": 0.01}})
        workspace = os.path.join(self.tmp, "p2")
        scaffold = generate_scaffold(plan, workspace)
        artifact = complete_build(scaffold, plan, workspace)
        results = run_tests(artifact)
        bench = compare_against_thresholds(results, plan)
        self.assertTrue(should_publish(bench))


if __name__ == "__main__":
    unittest.main()
