# Virtual Environment Setup

### Overview:

Activating the virtual environment before launching Visual Studio Code (VS Code) is crucial for several reasons:

- **Consistency:** Ensures that VS Code uses the specific Python **interpreter** and **dependencies** installed in the virtual environment, maintaining consistency across development and production setups.
- **Isolation:** Prevents conflicts between project dependencies and globally installed Python packages by isolating them in a self-contained environment.
- **Reproducibility:** Facilitates reproducibility of the project environment, making it easier to share and collaborate with others without compatibility issues.

By following these steps, you ensure that the development environment is configured correctly, reducing potential issues related to package versions or configurations.

---

### Step-by-Step Instructions:

1. **Open Your Command Prompt**
   - Press `Win + R`, type `cmd`, and press `Enter` to open the Command Prompt.

2. **Navigate to Your Project Directory**
   - Change to the directory where your project is located by entering:
     ```
     cd C:\Users\mew\Documents\GitHub\MLOps-clean_code-project
     ```

3. **Activate Your Conda Environment**
   - Activate the environment `web_fastapi` by typing:
     ```
     conda create -n web_fastapi python=3.10
     conda activate web_fastapi
     ```
   - Ensure that the activation is successful. The name `(web_fastapi)` should appear in your command prompt, indicating that the environment is active.

4. **Open VS Code in the Current Environment**
   - Launch VS Code directly from this command prompt to ensure it uses the correct environment:
     ```
     code .
     ```
   - This command opens VS Code in the current directory, which is your project directory.

5. **Check and Set the Python Interpreter in VS Code**
   - Once VS Code is open, check the Python interpreter at the bottom left of the VS Code window to ensure it’s set to use the Python interpreter from your `web_fastapi` environment.
   - If it's not automatically set, click on the Python version shown in the status bar at the bottom, and select the interpreter that points to your `web_fastapi` environment.

6. **Verify the Setup**
   - Open a new terminal in VS Code by using `Terminal > New Terminal` from the menu. This terminal session should automatically use your `web_fastapi` environment, indicated by the `(web_fastapi)` prefix in the terminal.
   - You can run a small Python command to ensure everything is working correctly, for example, `python -c "import sys; print(sys.executable)"`, which should print the path to the Python executable in your `web_fastapi` environment.

### Virtual Environment Usage

- **Virtual Environments** (`venv`, `conda`):
  - In development, using a virtual environment is crucial for managing package versions and isolating your project's dependencies. However, in a Dockerized environment, the Docker container itself acts like a virtual environment, isolating your application and its dependencies from the host system.
  - Therefore, you do not need to activate a virtual environment inside the Docker container. All dependencies should be managed through the Dockerfile and the container's setup.

continue at [Deployment Guidelines](deployment.md)