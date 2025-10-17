import os

def ensure_workspace(root: str):
    os.makedirs(root, exist_ok=True)
    return root
