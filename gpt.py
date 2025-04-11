import g4f

def get_multiline_input():
    print("Ты: (Введи текст, затем нажми Enter дважды для отправки)")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "выход":
                return "выход"
            lines.append(line)
        except EOFError:  # Если Ctrl+D (в Unix) или Ctrl+Z+Enter (в Windows)
            break
        if len(lines) >= 2 and not lines[-1] and not lines[-2]:  # Два пустых Enter подряд
            lines = lines[:-2]  # Удаляем последние два пустых ввода
            break
    return "\n".join(lines) if lines else ""

def chat_with_memory():
    history = []
    print("Привет! Я твой AI-ассистент. Пиши многострочные сообщения или 'выход'.")
    
    while True:
        user_input = get_multiline_input()
        
        if user_input.lower().strip() in ['выход', 'exit', 'quit']:
            print("До свидания!")
            break
        
        if not user_input.strip():
            print("(Пустой ввод, попробуй ещё раз)")
            continue
        
        history.append({"role": "user", "content": user_input})
        
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-4",
                messages=history,
                stream=False
            )
            print(f"\nАссистент: {response}\n")
            history.append({"role": "assistant", "content": response})
            
        except Exception as e:
            print(f"Ошибка: {e}")
            history.pop()

if __name__ == "__main__":
    chat_with_memory()