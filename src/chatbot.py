def ask_question(chain, question):

    response = chain.invoke(question)

    return response
