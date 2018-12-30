#an attempt to encode images into sparse histograms

clc;
clear;

%reading the files
myFolder = '/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/ALLDATA';
savingFolder = '/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/ALLDATAcomp';
vbow_file_train = fullfile(savingFolder, 'vbow_train.csv');
labels_file_train = fullfile(savingFolder, 'labels_train.csv');
vbow_file_valid = fullfile(savingFolder, 'vbow_valid.csv');
labels_file_valid = fullfile(savingFolder, 'labels_valid.csv');
vbow_file_test = fullfile(savingFolder, 'vbow_test.csv');
labels_file_test = fullfile(savingFolder, 'labels_test.csv');
codebook_size=1000;
if or(~isdir(myFolder),~isdir(savingFolder))
  errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);
  uiwait(warndlg(errorMessage));
  return;
end
filePattern = fullfile(myFolder, '*.mat');
matFiles = dir(filePattern);
for i = 1:length(matFiles)
  baseFileName = matFiles(i).name;
  fullFileName = fullfile(myFolder, baseFileName);
  matData = load(fullFileName);
  start=1;
  for k=1:length(matData.image_sbow)
          if k<51
              x = histc(matData.image_sbow(k).sbow.word,0:codebook_size-1);
              x = x / norm(x);
              dlmwrite(vbow_file_valid,x,'delimiter',',','-append');
              dlmwrite(labels_file_valid,i,'delimiter',',','-append');
          elseif k<201
              x = histc(matData.image_sbow(k).sbow.word,0:codebook_size-1);
              x = x / norm(x);
              dlmwrite(vbow_file_test,x,'delimiter',',','-append');
              dlmwrite(labels_file_test,i,'delimiter',',','-append');
          else
              x = histc(matData.image_sbow(k).sbow.word,0:codebook_size-1);
              x = x / norm(x);
              dlmwrite(vbow_file_train,x,'delimiter',',','-append');
              dlmwrite(labels_file_train,i,'delimiter',',','-append');             
          end
  end
  if length(matData.image_sbow) < 500
      length(matData.image_sbow)
  end
  i
end

% fullFileName2 = fullfile(savingFolder, 'new.csv');
% save(fullFileName2)
% %extracting the data from the files
% %initialize data
% x = cell(length(matData),1);
% for i=1:length(matData)
%     x{i,1} = matData(i).image_sbow(1).ID(2:9);
%     for k = 1:length(matData(i).image_sbow)
%         data(i, k) = matData(i).image_sbow(k).sbow; %data(x,y), where x = file representing category & y = image in category
%     end
% end
% data_labels = cell2mat(x); %to get a row, data_labels(row,:)
