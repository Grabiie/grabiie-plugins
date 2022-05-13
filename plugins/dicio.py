import dicioinformal
from kannax import Message, kannax

@kannax.on_message("dicio", about={"header": "dicionário"})
async def dicio(message: Message):
    txt = message.input_str
    a = dicioinformal.definicao(txt)["results"]
    if a:
        frase = f'<b>{a[0]["title"]}:</b>\n{a[0]["tit"]}\n\n<i>{a[0]["desc"]}</i>'
    else:
        frase = "sem resultado"
    await message.reply(frase)
