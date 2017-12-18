#ifndef _SUSI_IMC_TEMPERATURESENSOR_API_H
#define _SUSI_IMC_TEMPERATURESENSOR_API_H

#include "SUSI_IMC_Types.h"

DLLAPI USHORT SUSI_IMC_TEMPERATURESENSOR_Initialize();
DLLAPI USHORT SUSI_IMC_TEMPERATURESENSOR_Deinitialize();
DLLAPI USHORT SUSI_IMC_TEMPERATURESENSOR_GetLibVersion( OUT char *version);
DLLAPI USHORT SUSI_IMC_TEMPERATURESENSOR_GetCPUCore1Temperature ( OUT PBYTE celsius );
DLLAPI USHORT SUSI_IMC_TEMPERATURESENSOR_GetCPUCore2Temperature ( OUT PBYTE celsius );
DLLAPI USHORT SUSI_IMC_TEMPERATURESENSOR_GetSystem1Temperature ( OUT PBYTE celsius );

#endif