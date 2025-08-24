from langfuse.langchain import CallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langfuse import get_client


def main():
    """Langfuseサンプル."""
    langfuse = get_client()
    langfuse_handler = CallbackHandler()
    langfuse_chat_prompt = langfuse.get_prompt("sample", type="chat")
    langchain_prompt = ChatPromptTemplate(
        langfuse_chat_prompt.get_langchain_prompt(),
        metadata={"langfuse_prompt": langfuse_chat_prompt},
    )
    model = langfuse_chat_prompt.config["model"]
    temperature = str(langfuse_chat_prompt.config["temperature"])
    print(f"Prompt model configurations\nModel: {model}\nTemperature: {temperature}")
    model = ChatGoogleGenerativeAI(model=model, temperature=temperature)
    chain = langchain_prompt | model
    response = chain.invoke(
        input={"topic": "cats"}, config={"callbacks": [langfuse_handler]}
    )
    print(response.content)


if __name__ == "__main__":
    main()
