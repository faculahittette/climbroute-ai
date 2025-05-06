"""Launches a Gradio UI that calls the FastAPI backend deployed on Render."""
import gradio as gr
import requests, json

API_URL = "https://climbroute-backend.onrender.com/predict"  # update with actual URL


def infer(img):
    resp = requests.post(API_URL, files={"image": ("upload.jpg", img, "image/jpeg")})
    data = resp.json()
    return json.dumps(data, indent=2)


iface = gr.Interface(
    fn=infer,
    inputs=gr.Image(type="file"),
    outputs=gr.JSON(label="Routes"),
    title="ClimbRoute AI Demo"
)


if __name__ == "__main__":
    iface.launch()
