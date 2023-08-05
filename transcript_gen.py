from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain

loader = YoutubeLoader.from_youtube_url('https://youtu.be/pNcQ5XXMgH4?list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5', add_video_info=True)

result = loader.load()

print(type(result))
print(f"Found video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
print(' \n')
print(result)

