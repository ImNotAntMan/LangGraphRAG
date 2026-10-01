from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv() # openai key 불러오기

emb = OpenAIEmbeddings(model="text-embedding-3-small")

vec = emb.embed_query("환불 규정이 궁금합니다.") # 질문을 벡터화

print("차원 수 :", len(vec))

first_10 = []

for value in vec[:10]:
    first_10.append(round(value, 4))

print("10개 :", first_10)