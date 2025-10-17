# -*- coding: utf-8 -*-
import json
import os

# 读取项目列表
PROJECTS_FILE = os.path.join(os.path.dirname(__file__), '..', 'projects.json')
with open(PROJECTS_FILE, 'r', encoding='utf-8') as f:
    PROJECT_NAMES = json.load(f)  # {"proj_id": "显示名"}

def handler(request):
    try:
        body = request.get_json()
        inputs = body.get("inputs", {})  # { "proj_id": [x1, x2, ..., x6] }

        results = {}
        for proj_id, values in inputs.items():
            if proj_id not in PROJECT_NAMES:
                continue
            
            # 解构6个输入值（确保有6个）
            if len(values) != 6:
                return {"error": f"{proj_id} 需要6个输入值"}
            
            x1, x2, x3, x4, x5, x6 = values
            E=2.718281828
            # 🔒 你的私有公式（示例）
            digital_defective_rate = 1-E^(-x4*LOGIC_DEFECT_DENSITY)
            memory_defective_rate = 1-E^(-x5*RAM_DEFECT_DENSITY)
            CP_YIELD_BEFORE_REPAIR = (x1 * 2.5 + x2) * (1 + x3 / 100)  # 可替换为任意逻辑
            CP_YIELD_AFTER_REPAIR = (x1 * 2.5 + x2) * (1 + x3 / 100) 

            results[proj_id] = [
                round(CP_YIELD_BEFORE_REPAIR, 4),
                round(CP_YIELD_AFTER_REPAIR, 2)
            ]

        return {"results": results}

    except Exception as e:
        return {"error": "计算失败，请检查输入"}
