# COMS W3132 Individual Project

## Author
Tobechi Onwuka
tio2003@barnard.edu,
Fahitza Quessa
fdq2000@barnard.edu



## Project Title
*Provide a short and descriptive title for your project.*

Name: Meme Maestro Bot

## Project Description
*Write a short, concise project description of what your project aims to achieve. Include the motivation for this project (why do you want to work on it), the problem your project aims to solve, and the main goals that you want to accomplish within the rest of the semester. Also mention why you think the project might be useful or interesting to others. Keep this section short. A couple of paragraphs would do.*

Our projects aims to create a deployable bot to discord server chats. Fahitza and Tobechi enjoy sharing memes to each other and we were wondering how we could create our love for memes into a cool python project. Tobechi is a frequent user of Discord while Fahitza is a frequent user of reddit, they both decided that since Tobechi was a little familiar with how discord bots work that they can start a discord bot. After figuring that out, we figured that discord bots are a great way for small games to occur within a discord chat server. So in order to use a data structure learned from class we thought about game polls and how users could submit items in a poll that can be voted on. The problem our project aims to solve is entertainment across groups of people within an online format as Discord is a format for chatting with others often. This project could be interesting to others because it combines the common meme culture in todays society and online chatting forums. Since, discord bots can be shared in any server with the right permissions, it means other people could use this memebot for their online games as well.

## Timeline

*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

| Date               | Milestone                                                                                              | Deliverables                | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-----------------------------|------------|
| **March&nbsp;29**  | Submit project description                                                                             | README.md                   | proposal   |
| **April&nbsp;5**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                   | approved   |
| **April&nbsp;12**  | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs | milestone1 |
| **April&nbsp;19**  | Progress on implementation (define your own goals)                                                     | Source code, unit tests     | milestone2 |
| **April&nbsp;26**  | Completely (or partially) finished implementation                                                      | Source code, documentation  | milestone3 |
| **May&nbsp;10**    | Final touches (conclusion, documentation, testing, etc.)                                               | Conclusion (README.md)      | conclusion |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories
*List the key requirements or features of your project. For each feature, provide a user story or a simple scenario explaining how the feature will be used. You don't have to get this section right the first time. Your understanding of the problem and requirements will improve as you work on your project. It is okay (and desirable) to come back to this section and revise it as you learn more about the problem you are trying to solve. The first version of this section should reflect your understanding of your problem at the beginning of the project.*

*Also list any required hardware, software, on online services you will need. In specific cases, we might be able to lend you hardware or obtain online services. Please email the instructor for more details.*


- We need the Discord library and the Discord website itself to code our project. We will not be using any hardware for our project, and we will use APIs: the Dalle API specifically.
The user can call the bot using a token, for example, $meme, and the meme-bot will generate an auditory response using a popular meme sound.
The user can also call the bot using a token, for example !respond, and the meme-bot will generate an image given a text input to create a meme. 
These are the two key features of our project.


## Technical Specification
*Detail the main algorithms, libraries, and technologies you plan to use. Explain your choice of technology and how it supports your project goals.*

→ Discord Library
→ Discord as a tool
→ Dalle API
→ Using a Queue for polling in Discord bot


## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or system. This should include major components, such as user interface elements, back-end services, and data storage, and show how they interact. Tools like Lucidchart, Draw.io, or even hand-drawn diagrams photographed and uploaded are acceptable. The purpose of the diagram is to help us understand the architecture of your solution. Diagram asthetics do not matter and will not be graded.*

Example UI:

<img width="767" alt="Screenshot 2024-03-28 at 1 52 05 AM" src="https://github.com/coms-w3132/final-project-toonwuka04/assets/62598554/524d1dd7-aa5b-4822-96c4-03375a1ea59b">

Code Architecture:

<img width="765" alt="Screenshot 2024-03-28 at 1 52 10 AM" src="https://github.com/coms-w3132/final-project-toonwuka04/assets/62598554/fc8a891d-a641-4f51-b01b-18fe5085bba7">



## Development Methodology
*Describe the methodology you'll use to organize and progress your work.*

*First, describe your plan for developing your project. This might include how (or if) you plan to use*
- *GitHub projects board to track progress on tasks and milestones*
- *GitHub issues to keep track of issues or problems*
- *Separate Git branches and/or GitHub pull requests for development*
- *GitHub actions for automated testing or deployment pipelines*
- *GitHub wiki for documentation and notes*

*Please also describe how (if) you plan test and evaluate your project's functionality. Do you plan to test manually or automatically? Any specific testing frameworks or libraries you plan to use?*

