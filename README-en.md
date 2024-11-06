# 👁️ **ScreenLogger** - My First Project

A **Simple ScreenLogger** built with **Python** that sends **Screenshots** to your email.

## 📚 About

This project was created for a school assignment and is based on other open-source projects found on GitHub. It was made entirely for educational purposes.

## 🔧 Features

- **Send Screenshots via Email**: Capture and send screenshots of your PC, along with **Hostname, System, User, and IP** information.
- **Customizable Settings**: Easily change the number of screenshots in each email and the delay between screenshots.
- **Auto Startup**: Once converted into an **executable**, the program will automatically add itself to the **Startup folder** of Windows.
  
## 🛠️ **Main Functions**

- ✅ **Screenshot Capture**
- ✅ **Hostname Retrieval**
- ✅ **User Information**
- ✅ **IP Address**
- ✅ **Auto Startup Integration**

## ⚙️ **Default Settings**

- `count = 20`: Number of screenshots in each email (default: 20 screenshots).
- `time.sleep(1)`: Time delay between each screenshot (default: 1 second).

## 🛡️ **AntiVirus Tests**

![Antivirus Test 1](https://github.com/user-attachments/assets/9bddf949-9f72-4810-b819-be4c866aee9e)  
![Antivirus Test 2](https://github.com/user-attachments/assets/e5bb72a7-e698-4806-9774-933af345e2e6)

## 💾 **How to Create the Executable (EXE)**

If you want to run **ScreenLogger** as an executable, you can use the library [AutoPyToExe](https://pypi.org/project/auto-py-to-exe/).

Once you have the **.exe file**, you will need to modify the variable `(originalfilename)` with the name of your executable. This, along with other changes like `(copiedfilename)`, will ensure that the executable is copied to the **Startup folder** of Windows, making it run on boot.

## 👨‍💻 **Credits**

This project is based on other open-source contributions. If you're the original creator of any used code, please reach out for proper credit.
