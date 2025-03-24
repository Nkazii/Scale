Code Showcase: https://youtu.be/ibEt8NW1JsE

# Scale

# Buildozer Android App Setup

This script automates the process of setting up and building an Android application using Buildozer. 

## Requirements

* Python 3.x
* Buildozer (installed through pip)
* Cython (version 0.29.19)
* Necessary Android SDK tools and dependencies (installed automatically by the script)


## Usage

1. **Install Dependencies:**
   - Run the script (`main.py`) to install all required packages and dependencies using pip and apt-get.
2. **Buildozer Initialization:**
   - The script initializes Buildozer using `buildozer init`. This will create a `buildozer.spec` file in the current directory, which you can modify to configure your app's settings (name, version, etc.).
3. **Build Android App:**
   - The script builds the app for Android using `buildozer -v android debug`.
4. **Clean Android Build:**
   - The script then uses `buildozer android clean` to remove temporary build artifacts.

## Steps Explained:

* **Install Buildozer and Dependencies:** 
   The code installs buildozer, cython, and necessary system libraries for building Kivy apps on Android.
* **Apt-get Installations:**
   - The script uses `apt-get` to install essential tools like Python, libraries for SDL, FFmpeg, and others needed for a successful Kivy build.
* **Buildozer Initialization:**
   - `buildozer init` sets up the Buildozer project.
* **Build Android Debug:**
   - `buildozer -v android debug` generates an APK for debugging purposes.
* **Clean Build:**
   - `buildozer android clean` removes the temporary build folders and files to keep your project clean.


## Notes

* Make sure you have a working internet connection to install all the required packages.
* This script is geared towards building Kivy-based applications for Android.
* Customize `buildozer.spec` to match your specific application requirements.



