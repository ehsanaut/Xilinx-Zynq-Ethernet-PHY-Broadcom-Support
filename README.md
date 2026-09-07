# Antminer S9 Ethernet PHY with Broadcom Support

A Vivado and Vitis-based Ethernet communication project for the **Antminer S9 board**, extending the Xilinx Ethernet PHY library with support for **Broadcom PHY devices** and evaluating Ethernet communication performance using a ping-pong communication benchmark.

The project includes the complete **Vivado hardware design**, **Vitis software application**, modified Xilinx Ethernet PHY library source code, and two testbench programs for evaluating round-trip communication latency and effective bandwidth.

## Abstract

Xilinx Ethernet libraries provide support for a range of Ethernet PHY devices; however, the **Broadcom PHY integrated into the Antminer S9 board was not supported by the corresponding Xilinx PHY library**.

This project addresses this limitation by extending the Xilinx Ethernet PHY library and adding dedicated support for the Broadcom PHY used by the Antminer S9.

The modified PHY implementation enables the Xilinx Ethernet driver to identify and communicate with the Broadcom device while preserving the existing PHY support provided by the Xilinx library.

The complete hardware/software system was developed using **Vivado and Vitis**, with the Vitis application based on the built-in **Echo Server** example. Ethernet communication performance was evaluated using a **ping-pong test methodology**, measuring round-trip time (RTT), effective bandwidth, latency distribution, and cumulative latency statistics.

Two versions of the communication test program are included:

* A baseline implementation without additional system-level optimization.
* An optimized implementation using warm-up iterations, high thread priority, timer-resolution configuration, and high-resolution performance counters.

The results demonstrate a significant reduction in communication latency and improved effective bandwidth after applying the optimization techniques.

---

## Table of Contents

