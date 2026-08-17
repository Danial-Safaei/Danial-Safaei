<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img alt="Danial Safaei — PhD Researcher, WMG, University of Warwick. Safe AI for autonomous systems." src="assets/banner-light.svg" width="100%">
  </picture>
</div>

<div align="center">
  <a href="https://danial-safaei.github.io"><b>Website</b></a> ·
  <a href="https://danial-safaei.github.io/cv.html"><b>CV</b></a> ·
  <a href="https://scholar.google.co.uk/citations?user=qNJPWrMAAAAJ&hl=en"><b>Scholar</b></a> ·
  <a href="https://orcid.org/0000-0002-4443-8763"><b>ORCID</b></a> ·
  <a href="https://www.linkedin.com/in/danial-safaei/"><b>LinkedIn</b></a> ·
  <a href="mailto:danial.safaei@warwick.ac.uk"><b>Email</b></a>
</div>

<br>

## The problem I work on

A driving model sees a real frame and outputs a 20° left turn. It sees the simulator's twin of that frame and outputs the same 20° left turn.

Perfect agreement. Ship it?

Look closer. In the real frame the decision was driven by **a pedestrian**. In the synthetic one, by **a road sign** — while the pedestrian went undetected. Same output, different reason. The test passed for the wrong reason, and no pixel-level or output-level metric can see it happening.

My research makes that failure mode measurable, so safety claims about autonomous systems rest on evidence rather than appearance.

> On one task, calibrating a generator for output agreement alone improved the output score by **74%** while making the decisive evidence **16% more divergent**. The score got better. The reasoning got worse.

<br>

## Publications

**Quantifying Fidelity: A Decisive Feature Approach to Comparing Synthetic and Real Imagery**<br>
<sub>D. Safaei, S. Khastgir, M. Alirezaei, J. Ploeg, C.-H. Cheng, S. Tong, X. Zhao</sub><br>
<sub><i>2026 IEEE Intelligent Vehicles Symposium (IV)</i>, pp. 847–854 · Detroit, MI, USA</sub><br>
[DOI](https://doi.org/10.1109/IV66570.2026.11624013) · [arXiv](https://arxiv.org/abs/2512.16468) · [Code](https://github.com/Danial-Safaei/DFF)

**DeePLT: Personalized Lighting Facilitates by Trajectory Prediction of Recognized Residents in the Smart Home**<br>
<sub>D. Safaei, A. Sobhani, A. A. Kiaei</sub><br>
<sub><i>International Journal of Information Technology</i>, vol. 16, no. 5, pp. 2987–2999</sub><br>
[DOI](https://doi.org/10.1007/s41870-023-01665-1) · [arXiv](https://arxiv.org/abs/2304.08027)

<sub>Full list including preprints → [Google Scholar](https://scholar.google.co.uk/citations?user=qNJPWrMAAAAJ&hl=en)</sub>

<br>

## Research

| | |
|:--|:--|
| **Safety assurance for AI** | Arguing safety and reliability claims with evidence when learned components operate in high-consequence settings |
| **Explainable evaluation** | Using interpretability methods as measurement instruments — comparing the evidence a model relies on, not only its outputs |
| **Synthetic-data fidelity** | Whether synthetic imagery is faithful to the decision-relevant structure of real data, so simulation results transfer |
| **Scenario-based testing** | Testing autonomous systems against the conditions that matter most for safety |

<sub>PhD supervised by Prof. Siddartha Khastgir and Prof. Matthew Higgins at WMG, in industrial partnership with Siemens Digital Industries Software.</sub>

<br>

## Featured repository

### [→ DFF](https://github.com/Danial-Safaei/DFF)
Reference implementation of Decisive Feature Fidelity: counterfactual-XAI decisive maps, ControlNet training wrappers, dataset manifests, and the calibration loop from the IEEE IV 2026 paper. Validated on 2,126 matched KITTI / Virtual KITTI 2 pairs across three frozen systems under test.

<br>

## Toolkit

<sub>**Languages**</sub><br>
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-E16737?style=flat-square&logo=mathworks&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

<sub>**Deep learning & vision**</sub><br>
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Diffusers-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

<sub>**Autonomy & simulation**</sub><br>
![CARLA](https://img.shields.io/badge/CARLA-000000?style=flat-square&logo=carthrottle&logoColor=white)
![SUMO](https://img.shields.io/badge/SUMO-008080?style=flat-square)
![ROS](https://img.shields.io/badge/ROS-22314E?style=flat-square&logo=ros&logoColor=white)
![OpenSCENARIO](https://img.shields.io/badge/OpenSCENARIO-4A5568?style=flat-square)
![KITTI](https://img.shields.io/badge/KITTI%20%2F%20vKITTI2-2D3748?style=flat-square)

<br>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/metrics-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/metrics-light.svg">
    <img alt="89 citations, h-index 6, i10-index 5, 11 works. Citations per year: 13 (2023), 42 (2024), 30 (2025), 4 (2026 to date). Source: Google Scholar." src="assets/metrics-light.svg" width="100%">
  </picture>
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Danial-Safaei/Danial-Safaei/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Danial-Safaei/Danial-Safaei/output/github-contribution-grid-snake.svg">
    <img alt="Contribution graph" src="https://raw.githubusercontent.com/Danial-Safaei/Danial-Safaei/output/github-contribution-grid-snake.svg">
  </picture>
</div>

<div align="center">
  <sub><i>Beyond visual realism, mechanistic realism is what makes virtual testing trustworthy.</i></sub>
</div>
