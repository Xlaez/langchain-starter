from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from env_loader import OPENAI_API_KEY


loader = YoutubeLoader.from_youtube_url('https://youtu.be/pNcQ5XXMgH4?list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5', add_video_info=True)

result = loader.load()

print(type(result))
print(f"Found video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
print(' \n')

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_summarize_chain(llm=llm, chain_type="stuff", verbose=False)
final_result = chain.run(result)
print(final_result)