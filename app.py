#!/usr/bin/env python3

import sys
import json
import requests

OPENROUTER_API_KEY = "ENTER YOUR OPENROUTER API KEY HERE"

MODEL = "meta-llama/llama-3.1-8b-instruct"

SYSTEM_PROMPT = """
You are wsl ubuntu terminal expert.
Give very short answer to my question.
The answer should be very short, but answer the question based on the terminal topic.
""".strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: myapp <question>")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "stream": True,
        },
        stream=True,
        timeout=300,
    )

    response.raise_for_status()

    for line in response.iter_lines():
        if not line:
            continue

        line = line.decode("utf-8")

        if not line.startswith("data: "):
            continue

        data = line[6:]

        if data == "[DONE]":
            break

        try:
            chunk = json.loads(data)
            delta = chunk["choices"][0].get("delta", {}).get("content")

            if delta:
                print(delta, end="", flush=True)

        except Exception:
            pass

    print()


if __name__ == "__main__":
    main()
