export default class ImgAsInput {

    constructor(imgLocal, fileInputLocal) {

        this.img = document.querySelector(imgLocal)
        this.input = document.querySelector(fileInputLocal)

    }

    addEvents = () => {
        this.img.addEventListener('click', this.clickInInput)
        this.input.addEventListener('change', this.LoadImgOfInput)
    }

    clickInInput = () => {
        this.input.click()
    }

    LoadImgOfInput = () => {
        if (this.input.files.length <= 0) return
    
        let reader = new FileReader()
    
        reader.onload = () => {
            this.img.src = reader.result
        }
        
        reader.readAsDataURL(this.input.files[0])
    }


}