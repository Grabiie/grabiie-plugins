# by DaviTudo


from userge import Message, userge

@userge.on_cmd("k|K", about={"header": "risada curta"}, allow_via_bot=False)
async def k(message: Message):
    out_str =f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("kkk|KKK", about={"header": "risada  longa"}, allow_via_bot=False)
async def kkk(message: Message):
    out_str = f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

