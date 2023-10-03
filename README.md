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

## Innovation Ideas

How can you use technology and the arts to help engage others or increase participation in what you love to do?                              

### Max

#### Automatic Song Writer

Max likes playing the piano. The most annoying thing about song writing is one has to play each note of the song individually, write it down on paper and then play again.

There could be an automatic song writer. It should listen to what's being played and generate notes automatically. 

It is an atttachment that can be slotted on to the top of a piano, if it is an electric piano there will be a device that plugs into a USB port and dectects what signal is being sent.

There will also be a printer on the side of the machine that will automaticly print after 1 minute, or if the user clicks a button that says print like ctrl + P




There will be a camera that sees which muffler is moving. Each muffler is assigned a  number 1-88 and say, muffler 23 was pressed. Say muffler 23 is B flat. It corresponds to the apropriate note on the display.
Features: Basic piano skills, Note recognizer, ability to record and play songs, printer

- Every time you play song it will compare it to the actual song. If you do something wrong, like if you play a wrong note or the tempo is a bit fast it will give you feedback after you are finished.
- This is basically a virtual piano teacher, because real life piano lessons are super expensive (100ish dollars per hour)
- If you want to learn piano but you don't think you can afford the 6,000 dollars per year for lessons, then this is the perfect solution


What abt micronotes
Needs to be more general-too specific
What abt upright pianos
For electric pianos-USB
### Kavya

#### VR Contact Lenses

Instead of VR headsets, use contact lenses to project VR environment to help performances.

Create a VR tennis game that plays a piano note depending on where the ball lands on the court.

Let's say a piano player wants to learn how to play tennis. For beginners, the entire court could be a single note. As your skill progresses, the target note could be smaller.

Music to tennis - probably will need to learn form. Different swings can be different notes

### Ishanvi

#### Translator

Make a software that "translates" sports language to easily understood phrases and helps learn a new instrument or a type of dance.

if a volleyball player wants to play violin - different strings can be different words

violin player wants to learn volleyball - different positions can be different strings

can help people who have experience in something and who want to learn something else

### Aron

Create a device to track what people are eating.

# Vivaan
Device attached to istrument to connect to an app and do the same things on the app as my second idea.

### second idea
AR glasses to show you how to do an art and also it teaches cool things about the art they want to learn and teach them a cool thing to do to get them intrested in it. Examples of arts you can learn: drawing, painting, musical arts, maybe dancing. maybe to get get them intrested into drawing teach them how to a 3d drawing and for painting teach them to paint blending colors. For piano maybe teaching how the piano works same for other musical instruments.



