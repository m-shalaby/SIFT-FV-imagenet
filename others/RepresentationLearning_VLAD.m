%an attempt to encode images using Vector of Locally Aggregated Descriptors (VLAD)

%need to run the following line:
%run('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/vlfeat-0.9.21/toolbox/vl_setup')
%To check that VLFeat is sucessfully installed, try to run the vl_version command: vl_version verbose

clc;
clear;

%reading the files
myFolder = '/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/ALLDATAtest';
if ~isdir(myFolder)
  errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);
  uiwait(warndlg(errorMessage));
  return;
end
filePattern = fullfile(myFolder, '*.mat');
matFiles = dir(filePattern);
for k = 1:length(matFiles)
  baseFileName = matFiles(k).name;
  fullFileName = fullfile(myFolder, baseFileName);
  k
  matData(k) = load(fullFileName);
end

%extracting the data from the files
%initialize data
x = cell(length(matData),1);
for i=1:length(matData)
    x{i,1} = matData(i).image_sbow(1).ID(2:9);
    for k = 1:length(matData(i).image_sbow)
        data(i, k) = matData(i).image_sbow(k).sbow; %data(x,y), where x = file representing category & y = image in category
    end
end
data_labels = cell2mat(x); %to get a row, data_labels(row,:)

centers = 0:999;
kdtree = vl_kdtreebuild(double(data(1,1).word));
nn = vl_kdtreequery(kdtree, centers, double(data(1,1).word)) ;
assignments = zeros(length(double(data(1,1).word)),length(double(data(1,1).word)));
assignments(sub2ind(size(assignments), nn, 1:length(nn))) = 1;
enc = vl_vlad(double(data(1,1).word),centers,assignments);

% for i=1:length(matFiles)
%      for k = 1:length(matData(i).image_sbow)
%          words(k,:) = double(data(i,k).word)';
%      end
% end

% for i=1:length(matFiles)
%      for k = 1:length(matData(i).image_sbow)
%          nn = vl_kdtreequery(kdtree, centers, double(data(i,k).word));
%          assignments = zeros(length(centers), length(double(data(i,k).word)));
%          assignments(sub2ind(size(assignments), nn, 1:length(nn))) = 1;
%          enc(i,k,:) = vl_vlad(double(data(i,k).word),centers,assignments);
%          k
%      end
% end
