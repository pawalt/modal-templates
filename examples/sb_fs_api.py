bmport modal

app = modal.App.lookup("sandbox-fs-demo", create_if_missing=True)
sb = modal.Sandbox.create(app=app)

with sb.open("test.txt", "w") as f:
    f.write("Hello World\n")
f = sb.open("test.txt", "rb")
print(f.read())
f.close()

sb.terminate()
