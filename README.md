# AiHTP
AI and HTP

# AiHTP - AI-powered House-Tree-Person Psychological Test Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
An AI-powered tool for analyzing House-Tree-Person (HTP) psychological test drawings through computer vision and LLM analysis. Integrates with leading AI APIs to provide psychological insights.

**Disclaimer**: This project is for educational/research purposes only. Not a substitute for professional psychological diagnosis or medical advice.

## Features
- 🖼️ HTP image analysis pipeline
- 🤖 Dual AI engine integration (Kimi Vision + DeepSeek)
- 📄 Automated report generation
- 🧠 Psychological pattern recognition
- 📁 Multi-file context analysis

## Installation
```bash
git clone https://github.com/yourusername/aihtp.git
cd aihtp
pip install -r requirements.txt
```

## Usage
```bash
python src/cli.py
```
When prompted, provide the path to your HTP drawing image.

## Configuration
1. Get API keys from:
   - Kimi: https://platform.moonshot.cn/
   - DeepSeek: https://platform.deepseek.com/
2. Add to `const/const.py`:
```python
KIMI_API_KEY = "your_kimi_key"
DEEPSEEK_API_KEY = "your_deepseek_key"
```

## Legal Disclaimer
This software is provided "as is" without warranty of any kind. Users assume all responsibility for:
- Compliance with AI service providers' terms of use
- Ethical use of psychological assessment tools
- Data privacy regulations adherence
- Proper clinical validation of results

Not certified for clinical use. Always consult licensed professionals for mental health assessments.

## License
MIT License
