import modal

app = modal.App("test")

@app.function()
def f():
    print("hello")


@app.local_entrypoint()
async def main():
    f.remote()