ANSWER:

Firstly, since this is a collaborative project, we have taken the initiative to split the work fairly. 
Tobechi’s Section: Focus on the feature where the user can call the bot using a token (e.g., $meme) to generate an auditory response using a popular meme sound. This involves working with audio files, integrating them into the bot, and handling command triggers to play these sounds. We plan to meet regularly to discuss progress, roadblocks, and testing feedback. Use this time to align on the next steps and ensure both features integrate well. Although each person is responsible for a different feature, we will review each other’s code and provide feedback to help catch issues early and ensure consistency in the quality and style of the code.

Fahitza’s Section: Concentrate on the image meme generation feature, where the user calls the bot with a different token (e.g., !respond), and the bot generates an image based on the given text input. This part requires integrating with the Dalle API to create memes.

Development Workflow:

For Both Sections: Utilize separate Git branches for developing each feature to keep the main branch stable.

Code Reviews and Pull Requests: Once a feature is ready for review, open a pull request. The other team member reviews the code, providing feedback or approval before it’s merged.

Testing and Feedback:
Implement unit tests and integration tests to ensure reliability and functionality.
Set up a test Discord server where we will deploy your bot for live testing.

→ We plan to test our project's functionality using Discord.

Potential Challenges and Roadblocks
Identify any potential challenges or roadblocks you anticipate facing during the development of your project. For each challenge, propose strategies or solutions you might use to overcome them, which may include getting help from the TAs/instructor. This could include technical hurdles or learning new technologies.


→ Setting up a polling system in Discord bot: technical hurdle 
 Start by researching existing implementations or tutorials on creating polling systems in Discord bots

Break down the polling feature into smaller tasks (e.g., creating a poll, voting, displaying results) and tackle them one at a time.

→ Fahitza has never used an API so this is a learning new technologies hurdle
	To counter this hurdle, I (Fahitza Quessa), plan to watch API integration videos, and read up on the documentation. If I have any lingering questions, I will consult Tobechi, who is much more familiar with the API, and or the TA’s. 
-------

## Potential Challenges and Roadblocks
*Identify any potential challenges or roadblocks you anticipate facing during the development of your project. For each challenge, propose strategies or solutions you might use to overcome them, which may include getting help from the TAs/instructor. This could include technical hurdles or learning new technologies.*

→ Setting up a polling system in Discord bot: technical hurdle 
 Start by researching existing implementations or tutorials on creating polling systems in Discord bots

Break down the polling feature into smaller tasks (e.g., creating a poll, voting, displaying results) and tackle them one at a time.

→ Fahitza has never used an API so this is a learning new technologies hurdle
	To counter this hurdle, I (Fahitza Quessa), plan to watch API integration videos, and read up on the documentation. If I have any lingering questions, I will consult Tobechi, who is much more familiar with the API, and or the TA’s. 


## Additional Resources
*Include any additional resources, tutorials, or documentation that will be helpful for this project.*

→ [Discord Bot Documentation](https://discord.com/developers/docs/intro)
→ [Dalle API Documentation](https://openai.com/blog/dall-e-api-now-available-in-public-beta)



## Conclusion and Future Work
*Wrap up your project description with any final thoughts, expectations, or goals not covered in the sections above. Also briefly discuss potential future work, i.e., what could be done next to improve the project.*

→ Expectations/Goals: Finish goal of implementing Dalle API, finishing goal of returning poll to user.
→ Potential future work: Deploying our Memebot to the public
→ Improvements: Creation of a Web UI that allows users to interact with the bot via website (kinda like a gaming format) 


## Response to TA Feedback
*how do you plan to incorporate "sound"? Based on this sentence, The user can call the bot using a token, for example, $meme, and the meme-bot will generate an auditory response using a popular meme sound. , it seems DALLE supports this. If it does not, do you have other ways to generate sound?

- We will use a folder and hold 10-15 pre-recorded meme audios from different free audio websites

*will you incorporate any moderation features to prevent inappropriate content or misused of the bot, if used in public?

- We think this could be an added security measure if our project was to go public, at the moment we think the project will be private.

*can you design your architecture so that it supports multiple sources aside from Reddit or discord?

- I think this would be a good future edit to make. As for right now we'd like to make sure our program works with Discord's bot architecture and possibly move forward with other platforms if we go public.
- 

#Milestone 2 Goals
[Milestone2.pdf](https://github.com/coms-w3132/final-project-toonwuka04/files/14962603/Milestone2.pdf)
