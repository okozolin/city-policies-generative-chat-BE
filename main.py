import policies
from utils import get_user_input, show_content


def process_question(question: str) -> str:
    answer = policies.answer_api(question)
    return answer


def main(question: str = None):
    # web input
    if question:
        process_question(question)
    # command line input
    else:
        while True:
            print("Welcome to Ask Me Policy!")
            question = get_user_input(
                "Please write your question about the public policies. The available topics are:\nTransport, Health, Real estate.\nWhen finished, press <Enter>:\nQ: ")
            if question.lower() in ["exit", "quit"]:
                print("Thank you for using Ask Me Policy. Have a great day!")
                break
            answer = process_question(question)
            print(f"A: {answer}\n")
            show_content(answer)


if __name__ == "__main__":
    main()
