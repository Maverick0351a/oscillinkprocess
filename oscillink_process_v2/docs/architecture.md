# Architecture (Conceptual, dependency-agnostic)

```
[Idea]
  |
[Planner] ---> [Scaffolder] ---> [Builder] ---> [Tester] ---> [Benchmarker] ---> [Publisher] ---> [Maintainer]
                   |                 |             |               |                 |                 |
                (project)         (artifact)    (results)       (metrics)         (release)        (updates)
```

- Roles are conceptual; implementations may combine roles or time-multiplex them in one agent.
- Policy gating occurs at **Benchmark**: only passing artifacts advance to **Publish**.
