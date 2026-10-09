# Architecture

Pipeline: **Kinect capture -> 3D skeleton -> normalization -> repetition segmentation -> feature extraction -> form-error model -> corrective cue -> audio/visual feedback.**

- **Acquisition** (`forms.acquisition`): synchronized color, depth and 25-joint body tracking via the Kinect SDK or a Python-accessible interface (unvalidated).
- **Skeleton** (`forms.skeleton`): normalizes for height, limb proportions and camera angle so the camera need not be at a specific position; depth lets us tell movement toward/away from the camera.
- **Features** (`forms.features`): joint angles, range of motion, torso lean, knee alignment, depth movement.
- **Models** (`forms.models`): PyTorch/scikit-learn classifiers of form errors (e.g. insufficient depth, torso lean, knee valgus).
- **Feedback** (`forms.feedback`): maps detected errors to understandable audio and visual cues.
- **Evaluation** (`forms.evaluation`): metrics in [metrics.md](metrics.md).

Squat issues targeted first: excessive torso lean, insufficient depth, inward knee movement.
