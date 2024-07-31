function [mLen, mMean, mStd, mSE, mUpperB, mLowerB] = stdget(input_array)
%[mLen, mMean, mStd, mSE, mUpperB, mLowerB] = stdget(input_array)
% This function takes a given array of data and calculates the length,
% mean, standard deviation, standard error and upper/lower bounds of 95% CI
% for the mean
mLen = length(input_array);
mMean = mean(input_array);
mStd = std(input_array);
mSE = mStd/sqrt(mLen);
crit_val = tinv(1 - 0.05/2, (mLen - 1));
MarginError = crit_val * mSE;
mUpperB = mMean + MarginError;
mLowerB = mMean - MarginError;


end