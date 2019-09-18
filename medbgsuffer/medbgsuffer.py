"""
Demonstrates reading and writing the SUFFER bits on mEDBG (Xplained Mini kits)

"""
from pyedbglib.hidtransport.hidtransportfactory import hid_transport
from pyedbglib.protocols import medbgprotocol

# Create and connect to transport
transport = hid_transport()
if not transport.connect(product="medbg"):
    raise Exception("mEDBG not found!")

# Create protocol with this transport
medbg = medbgprotocol.mEdbgProtocol(transport)

# Read out suffer
suffer = medbg.read_config(medbgprotocol.mEdbgProtocol.CONFIG_REG_SUFFER_BANK,
                           medbgprotocol.mEdbgProtocol.CONFIG_REG_SUFFER_OFFSET, 1)[1][0]
print("SUFFER read as 0x{:02X}".format(suffer))

# Modify and write back
suffer = 0xFF
print("Writing SUFFER to 0x{:02X}".format(suffer))
status = medbg.write_config(medbgprotocol.mEdbgProtocol.CONFIG_REG_SUFFER_BANK,
                            medbgprotocol.mEdbgProtocol.CONFIG_REG_SUFFER_OFFSET,
                            bytearray([suffer]))

# Read out again
suffer = medbg.read_config(medbgprotocol.mEdbgProtocol.CONFIG_REG_SUFFER_BANK,
                           medbgprotocol.mEdbgProtocol.CONFIG_REG_SUFFER_OFFSET, 1)[1][0]
print("SUFFER read back as 0x{:02X}".format(suffer))
transport.disconnect()
