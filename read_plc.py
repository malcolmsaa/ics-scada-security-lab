from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("localhost", port=502)

if not client.connect():
    print("Kunde inte ansluta till PLC")
    raise SystemExit(1)

print("Ansluten till PLC")

rr = client.read_holding_registers(address=0, count=5, slave=1)
print("Holding registers:", rr)

coils = client.read_coils(address=0, count=2, slave=1)
print("Coils:", coils)

client.close()
