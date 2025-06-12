import streamlit as st
from rag_engine import process_documents, answer_query
from flashcard_gen import generate_flashcards
from agent import general_chat

st.set_page_config(page_title="RAGucator AI", layout="wide")
st.title("📚🧠 RAGucator AI – Your Smart Study Buddy")

uploaded_files = st.file_uploader("Upload Study PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    docs = process_documents(uploaded_files)
    st.success("Documents processed and indexed for RAG.")

    query = st.text_input("❓ Ask a question based on your study material")
    if query:
        answer = answer_query(query, docs)
        st.markdown(f"### ✅ Answer:\n{answer}")

        with st.expander("🃏 Generate Flashcards"):
            cards = generate_flashcards(answer)
            for q, a in cards:
                st.write(f"**Q:** {q}\n**A:** {a}")

st.markdown("---")
st.subheader("🤖 General AI Assistant")
general_input = st.text_input("Ask any general academic or research question")
if general_input:
    response = general_chat(general_input)
    st.info(response)
