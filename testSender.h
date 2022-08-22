#include "sender.h"
#include <assert.h>

//To check if the sender reads data from input file
void TestCheckSenderReadsDatafromInputFile()
{
  std::vector<float> temperature;
  std::vector<float> stateOfCharge;
  int numberOfSamples = 0;
  assert(ReadBMSParametersFromInputFile(temperature, stateOfCharge, numberOfSamples) == SUCCESS); 
  
}

//To Check if the sender sends the sample or not.
void TestCheckSenderSentSamples()
{
  assert(SendBMSParameters() == SUCCESS); 
}


