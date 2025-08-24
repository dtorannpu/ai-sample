import os
import getpass
from langchain.chat_models import init_chat_model


def main():
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass(
            "Enter API key for Google Gemini: "
        )

    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")\

    m = model.invoke("Hello, world!")

    print(m.text())


if __name__ == "__main__":
    main()
