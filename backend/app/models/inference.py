"""Tiny wrapper around Ultralytics‑YOLO to detect climbing holds and sample routes."""
import io
from typing import List, Dict
from pathlib import Path
from PIL import Image

try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None  # allows unit tests without heavy deps

WEIGHTS = Path(__file__).resolve().parent.parent.parent / "weights" / "holds_detector.onnx"
_DEF_THRESHOLD = 0.30

class _LazyModel:
    _model = None

    @classmethod
    def model(cls):
        if cls._model is None:
            if YOLO is None:
                raise RuntimeError("ultralytics not installed – pip install ultralytics")
            cls._model = YOLO(str(WEIGHTS))
        return cls._model

def _detect_holds(img: Image.Image):
    """Returns list of dicts {x1,y1,x2,y2,conf} above threshold."""
    results = _LazyModel.model()(img, verbose=False)
    return [b for b in results[0].boxes if float(b.conf) > _DEF_THRESHOLD]

def suggest_routes(img_bytes: bytes, n_routes: int = 3) -> List[Dict]:
    """Very naïve sampler: picks every n‑th hold to build a route."""
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    holds = _detect_holds(img)
    if not holds:
        return []

    routes = []
    for r in range(n_routes):
        route_holds = holds[r::n_routes]
        routes.append({
            "id": r,
            "holds": [{"bbox": list(map(float, h.xyxy[0])), "conf": float(h.conf)} for h in route_holds]
        })
    return routes
