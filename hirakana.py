import tkinter as tk
import random

# 히라가나와 한국어 발음 대응표
hiragana_dict = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}

class HiraganaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("히라가나 게임")
        self.score = 0
        self.question_number = 0
        self.questions = random.sample(list(hiragana_dict.items()), 10)
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 24))
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_answer)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.feedback_label.pack(pady=20)

        self.next_button = tk.Button(root, text="다음", command=self.next_question, font=("Helvetica", 24))
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.score_label.pack(pady=20)
        
        self.next_question()

    def check_answer(self, event=None):
        user_answer = self.entry.get().strip()
        correct_answer = self.questions[self.question_number][1]
        
        if user_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="정답입니다!", fg="green")
        else:
            self.feedback_label.config(text=f"틀렸습니다! 정답은 {correct_answer}입니다.", fg="red")

        self.entry.delete(0, tk.END)
        self.question_number += 1

        if self.question_number >= 10:
            self.show_score()
        else:
            self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        if self.question_number < 10:
            self.question_label.config(text=self.questions[self.question_number][0])
            self.feedback_label.config(text="")
            self.next_button.config(state=tk.DISABLED)
            self.entry.focus()
        else:
            self.show_score()

    def show_score(self):
        self.question_label.config(text="")
        self.feedback_label.config(text="")
        self.next_button.pack_forget()
        self.entry.pack_forget()
        self.score_label.config(text=f"게임 끝! 점수: {self.score}/10")

if __name__ == "__main__":
    root = tk.Tk()
    game = HiraganaGame(root)
    root.mainloop()
