---
layout: home
title: Home
---

## About Me

I am a **Freelance Programmer** with a background in math, physics, bioinformatics,
and computational biology. My work spans phylogenetics, bioinformatics algorithm
development, and pathology image analysis.

Before that I was at **3DMed Diagnostics** in Shanghai.

## Education

- **Ph.D.** in Computational Biology, CAS-MPG Partner Institute for Computational
  Biology (PICB), Chinese Academy of Sciences — 2010–2017
- **B.A.** in Bioinformatics, Shanghai JiaoTong University — 2006–2010

## Employment

- **Senior Data Scientist**, 3DMed Diagnostics — 2025–2026
- **Senior Bioinformatics Engineer**, 3DMed Diagnostics — 2021–2025
- **Bioinformatics Scientist**, BGI Research Institute — 2018–2021
- **Postdoctoral Fellow**, Dept. of Mathematics, Simon Fraser University — 2017–2018
  *(Supervisors: Paul Tupper & David Bryant)*

## Working experience

- **LymphFind** (2025–2026) — End-to-end automatic lymph node metastasis detection
  in whole-slide pathology images. CTransPath vision transformer backbone with
  multiple-instance learning; achieved ROC of 0.995.
- **Slide Registration for APTime** (2025–2026) — Deployed rigid (LightGlue-based)
  and non-rigid (refactored Valis) registration modules for clinical pathology slides.
  Reduced non-rigid registration runtime from ~12 h to 1.5 h.
- **Low-frequency SNV Detection in cfDNA** (2023–2025) — Error-model-based pipeline
  for detecting low-frequency SNVs from dual consensus sequencing with automated QC.
- **CNV Detection in cfDNA** (2021–2023) — High-sensitivity CNV pipeline integrating
  fragmentomics features; halved the limit of detection for low-tumor-content cfDNA.
- **Genomic Epidemiology of Covid-19 in UAE** (2020–2021) — Deployed an analytical
  platform processing ~5,000 samples/day for SARS-CoV-2 genomic surveillance.
- **Assembly Software for Barcoded Sequencing** (2018–2020) — Algorithms for
  barcoded sequencing and gap-filling from third-generation reads.

## Awards

- **Alibaba Math Competition**, Bronze Prize — 2020, 2024
- **IMPRS Academic Exchange** — University of Otago (3 months), 2014

## Skills

- **Languages:** C++, Python, MATLAB, Perl
- **Domains:** Machine Learning, Deep Learning, Image Processing, Data Modeling
- **AI Tools:** Cursor, Claude Code, Codex

## Side projects

- **[Valis_X](https://github.com/PeterWu-Biomath/Valis_X)** —
  A simplified, in-memory refactoring of [VALIS](https://github.com/MathOnco/valis) (Virtual
  Alignment of pathoLogy Image Series) for whole-slide image registration.
  Focuses on pair-wise rigid + non-rigid registration with all operations
  in memory — format-agnostic, no intermediate disk I/O, and deployable
  across platforms.
- **[BWA-Capture](https://github.com/PeterWu-Biomath/bwa)** —
  Targeted alignment for panel/exome sequencing that extends BWA with a capture
  sub-index. Reads from target regions are aligned through a dense suffix array
  with an uncompressed OCC table built exclusively over regions of interest,
  while off-target reads fall back to the full genome BWT. A position table with
  run-length-encoded lookup maps sub-SA intervals to genome SA intervals for
  seamless cross-boundary alignment. Precomputed perfect-alignment caching skips
  chaining, Smith-Waterman, and deduplication for reads matching a target region
  exactly. Produces results identical to standard BWA — drops into existing
  pipelines without downstream validation.
- **[Residues and Duality — TeX typesetting](https://github.com/PeterWu-Biomath/Residues-and-Duality-Tex)** —
  A typesetting project for the book *Residues and Duality* by Robin Hartshorne. There are alternatives like (https://zhuanlan.zhihu.com/p/2091155695580231224)
- **[Completeness of Bethe Ansatz](/assets/BA.pdf)** —
  Notes on the completeness of the Bethe ansatz from the perspective of intersection theory (BKK theorem). Chinese ver.
  [[github](https://github.com/PeterWu-Biomath/Bananaspace_backup/blob/main/07-Bethe%20ansatz%E7%9A%84%E5%AE%8C%E5%A4%87%E6%80%A7.tex)]


## Contact

- **Email:** [wupei5060309031@gmail.com](mailto:wupei5060309031@gmail.com)
- **GitHub:** [PeterWu-Biomath](https://github.com/PeterWu-Biomath)
