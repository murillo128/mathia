from __future__ import annotations
import json
from pathlib import Path
from public_fixtures import build_public
from private_truth import build_private

ROOT=Path(__file__).resolve().parent
(ROOT/'public.json').write_text(json.dumps(build_public(),indent=2,ensure_ascii=False)+'\n')
(ROOT/'ground_truth.json').write_text(json.dumps(build_private(),indent=2,ensure_ascii=False)+'\n')
print('materialized public.json and ground_truth.json')
