# How to Obtain Github Personal Access Token and how to commit changes to repo using the personal access token ?

#### Obtaining Personal Access Token:

1. Click on your GitHub Profile Picture and Open Settings
2. Then from settings scroll down to the bottom of the page and click on Developer Settings
3. From Developer settings select Personal Access Token: 
	![](https://i.imgur.com/vdyOmY4.png)
4. Select Tokens (Classic) and Generate New Token, give it any name and any duration of validity.

# Authenticating Personal Access Token

Let's say you have cloned a repo that belongs to you locally. Now you need to push some files to the online repo, you need to use your OBTAINED personal access token.

First you need to remove Origin you can do that using:

1. `git remote remove origin`

Then you need to add personal token and a new origin try following this pattern:

2. `git remote add origin https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]`

	Your username is your GitHub Username and the token can be something like:
		`yydsiudsdsfbds` 
	And you repo name can be like sample-repo so this is how your command will look like:

	`git remote add origin https://yydsiudsdsfbds@github.com/shery7310/sample-repo`

	Remember username is repo owner. 

Then you can push anything using:

4. `git push origin main`

