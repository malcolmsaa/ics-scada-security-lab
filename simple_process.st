PROGRAM SimpleProcess
VAR
    Tank_Level : INT := 0;
    Pump_On : BOOL := FALSE;
    Valve_Open : BOOL := FALSE;
    Setpoint : INT := 500;
    High_Alarm : INT := 800;
END_VAR

IF Tank_Level < Setpoint THEN
    Pump_On := TRUE;
    Valve_Open := FALSE;
ELSIF Tank_Level > High_Alarm THEN
    Pump_On := FALSE;
    Valve_Open := TRUE;
ELSE
    Pump_On := FALSE;
    Valve_Open := FALSE;
END_IF;

END_PROGRAM
