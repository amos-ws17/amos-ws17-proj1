from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

import sys
import warnings

from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


class ActionSearchSights(Action):
    def name(self):
        return 'action_search_sights'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found")
        return []
