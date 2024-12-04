# What is Git and What is Github

We learnt to use commands git add, push, commit and pull. 

### What is Git? 

Git is an open source technology that Linus Torvalds made while developing the Linux Kernel after a proprietary distributed VCS failed him. Don't confuse it with #github as it's and open source technology while github is an for profit company owned by Microsoft. Github is a distributed version control system.

 #### Core Functionalities of Git when it was being developed were: 

- Speed
- Simplicity
- Non-Linear
- Distributed
- Large

This is a video that helped me along the way to practice and learn github commands:

https://youtu.be/mJ-qvsxPHpY 

### What is Version Control? 

It is a system made to track code changes over time so we can recall specific versions later. Version control systems are known as VCS. VCS can help us see who made a specific change in the code that is causing a problem and can help us revert back to previous version of a code base if we made a problem. 




![](https://i.imgur.com/7jgX0dP.png)


From my GitHub account i changed value of variable current_deployement in my flask project. 

### Types of Version Control Systems

There are three types of version control systems namely:

### Local Version Control Systems

Earlier people would copy the same project at different places to keep record of changes or maybe date it. But this wasn't as effective to deal with programmers came up with local version control systems that had a simple database to keep track of changes. One example was RCS. 

##### Advantages:

- Simplicity: Easy to use and understand.
- Speed: Operations are very fast as everything is on the local machine.
- Offline Access: No need for network access, allowing for work without an internet connection.
- Reduced Complexity: Less infrastructure and fewer dependencies compared to distributed systems.

##### Disadvantages:

- Limited Collaboration: Difficult to collaborate with multiple developers, as changes are not easily shared.
- Single Point of Failure: If the local machine fails, all version history and changes could be lost.
- Limited History: Typically stores limited history, making it harder to track long-term project evolution.
- Redundancy Issues: Multiple copies of projects can lead to confusion and wasted storage space.
### Centralized Version Control Systems

Multiple developers need to work on same project so local VCS weren't a good option. All developers viewed the project at a specific time stamp from one central server. It also provided views that would show who did what and admins had control over who can view/edit what parts of the code. This however was risky aswell as complete code was a single server and if server was down for some time no one would be able to commit code changes. Another risk was if data in the server's storage becomes corrupt and people don't have the complete code with them this would result in a huge loss. 
##### Advantages:

- Enhanced Collaboration: Multiple developers can work on the same project simultaneously with updates and changes available to everyone in real-time.
- Access Control: Administrators can manage permissions, controlling who can view and edit specific parts of the code.
- Centralized Backup: A single, central repository simplifies backups and management.
- Consistent State: Ensures all developers are working with the most recent version of the code base.

##### Disadvantages:

- Single Point of Failure: If the central server goes down, no one can commit changes, and work can be halted.
- Server Vulnerability: Data corruption or loss on the central server can lead to significant project setbacks if backups are not properly maintained.
- Network Dependency: Requires network access to commit and update code, limiting offline work capabilities.
- Scalability Issues: May struggle with performance and reliability as the number of users and size of the project grows.
### Distributed Version Control Systems 

In Distributed VCS like #github #Mercurial #Darcs #gist clients (users, developers in this case) can check out latest version of the code spanshot but they can also fully download the repository including full history. So if data is lost or server goes does it full copy can be restored back. Furthermore, many of these systems deal pretty well with having several remote repositories they
can work with, so you can collaborate with different groups of people in different ways simultaneously within the same project. This allows you to set up several types of workflows that aren’t possible in centralized systems, such as hierarchical models.
