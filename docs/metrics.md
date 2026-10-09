# Metrics

Targets are tentative and subject to change.

| Metric | Measures | Calculation | Target |
|---|---|---|---|
| Corrective Guidance Accuracy | Correct primary cue for the observed error | % of labeled faulty reps whose primary cue matches the labeled error/correction | >= 70% |
| Macro F1 | Balanced error classification | Per-class F1 averaged over classes | >= 0.80 |
| Joint-Angle MAE | Accuracy of angle measurements | Mean absolute difference (degrees) vs. reference angles on an evaluation subset | <= 10 deg |
| Inference speed | Interactive feedback | Average FPS or ms per frame | >= 30 FPS |