1. [Overview](#-overview)
2. [Objectives](#-objectives)
3. [System Architecture](#-system-architecture)
4. [Hardware Platform](#-hardware-platform)
5. [Software Environment](#-software-environment)
6. [Broadcom PHY Support](#-broadcom-phy-support)
7. [Vitis Echo Server Application](#-vitis-echo-server-application)
8. [Ping-Pong Communication Test](#-ping-pong-communication-test)
9. [Performance Optimization](#-performance-optimization)
10. [Performance Results](#-performance-results)
11. [Latency Analysis](#-latency-analysis)
12. [Project Structure](#-project-structure)
13. [Vivado Project](#-vivado-project)
14. [Vitis Project](#-vitis-project)
15. [Installation and Usage](#-installation-and-usage)
16. [Test Procedure](#-test-procedure)
17. [Future Improvements](#-future-improvements)
18. [Contributing](#-contributing)
19. [License](#-license)
20. [Author](#-author)

---

# 📌 Overview

The **Antminer S9** contains a Broadcom Ethernet PHY that is not natively supported by the corresponding Xilinx Ethernet PHY library.

As a result, applications running on the Xilinx processing system cannot directly use the standard PHY detection and speed configuration mechanisms for this device.

This project extends the Xilinx PHY implementation by adding support for the Broadcom PHY and integrates the modified library into a complete Vivado/Vitis Ethernet communication system.

The project consists of three main components:

* 🧩 **Vivado hardware design**
* 💻 **Vitis software application**
* 📊 **Ping-pong communication performance evaluation**

The Vitis application is based on the standard **Echo Server** example provided by Vitis. The echo server receives Ethernet packets from the host system and sends the received data back to the sender.

This behavior provides a suitable environment for measuring round-trip communication performance.

---

# 🎯 Objectives

The main objectives of this project are:

* Add **Broadcom PHY support** to the Xilinx Ethernet PHY library.
* Enable Ethernet communication on the **Antminer S9** board.
* Preserve the existing PHY support provided by the Xilinx library.
* Integrate the modified PHY library into a complete **Vivado/Vitis** project.
* Use the Vitis **Echo Server** example for Ethernet communication.
* Develop a ping-pong benchmark for communication performance evaluation.
* Measure round-trip latency and effective bandwidth.
* Analyze latency variations and operating-system-related latency spikes.
* Reduce measurement noise using system-level optimization techniques.
* Compare baseline and optimized communication performance.

---

# 🏗 System Architecture

The overall system consists of a host computer communicating with the Ethernet interface of the Antminer S9 board.

```text
┌──────────────────────────────┐
│        Host Computer         │
│                              │
│  Ping-Pong Test Application  │
│                              │
│  ┌────────────────────────┐  │
│  │ Packet Generation      │  │
│  │ RTT Measurement        │  │
│  │ Performance Analysis   │  │
│  └────────────────────────┘  │
└──────────────┬───────────────┘
               │
               │ Ethernet
               │
               ▼
┌──────────────────────────────┐
│        Antminer S9           │
│                              │
│  ┌────────────────────────┐  │
│  │ Broadcom Ethernet PHY  │  │
│  └────────────┬───────────┘  │
│               │               │
│  ┌────────────▼───────────┐  │
│  │ Xilinx Ethernet Driver │  │
│  │ + Broadcom PHY Support │  │
│  └────────────┬───────────┘  │
│               │               │
│  ┌────────────▼───────────┐  │
│  │ Vitis Echo Server      │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
```

The host sends a packet to the Antminer S9. The Echo Server receives the packet and immediately sends it back to the host.

The elapsed time between transmission and reception is measured as the **Round-Trip Time (RTT)**.

---

# 🖥 Hardware Platform

## Antminer S9

The target hardware platform used in this project is the **Antminer S9**.

The board provides an Ethernet interface based on a **Broadcom PHY device**.

The main challenge addressed by this project is that the Broadcom PHY was not included in the supported PHY devices of the Xilinx Ethernet library used by the project.

Therefore, the PHY driver had to be extended manually.

### Hardware Components

| Component               | Description  |
| ----------------------- | ------------ |
| Target Board            | Antminer S9  |
| Ethernet PHY            | Broadcom     |
| FPGA/SoC Platform       | Xilinx-based |
| Development Tool        | Vivado       |
| Software Tool           | Vitis        |
| Communication Interface | Ethernet     |
| Application             | Echo Server  |

---

# 🔧 Broadcom PHY Support

## Motivation

The standard Xilinx Ethernet PHY library provides support for several PHY vendors and devices.

However, the Broadcom PHY used by the Antminer S9 was not included in the supported device list.

Therefore, the original PHY implementation could not properly identify and configure the Broadcom device.

To solve this problem, Broadcom-specific PHY identification and speed-detection logic was added to the Xilinx Ethernet PHY library.

---

## Driver Modifications

The modified PHY implementation includes:

* Broadcom PHY identifier definition.
* Broadcom PHY model definitions.
* Broadcom PHY model mask.
* Broadcom PHY identification.
* Broadcom PHY speed detection.
* Broadcom-specific PHY initialization support.
* Integration with the existing IEEE PHY speed detection mechanism.
* Broadcom support in the PHY identification logic.

The modification was performed while preserving the existing Xilinx implementations for other PHY vendors.

Therefore, the modified library supports both the original PHY devices and the newly added Broadcom device.

### Supported Broadcom Device

The implementation specifically includes support for the Broadcom **B50612** family.

The driver also contains model detection for:

```text
B50612D
B50612E
```

This allows the PHY implementation to distinguish between supported Broadcom models.

---

# 💻 Vitis Echo Server Application

The software running on the Antminer S9 is based on the standard **Echo Server** example provided by Vitis.

The Echo Server implements a simple request-response communication mechanism:

```text
Host
 │
 │ Ethernet Packet
 ▼
Antminer S9
 │
 │ Echo
 ▼
Host
```

This makes the application suitable for evaluating communication latency because every transmitted packet generates a corresponding response.

No application-level processing is required between reception and transmission, allowing the benchmark to primarily observe the Ethernet communication path and software/networking overhead.

---

# 🔄 Ping-Pong Communication Test

Two test programs are included in the project for evaluating Ethernet communication performance.

The test follows a ping-pong communication pattern.

For every iteration:

1. The host sends a packet.
2. The Antminer S9 receives the packet.
3. The Echo Server sends the packet back.
4. The host receives the response.
5. The RTT is calculated.
6. The result is recorded.

The test is repeated for:

```text
20,000 samples
```

The measured parameters include:

* Round-Trip Time (RTT)
* Average RTT
* Robust average RTT
* Median RTT
* Standard deviation
* Minimum RTT
* Maximum RTT
* Effective bandwidth
* Cumulative latency distribution

---

# ⚙️ Performance Optimization

The baseline implementation was affected by operating-system scheduling and other system-level effects.

In particular, occasional latency spikes can be observed due to **operating-system context switching**.

To reduce these effects, several optimizations were applied to the measurement application.

## 🔥 Warm-Up

Before starting the actual measurement, the application performs:

```text
1,000 send/receive iterations
```

These warm-up iterations are intended to eliminate initial overheads such as:

* Initial buffer allocation
* Cache initialization
* Network stack initialization
* Other one-time system overheads

Only the measurements collected after the warm-up phase are used for the final performance analysis.

---

## 🚀 Thread Priority

The measurement thread is assigned the highest possible Windows thread priority using:

```text
THREAD_PRIORITY_TIME_CRITICAL
```

The implementation also disables temporary priority boosting using:

```text
SetThreadPriorityBoost(False)
```

This reduces the possibility of temporary scheduler-induced interruptions during the measurement process.

---

## ⏱ Timer Resolution

The application uses:

```text
timeBeginPeriod(1)
```

This requests a system timer resolution of approximately **1 ms**.

This configuration is useful for operations such as:

```text
time.sleep()
```

and other system-level timing functions.

It does not directly determine the resolution of the `perf_counter_ns()` measurement.

---

## 📏 High-Resolution Measurement

RTT measurements are performed using:

```text
perf_counter_ns()
```

This provides a high-resolution performance counter suitable for measuring short communication intervals.

The timestamps are taken immediately before packet transmission and after receiving the corresponding response.

---

# 📊 Performance Results

Three different host-system configurations were evaluated.

The experiments include:

1. Baseline system without optimization.
2. Optimized measurement on a medium-performance system.
3. Optimized measurement on a high-performance system.

---

## 1. Baseline System — No Optimization

The first experiment was performed without the optimization techniques described above.

| Metric                |      Result |
| --------------------- | ----------: |
| Total Samples         |      20,000 |
| Total Execution Time  |    6.2238 s |
| Effective Bandwidth   | 6426.95 B/s |
| Effective Bandwidth   |  0.051 Mbps |
| Average RTT           |    0.310 ms |
| Standard Deviation    |    0.795 ms |
| Minimum RTT           |    0.128 ms |
| Maximum RTT           |   29.946 ms |
| RTT ≤ 0.122 ms        |   0 samples |
| Percentage ≤ 0.122 ms |       0.00% |

The maximum RTT of approximately **29.946 ms** demonstrates the presence of significant latency spikes.

These spikes are attributed to operating-system scheduling and context-switching effects during the measurement process.

---

# 2. Optimized System — Medium Configuration

The second experiment applies the optimization techniques, including the warm-up stage and improved system configuration.

### Results

| Metric                |      Result |
| --------------------- | ----------: |
| Total Samples         |      20,000 |
| Total Execution Time  |    4.0197 s |
| Effective Bandwidth   | 9951.00 B/s |
| Effective Bandwidth   |  0.080 Mbps |
| Average RTT           |    0.199 ms |
| Robust Average RTT    |    0.198 ms |
| Median RTT            |    0.196 ms |
| Standard Deviation    |    0.011 ms |
| Minimum RTT           |    0.131 ms |
| Maximum RTT           |    0.399 ms |
| RTT ≤ 0.122 ms        |   0 samples |
| Percentage ≤ 0.122 ms |       0.00% |

Compared with the baseline configuration, the optimized configuration significantly reduces the variation in latency.

The maximum observed RTT decreases from:

```text
29.946 ms → 0.399 ms
```

and the standard deviation decreases from:

```text
0.795 ms → 0.011 ms
```

This demonstrates the importance of controlling the execution environment during low-latency communication measurements.

---

# 3. Optimized System — High-Performance Configuration

The third experiment was performed on a more powerful host system using the optimized measurement configuration.

### Results

| Metric                |         Result |
| --------------------- | -------------: |
| Total Samples         |         20,000 |
| Total Execution Time  |       1.5299 s |
| Effective Bandwidth   |   26146.06 B/s |
| Effective Bandwidth   |     0.209 Mbps |
| Average RTT           |       0.076 ms |
| Robust Average RTT    |       0.068 ms |
| Median RTT            |       0.071 ms |
| Standard Deviation    |       0.052 ms |
| Minimum RTT           |       0.049 ms |
| Maximum RTT           |       2.912 ms |
| RTT ≤ 0.122 ms        | 19,289 samples |
| Percentage ≤ 0.122 ms |         96.45% |

The optimized high-performance configuration achieves the lowest average latency:

```text
0.076 ms
```

and the highest effective bandwidth:

```text
0.209 Mbps
```

Furthermore, **96.45% of the measurements have an RTT below 0.122 ms**.

---

# 📈 Performance Comparison

| Metric         |   Baseline | Optimized – Medium | Optimized – High |
| -------------- | ---------: | -----------------: | ---------------: |
| Samples        |     20,000 |             20,000 |           20,000 |
| Execution Time |   6.2238 s |           4.0197 s |         1.5299 s |
| Bandwidth      | 0.051 Mbps |         0.080 Mbps |       0.209 Mbps |
| Average RTT    |   0.310 ms |           0.199 ms |         0.076 ms |
| Median RTT     |          — |           0.196 ms |         0.071 ms |
| Robust Average |          — |           0.198 ms |         0.068 ms |
| Std. Deviation |   0.795 ms |           0.011 ms |         0.052 ms |
| Minimum RTT    |   0.128 ms |           0.131 ms |         0.049 ms |
| Maximum RTT    |  29.946 ms |           0.399 ms |         2.912 ms |
| RTT ≤ 0.122 ms |      0.00% |              0.00% |           96.45% |

---

# 📉 Latency Analysis

The project includes several visualization results generated from the ping-pong measurements.

These figures can be placed in the `figures/` directory.

## Latency per Transmission

The first visualization shows the RTT measured for every packet transmission.

```text
figures/
└── latency_per_sample.png
```

This plot is useful for identifying:

* Latency spikes
* System scheduling effects
* Communication stability
* Outlier measurements

---

## Cumulative Percentage of Samples

The cumulative percentage plot shows the percentage of measurements below different RTT thresholds.

```text
figures/
└── cumulative_percentage.png
```

This visualization provides a direct representation of the percentage of packets achieving a specific latency target.

---

## Cumulative Distribution

The cumulative distribution visualization provides another view of the RTT distribution across all collected samples.

```text
figures/
└── cumulative_distribution.png
```

Together, these plots provide a more complete characterization of the communication latency than average RTT alone.

> **Note:** The actual figure filenames can be updated in this README to match the files included in the repository.

---

# 📁 Project Structure

The repository is organized into separate Vivado, Vitis, driver, benchmark, and analysis components.

```text
Antminer-S9-Ethernet-PHY-Broadcom-Support
│
├── vivado/
│   └── <Vivado project files>
│
├── vitis/
│   └── <Vitis workspace and application files>
│
├── drivers/
│   └── xilinx/
│       └── xemacpsif_physpeed.c
│
├── tests/
│   ├── ping_pong_baseline/
│   │   └── <baseline test application>
│   │
│   └── ping_pong_optimized/
│       └── <optimized test application>
│
├── results/
│   ├── baseline/
│   ├── optimized_medium/
│   └── optimized_high/
│
├── figures/
│   ├── latency_per_sample.png
│   ├── cumulative_percentage.png
│   └── cumulative_distribution.png
│
├── README.md
└── LICENSE
```

---

# 🛠 Vivado Project

The Vivado project contains the hardware design required to run the Ethernet communication system on the Antminer S9 platform.

The hardware project is responsible for configuring the target Xilinx system and providing the hardware platform required by the Vitis application.

The generated hardware platform is exported to Vitis, where the Echo Server application is built and executed.

---

# 💻 Vitis Project

The Vitis project contains the software application running on the target hardware.

The main application is based on the Vitis **Echo Server** example.

The modified Xilinx Ethernet PHY library is integrated into the software platform to provide Broadcom PHY support.

The application can therefore initialize the Ethernet interface and communicate with the Broadcom PHY used by the Antminer S9.

---

# 🚀 Installation and Usage

## Requirements

The project requires:

* Xilinx Vivado
* Xilinx Vitis
* Antminer S9 board
* Ethernet connection
* Host computer
* Modified Xilinx Ethernet PHY library

The exact Vivado/Vitis version used for the project should preferably be kept consistent when reproducing the results.

---

## Clone the Repository

```bash
git clone https://github.com/<your-username>/Antminer-S9-Ethernet-PHY-Broadcom-Support.git

cd Antminer-S9-Ethernet-PHY-Broadcom-Support
```

---

# 🏗 Build the Vivado Project

1. Open the Vivado project located in the `vivado/` directory.
2. Verify the target board/device configuration.
3. Generate the required hardware design.
4. Generate the bitstream.
5. Export the generated hardware platform for Vitis.

---

# 💻 Build the Vitis Project

1. Open Vitis.
2. Import the exported hardware platform.
3. Import or create the Echo Server application.
4. Make sure the modified Ethernet PHY library is used.
5. Build the application.
6. Program the Antminer S9.
7. Start the Echo Server.

---

# 🧪 Test Procedure

After the Echo Server is running on the Antminer S9:

1. Connect the host computer to the board through Ethernet.
2. Start the ping-pong test application.
3. Send a packet to the Echo Server.
4. Wait for the echoed packet.
5. Calculate RTT.
6. Repeat the process for 20,000 samples.
7. Store the measured RTT values.
8. Generate the latency and cumulative-distribution plots.
9. Compare the results between the baseline and optimized configurations.

---

# 📌 Important Notes

The latency measurements are affected by the operating system running the benchmark application.

In particular, **context switching and scheduler activity can introduce occasional latency spikes**.

For more consistent measurements, the benchmark process should ideally:

* Run with high priority.
* Be assigned to a specific CPU core.
* Use a warm-up phase before collecting measurements.
* Use a high-resolution performance counter.
* Minimize unnecessary background processes.

Therefore, the reported latency should be interpreted as an experimental measurement of the complete host-to-board communication path rather than as an absolute hardware-only PHY latency.

---

# 🔮 Future Improvements

Several improvements can be considered for future versions of the project:

### PHY Driver

* Extend support to additional Broadcom PHY models.
* Improve Broadcom PHY initialization.
* Add automatic PHY configuration.
* Add more detailed PHY diagnostics.
* Improve portability across Xilinx Ethernet driver versions.

### Performance Measurement

* Pin the benchmark process to a dedicated CPU core.
* Perform measurements on a real-time operating system.
* Reduce operating-system scheduling interference.
* Add packet-size sweep experiments.
* Evaluate throughput at different Ethernet configurations.
* Analyze packet loss and jitter.

### Hardware

* Investigate hardware-level timestamping.
* Compare PHY and MAC latency.
* Evaluate different Ethernet configurations.
* Integrate hardware performance counters.

### Analysis

* Add automated result generation.
* Add statistical confidence intervals.
* Compare additional host systems.
* Automate latency-distribution analysis.

---

# 🤝 Contributing

Contributions and improvements are welcome.

Possible contributions include:

* Supporting additional Broadcom PHY devices.
* Improving the PHY driver implementation.
* Adding additional Ethernet benchmarks.
* Improving the performance-analysis scripts.
* Adding new visualization methods.
* Testing the project on other Xilinx-based boards.

Feel free to:

* Open an issue.
* Submit a pull request.
* Report bugs.
* Suggest improvements.

---

# 📄 License

This project is licensed under the **MIT License**.

Please note that the modified Xilinx source files may be subject to the original licensing terms of the Xilinx/Vitis software distribution.

---

# 👤 Author

**Behzad Jannati**

M.Sc. Student in Computer Engineering — Computer Architecture
University of Tehran

Research Interests:

* Computer Architecture
* FPGA and Hardware Acceleration
* Embedded AI Systems
* Hardware/Software Co-Design
* Ethernet and Networked Embedded Systems
* Hardware Security
* Machine Learning Systems

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐.

---

Built with ❤️ using **Xilinx Vivado, Vitis, and the Antminer S9 Ethernet platform**.
