from langchain_community.document_loaders import WebBaseLoader

def load_medical_data():
    
    urls = [
        "https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444",
        "https://www.mayoclinic.org/diseases-conditions/asthma/symptoms-causes/syc-20369653"
    ]

    loader = WebBaseLoader(urls)

    documents = loader.load()

    return documents
