import modal

app = modal.App.lookup("sandbox", create_if_missing=True)
sb = modal.Sandbox.create(app=app)

p = sb.exec("ls", "-l")
print(p.stdout.read())

sb.terminate()
