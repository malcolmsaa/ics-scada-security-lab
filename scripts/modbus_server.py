from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [1] * 100),
    co=ModbusSequentialDataBlock(0, [0] * 100),
    hr=ModbusSequentialDataBlock(0, [10] * 100),
    ir=ModbusSequentialDataBlock(0, [20] * 100),
)
context = ModbusServerContext(slaves=store, single=True)

print("Starting Modbus server on 0.0.0.0:502")
StartTcpServer(context=context, address=("0.0.0.0", 502))
