%need to run the following line:
%run('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/vlfeat-0.9.21/toolbox/vl_setup')
%To check that VLFeat is sucessfully installed, try to run the vl_version command: vl_version verbose

clc
clear

    
%start timer
tic

% http://www.image-net.org/downloads/features/vldsift/n02119789.vldsift.mat
% outfilename = websave('n04140064.vldsift.mat','http://www.image-net.org/downloads/features/vldsift/n02119789.vldsift.mat');

% n02835271

myFolder = '/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/origImages/ImageNet_Downloads';
myDrive = '/Volumes/TOSHIBA AYM/Comp551FinalProject/origImages/ImageNet_Downloads';

if ~isdir(myFolder)
  errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);
  uiwait(warndlg(errorMessage));
  return;
end
filePattern_txt = fullfile(myDrive, 'sysnets.txt');
fid = fopen(filePattern_txt);
tline = fgetl(fid);
label_number = 0;
while ischar(tline)
    tline %display which file being processed
    contents = strsplit(tline);
    tline = fgetl(fid);
    classname_cell = contents(2);
    classname = classname_cell{1};
        filePattern = fullfile(myDrive, 'ImageData', classname,'*.JPEG');
        matFiles = dir(filePattern);
        
        %keep looping until the file is downloaded using the Python script
        %running in parallel
        if isempty(matFiles)
            disp('Waiting for the following file to be created')
            classname
        end
        while isempty(matFiles)
            matFiles = dir(filePattern);
        end
       
        M = cell(length(matFiles), 1);
        fullfeates = [];
        for k = 1:length(matFiles)
          baseFileName = matFiles(k).name;
          fullFileName = fullfile(myDrive, 'ImageData', classname, baseFileName);
          image = imread(fullFileName);
          %   imshow(image)
          try
            grayscale_image = rgb2gray(image);
          catch
            grayscale_image = image;
          end
          points = detectSURFFeatures(grayscale_image);
          [feates, valid_points] = extractFeatures(grayscale_image, points);
          numClusters = 50 ;
          M{k} = feates;
          fullfeates = vertcat(fullfeates,feates);
        end

    [means, covariances, priors] = vl_gmm(fullfeates', numClusters);
    for k = 1:length(matFiles)
        encoding = vl_fisher(M{k}', means, covariances, priors);
        dlmwrite('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/origImages/fisher_vectors.csv',encoding','delimiter',',','-append');
        dlmwrite('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/origImages/labels.csv',label_number,'delimiter',',','-append');
    end
label_number = label_number + 1;    

    
end

%end timer
toc