import { addMask } from './form/masks.js'
import { forMoneyBRMask, strMask, forDateBRMask } from './form/functions.js'



//! write ->  type = "module" in tag script
// test use class needs-validation



document.addEventListener('DOMContentLoaded', functionsForForm)
// DOMContentLoaded



function functionsForForm(){


    let useMasks = false
    let useStrip = true




    if (useMasks){
        //! <script src="https://cdn.jsdelivr.net/npm/cleave.js@1.6.0/dist/cleave.min.js"></script>
        //! Adaptado para uso com input do tipo text
        let modifications = [
            //['id_field', mask],
        ]//using id
        let allowedMasks = ['cpf', 'cnpj', 'phoneBR', 'dateBR', 'moneyBR', 'card', 'numericOnly', 'numericPositiveOnly', 'securityPasswordCard']
        for (let i in modifications){
            addMask(modifications[i][0], modifications[i][1])
        } 
        //* Functions
        // case mask for string --> strMask(idInput, False)
        // case moneyBR in modifications  --> forMoneyBRMask(idInput)
        // case dateBR in modifications  --> forDateBRMask(idInput)
    }


    

    if (useStrip){
        let textInputs = document.querySelectorAll('input[type="text"]')
        let passwordInputs = document.querySelectorAll('input[type="password"]')


        textInputs.forEach((input) => {
            input.addEventListener('blur', strip)
        })

        passwordInputs.forEach((input) => {
            input.addEventListener('blur', strip)
        })

        function strip(event) {
            event.currentTarget.value = event.currentTarget.value.trim()
        }
    }

}
