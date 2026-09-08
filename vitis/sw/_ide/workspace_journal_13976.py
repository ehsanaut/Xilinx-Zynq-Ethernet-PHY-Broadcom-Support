# 2026-09-01T20:32:51.643209600
import vitis

client = vitis.create_client()
client.set_workspace(path="sw")

platform = client.create_platform_component(name = "platform",hw_design = "$COMPONENT_LOCATION/../../design_1_wrapper.xsa",os = "standalone",cpu = "ps7_cortexa9_0",domain_name = "standalone_ps7_cortexa9_0")

platform = client.get_component(name="platform")
domain = platform.get_domain(name="standalone_ps7_cortexa9_0")

status = domain.set_lib(lib_name="lwip220", path="C:\Xilinx2024\Vitis\2024.2\data\embeddedsw\ThirdParty\sw_services\lwip220_v1_1")

status = platform.build()

comp = client.create_app_component(name="lwip_echo_server",platform = "$COMPONENT_LOCATION/../platform/export/platform/platform.xpfm",domain = "standalone_ps7_cortexa9_0",template = "lwip_echo_server")

status = platform.build()

comp = client.get_component(name="lwip_echo_server")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

vitis.dispose()

