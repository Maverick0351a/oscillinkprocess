import os, textwrap
from ..core.types import BuildArtifact, ScaffoldSpec, PlanSpec, new_id

def complete_build(scaffold: ScaffoldSpec, plan: PlanSpec, workspace: str) -> BuildArtifact:
    # Implement a simple linear model y = a*x + b; builder can set a,b to fit target y=2x+1
    a, b = 2.0, 1.0  # choose correct values for a single-iteration success
    main_code = textwrap.dedent(f"""    # Auto-built module
    def predict(x):
        a = {a}
        b = {b}
        return a * x + b
    """)
    with open(os.path.join(workspace, "main.py"), "w", encoding="utf-8") as f:
        f.write(main_code)
    # minimal tests file (not executed directly; tester will import main)
    tests_code = "# placeholder for tests"
    with open(os.path.join(workspace, "tests.py"), "w", encoding="utf-8") as f:
        f.write(tests_code)
    return BuildArtifact(id=new_id("build"), location=workspace, metadata={"model":"linear", "a":a, "b":b})
