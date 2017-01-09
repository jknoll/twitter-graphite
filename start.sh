#!/usr/bin/env bash

# Stop and unload the launchctl service if running
launchctl stop com.justinknoll.graphite.twitter
launchctl unload ./docs/com.justinknoll.graphite.twitter.plist

# Load and start the launchctl service
launchctl load ./docs/com.justinknoll.graphite.twitter.plist
launchctl start com.justinknoll.graphite.twitter
