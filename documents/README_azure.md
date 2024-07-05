Below is an updated version of the markdown content for GitHub with clickable titles that link to each section. This format allows for easy navigation through the document.

## Table of Contents

1. [PR Workflow](#pr-workflow)
   - [Steps to Reset and Manage Branches for Learning Milestones](#steps-to-reset-and-manage-branches-for-learning-milestones)
   - [Creating a New Branch and Pushing Changes](#creating-a-new-branch-and-pushing-changes)
2. [Setup](#setup)
   - [Initializing and Pushing to Azure DevOps](#initializing-and-pushing-to-azure-devops)
   - [Creating and Managing New Branches](#creating-and-managing-new-branches)
3. [Problems Encountered](#problems-encountered)
   - [Stale Tracking Branch Cleanup](#stale-tracking-branch-cleanup)
   - [Resolving "Refusing to Merge Unrelated Histories" Error](#resolving-refusing-to-merge-unrelated-histories-error)
   - [Syncing Local and Remote Branches](#syncing-local-and-remote-branches)
   - [Renaming and Deleting Branches](#renaming-and-deleting-branches)

## PR Workflow

### Steps to Reset and Manage Branches for Learning Milestones

1. **Delete Existing Branches:**
   - Backup your current work.
   - Delete local branches:
     ```bash
     git branch -D <branch-name>
     git branch -D new-feature-branch
     ```
   - Delete remote branches on Azure DevOps:
     ```bash
     git push origin --delete <branch-name>
     git push origin --delete new-feature-branch
     ```

2. **Create a New Branch for Each Learning Module:**
   - Create a new branch from your main branch:
     ```bash
     git checkout -b feature/<module-name>
     ```

3. **Implement Learning Milestones:**
   - Work on your changes in the respective branches.
   - Commit the changes:
     ```bash
     git add .
     git commit -m "Implement changes for <module-name>"
     ```

4. **Create Pull Requests:**
   - Push the branch to Azure DevOps:
     ```bash
     git push -u origin feature/<module-name>
     git push -u origin feature/cicd
     ```
   - Create a new PR in Azure DevOps and merge it into the main branch.

5. **Repeat for Each New Learning Module:**
   - Repeat the process for each new learning module.

### Creating a New Branch and Pushing Changes

1. **Create and Switch to a New Branch:**
   ```bash
   git checkout -b new-feature-branch
   ```

2. **Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Finished Exercise-1 before CI/CD"
   ```

3. **Push the New Branch to Remote:**
   ```bash
   git push -u origin new-feature-branch
   ```

4. **Create a Pull Request:**
   - Navigate to your repository on Azure DevOps.
   - Create a pull request from your newly pushed branch.

5. **Merge the Pull Request:**
   - Merge it into the main branch after review.

6. **Fetch and Checkout to Main:**
   ```bash
   git checkout main
   git fetch origin
   git merge origin/main
   ```

## Setup

### Initializing and Pushing to Azure DevOps

1. **Initialize Your Git Repository:**
   ```bash
   git init
   ```

2. **Add the Azure Repo as a Remote:**
   ```bash
   git remote add origin https://dev.azure.com/DM-Data-Platform/AIML_Demo/_git/Mew2
   ```
   - To change the remote URL:
     ```bash
     git remote set-url origin https://dev.azure.com/DM-Data-Platform/AIML_Demo/_git/Mew2
     git branch -m master main
     ```

3. **Add and Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Exercise-1 finish before CI/CD"
   ```

4. **Push Your Code to the Azure Repo:**
   ```bash
   git push -u origin main
   ```

### Creating and Managing New Branches

1. **Create and Switch to a New Branch:**
   ```bash
   git checkout -b new-feature-branch
   ```

2. **Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Finished Exercise-1 before CI/CD"
   ```

3. **Push the New Branch to Remote:**
   ```bash
   git push -u origin new-feature-branch
   ```

4. **Create a Pull Request:**
   - Navigate to your repository on Azure DevOps.
   - Create a pull request from your newly pushed branch.

5. **Merge the Pull Request:**
   - Merge it into the main branch after review.

6. **Fetch and Checkout to Main:**
   ```bash
   git checkout main
   git fetch origin
   git merge origin/main
   ```

## Problems Encountered

### Stale Tracking Branch Cleanup

- Remove stale remote tracking branches:
  ```bash
  git remote prune origin
  ```
- Delete a specific stale branch:
  ```bash
  git branch -dr origin/new-feature-branch
  ```

### Resolving "Refusing to Merge Unrelated Histories" Error

1. **Switch to the Branch to Update:**
   ```bash
   git checkout new-main
   ```

2. **Allow Unrelated Histories During Merge:**
   ```bash
   git pull origin new-main --allow-unrelated-histories
   git pull origin main --allow-unrelated-histories
   ```

3. **Resolve Any Merge Conflicts:**
   - Add resolved files:
     ```bash
     git add .
     ```
   - Commit the merge:
     ```bash
     git commit -m "Resolved merge conflicts between local and remote branches"
     ```

4. **Push Merged Changes to Remote:**
   ```bash
   git push origin new-main
   ```

### Syncing Local and Remote Branches

1. **Push Local Changes to Remote:**
   ```bash
   git checkout new-main
   git push origin new-main
   ```

2. **Check for Discrepancies Between Branches:**
   ```bash
   git fetch origin
   git fetch --all
   git diff new-main origin/new-main
   ```

3. **Merge Changes if Needed:**
   ```bash
   git checkout main
   git merge new-main
   git push origin main
   ```

4. **Ensure Branches are in Sync:**
   ```bash
   git status
   git branch -avv
   ```

### Renaming and Deleting Branches

- Rename a branch:
  ```bash
  git branch -m old-branch-name new-branch-name
  ```

- Delete a branch:
  ```bash
  git branch -d old-branch-name
  ```

This organized and clickable content outline should make it easier for you to manage and navigate through the markdown document on GitHub.