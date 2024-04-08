from langchain.document_loaders import Docx2txtLoader, PyPDFLoader, UnstructuredExcelLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import MultiQueryRetriever, ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.chat_models.openai import ChatOpenAI
import logging


class ChatDoc():
    def __init__(self):
        self.doc = None
        self.splitText = []  # 分割后的文本

    def getFile(self):
        doc = self.doc
        loaders = {
            "docx": Docx2txtLoader,
            "pdf": PyPDFLoader,
            "xlsx": UnstructuredExcelLoader,
        }
        file_extension = doc.split(".")[-1]
        loader_class = loaders.get(file_extension)
        if loader_class:
            try:
                loader = loader_class(doc)
                text = loader.load()
                return text
            except Exception as e:
                print(f"Error loading {file_extension} files:{e}")
        else:
            print(f"Unsupported file extension: {file_extension}")
            return None

    # 处理文档的函数
    def splitSentences(self):
        full_text = self.getFile()  # 获取文档内容
        if full_text is not None:
            # 对文档进行分割
            text_split = CharacterTextSplitter(
                chunk_size=150,
                chunk_overlap=20,
            )
            texts = text_split.split_documents(full_text)
            self.splitText = texts

    def embeddingAndVectorDB(self):
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )
        db = Chroma.from_documents(
            documents=self.splitText,
            embedding=embeddings,
        )
        return db

        # 提问并找到相关的文本块
    def askAndFindFiles(self, question):
        db = self.embeddingAndVectorDB()
        # retriever = db.as_retriever(search_type="mmr")
        retriever = db.as_retriever(search_type="similarity_score_threshold",
                                    search_kwargs={"score_threshold": .1, "k": 1})
        return retriever.get_relevant_documents(query=question)


chat_doc = ChatDoc()
chat_doc.doc = "fake.xlsx"
chat_doc.splitSentences()
# 设置下logging查看生成查询
# 设置下logging查看生成查询
logging.basicConfig(level=logging.INFO)
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.DEBUG)
unique_doc = chat_doc.askAndFindFiles("这间公司的负债有多少？")
print(unique_doc)
