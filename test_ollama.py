import ollama

response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'user',
            'content': 'Explain what a savings account is in simple words.'
        }
    ]
)

print(response['message']['content'])