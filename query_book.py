from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import pinecone
from env_loader import OPENAI_API_KEY, PINECONE_API_KEY,PINECONE_API_ENV

loader = UnstructuredPDFLoader('./data/statistics.pdf')

data = loader.load()

print(f"You have {len(data)} documents(s) in your data")
print(f"There are {len(data[0].page_content)} characters in your document")

# Break the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(data)

print(f"Now you have {len(texts)} documents")

# Setting embeddings and getting documents ready for search

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

index_name = 'langchain1'

if(index_name not in pinecone.list_indexes()):
    pinecone.create_index(name=index_name, metric='cosine', dimension=1536)

docSearch = Pinecone.from_texts([t.page_content for t in texts], embedding=embeddings, index_name=index_name)


llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

query = "What is probability theorem?"
docs = docSearch.similarity_search(query=query)

# convert to natural language
result = chain.run(input_documents=docs, question=query)
print(result)
