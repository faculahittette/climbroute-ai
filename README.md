# ClimbRoute AI – Zero‑Cost MVP

This repository contains a minimal, free‑tier‑friendly scaffold for a climbing‑wall
route suggestion demo.

## Quick Start (Local)

```bash
# clone & enter
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
# open http://localhost:8000/docs
```

## Quick Start (Docker)

```bash
docker compose up --build
# backend on http://localhost:8000
```

## Train a tiny detector in Google Colab

See `ml/scripts/train_detector.py` or follow the snippet in the docs.

## Render Deployment

Connect this repo to Render.com; it will pick up `render.yaml` and deploy
the FastAPI backend on the free plan.

## Gradio Demo

Run the local demo UI:

```bash
pip install gradio requests
python demo/gradio_app.py
```

Update `API_URL` inside `gradio_app.py` to point to your backend.

---
**Note**: place your trained weight file at `weights/holds_detector.onnx`.
