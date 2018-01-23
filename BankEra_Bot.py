import discord

token = "NDA0NjE0MDc1OTU2NDYxNTY4.DUi32g.4VQ5i5U0Gnak-bv0hKD1XM4mjbI"

client = discord.Client()

client.get_all_members()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("!bank"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            count = 0
            for member in client.get_all_members() :
                count += 1
            m = "報告します！ 現在 " + str(count) + "エラリストが参加中です！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)


client.run(token)

