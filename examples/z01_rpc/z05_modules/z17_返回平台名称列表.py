from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.platforms"))
msf.log.info(msf.call(module.platforms))
