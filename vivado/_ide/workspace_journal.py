# 2026-09-01T20:21:28.789738100
import vitis

client = vitis.create_client()
client.set_workspace(path="eproject_1")

platform = client.create_platform_component(name = "platform",hw_design = "$COMPONENT_LOCATION/../design_1_wrapper.xsa",os = "standalone",cpu = "ps7_cortexa9_0",domain_name = "standalone_ps7_cortexa9_0")

platform = client.get_component(name="platform")
domain = platform.get_domain(name="standalone_ps7_cortexa9_0")

status = domain.set_lib(lib_name="lwip220", path="C:\Xilinx2024\Vitis\2024.2\data\embeddedsw\ThirdParty\sw_services\lwip220_v1_1")

status = domain.regenerate()

status = platform.build()

status = domain.set_config(option = "lib", param = "XILTIMER_en_interval_timer", value = "true", lib_name="xiltimer")

status = platform.build()

vitis.dispose()

