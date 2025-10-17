# api/projects.py
import json
import os

PROJECTS_FILE = os.path.join(os.path.dirname(__file__), '..', 'projects.json')

def handler(request):
    with open(PROJECTS_FILE, 'r', encoding='utf-8') as f:
        raw = json.load(f)
    # 只返回 {id: name}，不泄露 params
    projects = {k: v["name"] for k, v in raw.items()}
    return {"projects": projects}
