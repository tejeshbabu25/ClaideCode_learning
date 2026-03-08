#Time to get Claude Code set up locally!

#Full setup directions can be found here: https://code.claude.com/docs/en/quickstart

#In short, you'll need to do the following:

#Install Claude Code
# 1. Windows CMD: curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
# 2. Add C:\Users\tejes\.local\bin to your system variables PATH environment variable (if it isn't already)
# 3. After installation, run claude at your terminal. The first time you run this command you will be prompted to authenticate
# 4. Now when you ran claude you should need "Welcome to Claude Code v2.1.71"
# 5. create a free claude code account and sign in 
# 6. Working with Claude Code for learning purposes, use the uigen.zip file to learn
#     Setup

        # This project requires a small amount of setup:

        # Ensure you have Node JS installed locally. Link to installation directions.
        # Download the zip file called uigen.zip attached to this lecture and extract it
        # In the project directory,cd to uigen folder & run npm run setup to install dependencies and set up a local SQLite database
        # I got error when running npm run dev, so i installed cross-env using command npm install cross-env --save-dev
        # once done, updated the package.json file to use cross-env for the dev, build, and start scripts. The updated scripts section looks like this:
        # "scripts": {
        #      "dev": "cross-env NODE_OPTIONS='--require ./node-compat.cjs' next dev --turbopack",
        #     "dev:daemon": "cross-env NODE_OPTIONS='--require ./node-compat.cjs' next dev --turbopack > logs.txt 2>&1 & echo 'Server started, writing logs to logs.txt'",
        #     "build": "cross-env NODE_OPTIONS='--require ./node-compat.cjs' next build",
        #     "start": "cross-env NODE_OPTIONS='--require ./node-compat.cjs' next start",
        #}
        # This still did not work, so I updated the scripts to use node -r instead of cross-env, which worked. The final scripts section looks like this:
        #         "scripts": {
        #   "dev": "node -r ./node-compat.cjs ./node_modules/next/dist/bin/next dev --turbopack",
        #   "dev:daemon": "node -r ./node-compat.cjs ./node_modules/next/dist/bin/next dev --turbopack > logs.txt 2>&1",
        #   "build": "node -r ./node-compat.cjs ./node_modules/next/dist/bin/next build",
        #   "start": "node -r ./node-compat.cjs ./node_modules/next/dist/bin/next start",
        #   "lint": "next lint",
        #   "test": "vitest",
        #   "setup": "npm install && npx prisma generate && npx prisma migrate dev",
        #   "db:reset": "npx prisma migrate reset --force"
        # }



