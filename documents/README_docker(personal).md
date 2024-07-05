### Docker Hub Steps

1. **Build your Docker Image**:
   Ensure you are in the project directory where your `Dockerfile` is located and run:
   ```bash
   docker build -t mewakin/stock-indicator-service:latest .
   ```
   This command builds a Docker image named `stock-indicator-service` with the tag `latest` under your Docker Hub username `mewakin`.

2. **Login to Docker Hub**:
   ```bash
   docker login
   ```
   Enter your Docker Hub username (`mewakin`) and password when prompted.

3. **Push the Image to Docker Hub**:
   ```bash
   docker push mewakin/stock-indicator-service:latest
   ```
   This command uploads your Docker image to your Docker Hub repository.

4. **Pull the Image from Docker Hub**:
   To download the image to any machine, use:
   ```bash
   docker pull mewakin/stock-indicator-service:latest
   ```

5. **Run the Container**:
   ```bash
   docker run -p 8000:8000 mewakin/stock-indicator-service:latest
   ```
   This will start a container from your image, mapping port 8000 of the container to port 8000 on the host.

### Pushing to Azure DevOps

1. **Initialize Your Git Repository**:
   If your project isn't already a Git repository:
   ```bash
   git init
   ```

2. **Add the Azure Repo as a Remote**:
   ```bash
   git remote add origin https://dev.azure.com/DM-Data-Platform/AIML_Demo/_git/Mew2
   ```
   Replace `Mew2` and `stock-indicator-service` with your actual Azure DevOps project and repository names.
   incase, want to change:
   ```bash
   git remote set-url origin https://dev.azure.com/DM-Data-Platform/AIML_Demo/_git/Mew2
   git branch -m master main
   ```

3. **Add and Commit Your Changes**:
   ```bash
   git add .
   git commit -m "Exercise-1 finish before CI/CD"
   ```
   if neeed to change the commit message:
   ```bash
   git commit --amend -m "planning how to learn CI/CD"
   git reset --hard HEAD@{2}
   ```
   

4. **Push Your Code to the Azure Repo**:
   ```bash
   git push -u origin main
   ```
   If your default branch is named differently (like `master`), replace `main` with your branch name.

### new banch
Creating a new branch and pushing your changes to it is a great way to safely introduce changes without directly affecting the main branch. This approach is particularly useful in collaborative environments where you want to review changes (via pull requests or merge requests) before they are integrated into the main branch. Here’s how you can do it:

### Step 1: Create and Switch to a New Branch
Create a new branch based on your current state and switch to it:
```bash
git checkout -b new-feature-branch
```

### Step 2: Commit Your Changes (If Not Already Done)
If you haven’t already committed your changes, do so now:
```bash
git add .
git commit -m "Fnished Exercise-1 before CI/CD"
```

### Step 3: Push the New Branch to Remote
Push your new branch to the remote repository:
```bash
git push -u origin new-feature-branch
```
This command pushes your branch to the remote repository and sets up tracking, which means in the future, you can simply use `git push` or `git pull` without specifying the branch.

### Step 4: Create a Pull Request
Navigate to your repository on Azure DevOps in your web browser. You should see a prompt to create a pull request from your newly pushed branch. If not, you can manually create one by going to the "Pull requests" section and selecting your new branch to merge into `main`.

### Step 5: Merge the Pull Request
Once your pull request is reviewed (by yourself or your teammates), you can merge it into the main branch. This action will integrate your changes into `main` and typically offers the option to do it via a merge commit or a squash merge, depending on your preference for maintaining history.

### Step 6: Fetch and Checkout to Main
After merging, make sure your local `main` branch is up to date:
```bash
git checkout main
git fetch origin
git merge origin/main
```

This sequence ensures that your local `main` branch reflects the remote main branch, including the changes you just merged through the pull request.

This process not only helps in maintaining a clean commit history but also ensures that all changes are validated (via pull requests) before they affect the production or the main development branch.

git branch -m main2 new-main
git checkout new-main

git branch -d old-branch-name  # Replace 'old-branch-name' with the actual branch name
git branch -d old-branch-name  # Replace 'old-branch-name' with the actual branch name