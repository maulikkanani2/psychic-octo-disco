const changePassword = document.getElementById('change_password_check')

const password_change = document.getElementById('password_change')
const new_password_change = document.getElementById('new_password_change')
const change_password_btn = document.getElementById('change_password_btn')
function changeEnableDisable() {
    if (changePassword.checked) {
        password_change.disabled = false
        new_password_change.disabled = false
        change_password_btn.disabled = false
    } else {
        password_change.disabled = true
        new_password_change.disabled = true
        change_password_btn.disabled = true
    }
}
changePassword.addEventListener('change', changeEnableDisable);
