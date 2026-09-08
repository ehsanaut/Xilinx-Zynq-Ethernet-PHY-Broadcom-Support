# 0 "D:\\Ethernet_Communication_Project\\eproject_1\\sw\\platform\\ps7_cortexa9_0\\standalone_ps7_cortexa9_0\\bsp\\lop-config.dts"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "D:\\Ethernet_Communication_Project\\eproject_1\\sw\\platform\\ps7_cortexa9_0\\standalone_ps7_cortexa9_0\\bsp\\lop-config.dts"

/dts-v1/;
/ {
        compatible = "system-device-tree-v1,lop";
        lops {
                lop_0 {
                        compatible = "system-device-tree-v1,lop,load";
                        load = "assists/baremetal_validate_comp_xlnx.py";
                };

                lop_1 {
                    compatible = "system-device-tree-v1,lop,assist-v1";
                    node = "/";
                    outdir = "D:/Ethernet_Communication_Project/eproject_1/sw/platform/ps7_cortexa9_0/standalone_ps7_cortexa9_0/bsp";
                    id = "module,baremetal_validate_comp_xlnx";
                    options = "ps7_cortexa9_0 C:/Xilinx2024/Vitis/2024.2/data/embeddedsw/ThirdParty/sw_services/lwip220_v1_1/src D:/Ethernet_Communication_Project/eproject_1/sw/_ide/.wsdata/.repo.yaml";
                };

        };
    };
