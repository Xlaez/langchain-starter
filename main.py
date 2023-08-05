from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.chains  import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import magic
import os
import nltk

load_dotenv()

# Remove API key before commiting
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

loader = DirectoryLoader('./data', glob='**/*.txt*')
document = loader.load()

text_splitter = CharacterTextSplitter(separator="\n\n")
texts = text_splitter.split_documents(document)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

docSearch = Chroma.from_documents(texts, embeddings)
# Initialize model

qa_chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=docSearch.as_retriever(search_kwargs={"k":1}))

query =  "What are the main problems in the Nigerian education system?"
answer = qa.run(query)
print(answer)


