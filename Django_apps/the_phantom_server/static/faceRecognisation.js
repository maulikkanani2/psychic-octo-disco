const videoElement = document.getElementById('videoElement');
const canvasElement = document.getElementById('canvasElement');
const photoElement = document.getElementById('photoElement');
const startButton = document.getElementById('startButton');
const captureButton = document.getElementById('captureButton');
const cancelButton = document.getElementById('cancelButton');
const imageSrc = document.getElementById('image_src');
const emailSrc = document.getElementById('email_src');
const imageForm = document.getElementById('image_form');
const faceEmail = document.getElementById('face_email');
const faceVideo = document.getElementById('faceVideo');
const isFaceAuth = document.getElementById('is_face_auth');
isFaceAuth.value = false;

let stream;

async function startWebcam() {
    try {
        imageForm.style.display = 'none'
        // videoElement.style.display = 'block';
        faceVideo.style.display = 'block';
        isFaceAuth.value = true;
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElement.srcObject = stream;
        startButton.style.display = 'none';
        captureButton.style.display = 'block';
        cancelButton.style.display = 'block';
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
}

startButton.addEventListener('click', startWebcam);

function capturePhoto() {
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    canvasElement.getContext('2d').drawImage(videoElement, 0, 0);
    const photoDataUrl = canvasElement.toDataURL('image/jpeg');
    imageSrc.value = photoDataUrl;
    emailSrc.value = faceEmail.value;
    imageForm.submit();
    videoElement.style.display = 'none';
}

captureButton.addEventListener('click', capturePhoto);


function cancelFaceAuth(){
    imageForm.style.display = 'block'
    faceVideo.style.display = 'none';
    startButton.style.display = 'block';
    captureButton.style.display = 'none';
    cancelButton.style.display = 'none';
}
cancelButton.addEventListener('click', cancelFaceAuth);