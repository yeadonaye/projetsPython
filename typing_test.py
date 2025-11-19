import tkinter as tk
import time
import random

# Sentences in English and French
sentences_en = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes perfect.",
    "Artificial intelligence is fascinating.",
    "Type this sentence as fast as you can!",
]

sentences_fr = [
    "Le chat dort sous la table.",
    "Je vais au marché pour acheter des fruits.",
    "Il pleut beaucoup en automne.",
    "Nous aimons regarder les étoiles la nuit.",
    "Elle lit un livre passionnant.",
]


def get_random_sentence(language):
    if language == "en":
        return random.choice(sentences_en)
    elif language == "fr":
        return random.choice(sentences_fr)


def start_test(language):
    global start_time, target_sentence
    target_sentence = get_random_sentence(language)
    sentence_label.config(text=target_sentence)
    user_input.delete(0, tk.END)
    start_time = time.time()
    result_label.config(text="")


def calculate_results():
    end_time = time.time()
    time_taken = end_time - start_time
    user_text = user_input.get()

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(target_sentence, user_text) if a == b)
    accuracy = (correct_chars / len(target_sentence)) * 100 if len(target_sentence) > 0 else 0

    # Calculate WPM
    words = len(target_sentence.split())
    wpm = words / (time_taken / 60) if time_taken > 0 else 0

    # Show results
    result_label.config(
        text=(
            f"Time: {time_taken:.2f} sec | "
            f"WPM: {wpm:.2f} | "
            f"Accuracy: {accuracy:.2f}%"
        )
    )


# Main Window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")
root.configure(bg="#f7f7f7")

# Title
tk.Label(
    root, text="Typing Speed Test", font=("Helvetica", 20, "bold"), bg="#f7f7f7", fg="#333"
).pack(pady=10)

# Language Selection
language_var = tk.StringVar(value="en")
tk.Label(root, text="Select a Language:", font=("Helvetica", 14), bg="#f7f7f7", fg="#555").pack(pady=5)
lang_frame = tk.Frame(root, bg="#f7f7f7")
lang_frame.pack()
tk.Radiobutton(
    lang_frame, text="English", variable=language_var, value="en", font=("Helvetica", 12), bg="#f7f7f7", fg="#333"
).pack(side="left", padx=10)
tk.Radiobutton(
    lang_frame, text="Français", variable=language_var, value="fr", font=("Helvetica", 12), bg="#f7f7f7", fg="#333"
).pack(side="left", padx=10)

# Sentence Display
sentence_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=500, bg="#f7f7f7", fg="#444",
                          justify="center")
sentence_label.pack(pady=20)

# User Input
user_input = tk.Entry(root, font=("Helvetica", 14), width=50, bg="#ffffff", fg="#333")
user_input.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f7f7f7")
button_frame.pack(pady=10)
start_button = tk.Button(
    button_frame,
    text="Start Test",
    command=lambda: start_test(language_var.get()),
    font=("Helvetica", 12, "bold"),
    bg="#4caf50",
    fg="white",
    width=12,
)
start_button.pack(side="left", padx=5)
submit_button = tk.Button(
    button_frame,
    text="Submit",
    command=calculate_results,
    font=("Helvetica", 12, "bold"),
    bg="#2196f3",
    fg="white",
    width=12,
)
submit_button.pack(side="left", padx=5)

# Results
result_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"), bg="#f7f7f7", fg="#ff5722")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
