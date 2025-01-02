import modal

app = modal.App.lookup("sandbox", create_if_missing=True)

sb = modal.Sandbox.create(
    "bash",
    "-c",
    "python3 -m http.server 12345",
    encrypted_ports=[12345],
    app=app,
)

tunnel = sb.tunnels()[12345]
print(tunnel)

sb.terminate()
