# ![logo EDIH](imgs/banner.png)

# D6.3 – Open Source Components Repository

## Introduction

This repository constitutes the **D6.3 Open Source Components Repository** of the **EDIH GreenPowerIT** project. It contains a curated selection of reusable open-source software components realised to support project activities. Components have been selected based on their suitability for public release and reusability.

This repository serves as the official software deposit for Deliverable D6.3. Its purpose is to preserve and disseminate reusable software assets produced within the EDIH GreenPowerIT project while respecting confidentiality, intellectual property, and contractual obligations associated with project-specific developments.


## Repository Layout

- `components/` – Reusable software components.
- `imgs/` – Documentation assets.

## Component Catalog
| Component | Purpose | Technologies | Project Category |
|-----------|---------|--------------|------------------|
| lightfm-recommender | TTrain and persist LightFM recommendation models | Python, LightFM, pandas | Model training |
| html-content-parser | Parse HTML and convert it to JSON | Python, BeautifulSoup | Data parsing |
| qr-code-reader | Decode QR codes from images | Python, pyzbar, Pillow | Computer vision |
| flutter-video-player | Provide a reusable Flutter component for playing video using media_kit | Flutter, media_kit | Video playback |
| color-delta-calculator | Compute perceptual color differences (Delta E) | Python, colour-science | Color processing |
| optical-flow-processor | Compute dense optical flow between consecutive images | Python, OpenCV, NumPy | Motion analysis |
| object-detection-processor | Detect objects using MediaPipe | Python, MediaPipe, OpenCV | Computer vision |
| constraint-optimizer | Provide generic linear programming utilities using PuLP | Python, PuLP | Optimization utilities |
| rag-chunker | Split documents into chunks for RAG pipelines | Python, LangChain | Text splitting utilities |

## Technology Inventory
| Technology | Category | Purpose | License |
|------------|----------|---------|--------|
| Python | Programming Language | Core implementation | Python Software Foundation License |
| pandas | Data Processing | Data manipulation and CSV handling | BSD-3-Clause |
| LightFM | Machine Learning | Matrix factorization recommendation model | BSD-3-Clause |
| BeautifulSoup | HTML Parsing | HTML parsing and content extraction | MIT |
| pyzbar | QR Code Decoding | QR code decoding | MIT |
| Pillow | Computer Vision | Image handling | HPND |
| Flutter | UI Toolkit | UI toolkit for building natively compiled applications | BSD-3-Clause |
| media_kit | Media player | Video playback and streaming library for Flutter | MIT |
| colour-science | Computer Vision | Colour conversion and Delta E computation | MIT |
| OpenCV | Computer Vision | Image processing and computer vision | Apache-2.0 |
| MediaPipe | Computer Vision | Object detection and vision pipelines | Apache-2.0 |
| PuLP | Optimization Library | Linear Programming | MIT |
| LangChain | Framework | Document processing and RAG pipelines | Apache-2.0 |

## How to Use
1. Browse the `components/` directory to find reusable modules.  
2. Read each component’s `README.md` for installation and usage instructions.

## Open Datasets

During the EDIH GreenPowerIT project, several proprietary datasets were generated to support project activities. As these datasets contain non-public data, they cannot be released. The following open datasets were also used and remain publicly available:

| Dataset      | Description (use‑case)                                   | Source / Link                                      | License |
|--------------|----------------------------------------------------------|----------------------------------------------------|---------|
| OpenFoodFacts| Global food‑product database (nutrition, ingredients, …) | <https://world.openfoodfacts.org/>                | Open Database License |
| MovieLens    | User‑movie rating data for recommender‑system research   | <https://grouplens.org/datasets/movielens/>        | Various (GroupLens dataset license) |
| PASTIS       | Panoptic & semantic segmentation benchmark of agricultural parcels from satellite time‑series | <https://github.com/VSainteuf/pastis-benchmark>   | MIT License |

## Repository Scope

Some components have been generalized or adapted for public release to remove confidential information, proprietary datasets, or project-specific dependencies. Where necessary, synthetic data and publicly available resources have been used in place of non-public project assets. The published implementations preserve the general functionality and demonstrate the reusable software assets developed within the EDIH GreenPowerIT project while respecting confidentiality and intellectual property obligations.

## License

This repository is released under the MIT License. See the [LICENSE](LICENSE) file for details.