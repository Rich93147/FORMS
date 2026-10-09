# FORMS
**Form Optimization and Repetition Monitoring System**

FORMS uses a Microsoft Kinect (Xbox One / Kinect v2) to turn a workout into a normalized 3D skeleton, detect deviations from ideal form, and give audio and visual corrective guidance. The first milestone is the **squat**; the pipeline is meant to extend to other lifts such as barbell rows.

> **Status:** project outline only. Packages and modules are placeholders with no functional code yet.

## Requirements
- **Hardware:** Microsoft Kinect for Xbox One (v2) with the Kinect Adapter for Windows (USB 3.0) and a USB 3.0 port. Webcam support is a future goal.
- **OS:** Windows 10/11 for the Kinect v2 SDK (Python access to the sensor is still to be validated).
- **Software:** Python 3.10+, [Kinect for Windows SDK 2.0](https://www.microsoft.com/en-us/download/details.aspx?id=44561).
- **Python libraries:** NumPy, OpenCV, PyTorch, scikit-learn (see `requirements.txt`).
- **Datasets** (downloaded separately, not committed): KIMORE, UI-PRMD, MSRC-12. See [docs/datasets.md](docs/datasets.md).

## Setup
```
python -m venv .venv
.venv\Scripts\activate   # or: source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Layout
```
src/forms/
  acquisition/  Kinect capture and recording
  datasets/     KIMORE, UI-PRMD, MSRC-12 loaders
  skeleton/     25-joint definition, normalization, rep segmentation
  features/     joint angles, depth/motion features
  models/       PyTorch form-error classifier and training
  feedback/     corrective cues, audio, visual overlay
  evaluation/   metrics and Kinect-vs-Vicon validation
configs/  tests/  scripts/  notebooks/  data/  docs/
```

## Documentation
- [Architecture](docs/architecture.md)
- [Datasets](docs/datasets.md)
- [Metrics](docs/metrics.md)
- [Roadmap](docs/roadmap.md)
