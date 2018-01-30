kanban = {
    'kanban': {
        'general': 'Kanban is an agile method to improve productivity of a team and quality of a product by applying the Theory Of Constraints to teamwork.\nSurprisingly, the history of Kanban initially goes back to automotive industry and not software development.\nParallel Tasks are minimised to maximise focus, Kaizen is requested to be performed when defects are recognised.\nKanban does not define any roles.\nYou have to have at least one team which is responsible to get things done.\nThis team has to be free in organizing its work and must not be micromanaged by another person.',
        'details': {
            'history': 'Kanban was developed at Toyota as a method to optimise the car production applying the theory of constraints an drum buffer rope to achieve just in time delivery.\nLater on it was adopted and modified to fit to the requirements of software development.\nTaiichi Ohno published it back in 1988 as part of the „Toyota Production System.',
            'kaizen': 'Kaizen is the culture or mindset to improve everything you do step by step and to not give up improving continuously.\nIn Kanban you „stop the line“ when you encounter a quality mismatch or a underflow, which means that a person can not work because one is not allowed to exceed a WIP limit.'
        },
        'position': 1
    },
    'artefacts': {
        'general': 'The kanban board with its cards, the Cumulative Flow Diagram (CFD), Run Chart, Lead Time Distribution Chart.',
        'position': 2
    },
    'board': {
        'general': 'A Kanban Board has at least three columns and at least two rows.\nOne column for tickets to be processed on the left, one column for tickets which are done on the right and one column for every workstation in between.\nWorkers process given Tickets depending on the indicators "cycle time", "lead time", and "stop the line".\nTickets move from the left to the right passing every workstation.\nThey are pulled by the workers into their column.\nAfter processing, they mark the ticket so that the next worker knows, that this ticket may be pulled further.\nA worker may only pull a ticket, if the WIP Limit is not exceeded.',
        'details': {
            'cycle time': 'The cycle time is the time a ticket needs from being pulled out of the todo column until reaching the done column.',
            'lead time': 'The lead time is the time a ticket needs from showing up on the board until it reaches the done column.',
            'stop the line': 'When at a workstation a defect is noticed, so that the quality does not fit to the expectation, the work is stopped at all workstations to do a root cause analysis.'
        },
        'position': 3
    },
    'tickets': {
        'general': 'Kanban defines three types of Tickets:\n- standard tickets, which are just processed as usual\n- fixed date tickets, which only have a business value, if they are done in time\n- expedite tickets, which have a crucial business value and have to be processed immediately on every workstation. They don’t count into the WIP limit, there may be only a very small number of expedites simultaneously.\nKanban does not define a backlog, but it comes in handy for a product manager to decide which items he will hand over in the next Replenishment Meeting.',
        'position': 4
    },
    'estimations': {
        'general': 'You don’t have to estimate anything.\nAlthough your tickets should have a maximum size to let Kanban work.\nA team may consider a ticket „too large“, then it has to be cut down.',
        'position': 5
    },
    'wip': {
        'general': 'The Work In Progress Limit is used to prevent waste.\nSince humans are very bad at multitasking it is essential to keep focus.\nKanban supports this by limiting the tickets being processed simultaneously.\nThus every workstation column may only contain a limited number of tickets, regardless if they are done or currently in progress.\nDifferent workstation columns may use different WIP limits.\nIt is possible to use Buffers in WIPs. This could however, does handle WIPs in a different mechanism.\nThe WIP limits are reduced if they are not violated for a longer period of time. In case of violation in WIPS however, handling becomes more complicated.',
        'details': {
            'buffer': 'When you introduce buffers, you invalidate the WIP limit of the workstation column before.\nYou may introduce a buffer column next to a workstation column to distinguish between tickets in progress from processed tickets, but you have to count these into the WIP of this workstation.',
            'wip violation': 'A “stop the line” is performed, the root cause of the violation has to be searched, An experiment to fight this root cause is established, the WIP limit is temporarily changed so that no violation is currently visible and the jam can be dissolved.\nIf you observe a problem, there is usually a obvious reason. But this reason may have a cause itself, with a obvious reason.\nWhen hunting down a root cause, one searches for the first element of a causality chain, that would prevent a problem to escalate if removed.'
        },
        'position': 6
    },
    'pull principle': {
        'general': 'It is said, that Toyota developed it by having a closer look at the supply chain in their super markets.\nCustomers pull goods out of the store by grabbing them out of the shelfs.\nThe shelfs are refilled by pulling goods out of the storage.\nThe storage is refilled by ordering goods from the supplier.\nSo the whole stream of goods is propelled by pulling from the end of the chain to the beginning.\nThe system is most efficient, when the amount at every station is minimal, but refilled with least possible delay\nIn an agile context the Pull Principle refers to the effect, that individuals tend to adopt a task with higher motivation when choosing the task by free will instead of taking up a task by order (push).',
        'position': 7
    },
    'ceremonies': {
        'general': 'The replenishment meeting is used to fill the ToDo column with the tickets to be done.\nThe stakeholders who need a ticket to be processed have to transfer the knowledge what is needed to fulfil the ticket successfully to the team working on this board.\nThe team ensures that they know everything they need to know to fulfil these tasks.',
        'position': 8
    }
}
