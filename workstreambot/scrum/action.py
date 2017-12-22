from rasa_core.actions import Action

import json

# the themes that scrum can talk about, should be persisted in the DB
theme_list = ['scrum', 'roles', 'stories', 'sprint', 'ceremonies', 'backlog', 'estimations',
              'release', 'burndown', 'velocity', 'extras', 'spike', 'goals']
# the explanations of the themes
theme_dict = {'scrum': 'Scrum is an agile process that allows us to focus on delivering the highest business value in the shortest time.'
                        + '\nIt allows us to rapidly and repeatedly deliver actual working software (Every two weeks to one month - a sprint).'
                        + '\nThe customer sets the priorities for what features are important.'
                        + '\nDevelopment teams self-organize to determine the best way to deliver the highest-priority features first. ',
              'roles': 'Product owner: The product owner is the project`s key stakeholder and represents users, customers/clients in the process.'
                        + '\nScrumMaster: The Scrum Master is responsible for making sure the team is as productive as possible.'
                        + '\nDevelopers: The team responsible for implementing the features as stated by the product owner',
              'stories': 'User stories represent customer`s requirements. Requirements represent the functionality that the software must provide.'
                         + '\nUser stories can include functional and non-functional requirements.'
                         + '\nUser stories are short, simple descriptions of software features told from the perspective of the user or customer of the system.'
                         + '\nA user story is essentially an aide-memoire - it reminds the developers of some software feature that must be implemented.',
              'sprint': 'The Scrum Process marks progress via sprints. A sprint is typically 2 to 4 weeks, depending on the scale project.'
                        + '\nThe goal is to deliver to the customer a working software increment (i.e. new extra functionality) by the end of each sprint. Sprints will be some multiple of a work week (5 days, 10 days, etc.).'
                        + '\nOnce you decide on a sprint size, you should hold it constant. Sprints start with a sprint planning meeting. Sprints end with a sprint retrospective and reviewing meeting',
              'ceremonies': 'Sprint planning meeting: At the start of each sprint, a sprint planning meeting is held, during which the product owner presents the top items on the product backlog to the team. The development team selects the work they can complete during the coming sprint. That work is then moved from the product backlog to a sprint backlog, which is the list of tasks needed to complete the product backlog items the team has committed to complete in the sprint.'
                            + '\nDaily Scrum: Each day during the sprint, a brief meeting, called the daily scrum, is conducted. This meeting helps set the context for each day`s work and helps the team stay on track. All team members are required to attend the daily scrum.'
                            + '\nSprint review meeting: At the end of each sprint, the team demonstrates the completed functionality at a sprint review meeting, during which, the team shows what they accomplished during the sprint. Typically, this takes the form of a demonstration of the new features, but in an informal way. The meeting must not become a task in itself nor a distraction from the process.'
                            + '\nSprint retrospective: Also at the end of each sprint, the team conducts a sprint retrospective, which is a meeting during which the team (including its Scrum Master and Product Owner) reflect on how well Scrum is working for them and what changes they may wish to make for it to work even better.',
              'backlog': 'Product backlog: The agile product backlog is a list of prioritized features, containing short descriptions (user stories) of all functionality (discovered so far) that customer wants to be implemented as the final product.'
                          + '\nSprint backlog: The sprint backlog is the list of user stories identified by the customer/team for development in the current sprint. The user stories are taken from the product backlog.',
              'estimations': '',
              'release': '',
              'burndown': '',
              'velocity': '',
              'extras': '',
              'spike': '',
              'goals': ''}

current_theme = theme_list[0]


# get the next element to explain
def getNextElement(theme):
    current_index = theme_list.index(theme)
    try:
        current_index += 1
        return theme_list[current_index]
    except IndexError:
        return None


def getResponse(action_name, tracker, response):
    data = {}
    data['action_name'] = action_name
    data['paused'] = tracker.is_paused()
    data['slots'] = tracker.current_slot_values()
    data['dialogue_message'] = tracker.latest_message.parse_data
    data['response'] = response

    return json.dumps(data)

# ask to continue to the next theme
class ActionContinue(Action):
    def name(self):
        return 'action_continue'

    def run(self, dispatcher, tracker, domain):
        global current_theme

        # find the next theme
        next_theme = getNextElement(current_theme)
        # pass it to the global variable
        current_theme = next_theme

        # if all themes are explained end the guide otherwise ask for the next one
        if not next_theme:
            response = 'That is it for the crash course in scrum. Would you like to restart?'
            current_theme = theme_list[0]
        else:
            response = 'Would you like to know about ' + current_theme + '?'

        dispatcher.utter_message(getResponse(self.name(), tracker, response))
        return []


class ActionExplain(Action):
    def name(self):
        return 'action_explain'

    def run(self, dispatcher, tracker, domain):
        global current_theme

        if tracker.latest_message.parse_data['intent']['name'] == 'switch_scrum':
            current_theme = theme_list[0]

        # explain the current theme
        dispatcher.utter_message(getResponse(self.name(), tracker, theme_dict[current_theme]))
        return []
