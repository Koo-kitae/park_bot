//Initialize serial communication in ROS
int InitSerialComm(void)
{
    try
    {
        ser.setPort("/dev/ttyRS485");
        ser.setBaudrate(robotParamData.nBaudrate);
        serial::Timeout to = serial::Timeout::simpleTimeout(1667); //1667 when baud is 57600, 0.6ms
                                                                   //2857 when baud is 115200, 0.35ms
        ser.setTimeout(to);
        ser.open();
    }

