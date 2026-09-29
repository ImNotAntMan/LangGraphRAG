from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 문서 로드
loader = TextLoader("../../data/notice.txt", encoding="utf-8")
documents = loader.load()
print(f"문서갯수: {len(documents)}")

# 문서를 청크로 나누기
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,  
    chunk_overlap = 30
)
chunks = splitter.split_documents(documents)

print(f"chunk 갯수: {len(chunks)}")
print(f"첫 chunk: {chunks[0].page_content}")
print(f"두번째 chunk: {chunks[1].page_content}")