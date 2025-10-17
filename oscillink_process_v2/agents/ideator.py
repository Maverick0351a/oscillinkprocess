from ..core.types import IdeaSpec

def capture_idea(statement: str, constraints=None) -> IdeaSpec:
    return IdeaSpec(statement=statement, constraints=constraints or [])
