# Features:
  - Kick/Ban/Purge Admin Commands
  - Changeable Prefix on a per-server basis
  - Facts/Riddles for some fun
  - Poll Functionality - Yes/No Questions and MCQ's
  - Welcome Messages - You can change the contents of these
  
  
And more to come!

# Planned Features
  - Mute Commands
  - Timers
  - Temp-Ban/Mute
  - Giveaway Commands
  - Upgraded Help Commands
  - Reaction Roles
  - Custom Commands

And more!

# All commands:

If you do not know the prefix, always just to `-prefix` and it will respond with the prefix.

  - Owner \[of the bot] Only:
    - `Shutdown` - Shuts down the bot. Syntax: `!shutdown`
    - `Clear` - Clears the terminal of any errors. Syntax: `!clear`


  - Administrator \[of a server] Only:
    - `welcome_message` Category:
      - `set`: Set a welcome message and channel for newcomers. You can use \ping in place of the newcomer's ping. Place the message in quotes. Channel must be mentioned. Syntax: `!welcome_message set "Welcome \ping to the server!" #channel-goes-here`
      - `remove`: Remove your welcome message. Syntax: `!welcome_message remove`
    - `ban`: Self-Explanatory. Syntax: `!ban @user`
    - `kick`: Self-Explanatory. Syntax: `!kick @user`
    - `purge`: Deletes messages. You can either give `max`, or a number between 1 and 2000 as the number of messages to delete. Syntax: `!purge 20` \[Replace 20 with a number of your choice or `max`]
    - `prefix`: Changes the prefix. Syntax: `!prefix ?` \[Replace `?` with prefix of your choice]
    -  `poll` Group:
        - `YesOrNo`: This command produces an embed with a yes or no choice (done using reactions.) Syntax: `!poll YesOrNo "Question Here" "Optional Description Here"`
        - `MCQ`: This command produces an embed with multiple options. Upto 26 options. Syntax: `!poll MCQ "Question Here" "Options/Seperated/By/Forward/Slashes" "Optional Description Here"`
  - Normal Users:
    - `fact`: Sends a random fact from a list of 40. Syntax: `!fact`
    - `riddle`: Sends a random riddle from a list of 40, and replies with the answer 10 seconds after. Syntax: `!riddle`
