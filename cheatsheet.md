# Terminal Commands

- `cd` Change directory
  - `cd ..` navigates to previous folder
  - `cd <folder_name>` navigates to the folder (usually drill down or paste the direct path)
- `git` git good scrub
  - `git clone <url>` clones the repo with url
  - `git fetch` fetches latest and updates ALL the remote branches
  - `git pull` fetches latest and updates the branch I'm on 
  - `git add .` adds files changed to the staging area 
  - `git commit -m '<message>'` adds a commit message to the commit 
  - `git push` pushes all commits of the branch to the remote branch of the same name
  - `git status` checks status of git (files changed, staged, etc.)
  - **To get latest changes**: use `git fetch` and `git pull`
  - **To push local changes to remote repo**: use `git add .` -> `git commit -m <message>` -> `git push`

# Terminology
### Engineering Terms
| Term             | Description                                            | Example                                          | Notes           |
|------------------|--------------------------------------------------------|--------------------------------------------------|-----------------|
| Project Explorer | Area where all the files are listed in VS Code         | ![files_icon](img/files_icon.PNG)                | left of VS Code |
| Version Control  | Version Control is a way of life. It's also this icon. | ![version control icon](img/version_control.PNG) | left of VS Code |

### Python Terms
| Term      | Description                                            | Example                                          | Notes           |
|-----------|--------------------------------------------------------|--------------------------------------------------|-----------------|
| `module`  | A pre-existing code within python                      | `import random`                                  |                 |


# Helpful Resources
* [Markdown Cheatsheet](https://www.markdownguide.org/basic-syntax/#reference-style-links)
* [How to run Python on VS Code](https://code.visualstudio.com/docs/python/run#_run-python-code)
    * <details>
        <summary>Example</summary>
        <img src="https://code.visualstudio.com/assets/docs/python/shared/nativeREPL-demo.gif" alt="How to run Python on VS Code">"
    </details>
  