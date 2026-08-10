import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Meme Sidecar API")

# Пошловатые и смешные ASCII-мемы
MEMES = [
    r"""
     (\_/)
     ( •_•)
    / > 8==D~ Вычисления прошли успешно!
    """,
    r"""
      .---.
     /_____\
     ( '.' )
      \_-_/_
    .-"`'V'//-.
   / ,   |// , \
  / /|Ll //Ll|\ \
 / / |__//   | \_\
 \ \/---|[]==| / /
  \/\__/ |   \/\/
   |/_   | Ll_\|
     |`^"""^`|
     |   |   |
     |   |   |
     |   |   |
     |   |   |
     L___l___J
      |_ | _|
     (___|___)
    """,
    r"""
    ( ͡° ͜ʖ ͡°)
    Я починил твою математику, бро.
    """,
    r"""
       _
      / \
      | |
      | |
      | |
     /   \
     |   |
     \___/
    У меня встал... вопрос, как ты так считаешь?
    """
]

# Простая 3D генерация цифр для консоли
DIGITS_3D = {
    '0': ["  ___  ", " / _ \ ", "| | | |", "| |_| |", " \___/ "],
    '1': [" __ ", "/_ |", " | |", " | |", " |_|"],
    '2': [" ___  ", "|__ \ ", "   ) |", "  / / ", " /___\ "],
    '3': [" ____  ", "|___ \ ", "  __) |", " |__ < ", " |___/ "],
    '4': [" _  _   ", "| || |  ", "| || |_ ", "|__   _|", "   |_|  "],
    '5': [" _____ ", "| ____|", "| |__  ", "|___ \ ", " |___/ "],
    '6': ["   __  ", "  / /  ", " / /_  ", "| '_ \ ", " \___/ "],
    '7': [" ______ ", "|____  |", "    / / ", "   / /  ", "  /_/   "],
    '8': ["  ___  ", " / _ \ ", "| (_) |", " > _ < ", "| (_) |", " \___/ "],
    '9': ["  ___  ", " / _ \ ", "| (_) |", " \__, |", "   /_/ "]
}

class MemeResponse(BaseModel):
    meme: str

class ArtResponse(BaseModel):
    art: str

@app.get("/meme", response_model=MemeResponse)
def get_random_meme():
    return {"meme": random.choice(MEMES).strip("\n")}

@app.get("/3d/{number}", response_model=ArtResponse)
def get_3d_number(number: str):
    # Генерируем 3D текст из цифр (собираем построчно)
    if not all(char in DIGITS_3D or char == '-' for char in number):
        return {"art": number} # Возвращаем как есть, если это не просто цифры
        
    lines = ["", "", "", "", "", ""]
    for char in number:
        if char == '-':
            art = ["      ", "      ", " ____ ", "|____|", "      ", "      "]
        else:
            art = DIGITS_3D.get(char, [""]*6)
            # Дополняем до 6 строк, если меньше
            while len(art) < 6:
                art.append(" " * len(art[0]))
        
        for i in range(6):
            if i < len(art):
                lines[i] += art[i] + "  "
                
    return {"art": "\n".join(line for line in lines if line.strip())}
