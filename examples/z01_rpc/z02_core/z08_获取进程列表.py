from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.thread_list"))
msf.log.info(msf.call(core.thread_list))
