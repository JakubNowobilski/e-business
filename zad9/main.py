from llama_client import generate_text


def run_server():
    result = generate_text("Why is the sky blue?")
    print(result)


if __name__ == '__main__':
    run_server()

