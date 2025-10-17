from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid

def new_id(prefix: str = "art") -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

@dataclass
class IdeaSpec:
    statement: str
    constraints: List[str] = field(default_factory=list)

@dataclass
class PlanSpec:
    steps: List[str]
    components: List[str]
    acceptance: Dict[str, float]
    iterations: int = 3

@dataclass
class ScaffoldSpec:
    structure: Dict[str, str]  # filename -> description

@dataclass
class BuildArtifact:
    id: str
    location: str  # path on disk
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class TestResults:
    passed: bool
    outputs: Dict[str, float]

@dataclass
class BenchmarkResult:
    passed: bool
    metrics: Dict[str, float]
    threshold: Dict[str, Any]
