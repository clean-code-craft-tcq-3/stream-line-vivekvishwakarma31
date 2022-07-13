#include "sender.h"
using namespace std;

SenderStatus ReadBMSParametersFromInputFile(std::vector<float> &temperature, std::vector<float> &stateOfCharge, int &numberOfSamples)
{
    float fTempVal, fChargeRateVal = 0;
    string TempVal, ChargeRateVal;
    string line;
    SenderStatus readingFileStatus;
    ifstream inputFileStream;
    inputFileStream.open("./samples.txt");
    if (!inputFileStream)
    {
        readingFileStatus = SenderStatus::FAILURE;
    }
    else
    {
        while (inputFileStream.peek() != EOF)
        {
            getline(inputFileStream, TempVal, ',');
            getline(inputFileStream, ChargeRateVal, '\n');
            fTempVal = std::stof(TempVal);
            fChargeRateVal = std::stof(ChargeRateVal);
            temperature.push_back(fTempVal);
            stateOfCharge.push_back(fChargeRateVal);
            numberOfSamples++;
        }
        readingFileStatus = SenderStatus::SUCCESS;
    }
    inputFileStream.close();
    return readingFileStatus;
}

void printBMSParamsOnConsole(std::vector<float> &temperature, std::vector<float> &stateOfCharge, int &numberOfSamples)
{
    for (int i = 0; i<numberOfSamples; i++)
    {
        printf(" Temperature:%.2f, StateofCharge:%.2f \n", (temperature[i]), (stateOfCharge[i]));  
    }
    return;

}

SenderStatus SendBMSParameters()
{
    std::vector<float> temperature;
    std::vector<float> stateOfCharge;
    int numberOfSamples;
    ReadBMSParametersFromInputFile(temperature, stateOfCharge, numberOfSamples);
    printBMSParamsOnConsole(temperature, stateOfCharge, numberOfSamples);
    return SenderStatus::SUCCESS;
}
