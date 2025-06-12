from agent import general_chat

def generate_flashcards(text):
    prompt = f"Convert this explanation into 3 flashcards with Q&A format:\n\n{text}"
    raw = general_chat(prompt)
    cards = []
    for line in raw.split("\n"):
        if "Q:" in line and "A:" in line:
            q = line.split("Q:")[1].split("A:")[0].strip()
            a = line.split("A:")[1].strip()
            cards.append((q, a))
    return cards
