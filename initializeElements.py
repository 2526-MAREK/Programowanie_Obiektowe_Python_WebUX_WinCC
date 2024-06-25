from ElementFile import Element

def processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj):
    elementObj = Element(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition)
    filePath, nameOfFunction = elementObj.ReadElementFromJson(fileName)
    if filePath is not None:
        filePathTabOfPropObj.append(filePath)
        nameOfFunctionTabOfPropObj.append(nameOfFunction)

def initializeElementsFnc(fileName):
    filePathTabOfPropObj = []
    nameOfFunctionTabOfPropObj = []


    typeOfElement = "AirKnocker"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\AirKnocker_Icon.FPT"
    listOfProps = ['SIMPLE_VALVE_Status', 'FullTagName', 'SIMPLE_VALVE_Config', 'Top', 'Tag', 'ElementID', 'Left', 'SIMPLE_VALVE_Status02', 'SIMPLE_VALVE_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['FullTagName', 'Tag']
    listOfTextProps = {
        'Tag': 0,
        'FullTagName': 1,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ElectricHeater"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Electric_Heater_A01.FPT"
    listOfProps = ['Value', 'ElementID', 'Top', 'Name', 'Left', 'FillColor']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Name']
    listOfTextProps = {
        'Name': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ArrowRight"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Arrow_Right.FPT"
    listOfProps = ['kolor', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveDirectional"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveDirectional_Icon.FPT"
    listOfProps = ['SIMPLE_VALVE_Status', 'FullTagName', 'SIMPLE_VALVE_Config', 'Top', 'Tag', 'ElementID', 'Left', 'SIMPLE_VALVE_Status02', 'SIMPLE_VALVE_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['FullTagName', 'Tag']
    listOfTextProps = {
        'Tag': 0,
        'FullTagName': 1,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "BigBag"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Bigbag.FPT"
    listOfProps = ['Label', 'ElementID', 'Bigbag_Ready', 'Top', 'Bigbag_Error', 'Left', 'Bigbag_Dosing']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "CtrVav"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveCtr_Icon.FPT"
    listOfProps = ['CONTROL_VALVE_Status', 'CONTROL_VALVE_PositionFbk', 'CONTROL_VALVE_StatusAlarm', 'Label', 'CONTROL_VALVE_Config', 'ElementID', 'Tag', 'Top', 'CONTROL_VALVE_Status02', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "DigitalInput"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\DI_Icon.FPT"
    listOfProps = ['DIGITAL_INPUT_PV', 'Label', 'DIGITAL_INPUT_Config', 'ElementID', 'Tag', 'Top', 'Left', 'DIGITAL_INPUT_Status_Failure', 'DIGITAL_INPUT_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "DigitalOutput"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\DO_Icon.FPT"
    listOfProps = ['Label', 'ElementID', 'Tag', 'Top', 'DIGITAL_OUTPUT_Status02', 'DIGITAL_OUTPUT_Config', 'DIGITAL_OUTPUT_Status', 'DIGITAL_OUTPUT_StatusAlarm', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "HOPPER"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Hopper.FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MtrFq"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MotorFq_Icon.FPT"
    listOfProps = ['FQ_MOTOR_SpeedFbk', 'FQ_MOTOR_Config', 'PumpRevLinesVisibility', 'Label', 'ElementID', 'Tag', 'Top', 'MotorVisibility', 'FanRevLinesVisibility', 'FanFwdLinesVisibility', 'FQ_MOTOR_Status02', 'Left', 'PumpFwdLinesVisibility', 'FQ_MOTOR_StatusAlarm', 'Unit', 'FQ_MOTOR_Status', 'MaxLimit']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'Unit', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
        'Label': 0,
        'Unit': 3,
        'MaxLimit': 4,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Output"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Unknown"
    listOfProps = ['OutputValue', 'ObjectName', 'ElementID']
    listOfPropsToDelete = ['ElementID']
    listOfStringInPropsToCondition = ['ObjectName']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "PID"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\PID_Icon.FPT"
    listOfProps = ['SP_Unit', 'PID_Config', 'PID_ProcessData_SPRampOut', 'Label', 'ElementID', 'Tag', 'Top', 'PID_Status', 'Left', 'PID_ProcessData_PID_RegulatorCV', 'PV_Unit', 'PID_ProcessData_PVLagOut', 'PID_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['PV_Unit', 'Label', 'SP_Unit', 'Tag']
    listOfTextProps = {
        'Label': 0,
        'PV_Unit': 1,
        'SP_Unit': 2,
        'Tag': 3,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Seal"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Seal_Icon.FPT"
    listOfProps = ['SIMPLE_VALVE_Status', 'Label', 'SIMPLE_VALVE_Config', 'Tag', 'Top', 'ElementID', 'Left', 'SIMPLE_VALVE_Status02', 'SIMPLE_VALVE_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Sequence"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Sequence_icon.FPT"
    listOfProps = ['SEQUENCER_Aborting_StepNo', 'SEQUENCER_Holding_StepNo', 'SEQUENCER_Status', 'Label', 'SEQUENCER_StatusAlarm', 'Tag', 'Top', 'ElementID', 'SEQUENCER_Running_StepNo', 'Left', 'Text', 'SEQUENCER_Stopping_StepNo']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Text', 'Label', 'Tag']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "VavSmpV"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveSimple_IconV.FPT"
    listOfProps = ['SIMPLE_VALVE_Status', 'Label', 'SIMPLE_VALVE_Config', 'Tag', 'Top', 'ElementID', 'Left', 'SIMPLE_VALVE_Status02', 'SIMPLE_VALVE_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ThreeWayValveSimpleD3_IconV"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\3WayValveSimpleD3_IconV.FPT"
    listOfProps = ['3WAY_VALVE_Status02', '3WAY_VALVE_Config', 'ObjectName', 'Label', '3WAY_VALVE_StatusAlarm', 'Tag', 'Top', 'Configuration_D03', 'ElementID', '3WAY_VALVE_Status', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ThreeWayValveSimpleD3_Icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\3WayValveSimpleD3_Icon.FPT"
    listOfProps = ['3WAY_VALVE_Status02', '3WAY_VALVE_Config', 'ObjectName', 'FromLeftToRight', 'Label', '3WAY_VALVE_StatusAlarm', 'Tag', 'Top', 'Configuration_D03', 'ElementID', '3WAY_VALVE_Status', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ThreeWayValveSimple_IconV"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\3WayValveSimple_IconV.FPT"
    listOfProps = ['3WAY_VALVE_Status02', '3WAY_VALVE_Config', 'ObjectName', 'Label', '3WAY_VALVE_StatusAlarm', 'Tag', 'Top', 'Configuration_D03', 'ElementID', '3WAY_VALVE_Status', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ThreeWayValveSimple_Icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\3WayValveSimple_Icon.FPT"
    listOfProps = ['3WAY_VALVE_Status02', '3WAY_VALVE_Config', 'ObjectName', 'FromLeftToRight', 'Label', '3WAY_VALVE_StatusAlarm', 'Tag', 'Top', 'Configuration_D03', 'ElementID', '3WAY_VALVE_Status', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ThreeWayValveSimple_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\3WayValveSimple_Icon_HIMTECH.FPT"
    listOfProps = ['Valve_Close_2Way', 'ObjectName', 'Valve_Open', 'Label', 'Interlock_Active', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Valve_Close_1Way', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "AngInpt"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\AI_Icon.FPT"
    listOfProps = ['Max', 'EngUnits', 'alLo', 'Label', 'alTechLo', 'ElementID', 'Min', 'alTechOn', 'Top', 'Value', 'ANALOG_INPUT_StatusAlarm', 'Tag', 'alHiHi', 'alLoLo', 'ANALOG_INPUT_Status', 'alHi', 'alTechHi', 'Left', 'ANALOG_INPUT_Config']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'EngUnits', 'Tag', 'alTechOn']
    listOfTextProps = {
        'EngUnits': 0,
        'Label': 1,
        'Tag': 2,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Arrow_Down"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Arrow_Down.FPT"
    listOfProps = ['kolor', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Arrow_Left"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Arrow_Left.FPT"
    listOfProps = ['ObjectName', 'kolor', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'ObjectName']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Arrow_UP"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Arrow_UP.FPT"
    listOfProps = ['ObjectName', 'kolor', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'ObjectName']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Auto_Bag_Filter"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Auto-Bag Filter.FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "BarGraph_Furnance_2"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\BarGraph_Furnance_2.FPT"
    listOfProps = ['Max', 'EngUnits', 'alLo', 'Label', 'alTechLo', 'ElementID', 'alHiLoOn', 'Min', 'alTechOn', 'Top', 'SP', 'Value', 'spOn', 'alHiHi', 'alLoLo', 'alHi', 'alTechHi', 'alHiHiLoLoOn', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['EngUnits', 'alHiHiLoLoOn', 'Label', 'spOn', 'alTechOn', 'alHiLoOn']
    listOfTextProps = {
        'Label': 0,
        'EngUnits': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Furnace_BarGraph_Horizontal"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Furnace_BarGraph_Horizontal.FPT"
    listOfProps = ['Max', 'EngUnits', 'alLo', 'Label', 'alTechLo', 'ElementID', 'alLoOn', 'Min', 'alTechOn', 'Top', 'alHiOn', 'SP', 'Value', 'spOn', 'alHiHi', 'alLoLo', 'alHi', 'alTechHi', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['EngUnits', 'Label', 'spOn', 'alTechOn', 'alLoOn', 'alHiOn']
    listOfTextProps = {
        'Label': 0,
        'EngUnits': 1,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "BarGraph_Furnance_2_Long_Label_Format"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\BarGraph_Furnance_2_Long_Label_Format.FPT"
    listOfProps = ['Max', 'EngUnits', 'alLo', 'Label', 'alTechLo', 'ElementID', 'alHiLoOn', 'Min', 'alTechOn', 'Top', 'SP', 'Value', 'spOn', 'alHiHi', 'alLoLo', 'alHi', 'alTechHi', 'alHiHiLoLoOn', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['EngUnits', 'alHiHiLoLoOn', 'Label', 'spOn', 'alTechOn', 'alHiLoOn']
    listOfTextProps = {
        'Label': 0,
        'EngUnits': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Bead_Mill"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Bead Mill.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Cartridge_Filter"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Cartridge Filter.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Cooler_Mixer"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Cooler Mixer.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveCtr_IconV"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveCtr_IconV.FPT"
    listOfProps = ['CONTROL_VALVE_Status', 'CONTROL_VALVE_PositionFbk', 'CONTROL_VALVE_StatusAlarm', 'Label', 'CONTROL_VALVE_Config', 'FullTagName', 'ElementID', 'Top', 'CONTROL_VALVE_Status02', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'FullTagName', 'Tag']
    listOfTextProps = {
        'Label': 0,
        'FullTagName': 1,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "DI_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\DI_Icon_HIMTECH.FPT"
    listOfProps = ['ObjectName', 'DIGITAL_INPUT_PV', 'Label', 'DIGITAL_INPUT_Config', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Left', 'DIGITAL_INPUT_Status_Failure', 'DIGITAL_INPUT_StatusAlarm', 'DI_Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Dumping_Unit"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Dumping_Unit.FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "EM_Electro_magnetic_separator"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\EM - Electro magnetic separator.FPT"
    listOfProps = ['ObjectName', 'label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Filter_Press"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Filter Press.FPT"
    listOfProps = ['Connection_Right_Visibility2', 'ObjectName', 'Connction_Left_Visibility', 'Connection_Right_Visibility', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Connection_Right_Visibility', 'Connection_Right_Visibility2', 'ObjectName', 'Connction_Left_Visibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "FlowBinFI_Icon_small"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\FlowBinFI_Icon_small.FPT"
    listOfProps = ['ObjectName', 'FlowBin_AlarmLimit', 'FLOW_BIN_READY_FlowbinFI_Ready', 'ElementID', 'FLOW_BIN_FI_FlowbinFI_Error', 'Top', 'FlowBin_Error', 'FlowBin_Name', 'Left', 'FlowBin_Ready']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['FlowBin_Name', 'FLOW_BIN_READY_FlowbinFI_Ready', 'ObjectName', 'FLOW_BIN_FI_FlowbinFI_Error']
    listOfTextProps = {
        'FlowBin_Name': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "FlowBinFU_Icon_small"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\FlowBinFU_Icon_small.FPT"
    listOfProps = ['FLOW_BIN_FU_FlowbinFU_Error', 'ObjectName', 'FLOW_BIN_FU_FlowbinFU_DosingOn', 'FlowBin_AlarmLimit', 'FlowBin_Dosing', 'ElementID', 'Top', 'FlowBin_Error', 'FlowBin_Name', 'Left', 'FlowBin_Ready', 'FLOW_BIN_READY_FlowbinFU_Ready']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['FLOW_BIN_FU_FlowbinFU_Error', 'ObjectName', 'FLOW_BIN_FU_FlowbinFU_DosingOn', 'FlowBin_Name', 'FLOW_BIN_READY_FlowbinFU_Ready']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "FI"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\FlowBinFI_Icon.FPT"
    listOfProps = ['FlowBin_AlarmLimit', 'ElapsedTime', 'FlowBinTimer_Visibility', 'FLOW_BIN_READY_FlowbinFI_Ready', 'ElementID', 'FLOW_BIN_FI_FlowbinFI_Error', 'Top', 'FlowBin_Error', 'FlowBin_Color', 'FlowBin_Name', 'Left', 'FlowBin_Ready']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['FlowBinTimer_Visibility', 'FLOW_BIN_READY_FlowbinFI_Ready', 'FlowBin_Name', 'FLOW_BIN_FI_FlowbinFI_Error']
    listOfTextProps = {
        'FlowBin_Name': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "FlowBinFU_Icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\FlowBinFU_Icon.FPT"
    listOfProps = ['FlowBin_AlarmLimit', 'ElapsedTime', 'ElementID', 'FlowBin_Dosing', 'Top', 'FlowBin_Error', 'FlowBin_Color', 'FlowBin_Name', 'Left', 'FlowBin_Ready']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['FlowBin_Name']
    listOfTextProps = {
        'FlowBin_Name': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Gas_Liquid_Separator"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Gas-Liquid Separator.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Hydraulic_Unit"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Hydraulic Unit.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "In_Line_Filter"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\In-Line Filter.FPT"
    listOfProps = ['ObjectName', 'ElementID', 'Top', 'Left', 'LF_status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "KTron"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\KTron_Icon.FPT"
    listOfProps = ['ObjectName', 'Label', 'K-TRON_StatusAlarm', 'ElementID', 'Tag', 'Top', 'MotorVisibility', 'FanRevLinesVisibility', 'K-TRON_Status', 'K-TRON_Config', 'Left', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'K-TRON_Status02', 'FanFwdLinesVisibility']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Local_Filter_HF"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Local Filter (HF).FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MF_icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MF_icon.FPT"
    listOfProps = ['ObjectName', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MixerIcon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\MixerIcon.FPT"
    listOfProps = ['SEQUENCER_Aborting_StepNo', 'SEQUENCER_Status', 'PoVisibility', 'ObjectName', 'MXRunning', 'ElementID', 'Top', 'LeftRight', 'PONumber', 'SEQUENCER_Running_StepNo', 'FQ_MOTOR_Status_Running', 'SEQUENCER_StepNo', 'SIMPLE_MOTOR_Status_Running', 'SEQUENCER_Holding_StepNo', 'Left', 'SEQUENCER_Stopping_StepNo']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['PoVisibility', 'ObjectName', 'LeftRight', 'FQ_MOTOR_Status_Running', 'SIMPLE_MOTOR_Status_Running']
    listOfTextProps = {
        'PONumber': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MotorFq_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MotorFq_Icon_HIMTECH.FPT"
    listOfProps = ['ObjectName', 'Label', 'Interlock_Active', 'Motor_SpeedFbk', 'Motor_Running', 'Tag', 'Top', 'MotorVisibility', 'FanRevLinesVisibility', 'ElementID', 'FanFwdLinesVisibility', 'Alarm_Active', 'Left', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'Unit', 'Motor_Stopping', 'MaxLimit']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'Unit', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
        'Unit': 3,
        'MaxLimit': 4,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MotorSample_Icon_HIMTECHOverview"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MotorSample_Icon_HIMTECHOverview.FPT"
    listOfProps = ['ObjectName', 'MotorARunning', 'Label', 'AlarmMotorB', 'ElementID', 'Top', 'MotorBRunning', 'AlarmMotorA', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'ObjectName']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MotorSample_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MotorSample_Icon_HIMTECH.FPT"
    listOfProps = ['ObjectName', 'Label', 'Interlock_Active', 'Motor_Running', 'Tag', 'Top', 'MotorVisibility', 'FanRevLinesVisibility', 'ElementID', 'Alarm_Active', 'Left', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'Motor_Stopping', 'FanFwdLinesVisibility']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "mtrSmp"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MotorSample_Icon.FPT"
    listOfProps = ['SIMPLE_MOTOR_Config', 'SIMPLE_MOTOR_Status', 'Label', 'ElementID', 'Tag', 'Top', 'MotorVisibility', 'FanRevLinesVisibility', 'Left', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'SIMPLE_MOTOR_StatusAlarm', 'SIMPLE_MOTOR_Status02', 'FanFwdLinesVisibility']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MtrSmp_Ov"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MotorSample_IconOverview.FPT"
    listOfProps = ['SIMPLE_MOTOR_Status02', 'PumpRevLinesVisibility', 'FQ_MOTOR_Config', 'ObjectName', 'SIMPLE_MOTOR_Config', 'SIMPLE_MOTOR_Status', 'ElementID', 'Tag', 'Top', 'MotorVisibility', 'FanRevLinesVisibility', 'FQ_MOTOR_Status02', 'Left', 'PumpFwdLinesVisibility', 'FQ_MOTOR_StatusAlarm', 'SIMPLE_MOTOR_StatusAlarm', 'FQ_MOTOR_Status', 'FanFwdLinesVisibility']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "MXSequence_Icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\MXSequence_Icon.FPT"
    listOfProps = ['StepNo', 'ObjectName', 'ElementID', 'Top', 'PONumber', 'Left', 'Text', 'StopButtVis']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['TextList', 'PoVisibility', 'ObjectName', 'PONumber', 'Text', 'PrefixName', 'SEQUENCER_BLENDER', 'SequenceName']
    listOfTextProps = {
        'Text': 0,
        'PONumber': 2,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Paddle_Dryer"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Paddle Dryer.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Pressure_Vessel"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Pressure Vessel.fpt"
    listOfProps = ['ElementID', 'FullTagName', 'Top', 'PRESSURE_VESSEL_StatusAlarm', 'PRESSURE_VESSEL_Machine_State', 'Left', 'Text', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Text', 'FullTagName']
    listOfTextProps = {
        'Text': 0,
        'FullTagName': 3,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Pressure_Vessel_small"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Pressure Vessel_small.fpt"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Text', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'Text', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Text': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Roll_Mill"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Roll Mill.FPT"
    listOfProps = ['ObjectName', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Rotary_Valve"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Rotary Valve.FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Rotary_Magnet_Filter"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Rotary Magnet.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Scattering_Machine"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Scattering Machine.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Status', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Screw_Feeder_connetor"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Screw Feeder-connetor.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Status', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Screw_Feeder_Left"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Screw Feeder-Left.FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'ststus', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Screw_Feeder_Right"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Screw Feeder-Right.FPT"
    listOfProps = ['Label', 'ElementID', 'Top', 'ststus', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Screw_Feeder_separator"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Screw Feeder-separator.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Scrubber_Demister_Tank"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Scrubber (Demister Tank).FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Seal_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Seal_Icon_HIMTECH.FPT"
    listOfProps = ['ObjectName', 'Seal_Status', 'Label', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Sequence_FI"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Sequence_FI.FPT"
    listOfProps = ['SEQUENCER_Status', 'StepNo', 'FI_SEQUENCER_Undocking_StepNo', 'FI_SEQUENCER_Docking_StepNo', 'FullTagName', 'WordDimension', 'Top', 'SEQUENCER_StatusAlarm', 'ElementID', 'Left', 'Text', 'PrefixName']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Text', 'PrefixName', 'FullTagName']
    listOfTextProps = {
        'FullTagName': 2,
        'Text': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Sequence_FU"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Sequence_FU.FPT"
    listOfProps = ['SEQUENCER_Status', 'StepNo', 'FU_SEQUENCER_Docking_StepNo', 'FullTagName', 'WordDimension', 'Top', 'SEQUENCER_StatusAlarm', 'ElementID', 'FU_SEQUENCER_Undocking_StepNo', 'Left', 'Text', 'PrefixName']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Text', 'PrefixName', 'FullTagName']
    listOfTextProps = {
        'FullTagName': 2,
        'Text': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "SequenceWater_Tank"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\SequenceWater Tank.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['TextList', 'ObjectName', 'Label', 'ButtGenName', 'PrefixName', 'SequenceName']
    listOfTextProps = {
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Sieve"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Sieve.FPT"
    listOfProps = ['ObjectName', 'label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Totalizer_Icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\Totalizer_Icon.FPT"
    listOfProps = ['SP1_Unit', 'ObjectName', 'Label', 'ElementID', 'Tag', 'Top', 'CUR_Unit', 'REM_Unit', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['SP1_Unit', 'ObjectName', 'Label', 'Tag', 'CUR_Unit', 'REM_Unit']
    listOfTextProps = {
        'Label': 0,
        'Tag': 0,
        'CUR_Unit': 1,
        'SP1_Unit': 2,
        'REM_Unit': 5,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Unit"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\PM Manage\\Unit.FPT"
    listOfProps = ['ElementID', 'EndTimeTag', 'QuantitySPTag', 'RequestTag', 'Left', 'StartTimeTag', 'MaterialNumberTag', 'JobNameTag', 'SelectedUnitTag', 'StatusAbrtd', 'Top', 'StatusError', 'QuantityPVTag', 'StatusDone', 'StatusIntlk', 'StatusHeld', 'StatusReady', 'ProductionLineTag', 'MaterialNameTag', 'BatchActiveTag', 'JobCtrlTag', 'ObjectName', 'CMDRequestTag', 'UnitNameText', 'StatusRun', 'PMQStatusTag']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'UnitNameText', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'UnitNameText': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Vacuum_Kettle_Dryer"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Vacuum Kettle Dryer.FPT"
    listOfProps = ['Motor2', 'Motor1', 'ObjectName', 'Label', 'ElementID', 'Top', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Vacuum_Pump"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Vacuum Pump.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Kolor']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveCtrl_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveCtrl_Icon_HIMTECH.FPT"
    listOfProps = ['PositionFbk', 'Valve_Close', 'ObjectName', 'Valve_Open', 'Label', 'Interlock_Active', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveCtrl_Icon_V_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveCtrl_Icon_V_HIMTECH.FPT"
    listOfProps = ['PositionFbk', 'Valve_Close', 'ObjectName', 'Valve_Open', 'Label', 'Interlock_Active', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveMotor_Icon"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveMotor_Icon.FPT"
    listOfProps = ['SIMPLE_VALVE_Status', 'Label', 'SIMPLE_VALVE_Config', 'Tag', 'Top', 'FullTagName', 'ElementID', 'Left', 'SIMPLE_VALVE_Status02', 'SIMPLE_VALVE_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'FullTagName', 'Tag']
    listOfTextProps = {
        'FullTagName': 1,
        'Label': 0,
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveSimple_IconV_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveSimple_IconV_HIMTECH.FPT"
    listOfProps = ['Valve_Close', 'ObjectName', 'Valve_Open', 'Label', 'Interlock_Active', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "ValveSimple_Icon_HIMTECH"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveSimple_Icon_HIMTECH.FPT"
    listOfProps = ['Valve_Close', 'ObjectName', 'Valve_Open', 'Label', 'Interlock_Active', 'ElementID', 'Tag', 'Top', 'Alarm_Active', 'Left']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
        'Tag': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "VavSmp"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Devices\\Icons\\ValveSimple_Icon.FPT"
    listOfProps = ['SIMPLE_VALVE_Status', 'Label', 'SIMPLE_VALVE_Config', 'Tag', 'Top', 'ElementID', 'Left', 'SIMPLE_VALVE_Status02', 'SIMPLE_VALVE_StatusAlarm']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Label', 'Tag']
    listOfTextProps = {
        'Tag': 1,
        'Label': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Vibrator_Feeder_mirror"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Vibrator Feeder_mirror.fpt"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "VP_Separator"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\VP_Separator.FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Water_Tank"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Water Tank.FPT"
    listOfProps = ['ElementID', 'Top', 'Agitator_Visibility', 'Left', 'Text', 'status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['Text', 'Agitator_Visibility']
    listOfTextProps = {
        'Text': 0,
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Water_Cooler_Condensor"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Water Cooler (Condensor).FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Status', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)


    typeOfElement = "Water_Cooler_Heat_Exchanger"
    kindOfFunctionToInitializeElement = "W2A"
    faceplateType = "Faceplates\\Water Cooler (geat Exchanger).FPT"
    listOfProps = ['ObjectName', 'Label', 'ElementID', 'Top', 'Left', 'Status']
    listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    listOfStringInPropsToCondition = ['ObjectName', 'Label', 'Tag', 'MotorVisibility', 'FanRevLinesVisibility', 'PumpFwdLinesVisibility', 'PumpRevLinesVisibility', 'FanFwdLinesVisibility']
    listOfTextProps = {
    }

    processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)




    return filePathTabOfPropObj, nameOfFunctionTabOfPropObj