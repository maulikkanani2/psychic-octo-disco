const changePhoto = document.getElementById('changePhoto')
const fileToUpload = document.getElementById('fileToUpload')

function submitProfileForm() {
    changePhoto.submit();
}
fileToUpload.addEventListener('change', submitProfileForm);


const updateProfileBTN = document.getElementById('update_profile_btn')
const updateProfileCheck = document.getElementById('update_profile_check')
function updateProfile(){
    if (updateProfileCheck.checked) {
        
        updateProfileBTN.disabled=false
    }else{
        updateProfileBTN.disabled=true
    }
}
updateProfileCheck.addEventListener('change', updateProfile);



const enableFaceAuth = document.getElementById('face_auth_check')
const startButtoneEnable = document.getElementById('startButtoneEnable')
const videoElementEnable = document.getElementById('videoElementEnable');
const canvasElementEnable = document.getElementById('canvasElementEnable');
const captureButtonEnable = document.getElementById('captureButtonEnable');
const imageSrcEnable = document.getElementById('image_src_enable');
const imageFormEnable = document.getElementById('enable_face_authentication');

let streamEnable;

function faceAuthEnableDisable() {
    if (enableFaceAuth.checked) {
        startButtoneEnable.disabled = false
    } else {
        startButtoneEnable.disabled = true
    }
}
enableFaceAuth.addEventListener('change', faceAuthEnableDisable);


async function startWebcamEnable() {
    try {
        videoElementEnable.style.display = 'block';
        streamEnable = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElementEnable.srcObject = streamEnable;
        startButtoneEnable.style.display = 'none';
        captureButtonEnable.style.display = 'block';
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
}

startButtoneEnable.addEventListener('click', startWebcamEnable);

function capturePhotoEnable() {
    canvasElementEnable.width = videoElementEnable.videoWidth;
    canvasElementEnable.height = videoElementEnable.videoHeight;
    canvasElementEnable.getContext('2d').drawImage(videoElementEnable, 0, 0);
    const photoDataUrl = canvasElementEnable.toDataURL('image/jpeg');
    imageSrcEnable.value = photoDataUrl;
    imageFormEnable.submit();
    videoElementEnable.style.display = 'none';
}

captureButtonEnable.addEventListener('click', capturePhotoEnable);


// function cancelEnableFaceAuth(){
//     imageForm.style.display = 'block'
//     faceVideo.style.display = 'none';
//     startButton.style.display = 'block';
//     captureButton.style.display = 'none';
//     cancelButton.style.display = 'none';
// }
// cancelButton.addEventListener('click', cancelFaceAuth);




