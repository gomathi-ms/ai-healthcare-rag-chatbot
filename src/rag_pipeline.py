from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def create_rag_chain(vector_db):

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo"
    )

    retriever = vector_db.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain
