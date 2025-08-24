from langsmith import Client


def main():
    """Langsmithサンプル."""

    client = Client()
    chain = client.pull_prompt("sample", include_model=True)
    response = chain.invoke({})
    print(response.text())


if __name__ == "__main__":
    main()
