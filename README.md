# Face Recognition API
This repo contains the django app including a custom API for facial recognition. The views file contains the necessary scripts to send data about analysed images in JSON format.

--
The format of data retrieved is the following: 
```
{
    "num_faces": number of faces detected in certain image;
    "success": a boolean saying whether the image has been read correctly or not;
    "faces": [(x,y,w,h)] set of coordinates representing bottom left and top right corners of squares bounding faces
}
```
Class is still in development and I am going to add new methods and increase its functionality. Feel free to fork and come with suggestions !
