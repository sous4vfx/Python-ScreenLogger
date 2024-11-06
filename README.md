# 👁️ ScreenLogger (My First Project)

A **Simple ScreenLogger** built with **Python** that sends **Screenshots** via email.

## 📕 About

This project was created for a school assignment, inspired by similar projects found on GitHub, and is intended for **educational purposes**.

## 💻 What Does This Project Do?

- This project allows you to send **screenshots** from your PC to an email, along with system information such as **Hostname**, **User**, **IP**, and **OS**.
- You can configure the **number of screenshots per email** and the **delay** between screenshots.
- The script can be converted into an **executable file** and automatically added to the **Startup folder** of the system, so it runs on startup.

## 🛠️ Features

![Features](https://github.com/user-attachments/assets/54deb6db-15dd-4f27-bb21-49e410000769)

- **Copy the executable to Startup**
- Take **Screenshots**
- Get **Hostname**
- Get **User** Information
- Get **IP Address**

## ⚙️ Default Settings

- `count >= 20`: The number of screenshots per email (default: **20**).
- `time.sleep(1)`: The delay between each screenshot (default: **1 second**).

## 🛡️ Antivirus Test

![Antivirus Test](https://github.com/user-attachments/assets/9bddf949-9f72-4810-b819-be4c866aee9e)
![Antivirus Test 2](https://github.com/user-attachments/assets/e5bb72a7-e698-4806-9774-933af345e2e6)

## 💾 EXE File

If you want to use ScreenLogger as an executable, you can use the [AutoPyToExe](https://pypi.org/project/auto-py-to-exe/) library.

After creating the **.exe file**, change the variable `(originalfilename)` to the name of your executable file. Other adjustments, such as modifying the `(copiedfilename)` variable, will enable the program to automatically copy the executable to the **Startup folder** of the Windows system.

## 💡 Credits

This ScreenLogger was inspired by various other projects. If any creator recognizes their work here, please contact me for proper attribution!
