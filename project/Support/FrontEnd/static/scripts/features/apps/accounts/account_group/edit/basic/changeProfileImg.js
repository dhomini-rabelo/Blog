let img = document.querySelector('#id_profile_img')
let fileInput = document.querySelector('#id_photo')


img.addEventListener('click', addImgInInput)
fileInput.addEventListener('change', changeImgInInput)

function addImgInInput() {
    fileInput.click()
}

function changeImgInInput() {
    if (fileInput.files.length <= 0) return

    let reader = new FileReader();

    reader.onload = () => {
        img.src = reader.result;
    }

    reader.readAsDataURL(fileInput.files[0]);
}
