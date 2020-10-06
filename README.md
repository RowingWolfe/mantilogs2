# mantilogs
I'll get around to writing this later. It's a Django app, written in Python3 and using SQLite for the DB.

Currently the work is focused on bug fixes and then frontend improvements as well as QOL.
Soon I hope to be adding better forms, possibly in React. I'll have to write some endpoints to process the JSON.


After that I will be adding new features like a QR code function that will open a profile for whatever the QR code is linked to just to make things a little quicker for data entry.

For now it is setup to log cultures of insects, mantids and geckos. I've got a basic morph model for the geckos but I feel like I may change it a bit when I add the functions for genetic calculators.

# Environmental logging node via ESP8266
https://github.com/RowingWolfe/mantilogs-env-node/tree/master
Takes a dht11/12/22 and an ESP8266 and posts to an endpoint in the mantilogs server with the temperature, humidity and location of the node.
Will later integrate this into the logs for mantids, geckos, etc so no more need to manually enter the environmental data.

