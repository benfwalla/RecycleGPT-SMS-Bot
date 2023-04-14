# RecycleGPT ♻️
RecycleGPT is a GPT4-powered SMS text bot that aims to edcuate Denver⛰️ residents on what they can and can't recycle. 

Have you have stood with an object in front of your trash and recycling bins thinking, "what the heck do I do with this?" I have! Sure, you can Google it, but different counties have different rules (i.e. you **can't** recycle crushed aluminum cans in Denver, but you can in my hometown of Pittsburgh). So, instead of navigating old, outdated government websites, I built this simple text bot! RecycleGPT will give you recycling (and eventually trash and composting advice) that is county-specific to you. Today, RecycleGPT only works with data from the City and County of Denver.
The bot is given context from the [the City and County of Denver's Recycling wiki](https://denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Recycle-Compost-Trash/Recycle). The embeddings and database is a simple csv file, which can be found in [data/co_recycling_data_with_embeddings.csv](data/co_recycling_data_with_embeddings.csv).

RecycleGPT is a proof-of-concept for a much greater ambition: building a GPT-powered bot that consumes all government websites and delivers clear and actionable information and course-of-action to the users. Government sites are notorious for having terrible UXs. A project like this will empower U.S. citizens the transparency of law that they ought to hve the right to have.

## Getting Started 👋
To use the text bot, text **+1 (720) 806-5461**. Scan this QR Code to open up a new text message:

![RecycleGPT SMS Number QR Code](static/bot-qr-code.png)

### Example Queries 🤔
Try sending the following messages and see how RecycleGPT replies:
* "Can I recycle dirty cardboard?"
* "Is it okay recycle a solo cup with Sharpie marker?"
* "Who are you?"

## Product Roadmap 🗺️
The following is a list of idea I hope to include in RecycleGPT:
* Add [Compost Wiki](https://denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Recycle-Compost-Trash/Compost)
* Add [Trash Wiki](https://denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Recycle-Compost-Trash/Trash)
* Cite links in RecycleGPT's text messages
* Work with AutoGPT🤖 to automicatically scrape from any county's recycling, compost, and trash data.