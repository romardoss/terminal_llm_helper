# terminal_llm_helper
## Description
Use this script to enhance linux terminal learning. It uses LLM to answer the questions

## Setup
In app.py change OPENROUTER_API_KEY to your openrouter key
You also can change MODEL to your loved one, but take into account the api prices
You also can change SYSTEM_PROMPT or completely remove it to get universal llm in terminal

## Create a tool
You can make this script run as command in linux, google how to do that
I made it another way by adding alias

```bash
nano ~/.bashrc
# move to the bottom of the file and add next line
alias llm='~/projects/terminal_llm_helper/app.py'
# then press ctrl+O, enter, ctrl+X, and reload terminal
source ~/.bashrc
```

Now I can call my helper by typing
```bash
llm <my prompt>
```
