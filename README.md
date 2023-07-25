# Knowledge Base Q&A Slack application

This is a Slack application designed for searching and accessing company documents solely through text-based communication and chat interactions.

## How to develop this application

Develop only in your own slack workspace. 

To create one, you need to proceed to [slack home page](https://slack.com/get-started#/landing)->Create Workspace. 

To create your own slack application:

1. Do it [here](https://api.slack.com/apps)->Create New App->From Scratch;
2. Paste your Signing Secret in `.env.dev`; 
3. Add Bot Token Scopes for your application in OAuth & Permissions section. Add following: `chat:write`, `users:read.email`, `users:read`; 
4. Install to your recently created workspace by pressing `Install to Workspace`;
5. Copy Bot User OAuth Token to `.env.dev`;
6. Copy your OpenAI API key to `.env.dev`;
7. Run `docker-compose up`, open new terminal, run `gp ports list` and copy 8000 port URL;
8. Enable Event Subscription. Paste your URL in format your-url.gitpod.io/slack/events. It must be valid for Slack. Don't forget to save your changes and reinstall app!
9. Subscribe to bot event `message.im`;
10. In `App Home` scroll down and turn on `Allow users to send Slash commands and messages from the messages tab`;
11. Test your bot in workspace.

## How to debug

In VSCode open Run And Debug section -> Remote Attach.
