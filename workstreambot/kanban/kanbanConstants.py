
# the general topics that kanban can talk about
kanbanGeneralKeys = ['kanban', 'artefact', 'board', 'ticket',
				'estimation', 'wip', 'pull principle', 'ceremony']

# the explanations of the general topics
kanbanGeneralKeysValues = {
    'kanban': 'Kanban is an agile method to improve productivity of a team and quality of a product by applying the Theory Of Constraints to teamwork.'
             + '\nParallel Tasks are minimised to maximise focus, Kaizen is requested to be performed when defects are recognised.'
             + '\nKanban does not define any roles.'
             + '\nYou have to have at least one team which is responsible to get things done.'
			 + '\nThis team has to be free in organizing its work and must not be micromanaged by another person.',
    'artefact': 'The kanban board with its cards, the Cumulative Flow Diagram (CFD), Run Chart, Lead Time Distribution Chart.',
    'board': 'A Kanban Board has at least three columns and at least two rows.'
             + '\nOne column for tickets to be processed on the left, one column for tickets which are done on the right and one column for every workstation in between.'
             + '\nTickets move from the left to the right passing every workstation.'
             + '\nThey are pulled by the workers into their column.'
			 + '\nAfter processing, they mark the ticket so that the next worker knows, that this ticket may be pulled further.'
			 + '\nA worker may only pull a ticket, if the WIP Limit is not exceeded.',
    'ticket': 'Kanban defines three types of Tickets:'
             + '\n- standard tickets, which are just processed as usual'
			 + '\n- fixed date tickets, which only have a business value, if they are done in time'
			 + '\n- expedite tickets, which have a crucial business value and have to be processed immediately on every workstation. They don’t count into the WIP limit, there may be only a very small number of expedites simultaneously.'
             + '\nKanban does not define a backlog, but it comes in handy for a product manager to decide which items he will hand over in the next Replenishment Meeting.',
    'estimation': 'You don’t have to estimate anything.'
             + '\nAlthough your tickets should have a maximum size to let Kanban work.'
             + '\nA team may consider a ticket „too large“, then it has to be cut down.',
    'wip': 'The Work In Progress Limit is used to prevent waste.'
             + '\nSince humans are very bad at multitasking it is essential to keep focus.'
			 + '\nKanban supports this by limiting the tickets being processed simultaneously.'
			 + '\nThus every workstation column may only contain a limited number of tickets, regardless if they are done or currently in progress.'
			 + '\nDifferent workstation columns may use different WIP limits.'
			 + '\nThe WIP limits are reduced if they are not violated for a longer period of time.',
    'pull principle': 'It is said, that Toyota developed it by having a closer look at the supply chain in their super markets.'
    		 + '\nCustomers pull goods out of the store by grabbing them out of the shelfs.'
    		 + '\nThe shelfs are refilled by pulling goods out of the storage.'
    		 + '\nThe storage is refilled by ordering goods from the supplier.'
    		 + '\nSo the whole stream of goods is propelled by pulling from the end of the chain to the beginning.'
			 + '\nThe system is most efficient, when the amount at every station is minimal, but refilled with least possible delay'
			 + '\nIn an agile context the Pull Principle refers to the effect, that individuals tend to adopt a task with higher motivation when choosing the task by free will instead of taking up a task by order (push).',
    'ceremony': 'The replenishment meeting is used to fill the ToDo column with the tickets to be done.'
    		 + '\nThe stakeholders who need a ticket to be processed have to transfer the knowledge what is needed to fulfil the ticket successfully to the team working on this board.'
    		 + '\nThe team ensures that they know everything they need to know to fulfil these tasks.',
    		}


# TODO FOR OMAR FROM DANIEL.
# The entity names that the NLU will give you are named as follows: 
toBeFixedOmar = ['history', 'kaizen', 'stop the line', 'lead time', 'cycle time', 'buffer', 'violation']

# the detailed topics that kanban can talk about
kanbanDetailsKeys = [['agile','business value'],
                    ['product owner', 'scrum master', 'developers'],
                    ['functional requirements', 'non-functional requirements'],
                    ['daily', 'planning meeting', 'review meeting','retrospective meeting'],
                    ['product backlog', 'sprint backlog'],
                    ['predicted burndown', 'actual burndown'],
                    ['release plan']]

# the explanations of the detailed topics
kanbanDetailsKeysValues = {
    'agile': 'Agile is a technique used for organizing and coordinating Software projects.',
    'business value': 'An observable behaviour, feature or function that the user can watch and use upon interacting with the software after the end of a certain development stage.',
    'product owner': 'A product owner has the major role for promoting the success of a software development project that is based on scrum. His duties include: formulating customer requirements into tasks, grooming the backlog, prioritizing tasks accordingly, and monitoring the all aspects relating to the releases as well as the visibility of the business value after having finished a development phase.',
    'scrum master': 'A scrum master is the key person that is responsible for organizing ceremonies to the scrum team, as well as monitoring burndown charts and general progress of the development team. His duties include: preparing all requirements for the meeting, such as the venue, the deployment and development environment, as well as guiding the development team through their meetings and conducting notes to summarize all important remarks during different ceremonies.'
                    + '\nA scrum master is the key person in terms of communication between the product owner and the software developers',
    'developers': 'The Team that is responsible for implementing and developing a technical solution in order to fulfill the requirements that have been specified by the product owner.',
}
