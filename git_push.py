import subprocess
import os

repo_dir = r"D:\mindtrap_ai-main"

def run_cmd(cmd):
    p = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True, shell=True)
    print(f"CMD: {cmd}")
    print(f"STDOUT:\n{p.stdout}")
    print(f"STDERR:\n{p.stderr}")
    print(f"EXIT: {p.returncode}\n{'-'*40}")

run_cmd("git status")
run_cmd("git add -A")
run_cmd('git commit -m "Update Play Console release info and assets for Word Puzzle - Language Quest"')
run_cmd("git push origin main")
run_cmd("git status")
