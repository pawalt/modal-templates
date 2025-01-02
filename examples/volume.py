import modal

app = modal.App("test")

volume = modal.Volume.from_name("test-volume", create_if_missing=True)


@app.function(volumes={"/my-mount": volume})
def f():
    print("hello")


@app.local_entrypoint()
async def main():
    f.remote()
