from gi.repository import RB

class CoherenceDBEntryType(RB.RhythmDBEntryType):
	def __init__(self, client_id):
		entry_name = "CoherenceUpnp:%s", client_id
		RB.RhythmDBEntryType.__init__(self, name=entry_name)
