import os
import time
from openai import OpenAI
from dotenv import load_dotenv  # Import python-dotenv
from openai.types.beta.threads import Run

from utils import show_json

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

assistant_id=os.environ.get("ASSISTANT_ID")


def wait_on_run(run_wait, thread_wait):
    while run_wait.status == "queued" or run_wait.status == "in_progress":
        run_wait: Run = client.beta.threads.runs.retrieve(
            thread_id=thread_wait.id,
            run_id=run_wait.id,
        )
        time.sleep(0.5)
    return run_wait


def answer_api(question):
    #thread
    thread = client.beta.threads.create()
    show_json(thread)

    #message
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        # content="מה המדיניות לגבי קירות תמך?",
        content=question,
    )
    #show_json(message)

    #run
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )
    #show_json(run)

    run = wait_on_run(run, thread)
    #show_json(run)

    #messages
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    #show_json(messages)


    # Retrieve all the messages added after our last user message
    messages_after = client.beta.threads.messages.list(
        thread_id=thread.id, order="asc", after=message.id
    )
    # show_json(messages_after)
    return messages_after

