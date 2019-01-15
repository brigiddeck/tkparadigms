# -- dictionaries of params for different stages --

sidesDirectMode = {'outcomeMode':'sides_direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

directMode = {'outcomeMode':'direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

nextCorrectNoDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only' }

nextCorrectDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.1, 'delayToTargetHalfRange':0.05 }

nextCorrectDel2 = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

outcomeOnlyifCorrect= {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

outcomeOnlyifCorrectOffOnWithdrawal = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 
                        'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 
                        'bandMode':'white_only',
                        'soundMode':'off_on_withdrawal'}

onlyIfCorrectMultipleBandwidths = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 
                        'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 
                        'bandMode':'uniform', 'minBand':0.25, 'maxBand':0.25, 'numBands':1, 'includeWhite':'yes',
                        'soundMode':'off_on_withdrawal'}

bandEasySNR = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':10, 'maxSNR':20, 'numSNRs':3, 
               'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
               'bandMode':'uniform', 'minBand':0.25, 'maxBand':0.25, 'numBands':1, 'includeWhite':'yes',
               'soundMode':'off_on_withdrawal','noiseMode':'max_only'}

bandEasySNR2BW = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':10, 'maxSNR':20, 'numSNRs':3, 
               'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
               'bandMode':'uniform', 'minBand':0.25, 'maxBand':0.25, 'numBands':1, 'includeWhite':'yes',
               'soundMode':'off_on_withdrawal','noiseMode':'max_only'}

amplitudevariation = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':10, 'maxSNR':20, 'numSNRs':3, 
               'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
               'bandMode':'uniform', 'minBand':0.25, 'maxBand':0.25, 'numBands':1, 'includeWhite':'no',
               'soundMode':'off_on_withdrawal','noiseMode':'uniform'}

bandEasySNR1BW = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':10, 'maxSNR':20, 'numSNRs':3, 
               'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
               'bandMode':'uniform', 'minBand':0.25, 'maxBand':0.25, 'numBands':1, 'includeWhite':'no',
               'soundMode':'off_on_withdrawal','noiseMode':'max_only'}


bilateralLaser = {'laserMode':'random'}

# -- bandwidth mice --

pardict = {'subject': 'band046', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
pardict.update(bilateralLaser)
band046 = pardict.copy()

pardict = {'subject': 'band047', 'experimenter': 'nadav'}
pardict.update(amplitudevariation)
band047 = pardict.copy()

pardict = {'subject': 'band048', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band048 = pardict.copy()

pardict = {'subject': 'band049', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band049 = pardict.copy()

pardict = {'subject': 'band050', 'experimenter': 'nadav'}
pardict.update(onlyIfCorrectMultipleBandwidths)
band050 = pardict.copy()

pardict = {'subject': 'band051', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
pardict.update(bilateralLaser)
band051 = pardict.copy()

pardict = {'subject': 'band052', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
pardict.update(bilateralLaser)
band052 = pardict.copy()

pardict = {'subject': 'band053', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band053 = pardict.copy()

pardict = {'subject': 'band065', 'experimenter': 'nadav'}
pardict.update(bandEasySNR1BW)
bilateralLaser = {'laserMode':'random'}
band065 = pardict.copy()

pardict = {'subject': 'band066', 'experimenter': 'nadav'}
pardict.update(bandEasySNR2BW)
#bilateralLaser = {'laserMode':'random'}
band066 = pardict.copy()

pardict = {'subject': 'band067', 'experimenter': 'nadav'}
pardict.update(bandEasySNR2BW)
band067 = pardict.copy()

pardict = {'subject': 'band068', 'experimenter': 'nadav'}
pardict.update(bandEasySNR2BW)
band068 = pardict.copy()

pardict = {'subject': 'band069', 'experimenter': 'nadav'}
pardict.update(bandEasySNR2BW)
#pardict.update({'antibiasMode':'repeat_mistake'})
band069 = pardict.copy()

pardict = {'subject': 'band070', 'experimenter': 'nadav'}
pardict.update(bandEasySNR2BW)
#bilateralLaser = {'laserMode':'random'}
#pardict.update({'antibiasMode':'repeat_mistake'})
band070 = pardict.copy()

pardict = {'subject': 'band071', 'experimenter': 'nadav'}
pardict.update(bandEasySNR2BW)
#bilateralLaser = {'laserMode':'random'}
#pardict.update({'antibiasMode':'repeat_mistake'})
band071 = pardict.copy()



pardict = {'subject': 'band078', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band078 = pardict.copy()

pardict = {'subject': 'band079', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band079 = pardict.copy()

pardict = {'subject': 'band080', 'experimenter': 'nadav'}
pardict.update(directMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
band080 = pardict.copy()

pardict = {'subject': 'band081', 'experimenter': 'nadav'}
pardict.update(nextCorrectDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band081 = pardict.copy()

pardict = {'subject': 'band082', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band082 = pardict.copy()

pardict = {'subject': 'band083', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band083 = pardict.copy()

pardict = {'subject': 'band084', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band084 = pardict.copy()

pardict = {'subject': 'band085', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band085 = pardict.copy()

pardict = {'subject': 'band086', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band086 = pardict.copy()

pardict = {'subject': 'band087', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
#pardict.update({'antibiasMode':'repeat_mistake'})
band087 = pardict.copy()
