# Facial Recognition System Using Python

**Libraries Used:** face_recognition, OpenCV, OS

- I have used _OpenCV_ for labelling on the images and _OS_ for working with the directories.
- I have created two directories, known_faces and unknown_faces. Inside known_faces I have added three images of elon musk and in unknown_faces, 
I have added images I intend to label.

## **Known_directory**

![elonmusk3](https://user-images.githubusercontent.com/84052591/132956386-49e7ab9b-14f3-4ebb-9254-50de124aa6ba.jpeg)
<br/>
![oie_111943123aY81j85](https://user-images.githubusercontent.com/84052591/132956588-44cfded6-8321-4a5a-a787-a892cf77e038.jpg)

![oie_11194235h794k682](https://user-images.githubusercontent.com/84052591/132956594-da03f170-689a-4618-a821-047b842c11ac.jpg)

## **Unknown_directory**

![oie_11194851DopTQftn](https://user-images.githubusercontent.com/84052591/132956747-b53f9ca0-53ef-41d0-b764-2b9f36acae32.jpg)
![oie_111948217DjgtY2H](https://user-images.githubusercontent.com/84052591/132956754-f89204d8-5881-4b3e-98cb-f5eb84fd2822.jpg)
![oie_11194754zNjN3r2T](https://user-images.githubusercontent.com/84052591/132956757-ca0f33cd-b9ca-4d5a-90de-e70718b0498f.png)

### - I used the tolerance of 0.6 for the face recognition and hog model to analyze the visual image 
### - Firstly, I iterated over the known faces directory, loaded images, encoded each face (128 dimesion face encoding) and stored the encodings. 
### - After that, I terated over the unknown directory and compared to the known faces. 
### - After finding a match with any of the known faces, I drew the rectangle around it. 
### - Lastly, I painted the frame around the face and wrote name. 
### - Used imshow from OpenCV to display the images.
 
## **Example of results**

<img width="500" alt="oie_1204238a6uGZhDE" src="https://user-images.githubusercontent.com/84052591/132963337-f55653aa-cbb2-4e24-850b-1345580b996d.png">
<img width="557" alt="oie_120433UqKh0WuD" src="https://user-images.githubusercontent.com/84052591/132963339-a481348b-a6bb-4869-90f1-c2e68c59492d.png">
<img width="525" alt="oie_1204359CnNSPPog" src="https://user-images.githubusercontent.com/84052591/132963342-e403833d-1549-4132-b42f-762f23ac89d0.png">
