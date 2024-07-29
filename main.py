import policies
from utils import get_user_input, show_content


def main():
    print("Welcome to Ask Me Policy!")
    while True:
        question = get_user_input("Please write your question about the public policies. The available topics are:\nTransport, Health, Real estate.\nWhen finished, press <Enter>:\nQ: ")
        if question.lower() in ["exit", "quit"]:
            print("Thank you for using Ask Me Policy. Have a great day!")
            break
        answer = policies.answer_api(question)
        # print(f"A: {answer}\n")
        show_content(answer)

if __name__ == "__main__":
    main()
