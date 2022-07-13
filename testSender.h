#include "sender.h"
#include <assert.h>

//To check if the sender reads data from input file
void TestCheckSenderReadsDatafromInputFile()
{
  SenderStatus status;
  std::vector<float> temperature;
  std::vector<float> stateOfCharge;
  int numberOfSamples = 0;
  assert(ReadBMSParametersFromInputFile(temperature, stateOfCharge, numberOfSamples) == SenderStatus::SUCCESS); 
}
