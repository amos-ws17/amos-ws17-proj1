from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import json

from flask import Blueprint, request, jsonify
import requests
from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent

logger = logging.getLogger(__name__)


class BotOutput(OutputChannel):
    """A bot that uses a custom channel to communicate."""

    def __init__(self):
        self.messages = []

    def send_text_message(self, recipient_id, message):
        data = {}
        data['info_message'] = json.loads(message)
        self.messages.append(json.dumps(data))


class BotInput(HttpInputComponent):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""
    def __init__(self):

        self.out_channel = BotOutput()
    def blueprint(self, on_new_message):

        webhook = Blueprint('webhook', __name__)

        @webhook.route("/bot", methods=['GET'])
        def health():
            return '<html><body><h3>Welcome to the weather bot</h3></body></html>'

        @webhook.route("/webhook", methods=['POST'])
        def receive():
            payload = request.json
            sender = payload.get("sender", None)
            text = payload.get("message", None)
            on_new_message(UserMessage(text, self.out_channel, sender))
            return "success"

        @webhook.route("/bot/<cid>/execute", methods=['GET', 'POST'])
        def execute(cid):
            text = request.args.get('query')
            user_msg = UserMessage(text, self.out_channel, cid)

            on_new_message(user_msg)

            first = True
            data = {}
            for i in range(0, len(self.out_channel.messages)):
               if first:
                   data['info_messages'] = json.loads(self.out_channel.messages[i])
                   first = False
               else:
                   data['info_messages'].append(json.loads(self.out_channel.messages[i]))

            self.out_channel.messages[:] = []

            return json.dumps(data)


        return webhook

        
