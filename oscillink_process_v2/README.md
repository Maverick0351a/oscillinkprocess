# The Oscillink Process™ (v2)
> The Oscillink Process™ is a patent-pending method for autonomous AI development (Idea → Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain).
**Patent Pending — U.S. Provisional No. 63/900,694**  
**Title:** Systems and Methods for Autonomous Idea → Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain

> The Oscillink Process™ is a **domain‑agnostic, repeatable workflow** in which intelligent agents transform an **idea** into a **published, maintained artifact** by executing eight concrete phases:
> **Idea → Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain**.

This repository is a **reference scaffold** suitable for GitHub. It demonstrates the method with **minimal, vendor‑neutral code** using only a standard interpreter (no external libraries). It is designed to communicate the **process**, not bind it to any proprietary dependency.

---

## The Oscillink Lifecycle (clear and concrete)

1. **Idea** – capture a goal or problem statement.  
2. **Plan** – generate a structured approach or roadmap.  
3. **Scaffold** – produce a project or code skeleton.  
4. **Build** – complete the scaffold into a running artifact.  
5. **Test** – execute in a controlled environment to produce results.  
6. **Benchmark** – compare results to declared acceptance thresholds.  
7. **Publish** – release or deploy approved artifacts.  
8. **Maintain** – monitor, update, and iteratively improve.

> This lifecycle is intentionally **dependency‑agnostic** and **domain‑agnostic**. Implementations may be software, simulations, data/ML, control systems, hardware workflows, or experimental protocols.

---

## What this repository contains

- **Agents** for each phase (simple, rule‑based placeholders).  
- A **sandbox runner** for controlled execution.  
- A **benchmark** with a numeric threshold.  
- A **policy gate** that only **publishes** on benchmark success.  
- A **maintenance step** to simulate post‑release checks.

**No “provenance” requirement** is included in v2; we keep all phases **concrete and technical** per your direction.

---

## Quick demonstration

> Requirements: a standard Python 3 interpreter.

Run:
```bash
python examples/quickstart_demo.py
```

What you’ll see:
- The system captures an **idea** and creates a **plan**.  
- It **scaffolds** a minimal project, **builds** it, then **tests** it.  
- **Benchmarking** applies a threshold (mean‑squared error).  
- If it passes, the artifact is **published** under `published/`.  
- A **maintenance** check then re-runs the tests once post‑release and logs status.

Outputs:
- Build artifacts under `workspace/` during the run.  
- Published artifact under `published/` upon success.  
- A `maintenance_log.txt` under `maintenance/` with post‑release status.

---

## Repository layout
```
/core          # Interfaces, data types, basic policy gating
/agents        # Idea, Plan, Scaffold, Build, Test, Benchmark, Publish, Maintain agents
/runner        # Controlled execution (sandbox)
/benchmarks    # Reference benchmarks and acceptance schemas
/policies      # Example acceptance thresholds
/docs          # Method documentation (dependency-agnostic)
/examples      # Minimal end-to-end demo
/published     # Final published artifacts (created at runtime)
/workspace     # Temporary build space (created at runtime)
/maintenance   # Maintenance logs (created at runtime)
/legal         # Notices
/.github       # Community & CI stub
```

---

## Patent & IP
- **Patent Pending:** U.S. Provisional No. **63/900,694** (Receipt Date: **Oct 17, 2025**).  
- The Oscillink Process™ may be covered by additional, related filings.  
- **Inventor:** **Travis Jacob Johnson**.

See `docs/patent.md` and `PATENT-NOTICE.md` for details.

---

## License
Open‑core. Community code under **AGPL‑3.0** (see `LICENSE-AGPL-3.0.txt`).  
Commercial extensions (advanced agent logic, domain packs, integrations) under a separate **Enterprise License** (see `LICENSE-ENTERPRISE.md`).

