import Prompt, Client

c = Client.Client("localhost", 2000)

p = Prompt.Prompt(c)

while c.running:
    p.prompt()
