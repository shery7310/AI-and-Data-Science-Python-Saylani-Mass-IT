# Cloning a GitHub Repository (Repo)

When it comes to GitHub a repository or repo means the same thing a repository is like a folder we created online instead of locally. A repo had the added ability of being able to be traceable meaning any changes i make be it code, directory or addition or removal of a file it is all tracked by git. 

![](https://i.imgur.com/iIIwkGw.png)

We can clone a repository by first copying it's URL from the blue code button.
Then in command prompt (cmd) or any terminal we have to type:

`git clone repo URL`

or 

In this case:

`git clone https://github.com/shery7310/AI-and-Data-Science-Python-Saylani-Mass-IT.git`

**Remember You Do Not need to be signed in just to clone a repository**

# Creating a Repository

Using GUI you can create a repository just by clicking on the plus (+) button next to your GitHub Profile Picture

![](https://i.imgur.com/rUdriRz.png)

Then after this you are shown a page like this:

![](https://i.imgur.com/BdcClKB.png)

Be sure to make a meaningful name and description. If you want your teacher to check your repository make sure it's Public, but if you want to keep some code or something personal use Private option. A README file is an md file which you can use to write detailed description or another post like this one. 

# Making Changes to a repository and Account Sign In

Before Making any changes to our GitHub repo we need to sign In and there are a number of ways to do that on Windows you might need to install GitHub Desktop App and that will authorize you to make changes to your GitHub repo either you install GitHub Desktop or Not you will have to sign in to your account, here's how you can do that:

`git config --global user.name "your name"`
`git config --global user.email "your email"`

Sign In with the email and password for GitHub

Let's say you have created a GitHub repository and have also cloned it this means that for your repository you have both a local and an online or global version. Local being the directory you cloned and online being the repo you created on GitHub. 

By default your repo only has a README.md file inside.

Github allows us to edit code files for example.py file or add a text file (.txt) or even add another directory and it will track the changes with messages, and we can see those message/commits later and even undo those if needed.

Let's say I added a text file called learning.txt locally and this is how i can add it to my GitHub Repository:

Since we are assuming that we cloned the repo locally we do not need to run `git init`, so follow these steps:

1. `git add learning.txt`

this means we are adding the newly added(changed) file to online repo, for other files it can be like:

`git add filename`

We can however also write `git add .` this will add everything different from the previous version of the repo to tracking

Then after we have added the file this means it is in staging area but still not being tracked with a message, so now we need to commit, this is how we commit:

2. `git commit -m "Added Text File"` here Added Text File is a message that we have saved to later remember why we did this.

Then after committing we have essentially saved the version history or changes history locally now we need to push it to the online repository to do that we do:

3. `git push origin main`

This will push everything to the default branch called main. We will study branches later which is an advanced concept.

# What if we made changes online and want to bring them to local repo?

If we made changes online let's say changed some content in README.md or any text file we have in any repo, we need to pull everything and our local and online repo must be on the same level. To do that we can do:

`git pull`

