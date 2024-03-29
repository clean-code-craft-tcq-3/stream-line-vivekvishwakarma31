#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include<iterator>
#include <stdio.h>
#define TOTALSAMPLES 50

enum SenderStatus{
    SUCCESS,
    FAILURE
};

SenderStatus ReadBMSParametersFromInputFile(std::vector<float> &temperature, std::vector<float> &stateOfCharge, int &numberOfSamples);
SenderStatus printBMSParamsOnConsole(std::vector<float> &temperature, std::vector<float> &stateOfCharge, int &numberOfSamples);
SenderStatus WriteBMSParamsToFile(std::vector<float> &temperature, std::vector<float> &stateOfCharge, int &numberOfSamples);
SenderStatus SendBMSParameters();
