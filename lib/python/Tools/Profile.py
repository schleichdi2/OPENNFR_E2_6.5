# the implementation here is a bit crappy.
from __future__ import print_function
from __future__ import absolute_import
from boxbranding import getBoxType
import time
from Tools.Directories import resolveFilename, SCOPE_CONFIG

boxtype = getBoxType()

PERCENTAGE_START = 50
PERCENTAGE_END = 100

profile_start = time.time()

profile_data = {}
total_time = 1
profile_file = None

try:
	f = open(resolveFilename(SCOPE_CONFIG, "profile"), "r")
	profile_old = f.readlines()
	f.close()

	t = None
	for line in profile_old:
		(t, id) = line[:-1].split('\t')
		t = float(t)
		total_time = t
		profile_data[id] = t
except:
	print("no profile data available")

try:
	profile_file = open(resolveFilename(SCOPE_CONFIG, "profile"), "w")
except IOError:
	print("WARNING: couldn't open profile file!")

def profile(id):
	now = time.time() - profile_start
	if profile_file:
		profile_file.write("%7.3f\t%s\n" % (now, id))

		if id in profile_data:
			t = profile_data[id]
			if total_time:
				perc = t * (PERCENTAGE_END - PERCENTAGE_START) / total_time + PERCENTAGE_START
			else:
				perc = PERCENTAGE_START
			try:
				if boxtype in ("classm", "ew7362", "atemio6100", "atemio6000", "atemio6200", "axodin", "axodinc", "starsatlx", "evo", "genius", "galaxym6", "formuler1", "sparktriplex", "sparkone" ):
					f = open("/dev/dbox/oled0", "w")
					f.write("%d" % perc)
				elif boxtype == "xpeedlx1":
					f = open("/proc/vfd", "w")
					f.write( "  %d" % perc)	
				elif boxtype == "bre2ze":
					f = open("/proc/vfd", "w")
					f.write( "%d" % perc)								
				elif boxtype == "xpeedlx2":
					f = open("/dev/dbox/oled0", "w")
					f.write("  %d  " % perc)  
				elif boxtype == "formuler1":
					f = open("/dev/dbox/oled0", "w")
					f.write("   %d   " % perc)						
				elif boxtype in ("sf4008", "sf3038"):
					f = open("/dev/dbox/oled0", "w")
					f.write("Load %d %%" % perc)
				elif boxtype == "gb800se" or boxtype == "gb800solo":
					f = open("/dev/dbox/oled0", "w")
					f.write("%d  \n" % perc)
				elif boxtype == "gb800seplus":
					f = open("/dev/mcu", "w")
					f.write("%d  \n" % perc)
				elif boxtype in ("mixosf5", "gi9196m", "osmini", "osmega", "spycatmini", "osminiplus"):
					f = open("/proc/progress", "w")
					f.write("%d" % perc)
				elif boxtype in ("xpeedlx3", "atemionemesis"):
					f = open("/proc/vfd", "w")
					f.write("Loading %d %%" % perc)
				elif getBoxType() in ('amikomini', 'amiko8900', 'sognorevolution', 'arguspingulux', 'arguspinguluxmini', 'sparkreloaded', 'sabsolo', 'sparklx', 'gis8120'):
					f = open("/proc/vfd", "w")
					f.write("%d \n" % perc)
				else:
					f = open("/proc/progress", "w")
					f.write("%d \n" % perc)
				f.close()
			except IOError:
				pass

def profile_final():
	global profile_file
	if profile_file is not None:
		profile_file.close()
		profile_file = None
