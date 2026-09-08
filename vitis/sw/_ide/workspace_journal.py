# 2026-09-07T18:42:46.959870300
import vitis

client = vitis.create_client()
client.set_workspace(path="sw")

platform = client.get_component(name="platform")
status = platform.build()

comp = client.get_component(name="lwip_echo_server")
comp.build()

status = platform.build()

status = platform.build()

comp.build()

vitis.dispose()

