# Pythonic Droids FIRST LEGO League 2023-2024 MASTERPIECE Challenge

This repository contains the Pythonic Droids' assets for FIRST LEGO League 2023-2024 MASTERPIECE challenge.

## Prerequisites

To use this repository, you need to do the following:

- Install [Python](https://www.python.org/downloads/) on your machine.
- Install [Git](https://git-scm.com/downloads) on your machine.
  - Learn what is git [here](https://www.youtube.com/watch?v=WBg9mlpzEYU&ab_channel=ScottHanselman)
  - Setup your username and email in git by running the following commands in command prompt:
    ```shell
    git config --global user.name <YOUR_NAME>
    git config --global user.email <YOUR_EMAIL>
    ```
- Install [Visual Studio Code](https://visualstudio.microsoft.com/)
  - Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - Learn how to [develop in python with Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- [Pybricks](https://pybricks.com/install/)
  - [Pybricks Code](https://code.pybricks.com/)
  - [API Documentation](https://docs.pybricks.com/en/latest/)

## Getting Started

#### Clone the github repository with git

You can find more on what is cloning a repository [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

```shell
git clone https://github.com/droidpythonic/masterpiece.git
```

#### Install python packages

```shell
cd src
pip install -r requirements.txt
```

#### Install Pybricks firmware

- Go to [Pybricks Code](https://code.pybricks.com/).
- Click the ⚙️ icon on the left to open the Settings & Help pane.
- Click the `Install Pybricks Firmware` button.
- Follow the instructions on the screen.

**_NOTE:_** This is only necessary if the robot does not already have Pybricks firmware installed.

#### Restore the original firmware

Once the Spike Prime hub has been flashed with Pybricks firmware, it no longer works with Spike Prime. If you want to use the robot with Spike Prime, you have to restore the original firmware.

- Go to [Pybricks Code](https://code.pybricks.com/).
- Click the ⚙️ icon on the left to open the Settings & Help pane.
- Click the `Restore Official LEGO Firmware` button.
- Follow the instructions on the screen.

## Start Coding

#### Create a feature branch

In order to work collaboratively, we should all work in our own branches. Before making any changes, you should create a local branch from the `main` branch. You can learn more about what is a branch [here](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

```shell
git branch -b feature/max/<branch-name>
```

#### Commit changes

You should commit your changes to your local repository once you are done with your changes or just want make a check point.

```shell
git commit -am "SOME MEANINGFUL MESSAGE EXPLAINING WHAT THE CHANGES ARE ABOUT"
```

#### Push changes

After you are done with all your changes, you should push your changes to Github so others have access to them too.

```shell
git push --set-upstream origin max/<branch-name>
```

You should be able to see your branch listed in Github afterwards.

#### Create a pull request

When you are ready to merge you branch back to the main branch, we should all review the changes together by doing a `pull request`. This allows us to gather feedbacks from others and also let others learn what you did in your branch. You can learn why you want to do pull requests [here](https://www.youtube.com/watch?v=Mfz8NQncwiQ&ab_channel=ScottHanselman)
