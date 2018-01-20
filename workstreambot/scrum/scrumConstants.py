
# the general topics that scrum can talk about
scrumGeneralKeys = ['scrum', 'roles', 'stories', 'sprint', 'ceremonies', 'backlog', 'estimations',
              'release', 'burndown', 'velocity', 'extras', 'spike', 'goals']

# the explanations of the general topics
scrumGeneralKeysValues = {
    'scrum': 'Scrum is an agile process that allows us to focus on delivering the highest business value in the shortest time.'
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
    'estimations': 'Part of planning an upcoming Sprint is undergoing an estimation of the stories that can be found in the sprint backlog.'
    		 + '\nThe user stories that are have been included within the sprint by the product owner have to be assigned to a number that indicates their complexity.'
    		 + '\nThe numbers that are assigned follow the beginning of a Fibonacci pattern, such that: 1,2,3,5,8,13 are typically assigned, taking the fact aside that the Fibonacci sequence is infinite. In terms of complexity, 1 represents the lowest complexity going ascendingly up to 13, which indicates a very high complexity.'
    		 + '\nThe complexity that is being evaluated depends on various factors, such as: expected time to accomlish the task, number of sub-tasks, as well as the know-how of developers regarding the handled topics.'
    		 + '\nThe collaborators who participate in the voting, which is often performed with poker cards, is the developers team. Upon the votes of the developers, the product owner assigns each user story its story points.',
    'release': 'A sprint release includes all new features that have been successfully built, tested, and deployed throughout a particular sprint'
    		 + '\nThe product owner is typically responsible for scheduling all sprint releases and document them in a release plan.'
    		 + '\nThe release plan that is created takes into account the requirements of the customer, the market, as well as sponsors or funding authorities.'
    		 + '\nAll sprint   releases should be equal in time, such that the start and end times for each sprint release is clearly documented in the release plan. The sequence of the sprint releases define the overall product roadmap.',
    'burndown': 'In scrum, a product owner is the only collaborator, who typically monitors a sprint burndown.'
    		 + '\nThe burndown chart is used to assist the product owner in capturing an image of the progress of the sprint'
    		 + '\nThe burndown chart includes the predicted size of stories and the corresponding predicted burndown, based on the story points that have been assigned in the sprint planning. As well as the actual values, which the developers provide at the sprint review.',
    'velocity': 'Velocity is an indicator, which shows the rate at which development is progressing within the Team.'
    		 + '\nIt is basically calculated through the follwing formula: The sum of user story points of features / time (#sprints).',
    'extras': 'Within a sprint, if the developers are done with their work, such that their work has been tested and finally committed, they typically spend a so called "slack time" till the end of their ongoing sprint.'
             + '\nThis slack time can be used in adapting the working environment, writing needed and recommended documentations, as well as attempting to process any task that is located in the backlog to be prepared or completely finished before the upcoming sprint(s) start(s).',
    'spike': 'Spike is a type of a ticket that can be included within a certain sprint backlog.'
    		 + '\nThe aim of a Spike is to conduct a research on a topic, which mostly analyses the feasability of using or deploying a certain technology for development within a team.'
    		 + '\nThe result of a spike can usually be found in a form of a documentation.',
    'goals': 'The goal of scrum is to ensure that the development of the product, which takes place throughout the consecutive sprints, completely fullfills the requirements of the customer/industrial partner.'
    		 + '\nScrum is one of the most significant IT project management strategies that if correctly and efficiently applied, guarantees to provide highly qualitative and feasabily costing product, which satisfies all requirements in an organized fashion, accompanied by continuous maintenance and a long lasting development lifecycle.',
    		}

# the detailed topics that scrum can talk about
scrumDetailsKeys = [['agile','business value'],
                    ['product owner', 'scrum master', 'developers'],
                    ['functional requirements', 'non-functional requirements'],
                    ['daily', 'planning meeting', 'review meeting','retrospective meeting'],
                    ['product backlog', 'sprint backlog'],
                    ['predicted burndown', 'actual burndown'],
                    ['release plan']]

# the explanations of the detailed topics
scrumDetailsKeysValues = {
    'agile': 'Agile is a technique used for organizing and coordinating Software projects.',
    'business value': 'An observable behaviour, feature or function that the user can watch and use upon interacting with the software after the end of a certain development stage.',
    'product owner': 'A product owner has the major role for promoting the success of a software development project that is based on scrum. His duties include: formulating customer requirements into tasks, grooming the backlog, prioritizing tasks accordingly, and monitoring the all aspects relating to the releases as well as the visibility of the business value after having finished a development phase.',
    'scrum master': 'A scrum master is the key person that is responsible for organizing ceremonies to the scrum team, as well as monitoring burndown charts and general progress of the development team. His duties include: preparing all requirements for the meeting, such as the venue, the deployment and development environment, as well as guiding the development team through their meetings and conducting notes to summarize all important remarks during different ceremonies.'
                    + '\nA scrum master is the key person in terms of communication between the product owner and the software developers',
    'developers': 'The Team that is responsible for implementing and developing a technical solution in order to fulfill the requirements that have been specified by the product owner.,
}
