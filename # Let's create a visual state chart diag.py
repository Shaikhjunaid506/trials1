# Let's create a visual state chart diagram using Graphviz to represent the hospital reception process.

from graphviz import Digraph

# Create a new directed graph
dot = Digraph(format='png')

# Define the states
states = [
    ("Idle", "Idle (Initial State)"),
    ("CheckIn", "Check-In"),
    ("RequestInfo", "Request Information"),
    ("DeterminePurpose", "Determine Purpose of Visit"),
    ("ConfirmAppointment", "Confirm Appointment"),
    ("DirectEmergency", "Direct to Emergency"),
    ("ScheduleOrWalkIn", "Schedule Appointment or Walk-In"),
    ("WaitDoctor", "Wait for Doctor"),
    ("SendConsultation", "Send to Consultation"),
    ("TerminateCheckIn", "Terminate Check-In")
]

# Add nodes to the graph
for state, label in states:
    dot.node(state, label)

# Define transitions between states
transitions = [
    ("Idle", "CheckIn", "Patient Arrives"),
    ("CheckIn", "DeterminePurpose", "Details Verified"),
    ("CheckIn", "RequestInfo", "Details Incomplete"),
    ("RequestInfo", "CheckIn", "Information Provided"),
    ("RequestInfo", "TerminateCheckIn", "Patient Refuses"),
    ("DeterminePurpose", "ConfirmAppointment", "Appointment Scheduled"),
    ("DeterminePurpose", "DirectEmergency", "Emergency Declared"),
    ("DeterminePurpose", "ScheduleOrWalkIn", "No Appointment"),
    ("ConfirmAppointment", "WaitDoctor", "Appointment Confirmed"),
    ("ConfirmAppointment", "RequestInfo", "Appointment Not Found"),
    ("ScheduleOrWalkIn", "WaitDoctor", "Appointment Scheduled"),
    ("WaitDoctor", "SendConsultation", "Doctor Ready"),
    ("SendConsultation", "Idle", "Consultation Completed"),
    ("DirectEmergency", "Idle", "Patient Directed"),
    ("TerminateCheckIn", "Idle", "Process Terminated"),
    ("WaitDoctor", "Idle", "Patient Leaves"),
    ("ScheduleOrWalkIn", "Idle", "Patient Leaves")
]

# Add edges to the graph
for src, dst, label in transitions:
    dot.edge(src, dst, label)

# Render the diagram to a file
dot.render('/mnt/data/Hospital_Reception_State_Chart', format='png', cleanup=True)

'/mnt/data/Hospital_Reception_State_Chart.png'
