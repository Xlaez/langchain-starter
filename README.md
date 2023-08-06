# langchain-starter

## Requirments 
- python version >= 3.6
- install langchain
- OpenAI's private key
- If you wan't to run the query_book.py then you'll also need the pinecode's apikey and apienv

You can always change the pdf and the text file to your preferred so as to get what you want.
using python or pthon3, run the file you want to execute. Example:

`python3 transcript_gen.py` would give you a summary of the video who's youtube link is in the code (you can update this to your preffered). It basically gets the transcript of the video then uses embeddings to get summaries of this video then get a summary of each individual summary.

The `query_book.py` splits the statistics university revision pdf to chunks of 98 then passes it through embeddings to postcone using cosine metrics and query's the book based on the question asked. It returns an answer based on what it got's from the book. So it's just like asking the pdf a question.