<!-- CI badge (auto-updated) -->
[![CI](https://github.com/Maverick0351a/oscillinkprocess/actions/workflows/ci.yml/badge.svg)](https://github.com/Maverick0351a/oscillinkprocess/actions/workflows/ci.yml)

Website (GitHub Pages): https://maverick0351a.github.io/oscillinkprocess/

---

## Safety, scope, and neutrality
- This reference implements the **process** only. It is **not bound** to any single vendor, IDE, or model.  
- The demo runs locally, without network activity, with small inputs.  
- Keep contributions **vendor‑neutral**; integrations should be packaged as optional plugins outside this core repository.

---

## Running & Testing

This project is a Python package. Prefer running with `-m` so package-relative imports work.

Windows (PowerShell):

```powershell
cd "C:\Users\Maver\Downloads\oscillink_process_v2"
python -m oscillink_process_v2.examples.quickstart_demo

# CLI with single-metric override
python -m oscillink_process_v2.cli --max-mse 0.005

# CLI with multi-metric thresholds (JSON)
python -m oscillink_process_v2.cli --thresholds '{"mse":{"lte":0.01},"mae":{"lte":0.02}}'
```

macOS/Linux:

```bash
cd /path/to/oscillink_process_v2
python -m oscillink_process_v2.examples.quickstart_demo
python -m oscillink_process_v2.cli --max-mse 0.005
python -m oscillink_process_v2.cli --thresholds '{"mse":{"lte":0.01},"mae":{"lte":0.02}}'
```

Logs:
- Console output plus persistent log at `workspace/logs/oscillink.log`.

Unit tests:

```powershell
cd "C:\Users\Maver\Downloads\oscillink_process_v2"
python -m unittest discover -s oscillink_process_v2\tests -p "test_*.py" -v
```

Policy configuration:
- Defaults load from `policies/default.json`.
- You can override via CLI flags as shown above.

---

## The Oscillink Process™ — Locked Reference

The following content is provided verbatim for direct reuse in claims, README, website, slides, or repo banners.

### 1) One-sentence elevator

**The Oscillink Process™** transforms a plan into a maintained product through seven concrete phases: **Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain**.

### 2) Patent-style independent claim (7-step core)

**A computer-implemented method for autonomous product generation, comprising:**
(1) **generating a plan** specifying components, steps, and acceptance thresholds;
(2) **constructing a scaffold** comprising a project structure and placeholders for components;
(3) **building a functional artifact** by completing the scaffold;
(4) **testing the artifact** in a controlled environment to produce results;
(5) **benchmarking the results** against the acceptance thresholds to determine compliance;
(6) **publishing the artifact** responsive to a determination of compliance; and
(7) **maintaining the artifact** by performing post-release checks and updates.

*(Add system + CRM claims in your filing as usual.)*

### 3) README block (copy-paste)

```markdown
## The Oscillink Process™ (Core Lifecycle)
**Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain**

- **Plan** – define components, steps, and acceptance thresholds.  
- **Scaffold** – generate a minimal project structure and placeholders.  
- **Build** – implement and assemble components into a working artifact.  
- **Test** – execute in a controlled environment to collect results.  
- **Benchmark** – compare results against declared thresholds (e.g., accuracy, latency, resource).  
- **Publish** – release or deploy only on benchmark pass (policy-gated).  
- **Maintain** – post-release checks and iterative improvements.

> Vendor- and domain-agnostic. Designed for autonomous or semi-autonomous workflows.
```

### 4) ASCII diagram

```
[Plan] -> [Scaffold] -> [Build] -> [Test] -> [Benchmark] -> [Publish] -> [Maintain]
	 |          |            |         |           |                |            |
 components   structure     artifact  results     pass/fail        release      updates
 steps        files         ready     captured    thresholds       delivered    checks
 thresholds
```

### 5) Website/SEO snippet

* **Title:** The Oscillink Process™ | Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain
* **Meta description:** The Oscillink Process™ defines a vendor-agnostic, seven-phase workflow for autonomous product generation: Plan, Scaffold, Build, Test, Benchmark, Publish, and Maintain.

