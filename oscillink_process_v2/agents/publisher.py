import os, shutil, time
from ..core.types import BuildArtifact

def publish(artifact: BuildArtifact, dest_root: str):
    os.makedirs(dest_root, exist_ok=True)
    release_dir = os.path.join(dest_root, artifact.id)
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    shutil.copytree(artifact.location, release_dir)
    with open(os.path.join(release_dir, "RELEASE.txt"), "w", encoding="utf-8") as f:
        f.write(f"Published: {time.strftime('%Y-%m-%d %H:%M:%SZ', time.gmtime())}\n")
    return release_dir
