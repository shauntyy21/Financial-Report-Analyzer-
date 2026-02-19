import streamlit as st
from pathlib import Path
from rag import RAGConfig, RAGSystem

# ── Config (uses absolute paths from rag.py) ────────────────────────────────
config = RAGConfig()
KB_PATH = Path(config.knowledge_base_path)
KB_PATH.mkdir(exist_ok=True)
Path(config.embeddings_path).mkdir(exist_ok=True)

st.set_page_config(page_title="PDF RAG Chatbot", page_icon="📄", layout="wide")

st.title("📄 PDF RAG Chatbot")
st.caption("Upload a PDF, then ask questions about it.")

# ── Sidebar: Upload PDF ─────────────────────────────────────────────────────
with st.sidebar:
    st.header("📂 Knowledge Base")

    uploaded = st.file_uploader("Upload a PDF", type=["pdf"])

    if uploaded:
        save_path = KB_PATH / uploaded.name
        save_path.write_bytes(uploaded.getbuffer())
        st.success(f"✅ Saved: {uploaded.name}")

    # Show what's currently in the knowledge base
    pdfs = list(KB_PATH.glob("*.pdf"))
    if pdfs:
        st.markdown("**PDFs in knowledge base:**")
        for p in pdfs:
            st.markdown(f"- {p.name}")
    else:
        st.warning("No PDFs uploaded yet.")

# ── Main: Query ─────────────────────────────────────────────────────────────
st.markdown("---")

query = st.text_area("Ask a question about your PDF:", height=100,
                      placeholder="e.g. What is the Operating Cash Flow to PAT percentage?")

if st.button("🔍 Get Answer", type="primary"):
    pdfs = list(KB_PATH.glob("*.pdf"))
    if not pdfs:
        st.error("Please upload a PDF first.")
    elif not query.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Searching PDF and generating answer..."):
            rag = RAGSystem(config)
            answer = rag.query(query)

        st.markdown("### Answer")
        st.write(answer)
