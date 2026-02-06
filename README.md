# 📊Financial Report Analyzer
 
**Fast, AI-powered analysis of financial reports using PDF parsing, NLP compression, and interactive dashboards.**

---

## 🧠Problem Statement

Annual and quarterly financial reports often exceed 100+ pages and contain dense financial and narrative information. Manually reviewing these documents is time-consuming and difficult, especially when comparing multiple companies across periods. Extracting risks, trends, sentiment, and key financial signals requires significant effort.

There is a need for a lightweight system that can quickly compress, analyze, and visualize financial reports to support faster understanding and comparison.

---

## 💡Solution Overview

Financial Report Analyzer project that analyzes uploaded financial report PDFs and combines document parsing, NLP compression, and market data analytics into a single Streamlit dashboard.

The application:

- Extracts text and tables from uploaded reports
- Compresses long narratives using ScaleDown-style summarization
- Performs sentiment analysis on financial narratives
- Extracts and summarizes risk factors
- Detects financial trends using Yahoo Finance data
- Compares peer companies
- Analyzes earnings call transcripts
- Displays insights in an interactive Streamlit dashboard
- Calculates ROI and latency savings from document compression

The system is designed to work without SEC APIs and instead relies on uploaded PDFs and Yahoo Finance structured data.

---

## 🔑Key Features

- PDF financial report parsing
- Narrative compression (target ~80% reduction)
- Financial table extraction from PDFs
- Risk factor detection and summarization
- Sentiment analysis of report narratives
- Earnings transcript analysis (paste-in text)
- Trend detection using Yahoo Finance data
- Peer company comparison
- Rule-based alert generation
- Interactive Streamlit dashboard

---

## ⚙️Tech Stack

- Python
- Streamlit
- pdfplumber
- camelot
- pandas
- yfinance
- transformers
- scikit-learn
- matplotlib / plotly

---

## 🏗️System Architecture

User PDF Upload
- Text & Table Extraction
- Narrative Compression
- NLP Analysis (Sentiment + Risk)
- Market Trend Data (Yahoo Finance)
- Peer Comparison
- Alerts + ROI Metrics
- Streamlit Dashboard

---

## 🔁Working

1. User uploads a financial report PDF.
2. The system extracts raw text and tables using PDF parsing tools.
3. Long narrative sections are split into chunks and summarized.
4. Sentiment analysis runs on compressed narrative text.
5. Risk factor sections are detected and summarized.
6. Historical stock data is fetched using Yahoo Finance.
7. Peer tickers are analyzed and compared.
8. Alert rules are evaluated based on risk, sentiment, and trends.
9. Results are displayed across dashboard tabs.

---

## 📊Dashboard Sections

**Filing Summary**
- Displays compressed narrative summary of the uploaded financial report
- Shows overall sentiment score and label (positive / neutral / negative)
- Highlights key extracted themes from the report

**Risk Factors**
- Extracted and summarized risk factor section from the report
- Lists top risk-related keywords using TF-IDF
- Quick view of major operational and financial risks mentioned

**Tables**
- Displays financial tables extracted from the PDF
- Structured preview using dataframes
- Supports multiple detected tables across pages

**Trends**
- Historical stock price chart from Yahoo Finance
- Moving averages (e.g., 50-day / 200-day)
- Basic volatility and growth indicators
- Visual trend direction signals

**Peer Comparison**
- Compare multiple ticker symbols side-by-side
- Growth and volatility comparison charts
- Relative performance metrics table
- Sentiment comparison (if multiple reports uploaded)

**Transcript Analysis**
- Earnings call transcript input box
- Auto-generated transcript summary
- Sentiment score and dominant themes
- Keyword frequency highlights

**Alerts**
- Rule-based warning indicators
- Flags negative sentiment
- Flags high volatility
- Flags risk-heavy language
- Flags downward trend signals

## ⚠️Limitations

- Uses simplified NLP summarization instead of finance-specialized models
- PDF parsing accuracy depends on report formatting and layout quality
- Table extraction may fail or produce noisy data for complex tables
- Sentiment analysis is general-purpose and may miss financial nuance
- Risk-factor detection is section-pattern based, not fully semantic
- Alert system is heuristic and rule-based, not predictive
- Compression may omit some low-frequency but important details
- Performance may slow down for very large PDFs
- No live filings API integration in current version
- Not investment or financial advice

## 🔮Future Improvements

- Integrate live filings APIs and automated report ingestion
- Use finance-tuned NLP and sentiment models
- Add semantic section segmentation for more accurate risk extraction
- Implement vector search across multiple reports and years
- Support multi-report and multi-period comparison
- Improve table normalization and financial metric detection
- Add automated financial ratio and fundamentals analysis
- Upgrade alerts from rules to ML-based anomaly detection
- Add caching and background processing for large documents
- Enable report-to-report diff analysis
- Add export options (PDF/Excel insight reports)
- Deploy as a scalable web service with user accounts
